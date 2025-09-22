"""
Grab-Lite Ride Booking Simulator
Part 2 of Innovation Life Cycle Assignment (Grab - Disruptive Model)

Features:
- Book a ride (GrabCar or GrabBike)
- Input pickup & dropoff locations
- Input estimated distance (km)
- Fare calculation (base fare + per km + surge pricing)
- Payment methods: wallet / cash / card
- Output receipt with timestamp
"""

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


# -------------------------------
# Function: Process Payment
# -------------------------------
def process_payment(method, amount, wallet_balance=50.0):
    """
    Simulate payment process.
    - Wallet: deduct from balance if sufficient.
    - Cash: pay directly to driver.
    - Card: assume successful payment.
    """
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


# -------------------------------
# Function: Book Ride
# -------------------------------
def book_ride(pickup, dropoff, distance_km, service="GrabCar", payment_method="wallet", surge=1.0):
    """
    Book a ride and generate receipt.
    """
    if distance_km <= 0:
        return {"status": "error", "message": "❌ Distance must be greater than 0 km."}

    # Calculate fare
    fare = calculate_fare(distance_km, surge=surge)

    # Process payment (simulate GrabPay wallet with balance 50)
    success, balance, payment_msg = process_payment(payment_method, fare, wallet_balance=50.0)

    # Generate receipt
    receipt = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "service": service,
        "pickup": pickup,
        "dropoff": dropoff,
        "distance_km": distance_km,
        "surge_multiplier": surge,
        "fare": fare,
        "payment_method": payment_method,
        "payment_status": "✅ success" if success else "❌ failed",
        "payment_message": payment_msg
    }
    return receipt


# -------------------------------
# MAIN PROGRAM (Interactive)
# -------------------------------
if __name__ == "__main__":
    print("=== 🚖 Grab-Lite Ride Booking Simulator ===")

    # Take inputs from user
    service = input("Choose service (GrabCar / GrabBike): ").strip()
    pickup = input("Enter pickup location: ").strip()
    dropoff = input("Enter dropoff location: ").strip()

    try:
        distance_km = float(input("Enter estimated distance (km): "))
    except ValueError:
        print("❌ Invalid distance. Please enter a number.")
        exit()

    try:
        surge = float(input("Enter surge multiplier (1.0 = normal): "))
    except ValueError:
        surge = 1.0  # default if invalid

    payment_method = input("Choose payment method (wallet / cash / card): ").strip().lower()

    # Book the ride
    receipt = book_ride(pickup, dropoff, distance_km, service, payment_method, surge)

    # Print receipt
    print("\n=== 📄 Ride Receipt ===")
    for key, value in receipt.items():
        print(f"{key}: {value}")

def get_valid_input(prompt, valid_options=None, cast_func=str, error_msg="Invalid input."):
    """
    Prompt user until valid input is received.
    """
    while True:
        value = input(prompt).strip()
        try:
            value_cast = cast_func(value)
            if valid_options and value_cast not in valid_options:
                print(error_msg)
                continue
            return value_cast
        except Exception:
            print(error_msg)

if __name__ == "__main__":
    print("=== 🚖 Grab-Lite Ride Booking Simulator ===")

    # Service selection
    services = ["GrabCar", "GrabBike"]
    print(f"Available services: {', '.join(services)}")
    service = get_valid_input("Choose service: ", services, str, "❌ Please choose GrabCar or GrabBike.")

    pickup = input("Enter pickup location: ").strip()
    dropoff = input("Enter dropoff location: ").strip()

    # Distance input
    distance_km = get_valid_input("Enter estimated distance (km): ", None, float, "❌ Please enter a valid number.")
    while distance_km <= 0:
        print("❌ Distance must be greater than 0 km.")
        distance_km = get_valid_input("Enter estimated distance (km): ", None, float, "❌ Please enter a valid number.")

    # Surge input
    surge = get_valid_input("Enter surge multiplier (1.0 = normal): ", None, float, "❌ Please enter a valid number.")
    if surge < 1.0:
        print("⚠️ Surge multiplier cannot be less than 1.0. Setting to 1.0.")
        surge = 1.0

    # Payment method
    payment_methods = ["wallet", "cash", "card"]
    print(f"Payment methods: {', '.join(payment_methods)}")
    payment_method = get_valid_input("Choose payment method: ", payment_methods, str, "❌ Please choose wallet, cash, or card.")

    # Book the ride
    receipt = book_ride(pickup, dropoff, distance_km, service, payment_method, surge)

    # Print formatted receipt
    print("\n=== 📄 Ride Receipt ===")
    print(f"Timestamp      : {receipt['timestamp']}")
    print(f"Service        : {receipt['service']}")
    print(f"Pickup         : {receipt['pickup']}")
    print(f"Dropoff        : {receipt['dropoff']}")
    print(f"Distance (km)  : {receipt['distance_km']}")
    print(f"Surge Multiplier: {receipt['surge_multiplier']}")
    print(f"Fare           : ${receipt['fare']:.2f}")
    print(f"Payment Method : {receipt['payment_method'].capitalize()}")
    print(f"Payment Status : {receipt['payment_status']}")
    print(f"Details        : {receipt['payment_message']}")
# ...existing code...