import papermill as pm
from pathlib import Path
from datetime import datetime, timezone
import time
import json
import subprocess
import shutil


NOTEBOOKS = [
    # "notebooks/01_data_preparation.ipynb",  # only needed once after cloning
    "notebooks/02_graph_construction.ipynb",
    "notebooks/03_network_capacity.ipynb",
    "notebooks/04_shelters_and_reachability.ipynb",
    "notebooks/05_population_assignment.ipynb",
    "notebooks/06_exits_evacuation.ipynb",
    "notebooks/07_flood_attachment.ipynb",
    "notebooks/08_transportation_model.ipynb",
    "notebooks/09_evacuation_simulation.ipynb",
    "notebooks/10_visualization.ipynb",
]
 
OUTPUT_DIR = Path("notebooks_executed")
RESULTS_BASE = Path("data/result")
CONFIG_PATH = Path("configs/simulation_config.py")


def get_git_commit():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except:
        return "unknown"
    

def run_pipeline() -> None:
    run_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    executed_at = datetime.now(timezone.utc).isoformat()
 
    output_dir = OUTPUT_DIR / run_id
    output_dir.mkdir(parents=True, exist_ok=True)
 
    results_dir = RESULTS_BASE / run_id
    results_dir.mkdir(parents=True, exist_ok=True)
 
    git_commit = get_git_commit()
    print(f"Run ID : {run_id}")
    print(f"Commit : {git_commit}")
    print(f"Notebooks: {len(NOTEBOOKS)}\n")
 
    notebook_stats = []
    pipeline_start = time.time()
    failed = False
 
    for nb in NOTEBOOKS:
        nb_path = Path(nb)
        output_path = output_dir / nb_path.name
 
        print(f"  → Running {nb_path.name} ...", flush=True)
        nb_start = time.time()
        status = "success"
 
        try:
            pm.execute_notebook(
                str(nb_path),
                str(output_path),
                parameters={"RESULT_FOLDER_NAME": run_id},
            )
        except pm.exceptions.PapermillExecutionError as exc:
            status = f"failed: {exc}"
            failed = True
            print(f"FAILED\n    {exc}")
        except FileNotFoundError:
            status = "failed: notebook not found"
            failed = True
            print(f"FAILED (file not found)")
        else:
            elapsed = time.time() - nb_start
            print(f"done ({elapsed:.1f}s)")
 
        notebook_stats.append({
            "notebook": nb,
            "status": status,
            "runtime_sec": round(time.time() - nb_start, 2),
        })
 
        if failed:
            print("\nPipeline aborted due to notebook failure.")
            break
 
    total_time = round(time.time() - pipeline_start, 2)
 
    metadata = {
        "run_id": run_id,
        "executed_at": executed_at,
        "git_commit": git_commit,
        "total_runtime_sec": total_time,
        "success": not failed,
        "notebooks": notebook_stats,
    }

    if CONFIG_PATH.exists():
        shutil.copy(CONFIG_PATH, results_dir / CONFIG_PATH.name)
        print(f"Config     : saved to {results_dir / CONFIG_PATH.name}")
 
    metadata_path = results_dir / "simulation_runtime.json"
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)
 
    print(f"\nPipeline {'completed' if not failed else 'failed'}.")
    print(f"Total time : {total_time}s")
    print(f"Results    : {results_dir}")
    print(f"Metadata   : {metadata_path}")

if __name__ == "__main__":
    run_pipeline()