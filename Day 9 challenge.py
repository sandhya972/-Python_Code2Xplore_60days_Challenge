import copy

def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]

def replicate_data(users):
    assigned = users
    shallow = list(users)
    deep = copy.deepcopy(users)
    return assigned, shallow, deep


def modify_data(data, roll):
    for user in data:

        if roll % 2 == 0:
            user["data"]["files"].append("new.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()

        user["data"]["usage"] += 50


def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap_set = set()

    for i in range(len(original)):
        orig_files = set(original[i]["data"]["files"])
        sh_files = set(shallow[i]["data"]["files"])
        dp_files = set(deep[i]["data"]["files"])

        if original[i]["data"]["files"] == shallow[i]["data"]["files"]:
            leakage += 1

        if original[i]["data"]["files"] != deep[i]["data"]["files"]:
            safe += 1

        overlap_set = overlap_set.union(orig_files & sh_files)

    return leakage, safe, len(overlap_set)


try:
    roll_number = int(input("Enter your roll number: "))
except:
    roll_number = 2

print("\nUsing Roll Number:", roll_number)

original = generate_data()

print("\n===== BEFORE MODIFICATION =====")
print("Original Data:", original)

assigned, shallow, deep = replicate_data(original)

modify_data(shallow, roll_number)

print("\n===== AFTER MODIFICATION =====")
print("Original Data:", original)
print("Assigned Data:", assigned)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

leakage, safe, overlap = check_integrity(original, shallow, deep)

print("\n===== INTEGRITY REPORT =====")
print("Data Corruption (Leakage Count):", leakage)
print("Deep Copy Safe Count:", safe)
print("Overlap Count (Common Files):", overlap)

print("\nFINAL OUTPUT TUPLE:")
print((leakage, safe, overlap))