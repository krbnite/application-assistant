Markdown test lifted from the corresponding notebook.

Still requires some clean-up.

--------------------






It's time to pull out some tricks.  

The random forest models are still 
* not performing very well
* and are fairly sensitive to random seed

As I've hypothesized earlier, this seems to suggest that 
* there is an important independent variable (or several) that dictate the performance
* however, this is a very rare event problem, so there are very few events to learn from
* this means that an important independent variable can be improperly split into training,
  validation, and test sets -- that is, without stratifying on these variables, the training
  set does not have a representative distribution of those independent variables
* some models can recover from this (e.g., a linear model that learns a formula)
* unfortunately, this is one of the few weakness of random forests, where a major assumption is
  that the training set is a representative sample of the population at large (especially when
  it comes to extrema -- mins and maxes)

# SMOTE
The imbalanced class ("rare event") problem should have not been overlooked.  However, this
project has changed hands a few times and we have always been on a tight deadline.  At WWE,
I had success in improving machine learning classifiers by using SMOTE ("Synthetic Minority
Over-sampling TEchnique").  This technique is applied to the training set to grow the 
minority class to a similar size as the majority class.  A simpler version of this technique
is to simply oversample the minority: duplicate the minority class records over and over until
you have similarly sized classes.  This can over-emphasize the particular minority examples in
the training set, which SMOTE hedges against a bit by generating synthetic records that look
like minority class records, but not perfectly.

Note that the empahsis on applying this technique to the training set:  there is risk for 
data leakage when using any data augmentation technique.  Namely, if you use SMOTE on the whole data
set before splitting, you are doing it wrong!  This will directly cause leakage ("information pathways")
between the training, validation, and test sets.

Python has a great module dedicated to the imbalanced class problem:
* https://imbalanced-learn.readthedocs.io/en/stable/generated/imblearn.over_sampling.SMOTE.html


You can get your hands on SMOTE quite easily:
```python
from imblearn.over_sampling import SMOTE
```

If you have a lot of categorical variables, it's actually better to use a modified version
of SMOTE for this use case:
```python
from imblearn.over_sampling import SMOTENC
```

For more info, read the original paper on SMOTE:
* N. V. Chawla, K. W. Bowyer, L. O.Hall, W. P. Kegelmeyer, “SMOTE: synthetic minority over-sampling technique,” Journal of artificial intelligence research, 321-357, 2002.


# Parametric Learning
In addition to class imblance, another issue I identified above is tied to 
the dependence of the random forest's performance on random seed.  Though there will
always be some variability when switching seeds, it shouldn't be the difference
between a 0.5 AUC and a 0.6 AUC (this is shown below with random forests).  

A significant dependence on random seed
implies that the model is sensitively dependent on the specifics and details of
the training set.  Specifically,
this implies a dependence on how certain important variables are distributed into
training, validation, and test.  

Some models are robust against this.  For example, assume the target is linearly 
dependent on an important independent variable, and assume that the independent 
variable was poorly split into training and validation, where the training set
sees only the bottom 70% of the variables range, while the training set only
holds instances in the range's top 30%.  A linear regression will learn a linear
formula on the training set, which will still be largely applicable and useful
on the validation set -- even though it never saw instances in the range's top
30%.  However, a random forest will not be able to do this.  Despite all of the
great properties of a random forest, it cannot extrapolate.  

In a rare event
classification problem, this issue is more likely to affect a random forest and
can only be mitigated if you properly stratify the data split on the important 
variables. Note that without this stratification, a signal augmentation technique
like SMOTE will not likely help all that much.


In previous attempts, we tried to mitigate this issue by stratifying on the target variable,
which helped ensure that the training distribution of the target matched the
distribution in validation; but this was not enough!  The poor performance implied
that there might be no signal, but the dependence on random seed implied that
there was -- some important variable(s) exist that, when split correctly ("when
using the right random seed"), improves the model performance.  However, it's not
clear how to identify all the right variables to stratify on.  Instead, given my
hypothesis, it would be better to use a parametric model, which has a chance of 
learning a formula that can extrapolate.  

Why not try logistic regression?

# Missing Indicator Method
One of the great properties of a random forest is that you really do not have to
do much to the data.  For example, it will figure out a linear, quadratic, or
exponential dependence equally well (or any monotonic transformation).  It is
also reasonably well-suited for figuring out conditional relationships (after all,
each tree is basically a heirarchy of if-then statements), which means you do not
necessarily have to worry about adding interactions in explicitly (e.g., x1, x2, and
x1\*x2).  If one assumes that missing data is validly informative (i.e., does not introduce
data leakage), then it can basically be left as-is or coded as some
extreme value way outside the variable's range (e.g.,-999999), whereas this would
destroy a linear model which requires a well-conceived imputation strategy.  

The missing indicator method (MIM) is a technique that is considered terrible
by statisticians interested in unbiased estimates of model coefficients (relationship
strengths), but which is actually top notch when it comes to building a predictive
model where one is less interested in unbiased coefficients and more interested
on predictive performance on held out data sets.  

To implement the MIM, you simply take any column with missing data (call it x) and
make a second column (call it x\_missing).  Wherever x has a missing value, x\_missing
is flagged with a 1, but is 0 otherwise.  Then, the missing values in x are recoded to
0.  

So, say you have a single-variable modes like so:
```
y = m*x+b
```

This now becomes:
```
y = m1*x + m2*x_missing + b
```

As you can see, instead of imputing with the median or mean, this technique will
optimize the best replacement value (i.e., after learning has occurred, you can 
essentially rewrite `m2` as `m2 = m1*x_replacement`; this allows `m1` to 
be learned without forcing an imputed value on it).

Since random forests are fairly robust against variable representation, its performance
shouldn't be affected all that much by choosing to use the MIM (or not).  However, predictive models
that require an imputation strategy will often show incredible performance boosts using
this technique.


# L1 Regularization
The downside to the MIM is that it can double the data dimensionality if every
variable has missing data (which is nearly true for our data set).  This wouldn't be
so bad if every variable was important -- but you can basically assume beforehand that
every variable is not important, and many are probably no better than noise.  This means
that you might be doubling the amount of useless variable, which can cause degradation in
model performance.  

Fortunately, there are techniques for eliminating variables in regressions.  One such technique
in linear regression is called LASSO, which uses the L1 penalty and chooses to zero out variables
that a penalized below a certain threshold.  Importantly, the L1 penalty does most of the
hard work here:  it serves to amplify coefficients of variables with signal and diminish the 
coefficients of noisy, useless variables.  

# Results
In this notebook, I explore:
* SMOTE, SMOTENC
* MIM
* RandomForest -> Logistic Regression
* L1 Penalized Logistic Regression 
    - and for comparison: no penalty, L2 penalty, and ElasticNet penalty


I find that SMOTE can help a random forest, but as assumed, only when the data
split was opportunistic.  For certain "bad" data splits (based on random seed), SMOTE
cannot help the random forest.

I then move on logistic regression, where I automatically include MIM because logistic
regression requires putting some thought into an imputation strategy.  **Starting with
SMOTE and L1 penalty, we find the AUC on validation at 0.995.**  Remember: the highest
AUC we got with "opportunistic" splits using the RF was around 0.58.  

I then investigate the cause of such a dramatic increase in AUC.  I find that SMOTE
is absolutely necessary for this success (without it, AUC suffers significantly).  I also
find that logistic regression performs well in general, independent of solver used: the worst
seen with no penalty was around 0.66 AUC, though most of the solvers got up to 0.83 AUC with
no penalty; L2 penalty has no improvement over 0.83 AUC (and in fact, almost the entire
tradeoff range in ElasticNet performs the same as well); however, nothing comes close
to beating pure L1 penalty.  Finally, by playing with random seeds a bit, I find that
the results are largely independent of random seed.  


# Next Steps
In the next notebook, I will explore variable importances in more detail.  I will
also look into using LIME to understand model decisions at the single-decision level. Finally,
since we found that the sensor data is nearly 100% ineffective (quick glance at importances in
this notebook places them at the tail end), I will use the larger "democlinical patient set"
to build this model on.  This set is about twice the size of the Toitu-restricted set I've been
using.  Importantly, since these ~1500 patients are unseen in this notebook, I should have
a holdout sample from this subset that is tested last...  

Since I do not have a test set in this notebook, these results should be strengthened using
cross validation.


===========================


# SMOTE
Here, we are still using a RandomForest, but we will be introducing SMOTE.

Set Up:
* Model: RandomForestClassifier
    - 100 trees
* Missing Data
    - Not treated (left as -999999)
* Target: adsc_dlvrybefore34wks
* Data: toif1pwr_demotoif1pwr_df
    - democlinical + Toitu Power Cols
* Col Drop: 
    - remove sensor_toi_f1_mvt_pwr_mvt41 
* SMOTE
    - using regular SMOTE
* Results
    - Terrible: ~0.5 AUC
    - **UPDATE (2020-Jan-27)**: found out that, yet again, these results depend on random seed; for example,
      in my last run, I updated all random seeds to 47 -- and suddenly we have a 0.58 AUC
      here...  except that on scenarios below that had higher AUCs, we now have lower AUCs;
      it's nearly inexplicable...


========================


# Missing Indicator Method
Note that, though a random forest can handle missing values be coded 
as -999999, most other methods cannot -- and this basically includes SMOTE.  Why?
Because SMOTE is using nearest neighbor methods, and you can bet those -999999 are
throwing things off a bit.  


Set Up:
* Model: RandomForestClassifier
    - 100 trees
* Missing Data
    - Missing Indictor Method (for every colX w/ missing data, another column is
      created, colX_missing, which flags all missing data in colX as 1 and non-missing
      data as 0; the missing data in colX are then zeroed out)
* Target: adsc_dlvrybefore34wks
* Data: toif1pwr_demotoif1pwr_df
    - democlinical + Toitu Power Cols
* Col Drop: 
    - remove sensor_toi_f1_mvt_pwr_mvt41 
* SMOTE
    - using SMOTENC
* Result
    - as would be expected by a RF, the typical 100-trees run gave back
      an AUC of 0.53 (RFs are usually fairly robust against these types of
      representational changes)
    - **UPDATE (2020-Jan-27)**: found out that, yet again, these results depend on random seed; for example,
      in my last run, I updated all random seeds to 47 -- and suddenly we have entirely different
      results (e.g., MIM degrades the AUC instead of maintaining it)


======================


# SMOTENC, MIM, and some RF Regularization (1)
Everything from the last run, but:
* Ensemble Regularization: trees increased: 100 -> 10k
* Depth Regularization:  max_depth: none -> 3


Set Up:
* Model: RandomForestClassifier
    - 10k trees
* Missing Data
    - Missing Indictor Method (for every colX w/ missing data, another column is
      created, colX_missing, which flags all missing data in colX as 1 and non-missing
      data as 0; the missing data in colX are then zeroed out)
* Target: adsc_dlvrybefore34wks
* Data: toif1pwr_demotoif1pwr_df
    - democlinical + Toitu Power Cols
* Col Drop: 
    - remove sensor_toi_f1_mvt_pwr_mvt41 
* SMOTE
    - using SMOTENC
* Regularization
    - Ensemble Regularization: trees increased: 100 -> 10k
    - Depth Regularization:  max_depth: none -> 3
* RESULTS
    - AUC IMPROVED:  0.53 -> 0.57
    - **UPDATE (2020-Jan-27)**: found out that, yet again, these results depend on random seed; for example,
      in my last run, I updated all random seeds to 47 -- and suddenly we have entirely different
      results 
      * impact here: regularization helps take the AUC back to 0.57 (where it began for seed47 on most naive
        set up)


======================


# SMOTENC, MIM, and some RF Regularization (2)
Tightened Depth Regularization:  3 -> 2


Set Up:
* Model: RandomForestClassifier
    - 10k trees
* Missing Data
    - Missing Indictor Method (for every colX w/ missing data, another column is
      created, colX_missing, which flags all missing data in colX as 1 and non-missing
      data as 0; the missing data in colX are then zeroed out)
* Target: adsc_dlvrybefore34wks
* Data: toif1pwr_demotoif1pwr_df
    - democlinical + Toitu Power Cols
* Col Drop: 
    - remove sensor_toi_f1_mvt_pwr_mvt41 
* SMOTE
    - using SMOTENC
* Regularization
    - Ensemble Regularization: trees increased: 100 -> 10k
    - Depth Regularization:  max_depth: 3 -> 2
* RESULTS
    - **AUC IMPROVED:  0.57 -> 0.60**
    - **UPDATE (2020-Jan-27)**: found out that, yet again, these results depend on random seed; for example,
      in my last run, I updated all random seeds to 47 -- and suddenly we have entirely different
      results 
      * Impact Here:  Instead of AUC improving, it now shot down to 0.5 AUC



========================


# SMOTENC, MIM, and some RF Regularization (3)
Tightened Depth Regularization:  2 -> 1
Increased Ensemble Regularziation:
* 1st Run: no increase
* 2nd Run: 10k trees -> 50k trees


Set Up:
* Model: RandomForestClassifier
    - 100 trees
* Missing Data
    - Missing Indictor Method (for every colX w/ missing data, another column is
      created, colX_missing, which flags all missing data in colX as 1 and non-missing
      data as 0; the missing data in colX are then zeroed out)
* Target: adsc_dlvrybefore34wks
* Data: toif1pwr_demotoif1pwr_df
    - democlinical + Toitu Power Cols
* Col Drop: 
    - remove sensor_toi_f1_mvt_pwr_mvt41 
* SMOTE
    - using SMOTENC
* Regularization
    - Ensemble Regularization: trees increased: 
        - 1st Run:  No change (10k trees)
        - 2nd Run:  10k trees -> 50k trees
    - Depth Regularization:  max_depth: 2 -> 1
* RESULTS
    - **TOO MUCH REGULARIZATION:  AUC: 0.6 -> 0.58 in both runs**
    - **UPDATE (2020-Jan-27)**: found out that, yet again, these results depend on random seed; for example,
      in my last run, I updated all random seeds to 47 -- and suddenly we have entirely different
      results 
      * Impact Here:  AUC remaining around 0.5 AUC 


============================


## MIM w/ LASSO
Here I do a LASSO Regression with rounding.  It's not a recommended technique, but 
something interesting happened:  despite having more false negatives, we have a lot
more true positives.  This motivates a logistic regression w/ L1 Penalty next.


NOTE: the random seed effect is also present here.  For example, when I initially
developed these notebooks, I used random seed 23 in `train_test_split` and 37 in `SMOTENC`. This
resulted in AUC 0.556.  HOWEVER, when I changed both seeds to 47 (like in above RF runs), the
AUC bumped up to 0.597.


=============================


# MIM, SMOTE, L1-Penalized LogReg
Holy shit. Wtf. This one is amazing.


### UPDATE (2020-Jan-27)
What's crazier is that this is more robust against random seed.  This really indicates to
me that we were experiencing an extrapolation nightmare scenario with the RF.  Basically, if
your training set is a representative sample, then RFs will be amazing; however if any of the
important independent vars or the target var is not representative in training, the RF will
not work on validation -- which is what we saw.


I originally ran this model w/ seed 23 in `train_test_split` and 37 in `SMOTENC`. This
resulted AUC of 0.998 on both training and validation; AUPRC of 0.998 on training, but 0.6
on validation; and a confusion matrix on validation like:
```
[[551   2]
 [  0   3]]
```

It was so good, I was afraid to change the random seed.  But when I change both to 47, we 
get very similar results:  trn/val AUC of 0.9996/0.9955;  tran/val AUPRC of 0.999/0.375;  and
a confusion matrix on validation like:
```
 [[548   5]
 [  0   3]]
```

The results have suffered a little, but only ever-so-slightly.  

When I change the seed to 57, we basically recover that slight decrease:
```
Trn AUROC: 0.9988363072148952
Val AUROC: 0.9981916817359856
-------------------
Trn AUPRC: 0.9976780185758514
Val AUPRC: 0.6
```

Point is, this is the real deal.  The coefficients of the linear model are learning
the important relationships in a way that can extrapolate -- something the RF can't do.  


======================


# Sanity Check:  What Causes Such Great Performance?
Below we find that:
* SMOTE is absolutely necessary (remove it and the AUC sinks to 0.5)
* L1 regularization is critically necessary
    - use L2 (penalty='l2') and AUC goes from 0.99 down to 0.66
    - remove it (penalty='none') 
    
# 1. Remove SMOTE
0.999 AUC?!?

Let's take out SMOTE and see what happens.

**Spoiler**:  AUC goes from 0.999 -> 0.5.  (SMOTE is amazing, eh?)

These results are robust:
* try un-commenting the SMOTENC lines: the AUC will shoot back up to 0.99
* try changing the random seed:  results will remain similar

==============================


# 2. Swap Out L1 with with other penalties

Here we put SMOTE back in, keep the MIM, but swap out L1 with L2-Penalized LogReg.


**SPOILER**:  
* L2 sucks here.  It's all about the L1 Penalty.
* To be more specific:  AUC on validation goes down to 0.66 (from 0.99)


## 2a: NO PENALTY (no rescaling)
**2020-Jan-27**

The `liblinear` solver does not work for `penalty=none` (logistic regressions default to
L2 penalties in sklearn), so we are forced to explore the other solvers:
* newton-cg
* lbfgs
* sag
* saga

I ran through each of them, recording the results below.  The `newton-cg` method
still did fairly well (AUC on validation of 0.83), though all other solvers did
terrible (worse than chance, i.e., smaller than 0.5 AUC).  From my learnings a week
or so ago, I already knew the SAGA needed variables to be rescaled to promise
convergence; I've not read that this is true for SAG as well.  I'm guessing this is
true for LBFGS as well.  

So, below I report non-scaled results.  Next, I'll rescale all continuous variables
and report again.

Newton-CG
```
Trn AUROC: 1.0
Val AUROC: 0.8306208559373116
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.2684652278177458
```

LBFGS w/o rescaling
```
Trn AUROC: 0.965477114041893
Val AUROC: 0.47106690777576854
-------------------
Trn AUPRC: 0.9374938857783774
Val AUPRC: 0.00539568345323741
```


Sag w/ rescaling
```
Trn AUROC: 0.8855702094647014
Val AUROC: 0.4113924050632911
-------------------
Trn AUPRC: 0.8238578777172731
Val AUPRC: 0.00539568345323741
```

Saga w/o rescaling
```
Trn AUROC: 0.865399534522886
Val AUROC: 0.3987341772151899
-------------------
Trn AUPRC: 0.7994590486456217
Val AUPRC: 0.00539568345323741
```


=========================


## 2b: NO PENALTY (with rescaled ind vars)
**2020-Jan-27**

Here, we use some rescale methods on the independent variables in order
to get variables on a similar scale...which is a requirement for convergence
for the SAG and SAGA solvers (and maybe LBFGS too).  

LBFGS improves, but SAG and SAGA remain sucky.  This might be due to using
bad stopping conditions... But I'm not sure.  There are related meta parameters
that we can play with to find out:
* `max_iter` is the number of iterations a solver goes through until it is
   assumed that the solver has converged; it defaults to 100
* `tol` is the tolerance for stopping criteria; it defaults to `1e-4`

We can experiment with these things in the next section.  Here, we leave them defaulted.

Newton-CG w/ rescale (default stopping conditions)
```
NCG w/ Standardizer ( (z-avg)/std )
Trn AUROC: 1.0
Val AUROC: 0.8297
-------------------
Val AUROC: 1.0
Val AUPRC: 0.2240

NCG w/ Normalizer ( (z-min)/(max-min) )
Trn AUROC: 1.0
Val AUROC: 0.8288
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.1923
```

LBFGS w/ rescale (default stopping conditions)
* this one is worse on validation, and actually just
  ever so slightly worse on training (it's not perfect)
* these shortcomings might have to do with the solver itself,
  or some meta parameters (stopping conditions)

```
w/ Standardizer
Trn AUROC: 0.9976726144297904
Val AUROC: 0.6621458710066305
-------------------
Trn AUPRC: 0.9965143383682782
Val AUPRC: 0.059152677857713824

w/ Normalizer
Trn AUROC: 0.9584949573312646
Val AUROC: 0.4629294755877034
-------------------
Trn AUPRC: 0.923352435530086
Val AUPRC: 0.00539568345323741
```

SAG w/ rescale (default stopping conditions)
```
w/ Standardizer
Trn AUROC: 0.6586501163692785
Val AUROC: 0.3291139240506329
-------------------
Trn AUPRC: 0.6036276415535662
Val AUPRC: 0.00539568345323741

w/ Normalizer
Trn AUROC: 0.9193173002327386
Val AUROC: 0.4358047016274864
-------------------
Trn AUPRC: 0.8643624049121339
Val AUPRC: 0.00539568345323741
```

SAGA w/ rescale (default stopping conditions)
```
w/ Standardizer
Trn AUROC: 0.6551590380139644
Val AUROC: 0.3381555153707052
-------------------
Trn AUPRC: 0.6020140131824097
Val AUPRC: 0.00539568345323741

w/ Normazlizer
Trn AUROC: 0.9053529868114819
Val AUROC: 0.42495479204339964
-------------------
Trn AUPRC: 0.8482413976043657
Val AUPRC: 0.00539568345323741
```

=======================


## 2b: NO PENALTY (with rescaled ind vars, revised stopping conditions)
**2020-Jan-27**

Here, explore we why SAG and SAGA remain sucky, assuming it might be due to
poorly planned stopping conditions.

Newton-CG works good for everything, so I focus more on LBFGS, SAG, and SAGA.

We have two major hyper parameters that control this:
* `max_iter` is the number of iterations a solver goes through until it is
   assumed that the solver has converged; it defaults to 100
* `tol` is the tolerance for stopping criteria; it defaults to `1e-4`


MAJOR RESULTS
* <font color='red'>though LBFGS remained fairly suboptimal around 0.66 AUC, I was able to
  get the SAG and SAGA solvers to perform at ~0.83 AUC, which is what Newton-CG
  was able to get without rescaling and using default hyperparameters</font>
* <font color='red'>the "normalizer" has dramatically worse performance than the "standardizer"
  on SAG and SAGA </font>
  - it might be salvageable with more hyperparam tweaking, but ... why bother?
  - **ODDLY**, using the Newton-CG solver, the situation is reversed:  the "normalizer"
    works its wonders, while the "standardizer" results in MUCH poorer performance
    

-------------------------------


LBFGS w/ rescale (default stopping conditions)

this one is worse on validation, and actually just ever so slightly worse on training (it's not perfect)
these shortcomings might have to do with the solver itself, or some meta parameters (stopping conditions)

LBFGS
* it is very hard to improve LBFGS
    - below I show one tweak, but I tried MANY, never getting better (if at all)
    
```
w/ Standardizer (from last time, max_iter=100)
Trn AUROC: 0.9976726144297904
Val AUROC: 0.6621458710066305
-------------------
Trn AUPRC: 0.9965143383682782
Val AUPRC: 0.059152677857713824

w/ Standardizer (this time, max_iter=5000)
Trn AUROC: 1.0
Val AUROC: 0.6630500301386376
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.07026378896882494
```


SAG w/ rescale (default stopping conditions)
* was able to get SAG up to ~0.83 AUC, which is what Newton-CG gets
* however, the "normalizer" hurts performance
    - use "standardizer"

```
w/ Standardizer (from last time, max_iter=100, tol=1e-4)
Trn AUROC: 0.6586501163692785
Val AUROC: 0.3291139240506329
-------------------
Trn AUPRC: 0.6036276415535662
Val AUPRC: 0.00539568345323741

*** BETTER ***
w/ Standardizer (max_iter=500, tol=1e-4)
Trn AUROC: 1.0
Val AUROC: 0.6621458710066305
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.059152677857713824


###########################################
#########   THIS ONE   ####################
###########################################
*** BETTER ***
w/ Standardizer (max_iter=5000, tol=1e-4)
Trn AUROC: 1.0
Val AUROC: 0.8288125376732971
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.1922747516272696


*** SAME ***
w/ Standardizer (max_iter=50k, tol=1e-4)
Trn AUROC: 1.0
Val AUROC: 0.8288125376732971
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.1922747516272696

*** WORSE ***  (better than original, but worse than best run)
w/ Standardizer (max_iter=5000, tol=1e-5)
Trn AUROC: 1.0
Val AUROC: 0.6621458710066305
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.059152677857713824

==========================================

w/ Normalizer (max_iter=5000, tol=1e-4)
Trn AUROC: 0.9375484871993794
Val AUROC: 0.6133212778782399      
-------------------
Trn AUPRC: 0.8889655172413793
Val AUPRC: 0.009152677857713828
```




SAGA w/ rescale (default stopping conditions)
* using SAG's best hyperparameters, we also can get SAGA up to ~0.83 AUC, which is what Newton-CG gets
* again, the "normalizer" hurts performance

```
w/ Standardizer (from last time: max_iter=100, tol=1e-4)
Trn AUROC: 0.6551590380139644
Val AUROC: 0.3381555153707052
-------------------
Trn AUPRC: 0.6020140131824097
Val AUPRC: 0.00539568345323741


w/ Standardizer (max_iter=5000, tol=1e-4)
Trn AUROC: 1.0
Val AUROC: 0.8288125376732971  #   <------ NICE
-------------------
Trn AUPRC: 1.0
Val AUPRC: 0.1922747516272696

==========================================

w/ Normalizer (max_iter=5000, tol=1e-4)
Trn AUROC: 0.9294026377036462
Val AUROC: 0.6088004822182037  #  <------- Ick! Ew!
-------------------
Trn AUPRC: 0.876274643099932
Val AUPRC: 0.008725327430363403
```


See this post for more info on the Solvers:
* https://stackoverflow.com/questions/38640109/logistic-regression-python-solvers-defintions

LBFGS probably is the worst b/c it is an approximation of Newton-CG...but doesn't seem
to have anything else going for it.  The SAG and SAGA methods are stochastic gradient
descent methods, so it's not surprising that (i) we had to normalize, and (ii) they ultimately
work.
    
    
HERE's something weird:  
* though the "standardizer" works so well for SAG and SAGA, while the
  "normalizer" is terrible, the situation is reversed for Newton-CG
  

==================================


## 2c: L2 PENALTY


For `penalty=none`, the `standardizer` was the go-to scaler for `sag` and
`saga`, while the `normalizer` seemed to be the go-to scaler for `newton-cg`.

For `penalty=l2`, everything seems to prefer the `standardizer`.

So many of the solvers got the SAME EXACT results that I thought something might be wrong, but
then SAG and SAGA gave slightly different (worse) values when using the "normalizer."  I then
also did a sanity check and changed `penalty=l2` to `penalty=l1` for the SAGA solver:
* for "normalizer", I got crappy disheartening results (AUC ~0.60)
* for "standardizer", I recovered the GREAT results that we got using L1 way above (AUC ~0.99)



Newton-CG
```
w/ Standardizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971

w/ Normalizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.6630500301386376
```

Liblinear
```
w/ Standardizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971

w/ Normalizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.6630500301386376
```


LBFGS
```
w/ Standardizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971

w/ Normalizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.6630500301386376
```

SAG
```
w/ Standardizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971

w/ Normalizer
Trn AUROC: 0.9375484871993794
Val AUROC: 0.6133212778782399
```

SAGA
```
w/ Standardizer
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971

w/ Normalizer
Trn AUROC: 0.9294026377036462
Val AUROC: 0.6088004822182037
```

============================


## 2D: ElasticNet

Ok, this one is weird... Results aren't changing as I toggle the parameter
between L1 and L2 penalties.

**Update**:  found out for "saga" solver, features must all be of similar scale, so I've 
been trying to normalize things...but still not working....

### UPDATE (2020-Jan-27)
The `penalty='elasticnet'` setting only works with the SAGA solver.

Here, we must introduce the ElasticNet mixing parameter:
* l1_ratio (float, default=None):  the Elastic-Net mixing parameter, with 0 <= l1_ratio <= 1. Only used if   
  `penalty='elasticnet'`. Setting `l1_ratio=0` is equivalent to using `penalty='l2'`, while setting 
  `l1_ratio=1` is equivalent to using `penalty='l1'`. For 0 < l1_ratio <1, the penalty is a combination 
  of L1 and L2.


First thing to check is if it converges on our L1 and L2 results:
```
L1 (l1_ratio=1)
Trn AUROC: 0.9988363072148954
Val AUROC: 0.9954792043399638

L2 (l1_ratio=0)
Trn AUROC: 0.999612102404965
Val AUROC: 0.8288125376732971
```

YES!  Results are reproduced.

Now for more interesting l1 ratios...


Random Seed: 47

| L1 Ratio | Trn AUROC | Val AUROC | Trn AUPRC | Val AUPRC |
|-----------|---------|--------|------------|--------------|
| 1.0 | 0.999 | 0.995 | 1.000 | 0.829 |
| 0.9 | 0.999 | 0.995 | 0.998 | 0.375 |
| 0.8 | 0.999 | 0.829 | 0.998 | 0.192 |
| 0.7 | 0.999 | 0.829 | 0.998 | 0.192 |
| 0.6 | 0.999 | 0.829 | 0.999 | 0.192 |
| 0.5 | 0.999 | 0.829 | 0.999 | 0.192 |
| 0.4 | 1.000 | 0.829 | 0.999 | 0.192 |
| 0.3 | 1.000 | 0.829 | 0.999 | 0.192 |
| 0.2 | 1.000 | 0.829 | 0.999 | 0.192 |
| 0.1 | 1.000 | 0.829 | 0.999 | 0.192 |
| 0.0 | 1.000 | 0.829 | 0.999 | 0.192 |

<font color='red'>Basically, what we find is rapid degradation in performance one we abandon
the L1 penalization.  By the time the L1 Ratio gets to 0.8, the performance
matches that of L2 penalization (`l1_ratio=0`).</font>


========================

# Remove the MIM
**2020-Jan-28**

Ok, so we know:
* we must use SMOTENC
* we should absolutely choose pure L1 penalty
* seems fairly robust against random seed (but we should explore this more below)
* MIM seems to be working just fine...but is it necessary?

Here, we will use the best model, but test taking out MIM.

**UPDATE**:  this section was supposed to be about removing the MIM, however I 
quickly found out that there was an odd random seed dependency that remained
(though not as severe as before).


============================


## For Reference:  Pipeline w/ MIM
Here, we just produce the good results with everything in harmony (SMOTENC, MIM,
L1-Penalized Logistic Regression).  

The only thing that changed is where I apply the MIM.  Above, it was being
applied before rescaling, which means though we say "missing values are recoded
as 0," they effectively are recoded as `-mean(colX)/std(colX)`.  From what I read
about MIM, this is actually fine (any constant can be used -- missing column's 
coefficient will just readjust), but conceptually it's a little uglier (there is
something more aesthetic about zeroing out `colX` when `colX_missing` kicks in).  
So, in order to retain the "recode to 0" aesthetic and to have the code match
the Eglish I use to explain what I'm doing, I've moved the application of MIM to
after variables are rescaled.  (This means I have to apply MIM to subsets instead
of the full set at once.)

For some reason, this reduced performance:  `0.995 AUC --> 0.83`.  However, the
performance was able to be picked back up by changing the tolerance:  `1e-4 --> 1e-3`. 
(This is assuming we keep solver as liblinear.)


Actually, after a few model runs and lots of "debugging", I realized that this
model tends to oscillate between 0.999 AUC and 0.83 AUC -- even with the same
parameters set.  This is true at least when using liblinear and using the
default `max_iter` -- in fact, do not even input the default into the model; just leave
the parameter out.  I found when explicitly using `max_iter=100`, the model would
run at 0.83 AUC, but when leaving it out, it would run at either 0.83 AUC or
0.999 AUC....  Very weird....



===================


Thought I was going crazy... So I went back to the simpler version of
the most performant model -- the one without need to specify many parameters.

At first, it seemed like this one was incredibly stable @ 0.999 AUC.  But then...every
once in a while...it would hit 0.83 AUC.  I initially thought this had to do with
me trying to add in a parameter, or remove one... But then the performance flip wouldn't
happen every time...  

So I just kept it simple and as-is -- then ran, ran, ran.  Yes, in truth, the AUC flips
between 0.999 and 0.83...

But, why?

Well, there is a random state we didn't specify: the one in the model build.
```
model = LogisticRegression(penalty='l1', solver='liblinear')
```

So, simlarly to the random forest, there is a sensitivity to the opportunistic data split.

One way we can control for this is by specifying the seed...

But we can also keep looking at variable importances between 0.83 AUC and 0.99.


===================================



