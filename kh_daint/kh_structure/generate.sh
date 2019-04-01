#!/bin/bash
set -e
export OMP_NUM_THREADS=1
name=kelvinhelmholtz

for perturbation in 0.1 0.01; 
do

    for r in 64 128 256 512 1024 2048;
    do
	s=1024
	NH=$(( (64*$r)/2048))
	mkdir ${name}_${perturbation}_${r};
	cd ${name}_${perturbation}_${r}
	cp -r ../${name} ./
	sed -i "s/NX/${r}/g" ${name}/${name}.xml
	sed -i "s/NH/${NH}/g" ${name}/${name}.xml
	sed -i "s/PERTURBATION/${perturbation}/g" ${name}/${name}.py
	cp ../submit.sh ./
#	sbatch submit.sh
	cd ..;
    done;
done;
