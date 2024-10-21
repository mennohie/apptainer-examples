#!/bin/sh
#SBATCH --partition=general # Request partition. Default is 'general'
#SBATCH --qos=short         # Request Quality of Service. Default is 'short' (maximum run time: 4 hours)
#SBATCH --time=3:00:00      # Request run time (wall-clock). Default is 1 minute
#SBATCH --ntasks=1          # Request number of parallel tasks per job. Default is 1
#SBATCH --cpus-per-task=2   # Request number of CPUs (threads) per task. Default is 1 (note: CPUs are always allocated to jobs per 2).
#SBATCH --mem=40290          # Request memory (MB) per node. Default is 1024MB (1GB). For multiple tasks, specify --mem-per-cpu instead
#SBATCH --mail-type=END     # Set mail type to 'END' to receive a mail when the job finishes.
#SBATCH --output=./logs/slurm_%j.out # Set name of output log. %j is the Slurm jobId
#SBATCH --error=./logs/slurm_%j.err # Set name of error log. %j is the Slurm jobId


if [ $# -ne 2 ]
  then
    echo "Input as arguments the number of rolls, and the output location"
    exit 1
fi


apptainer run --nv -C --no-home --bind ./results:/mnt ./image.sif "$1" "$2"