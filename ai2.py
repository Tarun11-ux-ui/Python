import random
import time
import os

# Smart AI Signal Logic
def smart_ai_signal(junction):
    base_time = 10
    total = sum(junction.values())
    lanes = ["North", "South", "West", "East", "pedestrians"]

    if total <= 10:
        return {lane: base_time for lane in lanes}
    else:
        return calculate_decision(junction, base_time)

def calculate_decision(junction, base_time=10):
    decision = {}
    for lane, count in junction.items():
        green_time = base_time + (count / 15) * base_time
        decision[lane] = min(green_time, base_time * 2)  # cap at 20 sec
    return decision

# Visualization
def display_junction(junction, decision, active_lane):
    os.system("cls" if os.name == "nt" else "clear")  # Clear console

    def light(lane):
        return "🟢" if lane == active_lane else "🔴"

    print("\nSmart Traffic Signal Simulation (Live)\n")
    print(f"       {light('North')} North ↑  ({junction['North']} cars)")
    print(f"         Green: {decision['North']:.1f}s\n")
    print(f"{light('West')} West ←  ({junction['West']} cars)    ({junction['East']} cars) → East {light('East')}")
    print(f"         Green: {decision['West']:.1f}s         Green: {decision['East']:.1f}s\n")
    print(f"       {light('South')} South ↓  ({junction['South']} cars)")
    print(f"         Green: {decision['South']:.1f}s\n")
    print(f" Pedestrians: {junction['pedestrians']} {light('pedestrians')}  Green: {decision['pedestrians']:.1f}s\n")

def run_simulation(cycle_count=5, delay=1):
    lanes = ["North", "South", "West", "East", "pedestrians"]

    for cycle in range(cycle_count):
        junction = {
            "North": random.randint(0, 20),
            "South": random.randint(0, 20),
            "East": random.randint(0, 20),
            "West": random.randint(0, 20),
            "pedestrians": random.randint(0, 10)
        }

        decision = smart_ai_signal(junction)

        # Rotate green light among lanes
        for lane in lanes:
            display_junction(junction, decision, lane)
            time.sleep(delay)

if __name__ == "__main__":
    run_simulation()
