import random
import math
import numpy as np
import pandas as pd

def simulate_data(n=18):
    data = []

    data.append({
        "zone": 1,
        "traffic": 0,
        "air_quality": 50,
        "energy": 100,
        "test_case": "Zero Traffic"
    })

    data.append({
        "zone": 2,
        "traffic": 95,
        "air_quality": 290,
        "energy": 480,
        "test_case": "Extreme Pollution"
    })

    data.append({
        "zone": 3,
        "traffic": 60,
        "air_quality": 150,
        "energy": 500,
        "test_case": "Random Spike"
    })

    for i in range(4, n + 1):
        data.append({
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500),
            "test_case": "Normal"
        })

    return data

def categorize(record):
    if record["air_quality"] > 200:
        if record["traffic"] > 80:
            return "Critical High Risk"
        return "High Risk"
    elif record["energy"] > 400:
        return "Energy Critical"
    elif record["traffic"] < 30:
        if record["air_quality"] < 100:
            return "Safe Zone"
    return "Moderate"


def calculate_risk(record):
    AQI = record["air_quality"]
    traffic = record["traffic"]
    energy = record["energy"]

    if AQI > 200:
        risk = (traffic * 0.3 + AQI * 0.6 + energy * 0.1)
    else:
        risk = (traffic * 0.4 + AQI * 0.3 + energy * 0.3)

    return risk

def custom_sort(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i]["risk_score"] < data[j]["risk_score"]:
                data[i], data[j] = data[j], data[i]
    return data

def detect_patterns(df):
    threshold = df["risk_score"].mean()

    df["AQI_rising"] = df["air_quality"].diff().fillna(0) > 0
    multi_risk = df[(df["risk_score"] > threshold) & (df["AQI_rising"])]

    traffic_variance = np.var(df["traffic"])

    clusters = []
    temp = []

    for i in range(len(df)):
        if df.iloc[i]["risk_score"] > threshold:
            temp.append(df.iloc[i]["zone"])
        else:
            if len(temp) >= 2:
                clusters.append(temp)
            temp = []

    return multi_risk, traffic_variance, clusters

roll_number = int(input("Enter your roll number: "))

data = simulate_data()

if roll_number % 3 == 0:
    print("Applying shuffle strategy...")
    random.shuffle(data)
else:
    print("Applying traffic sorting strategy...")
    data = sorted(data, key=lambda x: x["traffic"])

for d in data:
    d["category"] = categorize(d)
    d["risk_score"] = calculate_risk(d)
    d["sqrt_risk"] = math.sqrt(d["risk_score"])

df = pd.DataFrame(data)

np_data = df[["traffic", "air_quality", "energy"]].values
means = np.mean(np_data, axis=0)

category_set = set(df["category"])

sorted_data = custom_sort(data.copy())
top3 = sorted_data[:3]

multi_risk, traffic_var, clusters = detect_patterns(df)

risk_tuple = (
    df["risk_score"].max(),
    df["risk_score"].mean(),
    df["risk_score"].min()
)

avg_risk = risk_tuple[1]

if avg_risk < 100:
    decision = "City Stable"
elif avg_risk < 200:
    decision = "Moderate Risk"
elif avg_risk < 300:
    decision = "High Alert"
else:
    decision = "Critical Emergency"

print("\n--- DATAFRAME ---")
print(df)

print("\n--- MEAN VALUES ---")
print(means)

print("\n--- UNIQUE CATEGORIES ---")
print(category_set)

print("\n--- TOP 3 RISK ZONES ---")
for t in top3:
    print(t)

print("\n--- RISK TUPLE (max, avg, min) ---")
print(risk_tuple)

print("\n--- MULTI FACTOR RISK ZONES ---")
print(multi_risk[["zone", "risk_score"]])

print("\nTraffic Variance:", traffic_var)

print("\nCritical Clusters:", clusters)

print("\n--- TEST CASES ---")
print("Zone 1 → Zero Traffic")
print("Zone 2 → Extreme Pollution")
print("Zone 3 → Random Spike")

print("\n--- FINAL DECISION ---")
print(decision)

print("\n--- INSIGHT ---")
print("A smart city is a system that uses real-time data analysis "
      "to predict risks, manage resources efficiently, and ensure safety, "
      "sustainability, and better urban living.")
