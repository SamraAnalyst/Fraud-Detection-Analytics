import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

print("--- Step 1: Synthesizing Application Data Flow ---")

data = {
    "Name": ["Samra mahboob", "ahmed khan", "fake user", "sana malik", "bot account"],
    "Age": [23, 26, -5, 24, 150],
    "Submissions_Per_Min": [1, 2, 45, 1, 60]

}
df = pd.DataFrame(data)
print(df)

print("\n--- Step 2: Fixing the Logical Age Duplication Bug ---")
df.loc[((df["Age"] < 0) | (df["Age"] > 100)), "Age"] = 23

print("\n--- Step 3: Text Standardization ---")
df["Name"] = df["Name"].str.title()

print("\n--- Step 4: Machine Learning Anomaly (Fraud) Detection ---")

features = df[["Age", "Submissions_Per_Min"]]
model = IsolationForest(contamination=0.4, random_state=42)
model.fit(features)
df["Fraud_Status_Code"] = model.predict(features)
df["Analysis_Result"] = df["Fraud_Status_Code"].apply(lambda x: "REAL" if x == 1 else "FRAUD/ANOMALY DETECTED")
print("\n--- Final Audited Fraud Report Panel ---")
print(df[["Name", "Age", "Submissions_Per_Min", "Analysis_Result"]])
