## Assignment 1
Note:  Code formulated in conjunction with Kelsey Reid, William Xia, and Marc Toneatto, as well as following sample code provided 
by yw2278

This assignment pulled data from the "Manhattan MapPLUTO" shapefile and the "Energy and Water Data Disclosure for Local Law 84" csv
file, both provided New York City.  Both of these files were imported to pandas dataframes, cleaned / edited and then merged on the 
Borough / Block / Lot field.  The total energy usage vs. residential units relation was then analyzed, using scatterplotting both in their
base units and log plotting.  The best fit was then investigated by analyzing the data using the energy usage as the dependent variable
and residential units as the dependent variable separately for linear fits - it was found that the fit was better when energy usage 
was utilized as such.  A polynomial fit was then applied, and, using the likelihood ratio at a 0.05 significance level, the ratio 
exceeded the critical value, which rejected the Null Hypothesis (that linear fitting was the best fitting method for the data).




## Assignment 2

Authorea link: https://www.authorea.com/users/106219/articles/134338/_show_article?access_token=8Nww4GhkDJi3rmQq1Ec2pw
