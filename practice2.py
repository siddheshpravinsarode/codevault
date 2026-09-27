import pandas as pd
import numpy as np


# ============================================================
# 19. QUERY()
# ============================================================

# Filter rows using a string condition
result = df.query("Lead_Time_Days > 30")

print(result)


# Multiple conditions
result = df.query(
    "Lead_Time_Days > 30 and Disruption_Occurred == 1"
)

print(result)


# String value inside query
result = df.query(
    "Origin_Port == 'Singapore'"
)

print(result)


# ============================================================
# 20. SORTING
# ============================================================

# Sort by lead time
result = df.sort_values("Lead_Time_Days")

print(result)


# Highest lead time first
result = df.sort_values(
    "Lead_Time_Days",
    ascending=False
)

print(result)


# Sort using multiple columns
result = df.sort_values(
    ["Origin_Port", "Lead_Time_Days"],
    ascending=[True, False]
)

print(result)


# ============================================================
# 21. DUPLICATES
# ============================================================

# Check which rows are duplicates
print(df.duplicated())


# Count duplicate rows
print(df.duplicated().sum())


# Remove duplicate rows
result = df.drop_duplicates()

print(result)


# Check duplicates based on one column
print(df.duplicated("Shipment_ID").sum())


# Remove duplicates based on Shipment_ID
result = df.drop_duplicates(
    subset=["Shipment_ID"]
)

print(result)


# ============================================================
# 22. MISSING VALUES
# ============================================================

# Count missing values in every column
print(df.isnull().sum())


# Percentage of missing values
missing_percentage = (
    df.isnull().sum() / len(df)
) * 100

print(missing_percentage)


# Remove rows containing missing values
result = df.dropna()

print(result)


# Remove rows only when Lead_Time_Days is missing
result = df.dropna(
    subset=["Lead_Time_Days"]
)

print(result)


# Fill missing numerical values with median
df["Lead_Time_Days"] = df["Lead_Time_Days"].fillna(
    df["Lead_Time_Days"].median()
)


# Fill missing values with a fixed value
df["Carrier_Reliability_Score"] = df[
    "Carrier_Reliability_Score"
].fillna(0)


# ============================================================
# 23. MAP()
# ============================================================

# Convert 0/1 disruption into readable labels
df["Disruption_Label"] = df[
    "Disruption_Occurred"
].map({
    0: "No",
    1: "Yes"
})

print(df)


# ============================================================
# 24. REPLACE()
# ============================================================

# Replace specific values
df["Disruption_Occurred"] = df[
    "Disruption_Occurred"
].replace({
    0: "No",
    1: "Yes"
})

print(df)


# ============================================================
# 25. APPLY()
# ============================================================

# Create a custom classification
def classify_lead_time(x):

    if x < 10:
        return "Low"

    elif x < 30:
        return "Medium"

    else:
        return "High"


df["Lead_Time_Category"] = df[
    "Lead_Time_Days"
].apply(classify_lead_time)

print(df)


# ============================================================
# 26. LAMBDA WITH APPLY()
# ============================================================

# Create a new column using a simple calculation
df["Reliability_Percentage"] = df[
    "Carrier_Reliability_Score"
].apply(
    lambda x: x * 100
)

print(df)


# ============================================================
# 27. np.where()
# ============================================================

# Create a column using a condition
df["High_Risk"] = np.where(
    df["Disruption_Occurred"] == 1,
    "Yes",
    "No"
)

print(df)


# Multiple conditions using np.select()
conditions = [
    df["Lead_Time_Days"] < 10,
    df["Lead_Time_Days"] < 30,
    df["Lead_Time_Days"] >= 30
]

choices = [
    "Low",
    "Medium",
    "High"
]

df["Lead_Time_Category"] = np.select(
    conditions,
    choices
)

print(df)


# ============================================================
# 28. TRANSFORM() 🔥
# ============================================================

# Calculate average lead time for each port
# and put that average beside EVERY row of that port
df["Port_Average_Lead_Time"] = df.groupby(
    "Origin_Port"
)["Lead_Time_Days"].transform("mean")

print(df)


