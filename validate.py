import pandas as pd
import re

df = pd.read_csv("fake_leads.csv")

# remove duplicates
df = df.drop_duplicates(subset=["Email"])

pattern = re.compile(r'^\(\d{3}\)\s\d{3}-\d{4}$')

# Validate phones
df["IsValidPhone"] = df["Phone"].apply(lambda x: bool(pattern.match(str(x).strip())))

# Filter valid numbers only
valid_df = df[df["IsValidPhone"] == True]

# Save valid data
valid_df.to_csv("validated_leads.csv", index=False)

print(f"Validation complete! {len(valid_df)} valid rows saved to validated_leads.csv")
print(valid_df.head())
