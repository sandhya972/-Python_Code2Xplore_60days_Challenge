import random
import math
import copy
import numpy as np
import pandas as pd

def generate_data(n=15):
    data = []
    for i in range(n):
        data.append({
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 200),
                "pollution": random.randint(30, 150),
                "energy": random.randint(40, 180)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        })
    return data

def personalize_data(data, roll_number):
    if roll_number % 2 != 0:
        return data[3:] + data[:3]
    else:
        return list(reversed(data))

def custom_risk_score(entry):
    t = entry["metrics"]["traffic"]
    p = entry["metrics"]["pollution"]
    e = entry["metrics"]["energy"]
    return math.log(t + p + e)

def mutate_data(data):
    for entry in data:
        entry["metrics"]["traffic"] += 10
        entry["history"].append(random.randint(100, 200))
        entry["risk"] = custom_risk_score(entry)

def to_dataframe(data):
    rows = []
    for d in data:
        rows.append({
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": d.get("risk", 0)
        })
    return pd.DataFrame(rows)

def manual_correlation(x, y):
    mx = np.mean(x)
    my = np.mean(y)

    num = np.sum((x - mx) * (y - my))
    den = math.sqrt(np.sum((x - mx) ** 2) * np.sum((y - my) ** 2))

    return num / den

def analyze(df):
    mean_risk = df["risk"].mean()
    std_risk = df["risk"].std()

    anomalies = df[df["risk"] > mean_risk + std_risk]["zone"].tolist()

    variance = np.var(df["risk"])
    stability_index = 1 / variance if variance != 0 else 0

    max_risk = df["risk"].max()
    min_risk = df["risk"].min()

    corr = manual_correlation(df["traffic"].values, df["pollution"].values)

    return anomalies, (max_risk, min_risk, stability_index), variance, corr

def detect_clusters(anomalies):
    clusters = []
    temp = []

    for i in sorted(anomalies):
        if not temp or i == temp[-1] + 1:
            temp.append(i)
        else:
            clusters.append(temp)
            temp = [i]

    if temp:
        clusters.append(temp)

    return clusters

def final_decision(anomalies, variance):
    if len(anomalies) == 0:
        return "System Stable"
    else:
        if len(anomalies) < 3:
            return "Moderate Risk"
        else:
            if variance < 0.5:
                return "High Corruption Risk"
            else:
                return "Critical Failure"

roll_number = 1857
original = generate_data()
original = personalize_data(original, roll_number)

assigned = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("\n--- BEFORE MUTATION ---")
print("Original[0]:", original[0])
print("Shallow Copy[0]:", shallow[0])
print("Deep Copy[0]:", deep[0])

mutate_data(shallow)

print("\n--- AFTER MUTATION ---")
print("Original[0]:", original[0], " <-- CORRUPTED (shallow copy effect)")
print("Shallow Copy[0]:", shallow[0])
print("Deep Copy[0]:", deep[0], " <-- SAFE")

assigned[0]["metrics"]["traffic"] += 5
print("\nAssignment Copy effect on Original:", original[0])

df = to_dataframe(shallow)

print("\n--- DataFrame ---")
print(df)
anomalies, stats, variance, corr = analyze(df)

print("\n--- Anomaly Zones ---")
print(anomalies)

print("\nUnique Anomalies (Set):", set(anomalies))

print("\nClusters:", detect_clusters(anomalies))

print("\n--- Manual Correlation ---")
print(corr)

print("\n--- Tuple Output ---")
print("(max_risk, min_risk, stability_index)")
print(stats)

print("\n--- FINAL DECISION ---")
print('decision')

print("\n--- SYSTEM ANALYSIS COMPLETE ---")