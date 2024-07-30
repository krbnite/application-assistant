Extract the following write-ups from the various JNBs:

* Write-ups
  - Proper Grid Search Setup for Random Forests (JNB00a)
  - Model-Dependent Feature Encoding Strategies (JNB00a)
  - On Label Noise, Unlabeled Data, and Censored Data: 
     * How should we interpret pre-scheduled cesarians? 
     * Pre-terms and Ceseareans as a Dropout Problem
  - On the Curse of Data Heterogeneity and Random Seed Dependences
  - Balancing out rare-event problems with SMOTE
  - Random seed dependence? Don't use a Random Forest. (Will always overfit!)
    * Face-to-face with the Random Forest's Inability to Extrapolate from its Learning
  - Informative Missingness and Missingness Interpolation in Predictive Modeling: Missing Indicator Method
  - When the Missing Indicator Method Invokes the Curse of Dimensionality: a Need for L1 Penalization
  - The SMOTE-MIM-L1 Trifecta for Data Science Detective Work



# Notebooks

## 00a: Random Forest Deep Dive (Modeling the F3 Baseline)

Summary (2019-Dec-16)

### Background 
This was the very first analysis I did during the last week Udi was here, when
he initially onboarded me onto this project.  

### Problem Statement
What, if anything, was Udi doing wrong or sub-optimally?

### Code Review
Udi was doing some cool stuff, like
looking at multiple families of models (random forests, XGBoosts, LASSOs, etc), but I
noticed the generality was at the cost of specific expertise or insight into any
one particular model family. 

#### Random Forest Hyperparameters
For example, the random forest grid paramaters for Udi's random
grid search were not well-informed, IMHO.

**Max Features**
The `max_features` parameter only looked at `auto` (which is 1/3 the total number of input 
features for a RF regression) and `sqrt`; it's good
to try out values of `1` and `2` here.  

**Max Depth**
Also, `max_depth` had a very limited search (`[3,5,8]`); depending on the data set, these could be 
equivalent depths (e.g., for a forest whose "CART" implementation has  trees reaching 
a depth of 200 or more). 

