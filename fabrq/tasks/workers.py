from pathlib import Path

from fabric import task as task_fabric
from invoke import run as run_invoke
from invoke import task as task_invoke


@task_fabric
def start(
    c,
    queue=None,
    conda_env=None,
    num_workers="1",
    slurm=False,
    slurm_walltime="12:00:00",
    kill_existing=False,
):
    """Starts workers on a given host listening to given queue (local/remote)

    Workers are started within conda_env. Screen is used for persistence of the workers. 

    The number of workers can either be specified as a fixed positive number, or a negative number 
    can be passed. If a negative number is passed, the number of workers will be equal to the number
    of CPUs on the node minus |num_workers|. 

    The script also provides headers for running on slurm, however, this is currently untested. See
    `workers.sh`.
    """
    if queue is None:
        raise ValueError("Please specify queue")

    if kill_existing:
        stop(c)

    # Read template
    template_path = Path(__file__).parent / "workers.sh"
    with open(template_path, "r") as file:
        template = file.read()

    # Fill template with variables, save script
    host = c.host if hasattr(c, "host") else "local"
    script_path = Path(__file__).parent / "rq_workers_start.sh"
    script = template.format(
        conda_env=conda_env,
        num_workers=num_workers,
        queues=queue,
        slurm_walltime=slurm_walltime,
        user=c.user,
        host=host,
    )
    with open(script_path, "w") as f:
        f.writelines(script)

    # Transfer script to remote
    script_path_remote = "rq_workers_start.sh"
    if hasattr(c, "put"):
        c.put(script_path, script_path_remote)

    # Execute
    if not slurm:
        c.run(f"bash -i {script_path_remote}; rm {script_path_remote}")
    else:
        c.run(f"srun {script_path_remote}; rm {script_path_remote}")

    # Remove script
    script_path.unlink()


@task_fabric
def stop(c):
    """Run `pkill rqworker` (local/remote)
    """
    c.run("pkill -f rqworker")
