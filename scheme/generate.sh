#!/bin/bash

for reconstruction in 'MC' 'WENO2';
do
    mkdir reconst_${reconstruction}
    cd reconst_${reconstruction}
    for nx in 64 128 256 512 1024;
    do
	mkdir nx_${nx}
	cd nx_${nx}
	cp -r ../../kelvinhelmholtz_template ./kelvinhelmholtz
	
	sed -i "s/NX/${nx}/g" kelvinhelmholtz/kelvinhelmholtz.xml
	sed -i "s/RECONSTRUCTION/${reconstruction}/g" kelvinhelmholtz/kelvinhelmholtz.xml

	cd ..;
    done
    cd ..;
done