##### Suggested Strategy 
I find it's usually good to first do a CART random forest,
which allows trees to grow indefinitely to terminal purity, then to inform the 
`max_depth` portion of a grid search by looking at the tree depth statistics of the CART RF (e.g.,
min, Q1, median, Q3, max).  This way, you at least know 
1. the max depth (no use in have grid search looking at larger depths); 
2. what "light" depth regularization looks like (e.g., limiting growth to the CART RF's median depth); 
3. what "more tangible" depth regularization looks like (e.g., limiting growth to the
   CART RF's minimum depth); 
4. what "solid" and "extreme" depth regularization looks like (anything less than the 
   CART RF's minimum is starting to do some real work against noise variables, while anything 
   really small might be considered extreme...and perhaps not useful). 

#### Categorical Variable Encodings

Udi oneHot/dummy encoded any categorical variable he ran into.  

For linear models, a oneHot/dummy encoding is often essential
for linear models, or at least harmless.  However, it generally adds nothing 
to a random forest.  Worse, it can actually harm a forest:
* in extreme cases (categorical variables with 1000s of levels) such an encoding scheme can reduce a
  random forest's performance
* OH/dummy encoding can obscure the intuitive value of feature importances  

##### Suggested Strategy 
Having a more informed view of a particular model family also allows you to
optimize your feature representation.  

Perhaps unintuitively, the best representation for ordinal and nominal 
categorical variables in a RF is the standard N-integer ordinal
representation. Some data scientists learn early on that this representation would 
destroy a linear regression. Though it can be made to work in the linear/logistic 
regression case by adding in some extra features (e.g., negative effect can be eliminated
by using a "polyordinal" encoding scheme), some people tend to
automatically convert categorical variables to a dummy/oneHot encoding without much 
further though.  

In many cases, the oneHot/dummy encoding won't harm a tree-based model. However, in some cases it
will. If one is going to settle on a tree-based model, they should probably test this
encoding but also test the ordinal encoding as well.

In Udi's case, he does indeed settle on a tree-based method (XGBoost), so 
it would be a good sanity check to look at the ordinal encoding's impact on
his final models. 

### RESULTS
ANYWAY, the first thing I did is to apply some of my prior experience w/ tree-based 
methods to enhance and extend the general approach taken by Udi.

You will find in this notebook:
* a depth regularization search 
* an ensemble regularization search  
* a more complete, informed grid search overall
* heat maps corresponding to the grid searches 

I find that 
* none of this dramatically helps model performance  
  - similar training/validation metrics to Udi's
* it's VERY HARD to NOT overfit the data 
  - like Udi, my training metrics are often way better than validation
* optimizing for comparable training/validation metrics comes at the cost of
  training performance without any real improvements in validations performance

### Misc
**NOTE**: For analyses relevant to final report sent to Gates Foundation, please
check out notebooks `01_KU` through `04_KU` in `mbh001/mbh001_v3`.

<!-- #################################################### -->
<!-- #################################################### -->
<!-- #################################################### -->





## 00b: F3 Baseline Modeling Excursion: Cesarian Experiments

Summary (2019-Dec-16)

### Background
This was part of the earliest work I did during the last week Udi was here, when
he initially onboarded me onto this project.  

Basically, the gist is this: while talking with our partners at Columbia,
the topic of cesareans came up. I realized  that a pre-scheduled cesarean
might not be something we want to leave in the dataset when predicting labor 
onset.  The idea is simple, and it is similar to when I was doing dropout modeling 
for the CVN Dropout project:


In the TEDS-D Substance Abuse Disorder (SUD) data set I previously worked with,
there were several types of patients to consider:
* patients who completed a treatment (fine)
* patients who left treatment against medical advice (this is what I considered to be "dropout")
* patients with one of a misc list of reasons for "dropping out of treatment" that didn't really 
  meet the definition of "dropout" I was interested in, e.g.: 
  - death
  - hospitalization
  - incarceration
  -  moved to new state

I wanted to identify the risk of dropout that was intentional, but not due to 
extenuating circumstances that polluted the signal.  I thought the patients in the
third category above would essentialy amount to "dropout noise" 
if we included them under the "dropout" label.  My view was that these patients
represented "unlabeled" or "censored" data, i.e., my contention is that this subpopulation
represents people who would have either "completed treatment" or "dropped out"
but were intervened upon first (death, career change, etc), making it impossible to 
know which. Assuming they were unlabeled/censored at random, I dropped them from
the dataset.

### Problem Statement
Should pre-scheduled cesareans be included in the training set?

### Caveats
This work was exploratory and 
was my first foray into fudging around with and subsetting the data.  Much of the
code here (loading the data, dealing with sparsity, imputation) is borrowed directly from
Udi's last/latest Jupyter notebook (though I added the cesarean parts in the early data loading and
processing steps).  The underlying assumption made during this work is that Udi's final "full data table"
that is used here is good enough to use (which may be debatable) and that most of his processing
code used here was ok (I found that this wasn't strictly true as I worked on stuff, e.g., he
was accidentally dropping most/all of his categorical variables).

### Strategy (Unlabeled/Censored Interpretation)
In this situation (having unlabeled records),
you have some options.  

For one, you can use some clustering/labeling technique to impose
labels on the unlabeled records.  Alternatively (and this is what I chose), you can
assume that the unlabeled data is unlabeled completely at random -- thus, both the
labeled and unlabled records faithfully represent the same patient population.  This means that,
considering the unlabeled data is a small enough portion of the full data set, the
unlabled data can be discarded before engaging in a supervised learning method. 

It occurred to me that a pre-scheduled cesarean when predicting labor onset is a similar
scenario:  the patient ends up without a "label" (in this case, the label stems from a
continuous variable) due to an intervention that occurred before the labeling event
could occur.  This patient would have had a label, but doesn't. 

There is one caveat here: to my mind, the dropout interventions (death, hospitalization, 
incarceration, relocation) can reasonably be assumed to occur at random (likely
not totally true, but reasonable enough), it is not so straightforward that this is
the case with cesareans.  For example, 
* scheduling a cesarean probably means you've made it well past pre-term, which is not 
  random - it biases towards normal-term deliveries
* one can imagine a class of cesareans that were scheduled after labor onset, which
  is definitely not at random (bias towards normal-term again)  

#### Potential Setbacks
In this specific dataset, it might not be so straightforward, e.g.:  
* some of the cesareans are likely due to conditions that correlate with pre-term delivery 
  (i.e., doctors notice complications and take charge before something bad happens)  

So... Maybe there are enough sources driving cesareans that the cesarean class is 
distributed similarly enough in time to regular deliveries... Not sure... 

My hunch is, though, that a cesarean represents noise and
does not represent what we are trying to teach the model to learn, which is natural onset
of labor and delivery. 

Anyway, point is, I discussed this on the phone with Columbia during Udi's last week;
it was generally agreed that we might get a performance boost if we were to selectively
slim down the data set like this.

### Results
* Initially, removing cesareans seemed to strongly hurt the model performance, which led us
  to believe that there was something about the cesarean subpopulation we removed that
  had all the predictive power in it... 
  - However, this was not exactly the case (see next two bullets).
* One thing seems to be obvious: **This data set suffers from what Lee would call 
  the "curse of heterogeneity".** 
  - It is VERY HARD to not overfit to the training data, i.e., the
    data is heterogeneous enough that the validation data is almost never a great representation
    of the training data.
* **What's really strange** is that the major driver of
  model performance seems to be the **random seed** used for splitting the data.  
  - This tells me that there is an "opportunistic split" for some random seeds where the training and
    validation data have more congruent, harmonious distributions relative to each other.  
  - This gave me the idea to look at devising a stratification strategy for splitting the data, which
    I do in the next JNB. 
  - I started to get hints of this phenomenon in this notebook, but it wasn't until the next 
    notebook that it truly dawned on me.

<!-- #################################################### -->
<!-- #################################################### -->
<!-- #################################################### -->






## 00c: Ensuring Equivalent Population Representations in the Data Splits (a Failure of Random Seeding)

This work was from when we first took the project over from Udi (it began 2019-Oct-23, but the majority of it was done on 2019-Nov-01).

What this means is:

1. the assumption is Udi's data processing pipeline (which extends the first half of Carlos' original pipeline) works well enough
2. therefore, Udi's final outputted data table from this pipeline can be used for analysis.

