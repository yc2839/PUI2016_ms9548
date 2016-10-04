# Homework 4 README File, Assignment Descriptions / Writeups

## Assignment 1

CitibikeReview_ms9548.md pull request made with https://github.com/athenaxin/PUI2016_xt483/tree/master/HW3_xt483 - a
copy of that file is also in this repository.

## Assignment 2

### Group 1 Statistical Tests Selection / Analysis

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Chi-Squared | 1, Soil Attributes / Properties | Categorical | 1, Pocket Gopher subgenera | Categorical | None | N/A | 	Soil attributes dictate likelihood of the presence of certain subgeneras of Pocket Gophers  | H0: Any soil attributes/properties have the same influence on the presence of certain pocket gopher subgeneras as specific soil attributes / properties   | 0.05 | [Morphological Adaptations for Digging and Climate-Impacted Soil Properties Define Pocket Gopher (Thomomys spp.) Distributions](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0064935) |
  |||||||||

### Group 2 Statistical Tests Selection / Analysis

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
Correlation (Pearson's)	| 1, Type of Test Format Taken (Short Form vs. Long Form) | dichotomous categorical | 1, Performance on test| continuous | None | N/A | 	Short test is equally efficient at predicting executive-function capacity as long test.  | H0: Short Test Efficiency < Long Test Efficiency  | Not Given | [Evaluation of a Short-Form of the Berg Card Sorting Test](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0063885) |
  |||||||||
  
## Assignment 3
  
The "Hard to Employ" analysis was recreated using felony recidivism data from the same report.
  
Idea: Inmates participating in the hard to employ program who have been convicted of a felony are less likely to relapse into criminal behaviour (i.e., recidivism)

Null Hypothesis:  The percent of former prisoners convicted of a felony who relapse into crimininal behavior (i.e., recidivism) within 1 - 3 years after release is the same or higher for candidates who participated in the program as for the control group, significance level p = 0.05 (P1>= P0)

Alternative Hypothesis:  Ther percent of former prisoners convicted of a felony who relapse into criminal behavior (i.e, recidivism) within 1 - 3 years after relase is lower for candidates who participated in the program as for the control level, significance level  p = 0.05 (P1 < P0)

H0: P0 - P1 <= 0

H1: P0 - P1 > 0

α = 0.05

The z-Score was found to be be approximately ~ -0.8 - using the the Standard Normal Distribution Table (http://math.arizona.edu/~rsims/ma464/standardnormaltable.pdf) at a 0.05 significance, a value of 0.19766 was obtained, which was then subtracted from 1 to obtain the p-value, which was 0.80234.  This is larger than the significance threshold (0.05), and, therefore, the Null Hypothesis was not rejected.

Per the assignment, the data was also run through the Chi Square Evalution function provided by the professor, which x^2 value of 0.718493917505.  The x^2 probability at 1 degree of freedom at a 0.05 significance level is 3.84 (per the provided table: http://passel.unl.edu/Image/Namuth-CovertDeana956176274/chi-sqaure%20distribution%20table.PNG).  The x^2 distribution (0.72) is smaller than the probability threshold (3.84) and is therefore not significant at the 0.05 significance level.  And the null hypothesis is not rejected.

This finding should not be surprising - the program group and control group had a relatively similar sample size and the percentage of program participants that experienced recidivism within 1-3 years of release was comparable to its control group counterpart.  Thus, participation in the program had little impact on rates of recidivism.
  
## Assignment 4

I recreated the professor's Citibike Analysis using the June 2015 citibike data.  Note that I used the data acquiring method I used in the related assignment for homework 3, using the zipfile module.  Further, I tried to append the July 2015 dataset in order to use multiple datasets (as suggested by the instructions), but that was giving me duplication errors later in the analysis that I couldn't solve so I abandoned that approach, only using June 2015 data.


##  Idea:  Proportionally more men use citibike than women (P0 > P1)
##  Null Hypothesis:  The proportion of women who use citibike is equal to or greater than that of men(H0: P1 - P0 <= 0)
##  Alt Hypothesis:  Proportionally more men use citibike than women (H1: P0 - P1 > 0)
##  α = 0.05

After recreating the professor's analysis, I used the the three tests identified in the assignment including:

Kolmogorov–Smirnov Test (for the full sample and for a subsample of 1 every 200 records)
Pearsons Correlation Test (equal sized male and female samples, sorted)
Spearman's Correlation Test (equal sized male and female samples, sorted)

### Analysis Results

#### Kolmogorov–Smirnov Test (Full Dataset)

At a significance level of 0.05, the critical KS value is 1.36 (in the table provided in the example text).  The calculated KS statistic is approximate;y 0.102, much lower than the critical value.  Because it is lower than the threshold, we cannot reject the Null Hypothesis

#### Kolmogorov–Smirnov Test (Sub Dataset)

At a significance level of 0.05, the critical KS value is 1.36 (in the table provided in the example text).  The calculated KS statistic is approximate;y 0.113, much lower than the critical value.  Because it is lower than the threshold, we cannot reject the Null Hypothesis.

#### Pearsons Correlation Test

The calculated pearson's coefficient is approximately 0.997, indicating a very strong positive relationship between the two variables (a calculated coefficient of 1 indicating the strong possible correlation).  Under this condtion, it would be expected that as one variable increases, the other would too (and as one decreased, the other one would as well).  Regarding the Null Hypothesis, this relationship indicates that the proportional number of male riders would be relatively equal to the proportion of female riders (i.e., P0 = P1), so the Null cannot be rejected using the results of this test.

The p-value indicated the probability of the results of the test being random.  The calculated p-value for this analysis is 0, which states a 0 % chance these results are random.

#### Pearsons Correlation Test

Similar to the pearson's coefficient, the spearmen's coefficient indicates a very high positive correlation (0.999), which indicates that as one variable increases the other would be expected to as well.  Regarding the Null Hypothesis, this relationship indicates that the proportional number of male riders would be relatively equal to the proportion of female riders (i.e., P0 = P1), so the Null cannot be rejected using the results of this test.

The p-value indicated the probability of the results of the test being random.  The calculated p-value for this analysis is 0, which states a 0 % chance these results are random.
