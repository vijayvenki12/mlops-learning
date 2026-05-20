import pandas as pd

# Load dataset
df=pd.read_csv("titanic.csv")

# Basic cleaning
df = df.dropna(thresh=len(df.columns)*0.5)

#Fill missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("Data cleaned and saved!")