# Difference between each shipment's lead time
# and its port's average
df["Difference_From_Port_Average"] = (
    df["Lead_Time_Days"]
    - df["Port_Average_Lead_Time"]
)

print(df)


# ============================================================
# 29. GROUPBY + TRANSFORM FOR NORMALIZATION
# ============================================================

# Calculate average reliability for each port
df["Port_Average_Reliability"] = df.groupby(
    "Origin_Port"
)["Carrier_Reliability_Score"].transform("mean")

print(df)


# ============================================================
# 30. RANKING
# ============================================================

# Rank shipments based on lead time
df["Lead_Time_Rank"] = df[
    "Lead_Time_Days"
].rank(
    ascending=False
)

print(df)


# Rank within each origin port
df["Port_Lead_Time_Rank"] = df.groupby(
    "Origin_Port"
)["Lead_Time_Days"].rank(
    ascending=False
)

print(df)


# ============================================================
# 31. Nlargest / Nsmallest
# ============================================================

# 10 shipments with highest lead time
result = df.nlargest(
    10,
    "Lead_Time_Days"
)

print(result)


# 10 shipments with lowest lead time
result = df.nsmallest(
    10,
    "Lead_Time_Days"
)

print(result)


# ============================================================
# 32. PIVOT TABLE 🔥
# ============================================================

# Average lead time for each origin
# and disruption status
result = pd.pivot_table(
    df,
    values="Lead_Time_Days",
    index="Origin_Port",
    columns="Disruption_Occurred",
    aggfunc="mean"
)

print(result)


# Multiple aggregations
result = pd.pivot_table(
    df,
    values="Lead_Time_Days",
    index="Origin_Port",
    aggfunc=["mean", "max", "min"]
)

print(result)


# ============================================================
# 33. CROSSTAB
# ============================================================

# Count combinations of Origin_Port and disruption
result = pd.crosstab(
    df["Origin_Port"],
    df["Disruption_Occurred"]
)

print(result)


# Percentage instead of count
result = pd.crosstab(
    df["Origin_Port"],
    df["Disruption_Occurred"],
    normalize="index"
)

print(result)


# ============================================================
# 34. MERGE / JOIN 🔥🔥
# ============================================================

# Example second DataFrame

carrier_data = pd.DataFrame({
    "Origin_Port": [
        "Singapore",
        "Busan",
        "Rotterdam",
        "Houston"
    ],
    "Region": [
        "Asia",
        "Asia",
        "Europe",
        "USA"
    ]
})


# Merge the two DataFrames
result = pd.merge(
    df,
    carrier_data,
    on="Origin_Port",
    how="left"
)

print(result)


# INNER JOIN
result = pd.merge(
    df,
    carrier_data,
    on="Origin_Port",
    how="inner"
)

print(result)


# LEFT JOIN
result = pd.merge(
    df,
    carrier_data,
    on="Origin_Port",
    how="left"
)

print(result)


# ============================================================
# 35. MERGE USING DIFFERENT COLUMN NAMES
# ============================================================

carrier_data = pd.DataFrame({
    "Port": [
        "Singapore",
        "Busan",
        "Rotterdam"
    ],
    "Region": [
        "Asia",
        "Asia",
        "Europe"
    ]
})

result = pd.merge(
    df,
    carrier_data,
    left_on="Origin_Port",
    right_on="Port",
    how="left"
)

print(result)


# ============================================================
# 36. CONCAT
# ============================================================

df1 = df.iloc[:100]
df2 = df.iloc[100:200]

# Combine rows
result = pd.concat(
    [df1, df2],
    axis=0
)

print(result)


# Combine columns
result = pd.concat(
    [df1, df2],
    axis=1
)

print(result)


# ============================================================
# 37. RESET INDEX
# ============================================================

result = df.groupby(
    "Origin_Port"
)["Lead_Time_Days"].mean()

print(result)

# Convert index back into normal column
result = result.reset_index()

print(result)


# ============================================================
# 38. SET INDEX
# ============================================================

df_indexed = df.set_index(
    "Shipment_ID"
)

print(df_indexed)


# Access using index
result = df_indexed.loc["SC-10000"]

print(result)


# ============================================================
# 39. DATETIME FEATURES 🔥
# ============================================================

