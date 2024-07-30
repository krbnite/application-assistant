Some thought on human-machine interactions in machine learning.
 
Just a note on our human-in-the-loop removal project.  By removing injections of human/domain knowledge into the development of a model, we had several aims, e.g.:
(i)                  check if this is possible
(ii)                see if it’s worthwhile
(iii)               investigate whether the human-free model can then be further optimized by introducing human checkpoints at well-thought out entry points
 
As I was saying, ultimately we are building an app (“EaSi Platform”) along with our classification algorithms that can classify events in near-real time (at least on a nightly batch level).  Part of the plan is to have automated, triggered notifications like, “Are you currently walking?”  (when the user appears to be walking).  However, you said someone there will already be covering this.
 
Reducing Incorrect Identifications (FPs, FNs): 
Then I spoke about how I originally started this type of work by looking into automated recognition of psychological states (e.g., stress, anxiety, depression, etc).  Given a suite of psychological and/or physical activity classifications, one can build data products and models that track such quantities continuously in a manner relevant to a given disease or condition.  With a bit more effort, alerts can be triggered automatically for certain events of interest.  However, as is often expected, this is likely to produce a decent amount of false positives.  The clinician/doctor can reduce the number of false positives substantially (and the incurred cost of any subsequent actions that might be taken) by using their expertise to view the various data streams.  In this way, they may also notice events that should have been captured (false negatives).
 
I also spoke about the fact that labeling data is a privileged position to be in.  For many of the things we are interested in learning from wearable data, we do not have labels and it is not easy to get labels.  However, we still require sanity checks, so we rely on “soft labeling efforts” such as a caregiver or patient providing contextual logs throughout the day (or even just once per day at night, for example).  In this scenario, someone might write:  “I was out walking in the afternoon for an hour or so.”   This is not a label, but it does provide enough context for a sanity check:  Does the algorithm identify the interval of time that is likely being referred to?
 
This was just a brain dump.  It might not be 100% clear, so feel free to ask pointed questions for clarification.
