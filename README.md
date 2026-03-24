# Evacuation Simulation and Analysis for Flooding in Thailand Using Maximum Flow and Time-Expanded Networks 

## Installation

Install dependencies:
```bash
python3 -m pip install -r requirements.txt
```


## Project Structure
```
├── notebooks/              # Modular pipeline notebooks (main workflow)
│   ├── 01_data_preparation.ipynb
│   ├── 02_graph_construction.ipynb
│   └── ...
│
├── data/
│   ├── raw/                # Raw input data
│   ├── clean/              # Used by deprecated workflow
│   ├── tmp/                # Used by deprecated workflow
│   ├── processed/          # Intermediate outputs from pipeline
│   └── result/             # Result from the simulation
│
├── configs/                # Configuration and path utilities
├── run_pipeline.py         # Script to execute full pipeline
│
└── Test_on_HatYai.ipynb    # ⚠️ Deprecated monolithic notebook
```

## Usage

### Running the Pipeline (Recommended)

The project is now organized as a modular notebook pipeline.

To execute the full workflow:
```
python run_pipeline.py
```

**This will**
- Execute notebooks in `notebooks/` sequentially
- Save outputs to:
    - `data/processed/`
    - `data/result`
    - `notebooks_executed/`

> It is **recommended to run the full pipeline at least once**.

### Running Partial Pipeline

After the initial run, you can execute only specific steps by editing the notebook list in `run_pipeline.py`.

**Use this when modifying configurations specific stages.**

To skip steps, comment them out:
```
notebooks = [
    # "notebooks/01_data_preparation.ipynb",
    # "notebooks/02_graph_construction.ipynb",
    # "notebooks/03_network_capacity.ipynb",
    "notebooks/04_shelters_and_reachability.ipynb",
    "notebooks/05_population_assignment.ipynb",
    "notebooks/06_flood_attachment.ipynb",
    "notebooks/07_flood_time_interpolation.ipynb",
    "notebooks/08_transportation_model.ipynb",
    "notebooks/09_evacuation_simulation.ipynb",
]
```

### Visualizing Results

To visualize simulation outputs, use: `notebooks/10_visualization.ipynb`

Set the result folder name:
```
RESULT_FOLDER_NAME = "your_result_folder_name"
```

### Running Individual Notebooks

You can run notebooks independently for development or debugging:

```
cd notebooks
jupyter notebook
```

Each notebook will read input from `data/` and write output for the next step in the pipeline.


## Deprecated Workflow (Legacy)

```bash
mkdir data/tmp
```

Use fillter_location.ipynb to fillter to data in data/raw/flood

The original implementation was a single notebook: `Test_on_HatYai.ipynb`

This notebook contains the full pipeline in one place and kept for reference and debugging purposes.

> [!WARNING]
> This approach is deprecated and will not be maintained.
> Please use the modular pipeline in notebooks/ instead.