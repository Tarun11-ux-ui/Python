from flask import Flask, render_template
import random
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

app = Flask(_name_)

# ---------------- Improved AI Model Setup ---------------- #
# More realistic training data (traffic volume → green times)
# Based on 0.9 sec per vehicle with min 5 sec and max 30 sec
X_train = np.array([
    [10, 12, 8, 15, 5],    # Light traffic
    [20, 18, 15, 10, 7],   # Moderate traffic
    [15, 22, 18, 12, 10],  # Moderate-heavy traffic
    [30, 25, 20, 18, 12],  # Heavy traffic
    [5, 10, 7, 8, 3],      # Very light traffic
    [12, 15, 10, 10, 6],   # Light-moderate traffic
    [25, 30, 22, 28, 15],  # Heavy traffic
    [8, 5, 10, 7, 2],      # Very light traffic
    [35, 28, 30, 25, 20],  # Very heavy traffic (will be capped)
    [18, 20, 15, 22, 8],   # Moderate traffic
])

# Calculate green times based on 0.9 sec per vehicle with min 5 and max 30
def calculate_green_time(traffic_counts):
    green_times = []
    for count in traffic_counts:
        time = max(5, min(30, 0.9 * count))  # Apply constraints
        green_times.append(time)
    return green_times

# Generate training outputs
y_train = np.array([calculate_green_time(x) for x in X_train])

# Create model with standardization to prevent negative predictions
model = make_pipeline(StandardScaler(), LinearRegression(positive=True))
model.fit(X_train, y_train)

# ---------------- Flask App ---------------- #
@app.route("/")
def dashboard():
    # Random vehicle counts
    junction = {
        "North": random.randint(5, 40),
        "South": random.randint(5, 40),
        "East": random.randint(5, 40),
        "West": random.randint(5, 40),
        "Pedestrians": random.randint(0, 20),
    }

    # Predict green times with constraints
    input_data = np.array([[junction["North"], junction["South"], junction["East"],
                            junction["West"], junction["Pedestrians"]]])
    predicted_times = model.predict(input_data)[0]
    
    # Apply constraints to ensure realistic values (5-30 seconds)
    constrained_times = []
    for time in predicted_times:
        # Ensure minimum 5 seconds, maximum 30 seconds
        constrained_time = max(5, min(30, time))
        constrained_times.append(round(constrained_time, 1))

    ai_green_times = {
        "North": constrained_times[0],
        "South": constrained_times[1],
        "East": constrained_times[2],
        "West": constrained_times[3],
        "Pedestrians": constrained_times[4],
    }

    # Ambulance detection (20–30% chance)
    possible_lanes = ["North", "South", "East", "West"]
    emergency_lane = random.choice([None] * 7 + possible_lanes)  # 3 in 10 chance

    # Default all red
    status = {lane: "RED" for lane in junction.keys() if lane != "Pedestrians"}

    if emergency_lane:
        # 🚨 Ambulance → priority lane + opposite get green
        status[emergency_lane] = "GREEN ✅"
        if emergency_lane == "North":
            status["South"] = "GREEN ✅"
        elif emergency_lane == "South":
            status["North"] = "GREEN ✅"
        elif emergency_lane == "East":
            status["West"] = "GREEN ✅"
        elif emergency_lane == "West":
            status["East"] = "GREEN ✅"
    else:
        # AI + logic → choose busiest pair
        ns_total = junction["North"] + junction["South"]
        ew_total = junction["East"] + junction["West"]

        if ns_total >= ew_total:
            status["North"] = "GREEN ✅"
            status["South"] = "GREEN ✅"
        else:
            status["East"] = "GREEN ✅"
            status["West"] = "GREEN ✅"

    return render_template(
        "dashboard.html",
        junction=junction,
        status=status,
        emergency_lane=emergency_lane,
        ai_green_times=ai_green_times
    )

if _name_ == "_main_":
    app.run(debug=True)      