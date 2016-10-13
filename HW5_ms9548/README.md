## Assignment 1

In this assignment, the age distribution for the June 2015 citibike data was tested as a normal and logistic distribution using the Kolmogorov-Smirnov (KS) and Anderson Darling (AD) tests.  Two Null Hypothesis were developed for each distribution and tested:

### Gaussian / Normal Distribution Null Hypothesis

Null Hypothesis (HO): The data follows a normal / gaussian distribution
Alternative Hypothesis (HA): The data does not follow a normal / gaussian distribution
Significance Level - 0.05

Both the KS and AD goodness of fit tests demonstrated that their respective statistics exceeded their associated critical value at the 0.05 significance level, and therefore the Null Hypothesis is rejected.

### Logistic Distribution Null Hypothesis

Null Hypothesis (HO): The data follows a logistic distribution
Alternative Hypothesis (HA): The data does not follow a logistic distribution
Significance Level - 0.05

Both the KS and AD goodness of fit tests demonstrated that their respective statistics exceeded their associated critical value at the 0.05 significance level, and therefore the Null Hypothesis is rejected.

## Assignment 2

The census was read into respective separate dictionaries with appropriate key identifiers, then concatenated into all male and all female data sets.  Scatter plots were generated of total female median income versus male median income for all races considered (white, black, asian, hispanic, and all ethnicities).  Several regression lines were plotted on the scatter plot, including a 1-1 line, best fit line, and ordinary least squares regression, in order to develop tools to estimate comparisons for male vs. female pay.  

NOTE:  From part 4 of the asssignment on (Best Fit Line through the end) I relied heavily on William Xia's code, because I had no idea how to really approach these portions.  Usually, I have some idea of how to tackle the assignments, and can at least develop a stab at the code that needs some guidance / tweeks to be complete.  In this case, I really was lost and I did my best to research approaches and all of that.  I'm not going to make excuses, but to be transparent I thought it a stretch to go from what we covered in class to what was expected in the second half of this assignment.  Even William Xia's code that I borrowed was cited from someone else who apparently is very versed is python / statistics (not sure who, I'm sure William cited correctly in his README markdown).

Maybe I just need to review some more materials - 

## Assignment 3

### Do diets help lose more fat than the exercise?

Diet - P0  (Test)

Exercise - P1 (Control)

Null Hypowthesis (HO): Exercise help lose just as much or more fat than dieting (P0 - P1 <= 0).

Alt Hypothesis (HA): Diets help lose more fat than exervise (P0 - P1 > 0).

### Do American trust the president?

Trust - P0

No Trust - P1

Null Hypothesis (HO): The number of Americans who do not trust the president is greater than or equal to those who do trust the president (P0 - P1 <= 0).

Alt Hypothesis (HA):  THe number of Americans who trust the president is greater than the number of Americans who do not trust the president (P0 - P1 > 0).

### Effectiveness of nicotine patches to quit smoking

Nictone Patch - P0

Placebo - P1

Null Hypothesis (HO): Smoking cessation rates among placebo recipients are equal to or greater than cessation rates among nicotine patch recipients (P0 - P1 <= 0).

Alt Hypothesis (HA): Cessation rates among nicotine patch users are greater than cessation rates among placebo recipients (P0 - P1 > 0).

### Quantify the danger of smoking for pregnant women.

IQ levels among 1 - 4 year olds whose mother smoked during pregnancy (P0)

IQ levels among 1 - 4 year olds whose mother did not smoke during pregnancy (P1)

Null Hypothesis (H0): IQ levels among 1-4 year olds whose mother smoked during pregnancy are greater than or equal to IQ levels of 1-4 year olds of mothers who did not smoke during pregnancy (P0 - P1 >= 0).

Alt Hypothesis (HA): IQ levels among 1-4 year olds whose mother smoked during pregnancy are less than the IQ levels of 1-4 year olds of mothers who did not smoke (P0 - P1 < 0).


