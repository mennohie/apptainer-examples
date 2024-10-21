#!/bin/sh
#SBATCH --partition=general # Request partition. Default is 'general'
#SBATCH --qos=short         # Request Quality of Service. Default is 'short' (maximum run time: 4 hours)
#SBATCH --time=1:00:00      # Request run time (wall-clock). Default is 1 minute
#SBATCH --ntasks=1          # Request number of parallel tasks per job. Default is 1
#SBATCH --cpus-per-task=2   # Request number of CPUs (threads) per task. Default is 1 (note: CPUs are always allocated to jobs per 2).
#SBATCH --mem=40290          # Request memory (MB) per node. Default is 1024MB (1GB). For multiple tasks, specify --mem-per-cpu instead
#SBATCH --mail-type=END     # Set mail type to 'END' to receive a mail when the job finishes.
#SBATCH --output=./logs/slurm_%j.out # Set name of output log. %j is the Slurm jobId
#SBATCH --error=./logs/slurm_%j.err # Set name of error log. %j is the Slurm jobId

#SBATCH --gres=gpu:1 # Request 1 GPU
if [ $# -ne 4 ]; then
        echo "Input as arguments: model name (e.g. facebook/esm2_t6_8M_UR50D), output filename (e.g. esmv2_8M), batch size (e.g. 16), input fasta path."
        exit 1
fi
apptainer run --nv -C --no-home --writable --bind ./results:/mnt ./sandbox "$1" "$2" $3 "$4"