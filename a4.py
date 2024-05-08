# -*- coding: utf-8 -*-
"""a4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p9KRYHfVKT5sRLZVqn2kMFwAFyi42CJE

Perform the following operation using titanic data set.
1. Check how the price of the ticket (column name: &#39;fare&#39;) for each passenger is distributed by plotting a histogram.
2. Plot a box plot for distribution of age with respect to each gender along with the information about whether they survived or not. (Column names : &#39 sex&#39; and &#39;age&#39;)
3. Write observations on the inference from the above statistics.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('titanic.csv')
df

df.describe()

df.info()

df.ndim

df.shape

df.head()

df.tail()

df.dtypes

df.isnull().sum()

pf = df['Age'].mean()
df['Age'].fillna(pf, inplace=True)
df

df['Cabin'] = df['Cabin'].fillna(0)
df

df.isnull().sum()

"""1. Check how the price of the ticket (column name: &#39;fare&#39;) for each passenger is distributed by plotting a histogram."""

sns.countplot(data=df,x='Survived')
plt.show()

sns.countplot(x=df['Sex'])

# 1. Plotting histogram for ticket prices
plt.figure(figsize=(10, 6))
sns.histplot(df['Fare'], bins=20, kde=True)
plt.title('Distribution of Ticket Prices')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

# From the histogram of ticket prices, we can observe the distribution of fares paid by passengers.

"""2. Plot a box plot for distribution of age with respect to each gender along with the information about whether they survived or not. (Column names : &#39 sex&#39; and &#39;age&#39;)"""

# 2. Plotting box plot for age distribution with respect to gender and survival
plt.figure(figsize=(10, 6))
sns.boxplot(x='Sex', y='Age', hue='Survived', data=df)
plt.title('Age Distribution by Gender and Survival')
plt.xlabel('Gender')
plt.ylabel('Age')
#plt.legend(title='Survived', loc='upper right', labels=['No', 'Yes'])
plt.show()

# The box plot for age distribution with respect to gender and survival provides insights into the
# median, quartiles, and outliers in the age distribution for male and female passengers,
# categorized by survival status. We can observe if there are any differences in age distributions
# between male and female passengers who survived or did not survive.

"""3. Write observations on the inference from the above statistics.

From the box plot showing the distribution of age with respect to each gender and grouped by survival status, we can make several observations:

1. **Age Distribution by Gender**:
   - Overall, the age distribution appears slightly wider for males compared to females.
   - The median age for both genders seems to be around the same.
   - The range of ages for females appears to be slightly narrower compared to males.

2. **Survival Status**:
   - For both genders, the box plots show a notable difference in the distribution of age between those who survived and those who did not.
   - Among females, the box plots for both survival statuses appear similar, indicating that age alone might not be a significant factor in predicting survival among females.
   - Among males, the box plot for those who survived seems to have a slightly lower median age and a narrower interquartile range compared to those who did not survive. This suggests that younger males might have had a higher chance of survival compared to older males.

3. **Outliers**:
   - There are outliers present in both groups, particularly among males, indicating that there were individuals of varying ages who did not conform to the general trend.

4. **Gender Disparity**:
   - The plot underscores the societal norm of prioritizing the safety of women and children during emergencies, as evident from the narrower age distribution among females, especially among survivors.

5. **Further Analysis**:
   - It might be beneficial to conduct further statistical analysis to quantify the significance of age and gender in predicting survival on the Titanic, perhaps through logistic regression or other machine learning techniques.

In summary, the box plot provides valuable insights into the relationship between age, gender, and survival status among passengers on the Titanic, suggesting that while age and gender play a role, there are likely other factors at play as well.
"""

sns.histplot(df['Fare'], binwidth=30)
plt.show()

sns.histplot(df, x='Fare',hue='Pclass', binwidth=30)
plt.show()

sns.catplot(data=df, x="Age", y="Sex", hue="Survived", kind="boxen")

sns.catplot(data=df, x="Sex", y="Age")

sns.catplot(
    data=df, x="Sex", y="Age", hue="Survived",
    kind="violin", bw_adjust=.5, cut=0, split=True,
)

sns.catplot(data=df, x="Sex", y="Age", kind="violin", color=".9", inner=None)
sns.swarmplot(data=df, x="Sex", y="Age", size=3)

