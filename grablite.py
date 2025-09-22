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
from datetime import datetime

def calculate_fare(distance_km, base_fare=2.0, per_km=0.8, surge=1.0):
    fare = (base_fare + distance_km * per_km) * surge
    return round(fare, 2)

# -------------------------------
# Function: Process Payment
# -------------------------------
def process_payment(method, amount, wallet_balance=50.0):
    if method == "wallet":
        if wallet_balance >= amount:
            wallet_balance -= amount
            return True, wallet_balance, f"Paid {amount:.2f} with GrabPay. New balance: {wallet_balance:.2f}"
        else:
            return False, wallet_balance, "❌ Insufficient GrabPay balance."
    elif method == "cash":
        return True, wallet_balance, f"Will pay {amount:.2f} in cash to driver."
    elif method == "card":
        return True, wallet_balance, f"Paid {amount:.2f} with card on file."
    else:
        return False, wallet_balance, "❌ Unknown payment method."

print("=== 🚖 Grab-Lite Ride Booking Simulator ===")
distance = float(input("Enter estimated distance (km): "))
fare = calculate_fare(distance)
print(f"Calculated fare: RM {fare}")
method = input("Payment method (wallet/cash/card): ").strip().lower()
success, bal, msg = process_payment(method, fare)
print(msg)
