import Electricityprices

def simulate_battery_charging(prices, battery_capacity=20, start_charge=20, end_charge=90, charger_power=2):
    # Initial charge (in kWh)
    current_charge = (battery_capacity * start_charge) / 100
    target_charge = (battery_capacity * end_charge) / 100

    # Calculate the amount of energy that needs to be added
    energy_needed = target_charge - current_charge
    charging_time = 0

    # Iterate through the price list to simulate the charging process
    for price in prices:
        if price < 5:  # Charging occurs only if the price is below 5 cents per kWh
            current_charge += charger_power  # Charge 2 kWh each hour
            charging_time += 1
        if current_charge >= target_charge:  # Stop charging once the target charge is reached
            break

    if current_charge < target_charge:
        return None  # Could not reach the target charge

    # Return the estimated charging time in hours
    return charging_time

# Use the prices from Electricityprices.py
prices = Electricityprices.prices  # Access prices from the imported file

# Print the simulated prices for clarity (optional)
print(f"Simulated prices: {prices}")

# Estimate charging time from 20% to 90% charge
charging_time = simulate_battery_charging(prices)

if charging_time is not None:
    print(f"Charging time from 20% to 90% is estimated to be: {charging_time} hours.")
else:
    print("It was not possible to reach 90% charge due to price constraints.")
