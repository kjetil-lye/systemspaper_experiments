#!/bin/bash -l
#SBATCH --job-name=kh_time
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=02:00:00
#SBATCH --nodes=1024
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=normal
#SBATCH --constraint=gpu

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun $HOME/alsvinn/build/alsuqcli/alsuqcli kelvinhelmholtz/kelvinhelmholtz.xml
