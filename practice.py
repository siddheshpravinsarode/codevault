import pandas as pd

# Load your dataset
df = pd.read_csv("global_supply_chain_risk_2026.csv")


# ============================================================
# 1. BASIC FILTERING
# ============================================================

# Shipments where Lead_Time_Days is greater than 30
result = df[df["Lead_Time_Days"] > 30]
print(result)


# Shipments where Lead_Time_Days is less than 10
result = df[df["Lead_Time_Days"] < 10]
print(result)


# Shipments originating from Singapore
result = df[df["Origin_Port"] == "Singapore"]
print(result)


# Shipments where disruption occurred
result = df[df["Disruption_Occurred"] == 1]
print(result)


# Shipments where no disruption occurred
result = df[df["Disruption_Occurred"] == 0]
print(result)


# ============================================================
# 2. MULTIPLE CONDITIONS
# ============================================================

# Singapore AND Lead_Time_Days > 30
result = df[
    (df["Origin_Port"] == "Singapore") &
    (df["Lead_Time_Days"] > 30)
]
print(result)


# Singapore OR Busan
result = df[
    (df["Origin_Port"] == "Singapore") |
    (df["Origin_Port"] == "Busan")
]
print(result)


# Lead time between 10 and 30
result = df[
    (df["Lead_Time_Days"] >= 10) &
    (df["Lead_Time_Days"] <= 30)
]
print(result)


# Disrupted shipments with Lead_Time_Days > 30
result = df[
    (df["Disruption_Occurred"] == 1) &
    (df["Lead_Time_Days"] > 30)
]
print(result)


# Reliability score >= 0.8
result = df[
    df["Carrier_Reliability_Score"] >= 0.8
]
print(result)


# Reliability < 0.7 AND disruption occurred
result = df[
    (df["Carrier_Reliability_Score"] < 0.7) &
    (df["Disruption_Occurred"] == 1)
]
print(result)


# ============================================================
# 3. isin()
# ============================================================

# Shipments from Singapore OR Busan
result = df[
    df["Origin_Port"].isin(["Singapore", "Busan"])
]
print(result)


# Shipments NOT from Singapore or Busan
result = df[
    ~df["Origin_Port"].isin(["Singapore", "Busan"])
]
print(result)


# Shipments from three ports
result = df[
    df["Origin_Port"].isin(
        ["Singapore", "Busan", "Rotterdam"]
    )
]
print(result)


# ============================================================
# 4. STRING FILTERING
# ============================================================

# Shipment IDs starting with "SC"
result = df[
    df["Shipment_ID"].str.startswith("SC")
]
print(result)


# Origin port containing the word "sing"
result = df[
    df["Origin_Port"].str.contains(
        "sing",
        case=False,
        na=False
    )
]
print(result)


# ============================================================
# 5. DATE FILTERING
# ============================================================

# Convert Date column into datetime
df["Date"] = pd.to_datetime(df["Date"])


# Shipments after January 1, 2025
result = df[
    df["Date"] > "2025-01-01"
]
print(result)


# Shipments between January and June 2025
result = df[
    (df["Date"] >= "2025-01-01") &
    (df["Date"] <= "2025-06-30")
]
print(result)


# ============================================================
# 6. FILTER + SELECT COLUMNS
# ============================================================

# Disrupted shipments
# Display only ID, origin and lead time
result = df.loc[
    df["Disruption_Occurred"] == 1,
    ["Shipment_ID", "Origin_Port", "Lead_Time_Days"]
]

print(result)


# Lead time > 30
# Display only ID, carrier reliability and lead time
result = df.loc[
    df["Lead_Time_Days"] > 30,
    [
        "Shipment_ID",
        "Carrier_Reliability_Score",
        "Lead_Time_Days"
    ]
]

print(result)


# ============================================================
# 7. GROUPBY - BASIC AGGREGATION
# ============================================================

# Average lead time for each origin port
result = df.groupby("Origin_Port")["Lead_Time_Days"].mean()
print(result)


# Total lead time for each origin port
result = df.groupby("Origin_Port")["Lead_Time_Days"].sum()
print(result)


# Maximum lead time for each origin port
result = df.groupby("Origin_Port")["Lead_Time_Days"].max()
print(result)


# Minimum lead time for each origin port
result = df.groupby("Origin_Port")["Lead_Time_Days"].min()
print(result)


# Number of shipments from each origin port
result = df.groupby("Origin_Port")["Shipment_ID"].count()
print(result)


# ============================================================
# 8. GROUPBY + MULTIPLE AGGREGATIONS
# ============================================================

# Calculate mean, minimum and maximum lead time
# for each origin port
result = df.groupby("Origin_Port")["Lead_Time_Days"].agg(
    ["mean", "min", "max"]
)

