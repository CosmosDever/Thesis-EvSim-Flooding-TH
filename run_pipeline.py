import papermill as pm
from pathlib import Path

output_dir = Path("notebooks_executed")
output_dir.mkdir(exist_ok=True)

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
]

for nb in notebooks:
    nb_path = Path(nb)
    output = output_dir / nb_path.name

    pm.execute_notebook(
        nb_path,
        output
    )

print("Pipeline finished.")