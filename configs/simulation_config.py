# This config is used inside notebooks directory, so the path should start inside notebooks/

# 01_data_preparation
GRIDCODE_TO_DEPTH = {0: 0.0, 1: 0.5, 2: 1.0, 3: 1.5, 4: 2.0, 5: 2.5}

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

# 06_exits_evacuation
ENABLE_EXIT_EVACUATION = False
EXITS_CSV_PATH = "exit/hatyai_exits.csv"

# 07_flood_attachment
N_JOBS = 24
# Path start at data/
FLOOD_CONFIG = [
    {
        "path": "raw/flood/so.csv",
        "timestamp": "2025-11-21 06:00:00",
    },
    {
        "path": "processed/flood_depth_bc5_20251124_2200.csv",
        "timestamp": "2025-11-24 22:00:00",
    },
]
# h or min
TIME_STEP_FREQ = "5min"

# 08_transportation_model
TRANSPORTATION_MODE_PROBS = {"walk": 0.2, "drive": 0.8}

# 09_evacuation_simulation
DEFAULT_MODE_SPEED_KMH = {
    "walk": 5.0,   # walking 4–5 km/h
    "drive": 50.0  # urban driving 40–60 km/h
}

IMPASSABLE_FLOOD_DEPTH = 1
E = 2.71828

BIDIR_EVAC = True