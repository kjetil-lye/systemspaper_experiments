#!/bin/bash
nx=1024
set -e
for dist in 'uniform' 'normal';
do

    cd dist_${dist}
    for pertinv in 8 16 32 64 128 256 512;
    do
	cd pertinv_${pertinv}
	bsub -J "dist_${dist}_${pertinv}" -B -N -W 24:00 -n ${nx} mpirun -np ${nx} $SCRATCH/alsvinn/build/alsuqcli/alsuqcli --multi-sample ${nx} kelvinhelmholtz/kelvinhelmholtz.xml	
	cd ..;
    done
    cd ..;
done
