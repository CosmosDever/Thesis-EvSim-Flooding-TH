# This config is used inside notebooks directory, so the path should start inside notebooks/

# Seed for reproducibility
# Used by population_assignment and transportation_model notebook
RANDOM_SEED = 12345

# 03_network_capacity
LANE_WIDTH_M = 3.5
DEFAULT_LANES = 1

# 04_shelters_and_reachability
SHELTERS_CSV_PATH = "shelter/hatyai_shelters.csv"
SHELTERS_DEFAULT_CAPACITY = 9999

# Optional: mirror edges to allow reverse travel in reachability checks
MAKE_EDGES_BIDIR = True

# 05_population_assignment
# male: 64864, female: 75987, total: 140851, household: 70703
MALE_POPULATION = 2500
FEMALE_POPULATION = 2500
TOTAL_POPULATION = MALE_POPULATION + FEMALE_POPULATION

# 06_evacuation_destination
OUT_CITY_FRAC = 0

# 07_flood_attachment
N_JOBS = 24
# Path start at data/raw/
RAW_FLOOD_CONFIG = [
    {
        "path": "flood/so.csv",
        "timestamp": "2025-11-21 06:00:00",
    },
    {
        "path": "flood/bc5_20251124_2200.csv",
        "timestamp": "2025-11-24 22:00:00",
    },
]
# h or min
TIME_STEP_FREQ = "1h"
GRIDCODE_TO_DEPTH = {0: 0.0, 1: 0.5, 2: 1.0, 3: 1.5, 4: 2.0, 5: 2.5}

# 08_transportation_model
TRANSPORTATION_MODE_PROBS = {"walk": 0.2, "drive": 0.8}

# 09_evacuation_simulation
MODE_SPEED_KMH = {
    "walk": 5.0,   # walking 4–5 km/h
    "drive": 50.0  # urban driving 40–60 km/h
}
# Flood slowdown factors by level (multiplicative). Levels >= impassable_level drop the edge.
FLOOD_SLOWDOWN = {
    0: 1.0,   # dry
    1: 0.5,
    2: 0.2,
    3: 0.0,   # level 3+ impassable by rule below
    4: 0.0,
    5: 0.0,
}
IMPASSABLE_FLOOD_LEVEL = 3
BIDIR_EVAC = True