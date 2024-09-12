# Energy bill calculator program

# -------------------------
# Subprograms
# -------------------------

# Calculate the cost of energy from the diff in meter readings and the calorific value
def energy_cost(current_meter_reading, previous_meter_reading, calorific_value):
  units_used = current_meter_reading - previous_meter_reading
  kWh = units_used * 1.022 * (calorific_value / 3.6)
  cost = int(0.0284 * kWh)
  return cost

# -------------------------
# Main program
# -------------------------


previous_meter_reading = int(input("Enter the previous meter reading: ")[:4])
current_meter_reading = int(input("Enter the current meter reading rounded down: ")[:4])
calorific_value = 39.3
cost = energy_cost(current_meter_reading, previous_meter_reading, calorific_value)
print("Cost is £"+str(cost))
