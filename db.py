from datetime import datetime

# Function to initiate the data
def init_data():

    # Initial user data
    user_data = {
        "credit_left": 50.0,  # Remaining budget
        "max_credit": 100.0,  # Max budget available
        "co2_produced": 20.3,  # Total CO2 emitted in kg
        "commute_history": [
            {"Date": "2024-09-20", "Transport": "Car", "Co2 Emission": 5.2, "Credit Used": 10},
            {"Date": "2024-09-21", "Transport": "Bike", "Co2 Emission": 0.0, "Credit Used": 0},
            {"Date": "2024-09-22", "Transport": "Public Transport", "Co2 Emission": 1.5, "Credit Used": 5},
        ],
    }

    # Define credit and CO2 values for different transportation modes
    transport_data = {
        "car": {"credit_used": -10, "co2_emission": 5.0},
        "bike": {"credit_used": +10, "co2_emission": 0.0},
        "bus": {"credit_used": -5, "co2_emission": 1.5},
        "train": {"credit_used": -5, "co2_emission": 1.5},
        "scooter": {"credit_used": -5, "co2_emission": 1.5}
    }

    external_data = {
        "weather": "sunny", #rainy
        "traffic": "yes",    #no
        "existence_bike_lanes": "yes"
    }

    return user_data, transport_data, external_data

# Function to update the data
def update_data(user_data, transport_data, mode):

    # Update the commute history
    credit_used = transport_data[mode]["credit_used"]
    co2_emission = transport_data[mode]["co2_emission"]

    # Update user data
    user_data["credit_left"] += credit_used
    user_data["co2_produced"] += co2_emission

    # Log the new commute into history
    user_data["commute_history"].append({
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Transport": mode,
        "Co2 Emission": co2_emission,
        "Credit Used": credit_used
    })

    return user_data