At one point, Dani and I began questioning these assumptions and started everything from scratch 
(this explains the mbh001_v3 directory in the MBH001 GitLab repo, where I will also store a copy of this JNB for convenience).

**SIDE NOTE**: Starting from scratch was nontrivial since the full data set derives from about 40 tables, some of which (as we found) are not usable or valid data. These tables host a few thousand variables -- again, many of which need to be understood and vetted. I must say, though we originally had (harshly) questioned Carlos' methods (some of which perhaps deserved it) and subsequently Udi's methods (many of which just built on top of Carlos'), we ultimately could not "force" the data to do any better than Udi or Carlos could. It's possible that the strategy and methods used by Udi and Carlos would have borne fruit if there was enough fruit to bear. (More importantly, for better or worse, it's definitely possible that their methods would have been left unquestioned if they were able to capture some signal, independent of whether their methods were janky or suboptimal.)

Anyway, in this notebook, I explore methods that I had hoped would help "stabilize" the patient population between training, validation, and test sets.


### MOTIVATION
Basically, the first thing you will notice when working with this data is that it's very hard to not overfit to training. This is sometimes due to lack or regularization, but other times the problem can start earlier on in the pipeline. For example, in a highly-imbalanced binary classification problem, issues like this can be due to a bad splitting strategy (e.g., if you have a 1% event rate, its possible that a naive splitting strategy will accidentally land all your events in the validation and test sets, making training pointless and fruitless). Though we are doing a regression problem this motivates my major idea.

### IDEA

It is likely that a poor/naive splitting strategy can affect a regresion problem as well, so I adapt the concept of stratified splitting from a categorical target variable to a continuous target.

### RESULTS

* Overall, it seems to help a very little bit, but does not really save the day.
* Importantly, what I found is that any observed performance boosts are almost always due to the random seed used to split the data. To me, this means that there is some opportunistic splitting that we do not understand. That is, though stratifying on the continuous target variable did not prevent this issue, there must be some variable that does -- otherwise a random "random seed" wouldn't suddenly see a performance boost for no reason. One of our goals should be to try to identify this feature, if possible.


<!-- #################################################### -->
<!-- #################################################### -->
<!-- #################################################### -->




