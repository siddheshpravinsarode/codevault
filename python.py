import pandas as pd
num=[1,2,3,4,5]
series=pd.Series(num)
print(series.loc[0])
#loc location based on  labels
print(series.iloc[0])
#loc lacation based on index
print(series[series>3])
#filtering the series based on condition


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
dataframe = pd.DataFrame(data)
print(dataframe)
dataframe["Job"] = ["Engineer", "Doctor", "Teacher", "Lawyer"]
new_row = pd.DataFrame({"Name": ["Eve"], "Age": [28], "City": ["San Francisco"], "Job": ["Designer"]})
dataframe = pd.concat([dataframe, new_row], ignore_index=True)
print(dataframe)
newrows= [{"Name": ["Frank"], "Age": [32], "City": ["Seattle"], "Job": ["Manager"]},{"Name": ["Grace"], "Age": [29], "City": ["Boston"], "Job": ["Analyst"]}]

new_row_df = pd.DataFrame(newrows)
talage=dataframe[(dataframe["Age"]==35) & (dataframe["City"]=="Chicago")]
print(talage)

dataframe = pd.concat([dataframe, new_row_df], ignore_index=True)