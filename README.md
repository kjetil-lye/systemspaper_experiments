# systemspaper_experiments
Experiments configuration files for the paper  [U. S. Fjordholm, K. Lye, S. Mishra, F. Weber, Statistical solutions of hyperbolic systems of conservation laws: numerical approximation,  preprint arXiv:1906.02536 [math.NA]](http://arxiv.org/abs/1906.02536)

All the numerical experiments, except for the single sample runs, which are in the [postprocessing repository](https://github.com/kjetil-lye/statistical_systems_paper_experiments), can be run from configuration files in this repostiry.

## Prerequisites
First you need to download and install [alsvinn](https://alsvinn.github.io/alsvinn), or use the corresponding [alsvinn Docker containers](https://hub.docker.com/u/alsvinn).

The configuration files in the current repository can be run with alsvinn v0.4.1.

## Running the experiments

For each ```.xml``` file, run ```alsuqcli``` on that ```.xml``` file one directory up, eg

    cd kh_daint/samples_kelvinhelmholtz_0.1_1024
    alsuqcli kelvinhelmholtz/kelvinhelmholtz.xml

## Running the experiments with Docker

You can directly run all the experiments through the docker container ```alsvinn/alsvinn_cuda:release-0.4.1```. To run an experiment, do something like

    cd kh_daint/samples_kelvinhelmholtz_0.1_1024
    docker run -v $(pwd):$(pwd) -w $(pwd) --rm alsvinn/alsvinn_cuda:release-0.4.1 kelvinhelmholtz/kelvinhelmholtz.xml

If you are not on a POSIX complaint shell,  ```$(pwd)``` should be replaced by the current working directory.

