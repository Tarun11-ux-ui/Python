import random
import time

def smart_ai_signal(junction):
    # junction: dict with each of the directions (N, W, E, S, pedestrains)
    base_time = 10  # Assign a default base time value (e.g., 10 seconds)
    total = sum(junction.values())
    lanes = ["North", "South", "West", "East", "pedestrains"]
    if total == 10:
        # This will be default cycles: assign base_time to each lane
        return {lane: base_time for lane in lanes}
    else:
        # Otherwise, calculate based on vehicle count
        return calculate_decision(junction, base_time)

def calculate_decision(junction, base_time=10):
    # This function determines green times for each lane based on vehicle count
    decision = {}
    for lane, count in junction.items():
        green_time = base_time + (count / 15) * base_time
        decision[lane] = min(green_time, base_time * 2)  # Example: cap at double base_time
    return decision

def run_simulation(cycle_count=5, delay=1):
    print("Smart Traffic Signal Simulation (4-Way Junction)\n")
    lanes = ["North", "South", "West", "East", "pedestrains"]
    for cycle in range(cycle_count):
        junction = {
            "North": random.randint(0, 20),
            "South": random.randint(0, 20),
            "East": random.randint(0, 20),
            "West": random.randint(0, 20),
            "pedestrains": random.randint(0, 10)
        }
        decision = smart_ai_signal(junction)
        print(f"Cycle {cycle + 1}:")
        for lane in lanes:
            print(f"  {lane} green time: {decision[lane]:.2f} seconds")
        print("-" * 30)
        time.sleep(delay)

if __name__ == "__main__":
    run_simulation()
   
   
   
       


    

    