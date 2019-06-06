# systemspaper_experiments
Experiments for the systems paper in 2d.

All the numerical experiments, except for the single sample runs, which are in the [postprocessing repository](https://github.com/kjetil-lye/statistical_systems_paper_experiments), can be run from configuration files in this repostiry.

## Prerequisites
First you need to download and install [alsvinn](https://alsvinn.github.io/alsvinn), or use the corresponding [alsvinn Docker containers](https://cloud.docker.com/u/alsvinn/repository/docker/alsvinn/alsvinn_cuda_git).

The configuration files in the current repository can be run with alsvinn v0.2.0.

## Running the experiments

For each ```.xml``` file, run ```alsuqcli``` on that ```.xml``` file one directory up, eg

    cd /home/kjetil/projects/systemspaper_experiments/kh_daint/samples_kelvinhelmholtz_0.1_1024
    alsuqcli kelvinhelmholtz/kelvinhelmholtz.xml


