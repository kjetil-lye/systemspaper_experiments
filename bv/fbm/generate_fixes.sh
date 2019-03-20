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
	cd ${name}_${p}_${r}
	cp -r ../${name}/*.py ./${name}/
	sed -i "s/PERTURBATION/${p}/g" ${name}/${name}.py
	cd ..
    done;

done;
