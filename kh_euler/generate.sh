#!/bin/bash
set -e
export OMP_NUM_THREADS=1
name=kelvinhelmholtz

for perturbation in 0.5 0.25 0.1; 
do

    for r in 1024;#64 128 256 512 1024 2048;
    do
	s=1024
	NH=$(( (64*$r)/2048))
	mkdir ${name}_${perturbation}_${r};
	cd ${name}_${perturbation}_${r}
	cp -r ../${name} ./
	sed -i "s/NX/${r}/g" ${name}/${name}.xml
	sed -i "s/NH/${NH}/g" ${name}/${name}.xml
	sed -i "s/SAMPLES/${s}/g" ${name}/${name}.xml
	sed -i "s/PERTURBATION/${perturbation}/g" ${name}/${name}.py
	T='120:00'
	if [ "$r" -eq '2048' ]; 
	then
	    T='120:00'
	fi
	bsub -W $T -n 1024 -N -B mpirun -np 1024 $HOME/alsvinn/build_gcc/alsuqcli/alsuqcli ${name}/${name}.xml
	cd ..;
	
    done;
done;