#!/bin/bash -l
#SBATCH --job-name=kh
#SBATCH --mail-user=kjetil.lye@sam.math.ethz.ch
#SBATCH --time=02:00:00
#SBATCH --nodes=64
#SBATCH --ntasks-per-core=1
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=18
#SBATCH --partition=normal
#SBATCH --constraint=mc
#SBATCH --account=s665

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun $HOME/alsvinn/build/alsuqcli/alsuqcli kelvinhelmholtz/kelvinhelmholtz.xml

