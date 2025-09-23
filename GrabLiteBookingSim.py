# GrabLite Ride Booking Simulator

# -------------------------------
# Stage 1: Fare Calculation
# -------------------------------
def calculate_fare(distance_km, base_fare=5.0, rate_per_km=2.0):
    """
    Calculate total fare based on distance.
    Base fare + (rate_per_km * distance_km)
    """
    return base_fare + (rate_per_km * distance_km)

# Test Stage 1
if __name__ == "__main__":
    print("Testing Stage 1: Fare Calculation")
    print("Fare for 10 km:", calculate_fare(10))
