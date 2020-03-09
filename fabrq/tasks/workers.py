import os
from pathlib import Path

from fabric import task as task_fabric
from invoke import run as run_invoke
from invoke import task as task_invoke

try:
    REDIS_HOST = os.environ["REDIS_HOST"]
except:
    print("Environment variables should contain REDIS_HOST")
try:
    REDIS_PORT = os.environ["REDIS_PORT"]
except:
    print("Environment variables should contain REDIS_PORT")
try:
    REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
except:
    print("Environment variables should contain REDIS_PASSWORD")
try:
    REDIS_DB = os.environ["REDIS_DB"]
except:
    print("Environment variables should contain REDIS_DB")
try:
    REDIS_URL = os.environ["REDIS_URL"]
except:
    print("Environment variables should contain REDIS_URL")


@task_fabric
def start(c, 
    queue=None,
    conda_env=None,
    num_workers=None,
    ):
    assert queue is not None, "Specify queue"
    assert conda_env is not None, "Specify conda env"
    assert num_workers is not None, "Specify number of workers"

    for n in range(int(num_workers)):
        worker_name = f"rq_worker_{n}_`hostname`_`whoami`_`date +%s`"

        screen_cmd = f"screen -S {worker_name} -d -m bash -l -c"
        source_bashrc = f"source ~/.bashrc"
        set_env_vars = "export MKL_NUM_THREADS=1; export NUMEXPR_NUM_THREADS=1; export OMP_NUM_THREADS=1"
        activate_venv = f"conda activate {conda_env}"
        start_rq_worker = f"rq worker {queue} --url {REDIS_URL} --name {worker_name}"

        cmd = f"{screen_cmd} '{source_bashrc}; {set_env_vars}; {activate_venv}; {start_rq_worker}'"
        c.run(cmd)


@task_fabric
def stop(c):
    """Run `pkill rq_worker` (local/remote)
    """
    c.run("pkill -f rq_worker_*")
