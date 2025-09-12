import random
import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# -------------------------------
# Load dataset
# -------------------------------
data = pd.read_csv("traffic_data.csv")

# Features (vehicle/pedestrian counts)
X = data[["North", "South", "East", "West", "Pedestrians"]]

# Targets (green times for each direction)
y = data[["North_time", "South_time", "East_time", "West_time", "Ped_time"]]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Test accuracy
print("Accuracy (R^2):", model.score(X_test, y_test))

# Example prediction
sample = [[12, 7, 15, 10, 4]]
print("Predicted green times:", model.predict(sample))


# -------------------------------
# Smart AI Signal Functions
# -------------------------------
def smart_ai_signal(junction, model):
    """
    junction: dict with vehicle counts in each direction
              e.g., {"North":12, "South":7, "East":15, "West":10, "Pedestrians":4}
    model: trained ML model
    """
    total = sum(junction.values())
    lanes = ["North", "South", "East", "West", "Pedestrians"]

    # If no vehicles/pedestrians, return default base time
    if total == 0:
        base_time = 10
        return {lane: base_time for lane in lanes}
    else:
        return calculate_decision(junction, model)


def calculate_decision(junction, model):
    """
    Predicts optimal green times using trained ML model
    """
    sample = [[
        junction["North"],
        junction["South"],
        junction["East"],
        junction["West"],
        junction["Pedestrians"]
    ]]
    prediction = model.predict(sample)[0]  # get predicted times
    return {
        "North": prediction[0],
        "South": prediction[1],
        "East": prediction[2],
        "West": prediction[3],
        "Pedestrians": prediction[4]
    }


# -------------------------------
# Example Usage
# -------------------------------
junction_example = {"North": 12, "South": 7, "East": 15, "West": 10, "Pedestrians": 4}
green_times = smart_ai_signal(junction_example, model)
print("AI Decided green times:", green_times)
