# Homework 1

## Assignment 1
The code generates 100 samples of random sizes (sized > 10 and < 2000) from five different probability distributions, including Chi-Square, Poisson, Normal / Gaussian, Binomial, and Standard Gamma (student chosen) distribtions, all with a mean set to 100.  The results for each distribution were plotted in scatter plots (rendered in the ipython notebook), as well as the combined means on a histogram (all rendered).  Generally, the scatter plots and histgram show an increasing density of clustering values around the 100 value, which is to be expected as a the total number of samples is relatively large and is therefore consistent with the central limit theorem.

## Assignment 2
The code downloades February 2015 citibike data from the CUSP Data Facility and imports it into a pandas dataframe (downloading a zip file and unziping help / code provided by Bailey Griswold and from http://stackoverflow.com/questions/17142304/replace-string-value-in-entire-dataframe.  Our Team (including myself, Kelsey Reid, Marc Toneatto, and Ozgur Akkas) worked on formulating the following Null / Alt Hypothesis:
Idea - Subscribed users may be using citibike to commute during the weekdays and therfore using citibikes more.
Null Hypothesis - Nonsubscribers use citibikes during the week as much as or more than subscribers
Alternative Hypothesis - Subscribers are more likely to use citibikes during the week(sigma = 0.05, 95% certainty)
The code reducts the datafram down to the two necessary variables (user type and start time) - the usestype was converted to categorial data via the "replace" pandas method, and the start time data was converted to a readable format via the professor's sample code. These were then plotted on a histogram.

## Assignment 3
The new bus times csv file was imported and the "times" data was saved into a numpy array using the as_matrix method (obtained from: http://stackoverflow.com/questions/31789160/convert-select-columns-in-pandas-dataframe-to-numpy-array).  The mean of that was calculated using the .mean() method and that was applied using the z-Value formula using the "existing" data the professor provided.  The calculated z-value was approxiately 2.5, i.e., the difference in bus times between the old and new routes was greater than two standard deviations, indicating that, with 95% certainty, the shorter bus times are a result of new bus route and are not random.
