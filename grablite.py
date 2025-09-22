print("=== 🚖 Grab-Lite Ride Booking Simulator ===")
from datetime import datetime

# -------------------------------
# Function: Calculate Fare
# -------------------------------
def calculate_fare(distance_km, base_fare=2.0, per_km=0.8, surge=1.0):
    """
    Calculate total fare based on distance, base fare, per km rate, and surge multiplier.
    """
    fare = (base_fare + distance_km * per_km) * surge
    return round(fare, 2)

print("=== 🚖 Grab-Lite Ride Booking Simulator ===")
distance = float(input("Enter estimated distance (km): "))
print(f"Calculated fare: RM {calculate_fare(distance)}")
