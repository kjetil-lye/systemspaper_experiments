#!/bin/bash
set -e
export OMP_NUM_THREADS=1
name=kelvinhelmholtz

for perturbation in 0.75 0.05 0.075 0.025
do

    for r in 64 128 256 512 1024;
    do
	s=$r
	NH=$(( (64*$r)/2048))
	mkdir ${name}_${perturbation}_${r};
	cd ${name}_${perturbation}_${r}
	cp -r ../${name} ./
	sed -i "s/NX/${r}/g" ${name}/${name}.xml
	sed -i "s/NH/${NH}/g" ${name}/${name}.xml
	sed -i "s/SAMPLES/${s}/g" ${name}/${name}.xml
	sed -i "s/PERTURBATION/${perturbation}/g" ${name}/${name}.py
	T='24:00'
	if [ "$r" -eq '2048' ]; 
	then
	    T='120:00'
	fi
	bsub -W $T -n $s -N -B mpirun -np $s $HOME/alsvinn/build_gcc/alsuqcli/alsuqcli ${name}/${name}.xml
	cd ..;
	
    done;
done;