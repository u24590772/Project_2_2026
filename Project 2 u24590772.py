import math

#Part 1: EPQ Model
annual_demand = 12000
setup_cost = 50
holding_cost = 2
daily_demand_rate = 40
daily_production_rate = 100000 

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - (d_rate / p_rate))))

epq = calculate_epq(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - (daily_demand_rate / daily_production_rate))

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))
print("\n")

print("1. Increasing the daily production rate causes the EPQ to decrease from 1000 to 904.53")
print("2. Increasing the daily production rate to 100000 means that the stock is very fast which is similar to the assumption of the EPQ model that production hapens instantly.")

# Part 2: ABC Classification


skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    {"sku": "NUT-200", "demand": 5000, "cost": 1},
    {"sku": "PIN-300", "demand": 1000, "cost": 10}
]

def usage_value(demand, cost):
    return demand * cost

for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)

running_total = 0
for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"], "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])

# Step 7: Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}
for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print(tier_counts)

print("1. adding two more SKUs changed the split to: {'A': 4, 'B': 4, 'C': 2}")
print("2. Changing the classification thresholds to 70% / 90% changed the new split to: {'A': 3, 'B': 3, 'C': 4}")


print("question 3")
def classify_skus(skus):
    def usage_value(demand, cost):
        return demand * cost

    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])

    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

    def assign_tier(cum_pct):
        if cum_pct <= 70:
            return "A"
        elif cum_pct <= 90:
            return "B"
        else:
            return "C"
        
    for item in skus_sorted:
        item["tier"] = assign_tier(item["cum_pct"])
    return skus_sorted