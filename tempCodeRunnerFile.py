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