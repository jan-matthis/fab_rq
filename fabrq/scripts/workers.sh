#!/bin/bash
#SBATCH --partition=nomosix
#SBATCH --job-name=myjob
#SBATCH --mem=4G
#SBATCH --time={slurm_walltime}
#SBATCH --output=myjob.slurm.log

# get number of cores
NPROC_ALL=`nproc --all`

# if num_workers is greater 0, will start num_workers
# else num_workers is interpreted as an offset to the total number of cpus
if [ "{num_workers}" -ge 0 ]; then
    NUM_WORKERS={num_workers}
else
    NUM_WORKERS=$(($NPROC_ALL + {num_workers}))
    if [ $NUM_WORKERS -le 0 ]; then
        NUM_WORKERS=1
    fi
fi

# Disable multi-threading
export MKL_NUM_THREADS=1;
export NUMEXPR_NUM_THREADS=1;
export OMP_NUM_THREADS=1;

echo "Launching $NUM_WORKERS worker(s), executing:"
for i in `seq 1 $NUM_WORKERS`
do
    UUID_LONG=`uuidgen`
    WORKER_NAME=$(printf "{host}_{user}_rqworker_%02d_${{UUID_LONG:0:6}}" "$i")
    CMD="screen -S $WORKER_NAME -d -m bash -i -c 'conda activate {conda_env}; rq worker {queues} --url $REDIS_URL --name $WORKER_NAME'"
    echo $CMD
    eval $CMD
done
