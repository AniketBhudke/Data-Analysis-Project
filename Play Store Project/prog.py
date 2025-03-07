import pandas as pd
# 1. Find Total Number Apps in Google Play Store
#--------------------------------------------------------------------------------------------------------
df=pd.read_csv("D:\\Data Analysis Project\\Play Store Project\\googleplaystore.csv")
print(df)

# a=df["App"].count()
# print("Total Count Of Apps In Google Play Store Is: ",a)
#--------------------------------------------------------------------------------------------------------

# 2. Find the Total Number of Columns in Each app of Google Play Store
# --------------------------------------------------------
# df["Total Columns"]=len(df.columns)
# print(df[["App","Total Columns"]])

# print("count of total count in apps:",df['Total Columns'].sum())


# 1. Display Top 5 Rows of The Dataset


# 2. Check the Last 3 Rows of The Dataset
# 3. Find Shape of Our Dataset (Number of Rows & Number of Columns)
# 4. Get Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column 
#    And  Memory Requirement
# 5. Get Overall Statistics About The Dataframe OR Get the Descriptive Statistics about Google Play Store
# 6. Obtain Total Number of App Titles Contain Astrology
# 7. Find Average App Rating
# 8.  Find Total Number of Unique Category
# 9. Which Category Getting The Highest Average Rating?
# 10. Find Total Number of App having 5 Star Rating
