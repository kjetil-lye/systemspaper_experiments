#!/bin/bash -l
#SBATCH --nodes=256
#SBATCH --ntasks=256
#SBATCH --ntasks-per-node=1
#SBATCH --ntasks-per-core=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH -C gpu
#SBATCH --time=23:30:00
srun -C gpu -n $SLURM_NTASKS --ntasks-per-node=$SLURM_NTASKS_PER_NODE -c $SLURM_CPUS_PER_TASK --cpu_bind=rank $HOME/alsvinn/build/alsuqcli/alsuqcli kelvinhelmholtz/kelvinhelmholtz.xml
