import glob
import os.path
import re
import os
files = glob.glob("euler_brownian_*")

for f in files:
    datafiles = glob.glob(os.path.join(f, "*.nc"))
    if len(datafiles) == 0:
        print(f)
        match = re.search(r'euler_brownian_(.+)_(.+)', f)
        if match:
            resolution = int(match.group(2))

            os.chdir(f)
            command_to_run = "bsub -W 24:00 -N -B -n {r} mpirun -np {r} /cluster/scratch/klye/alsvinn/build/alsuqcli/alsuqcli --multi-sample {r} euler_brownian/euler_brownian.xml".format(
                r=resolution)
            os.system(command_to_run)
            os.chdir('..')
                          
