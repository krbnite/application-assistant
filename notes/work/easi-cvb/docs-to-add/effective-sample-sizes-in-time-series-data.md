Email written to EaSi team on: 2018-10-04

-----------



Hi all – I wanted to share some of my experience on this topic that came up today during the SleepWell discussion on the EarlySense data. 
 
When dealing with time series data, various statistical tests and methods can still be used, but must be modified to account for the correlation structure within the time series.  This is because such correlation structure violates the usual assumption of independent and identically-distributed (IID) random samples.  Neighboring measurements are not purely random: there is a deterministic component involved – a relationship between samples that destroys sample independence.
 
For example, imagine that the timescale at which the temperature of a room regularly oscillates is about 12 hours, slowly fluctuating between 68-72*F over the course of this time.  Now imagine sampling the temperature every minute for two hours… At the end of the two hours, we have a lot of data points, but what do we actually know about the mean or variance of this time series?  Though we have 120 data points, we do not have 120 bits of independent information. 
 
So how many bits of information do we have?  Answer: almost zero!
 
The actual amount of information we have is inversely proportional to the correlation time, N à N_eff = N/(1 + 2τ).  In other words, you can pretend that instead of having N correlated data points, you actually have N_eff independent data points. In our case N=2*60.  Assuming that the correlation time is about 12 hours, we have τ = 12*60 and N_eff = 2*60 / (1 + 2*12*60) ~= 1/12 ~= 0.08. 
 
In other words, we’ve collected almost no information about the time series :-p
 
This has important ramification about estimating things like the mean and standard deviation of the time series, for estimating confidence intervals, hypothesis testing, etc.  And that is how this ties in to the EarlySense data and the SleepWell project: Friso is interested in knowing how much data we must collect from how many patients.  The statisticians are pointing out that, due to the correlation structure of sleep (“if you are sleeping now, you are more likely to be sleeping 30 seconds from now than awake”), the number of independent samples in the data is effectively lower than the amount of data samples we actually have – and this impacts the power analysis. 
 
So why might the raw data be important?  Well, the raw data could allow the statisticians to estimate the correlation time of the various time series at play, and thus adjust the equations being used to estimate confidence intervals, etc.  Theoretically, the correlation time is the integrated/summed autocorrelation function: 
 
```
# was a picture
tau = sum(k=l:inf) rho[k]
```

In practice, there are several ways to estimate τ – e.g., A Comparison of Methods for Computing Autocorrelation Time [2010] or Effective Sample Size of the Cumulative Values of a Time Series [2017]. 
