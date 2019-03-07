#!/bin/bash
set -e
for reconstruction in 'MC' 'WENO2';
do
    cd reconst_${reconstruction}
    for nx in 64 128 256 512 1024;
    do
	cd nx_${nx}
	bsub -J "scheme_${reconstruction}_${nx}" -B -N -W 24:00 -n ${nx} mpirun -np ${nx} $SCRATCH/alsvinn/build/alsuqcli/alsuqcli --multi-sample ${nx} kelvinhelmholtz/kelvinhelmholtz.xml	
	cd ..;
    done
    cd ..;
done
