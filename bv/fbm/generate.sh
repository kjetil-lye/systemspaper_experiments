#!/bin/bash
set -e
export OMP_NUM_THREADS=1
name=euler_brownian

for p in 0.75 0.5 0.1
do
    for r in 64 128 256 512 1024;
    do
	s=$r
	NH=$(( (64*$r)/2048))
	mkdir ${name}_${p}_${r};
	cd ${name}_${p}_${r}
	cp -r ../${name} ./
	sed -i "s/NX/${r}/g" ${name}/${name}.xml
	sed -i "s/NH/${NH}/g" ${name}/${name}.xml
	sed -i "s/SAMPLES/${s}/g" ${name}/${name}.xml
	sed -i "s/PERTURBATION/${p}/g" ${name}/${name}.py
	cp ../submit.sh ./
	sed -i "s/NODES/$((${r}/2))/g" submit.sh
	T='24:00'

#	bsub -W $T -n $r  -N -B mpirun -np $r $HOME/alsvinn/build/alsuqcli/alsuqcli ${name}/${name}.xml
	cd ..;
    done;

done;
