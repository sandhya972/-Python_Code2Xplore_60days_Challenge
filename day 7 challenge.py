while True:
    n = int(input("\nEnter number of energy readings: "))

    if n <= 0:
        print("Invalid number of readings!")
        continue

    energy_readings = []
    for i in range(n):
        val = int(input(f"Enter reading {i+1}: "))
        energy_readings.append(val)

    categories = {
        "efficient": [],
        "moderate": [],
        "high": [],
        "invalid": []
    }

    for e in energy_readings:
        if e < 0:
            categories["invalid"].append(e)
        elif 0 <= e <= 50:
            categories["efficient"].append(e)
        elif 51 <= e <= 150:
            categories["moderate"].append(e)
        else:
            categories["high"].append(e)


    valid_readings = [e for e in energy_readings if e >= 0]

    total_consumption = sum(valid_readings)
    num_buildings = len(energy_readings)


    summary = (total_consumption, num_buildings)

    eff_count = len(categories["efficient"])
    mod_count = len(categories["moderate"])
    high_count = len(categories["high"])

    overconsumption = high_count > 3
    balanced_usage = abs(eff_count - mod_count) <= 1
    energy_waste = total_consumption > 600

    if energy_waste:
        result = "Energy Waste Detected"
    elif overconsumption:
        result = "High Consumption Alert"
    elif balanced_usage:
        result = "Efficient Campus"
    else:
        result = "Moderate Usage"

    print("\n--- Energy Report ---")
    for key, value in categories.items():
        print(f"{key}: {value}")

    print("Summary (Tuple):", summary)
    print("Total Consumption:", total_consumption)
    print("Number of Buildings:", num_buildings)
    print("Final Result:", result)

    choice = input("\nDo you want to enter another set? (yes/no): ")
    if choice.lower() != "yes":
        print("Program ended.")
        break