print(result)


# Multiple statistics for reliability score
result = df.groupby("Origin_Port")[
    "Carrier_Reliability_Score"
].agg(
    ["mean", "min", "max"]
)

print(result)


# ============================================================
# 9. GROUPBY MULTIPLE COLUMNS
# ============================================================

# Average lead time for each Origin_Port
# based on whether disruption occurred
result = df.groupby(
    ["Origin_Port", "Disruption_Occurred"]
)["Lead_Time_Days"].mean()

print(result)


# Number of shipments for each origin
# and disruption status
result = df.groupby(
    ["Origin_Port", "Disruption_Occurred"]
)["Shipment_ID"].count()

print(result)


# ============================================================
# 10. GROUPBY + AGG() WITH DIFFERENT FUNCTIONS
# ============================================================

# Calculate different statistics for different columns
result = df.groupby("Origin_Port").agg({
    "Lead_Time_Days": ["mean", "min", "max"],
    "Carrier_Reliability_Score": ["mean", "min", "max"],
    "Shipment_ID": ["count"]
})

print(result)


# ============================================================
# 11. NAMED AGGREGATION
# ============================================================

# Give meaningful names to the output columns
result = df.groupby("Origin_Port").agg(
    Average_Lead_Time=("Lead_Time_Days", "mean"),
    Maximum_Lead_Time=("Lead_Time_Days", "max"),
    Average_Reliability=("Carrier_Reliability_Score", "mean"),
    Number_of_Shipments=("Shipment_ID", "count")
)

print(result)


# ============================================================
# 12. FILTER FIRST, THEN GROUPBY
# ============================================================

# First keep only disrupted shipments
# Then calculate average lead time for each port
result = df[
    df["Disruption_Occurred"] == 1
].groupby("Origin_Port")[
    "Lead_Time_Days"
].mean()

print(result)


# Singapore and Busan only
# Then calculate average lead time
result = df[
    df["Origin_Port"].isin(["Singapore", "Busan"])
].groupby("Origin_Port")[
    "Lead_Time_Days"
].mean()

print(result)


# ============================================================
# 13. GROUPBY + SORT
# ============================================================

# Average lead time by port
# Then sort from highest to lowest
result = df.groupby("Origin_Port")[
    "Lead_Time_Days"
].mean().sort_values(ascending=False)

print(result)


# ============================================================
# 14. FILTER + GROUPBY + AGGREGATION
# ============================================================

# Disrupted shipments with reliability > 0.7
# Then calculate average lead time by port
result = df[
    (df["Disruption_Occurred"] == 1) &
    (df["Carrier_Reliability_Score"] > 0.7)
].groupby("Origin_Port")[
    "Lead_Time_Days"
].mean()

print(result)


# ============================================================
# 15. VALUE COUNTS
# ============================================================

# Number of shipments from each port
result = df["Origin_Port"].value_counts()
print(result)


# Percentage of shipments from each port
result = df["Origin_Port"].value_counts(
    normalize=True
) * 100

print(result)


# Number of disrupted vs non-disrupted shipments
result = df["Disruption_Occurred"].value_counts()
print(result)


# Percentage of disrupted vs non-disrupted shipments
result = df["Disruption_Occurred"].value_counts(
    normalize=True
) * 100

print(result)


# ============================================================
# 16. UNIQUE VALUES
# ============================================================

# Show all unique origin ports
print(df["Origin_Port"].unique())


# Count number of unique origin ports
print(df["Origin_Port"].nunique())


# ============================================================
# 17. COMPLEX OA-STYLE QUESTIONS
# ============================================================

# Singapore OR Busan
# Reliability > 0.75
# Disruption occurred
result = df[
    (df["Origin_Port"].isin(["Singapore", "Busan"])) &
    (df["Carrier_Reliability_Score"] > 0.75) &
    (df["Disruption_Occurred"] == 1)
]

print(result)


# Find average lead time for disrupted shipments
# for each origin port
result = df[
    df["Disruption_Occurred"] == 1
].groupby("Origin_Port").agg(
    Average_Lead_Time=("Lead_Time_Days", "mean"),
    Maximum_Lead_Time=("Lead_Time_Days", "max"),
    Number_of_Shipments=("Shipment_ID", "count")
)

print(result)


# Find the average reliability and average lead time
# for every origin port
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

print(result)


# ============================================================
# 18. RESET INDEX
# ============================================================

# groupby normally creates a grouped index
result = df.groupby("Origin_Port")[
    "Lead_Time_Days"
].mean()

# Convert the index back into a normal column
result = result.reset_index()

print(result)