df["Date"] = pd.to_datetime(
    df["Date"]
)


# Extract year
df["Year"] = df["Date"].dt.year


# Extract month
df["Month"] = df["Date"].dt.month


# Extract day
df["Day"] = df["Date"].dt.day


# Extract weekday
df["Weekday"] = df["Date"].dt.day_name()


print(df)


# ============================================================
# 40. DATE GROUPING
# ============================================================

# Average lead time by year
result = df.groupby(
    df["Date"].dt.year
)["Lead_Time_Days"].mean()

print(result)


# Average lead time by month
result = df.groupby(
    df["Date"].dt.month
)["Lead_Time_Days"].mean()

print(result)


# ============================================================
# 41. CORRELATION 🔥
# ============================================================

# Correlation between numerical columns
result = df[
    [
        "Carrier_Reliability_Score",
        "Lead_Time_Days",
        "Disruption_Occurred"
    ]
].corr()

print(result)


# ============================================================
# 42. DESCRIPTIVE STATISTICS
# ============================================================

# Statistics for numerical columns
print(df.describe())


# Mean
print(df["Lead_Time_Days"].mean())


# Median
print(df["Lead_Time_Days"].median())


# Standard deviation
print(df["Lead_Time_Days"].std())


# Variance
print(df["Lead_Time_Days"].var())


# Minimum
print(df["Lead_Time_Days"].min())


# Maximum
print(df["Lead_Time_Days"].max())


# ============================================================
# 43. MEMORY / DATA TYPES
# ============================================================

# Check data types
print(df.dtypes)


# Complete information
df.info()


# ============================================================
# 44. CHANGE DATA TYPE
# ============================================================

# Convert column to numeric
df["Lead_Time_Days"] = pd.to_numeric(
    df["Lead_Time_Days"],
    errors="coerce"
)


# Convert column to integer
# Only use this if there are no NaN values
# df["SomeColumn"] = df["SomeColumn"].astype(int)


# Convert to string
df["Shipment_ID"] = df[
    "Shipment_ID"
].astype(str)


# ============================================================
# 45. NORMALIZE A COLUMN
# ============================================================

# Min-Max normalization
minimum = df["Lead_Time_Days"].min()
maximum = df["Lead_Time_Days"].max()

df["Lead_Time_Normalized"] = (
    (df["Lead_Time_Days"] - minimum)
    / (maximum - minimum)
)

print(df)


# ============================================================
# 46. Z-SCORE STANDARDIZATION
# ============================================================

mean = df["Lead_Time_Days"].mean()
std = df["Lead_Time_Days"].std()

df["Lead_Time_ZScore"] = (
    (df["Lead_Time_Days"] - mean)
    / std
)

print(df)


# ============================================================
# 47. DUPLICATE / UNIQUE ANALYSIS
# ============================================================

# Number of unique shipment IDs
print(df["Shipment_ID"].nunique())


# Check whether every Shipment_ID is unique
print(df["Shipment_ID"].is_unique)


# ============================================================
# 48. TOP PORT BY NUMBER OF SHIPMENTS
# ============================================================

result = df["Origin_Port"].value_counts()

print(result)

top_port = result.index[0]

print("Top port:", top_port)


# ============================================================
# 49. TOP PORT BY AVERAGE LEAD TIME
# ============================================================

result = df.groupby(
    "Origin_Port"
)["Lead_Time_Days"].mean().sort_values(
    ascending=False
)

print(result)

print("Highest average lead time:")
print(result.index[0])


# ============================================================
# 50. OA-STYLE COMPLETE QUESTION
# ============================================================

# Find ports where:
#
# 1. Average reliability > 0.7
# 2. Average lead time > 25
#
# Then sort by average lead time.

result = df.groupby("Origin_Port").agg(
    Average_Reliability=(
        "Carrier_Reliability_Score",
        "mean"
    ),
    Average_Lead_Time=(
        "Lead_Time_Days",
        "mean"
    )
)

result = result[
    (result["Average_Reliability"] > 0.7) &
    (result["Average_Lead_Time"] > 25)
]

result = result.sort_values(
    "Average_Lead_Time",
    ascending=False
)

print(result)