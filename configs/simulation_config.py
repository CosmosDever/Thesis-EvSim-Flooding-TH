# This config is used inside notebooks directory, so the path should start inside notebooks/

# 03_network_capacity
LANE_WIDTH_M = 3.5
DEFAULT_LANES = 1

# 04_shelters_and_reachability
SHELTERS_CSV_PATH = "../data/raw/shelter/hatyai_shelters.csv"
SHELTERS_DEFAULT_CAPACITY = 750

# Optional: mirror edges to allow reverse travel in reachability checks
MAKE_EDGES_BIDIR = True

# 05_population_assignment
# male: 64864, female: 75987, total: 140851, household: 70703
MALE_POPULATION = 2500
FEMALE_POPULATION = 2500
TOTAL_POPULATION = MALE_POPULATION + FEMALE_POPULATION
HOUSEHOLDS = 3535

# 06_flood_attachment
N_JOBS = 24
RAW_FLOOD_CONFIG = [
    {
        "path": "../data/raw/flood/so.csv",
        "timestamp": "2025-11-21 06:00:00",
    },
    {
        "path": "../data/raw/flood/bc5_20251124_2200.csv",
        "timestamp": "2025-11-24 22:00:00",
    },
]
# h or min
TIME_STEP_FREQ = "1h"
LEVEL_TO_DEPTH = {0: 0.0, 1: 0.5, 2: 1.0, 3: 1.5, 4: 2.0, 5: 2.5}




OUT_CITY_FRAC = 0