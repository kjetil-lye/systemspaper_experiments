#!/bin/bash
nx=1024

for dist in 'uniform' 'normal';
do
    mkdir dist_${dist}
    cd dist_${dist}
    for pertinv in 8 16 32 64 128 256 512;
    do
	mkdir pertinv_${pertinv}
	cd pertinv_${pertinv}
	cp -r ../../kelvinhelmholtz_template ./kelvinhelmholtz
	
	sed -i "s/DIST/${dist}/g" kelvinhelmholtz/kelvinhelmholtz.xml
	sed -i "s/PERTURBATIONINV/${pertinv}/g" kelvinhelmholtz/kelvinhelmholtz.py

	cd ..;
    done
    cd ..;
done
