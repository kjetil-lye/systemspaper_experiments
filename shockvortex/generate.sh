#!/bin/bash
set -e
export OMP_NUM_THREADS=1
name=shockvortex


    for r in 64 128 256 512 1024;
    do
	s=$r
	NH=$(( (64*$r)/2048))
	mkdir ${name}_${r};
	cd ${name}_${r}
	cp -r ../${name} ./
	sed -i "s/NX/${r}/g" ${name}/${name}.xml
	sed -i "s/NH/${NH}/g" ${name}/${name}.xml
	sed -i "s/SAMPLES/${s}/g" ${name}/${name}.xml
	T='24:00'

	bsub -W $T -n $r  -N -B mpirun -np $r $HOME/alsvinn/build_gcc/alsuqcli/alsuqcli ${name}/${name}.xml
	cd ..;
	

done;