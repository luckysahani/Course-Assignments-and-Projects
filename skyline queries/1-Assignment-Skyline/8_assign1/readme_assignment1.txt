Th total time shows that the performance of SFS method becomes better or almost the same for anti-corelated data and independent data.In the coorelated datasets, the skyline can fit in memory,hence BNL requires only few passes,while SFS waste time sorting the data.
However, the total number of comparisions will always be less in SFS,as compared to that of BNL.

Analysis:
=============================================================
CORRELATED DATASET:
------------------------------------------------------------

BNL: 
Total running time(ms) = 4 
Number of object-to-object comparisons =  1603 
Size of skyline set =  13 

SFS:
Total running time(ms) = 6 
Number of object-to-object comparisons =  1101 
Size of skyline set =  13

ANTI-CORRELATED DATASET:
------------------------------------------------------------

BNL: 
Total running time(ms) = 443 
Number of object-to-object comparisons =  335269 
Size of skyline set =  705

SFS:
Total running time(ms) = 338 
Number of object-to-object comparisons =  265134 
Size of skyline set =  705 

INDEPENDENT DATASET:
------------------------------------------------------------

BNL: 
Total running time(ms) = 60 
Number of object-to-object comparisons =  35477 
Size of skyline set =  166 

SFS:
Total running time(ms) = 31 
Number of object-to-object comparisons =  17201 
Size of skyline set =  166 

Overall , we can say that performance of SFS is better than BNL in terms of number of comparisions.