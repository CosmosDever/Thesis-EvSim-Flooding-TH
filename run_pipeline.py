import papermill as pm
from pathlib import Path
from datetime import datetime

output_dir = Path("notebooks_executed")
output_dir.mkdir(exist_ok=True)

RESULT_FOLDER_NAME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

notebooks = [
    "notebooks/01_data_preparation.ipynb",
    "notebooks/02_graph_construction.ipynb",
    "notebooks/03_network_capacity.ipynb",
    "notebooks/04_shelters_and_reachability.ipynb",
    "notebooks/05_population_assignment.ipynb",
    "notebooks/06_evacuation_destinations.ipynb",
    "notebooks/07_flood_attachment.ipynb",
    "notebooks/08_transportation_model.ipynb",
    "notebooks/09_evacuation_simulation.ipynb",
    "notebooks/10_visualization.ipynb"
]

for nb in notebooks:
    nb_path = Path(nb)
    output = output_dir / nb_path.name

    pm.execute_notebook(
        nb_path,
        output,
        parameters={
            "RESULT_FOLDER_NAME": RESULT_FOLDER_NAME
        }
    )

print(f"Pipeline finished. Result folder: {RESULT_FOLDER_NAME}")