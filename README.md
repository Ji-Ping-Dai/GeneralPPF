# GeneralPPF Readme
This package is based on [CosmoMC](https://github.com/cmbant/CosmoMC) (version: Jun2016), a Fortran 2008 parallelized MCMC sampler. We aim to provide a general solution to solve the large-scale instability problem at the early universe when considering the interacting dark energy models (see more details in [Väliviita et al. 2008](https://iopscience.iop.org/article/10.1088/1475-7516/2008/07/020)). Based on the previous work ([Li et al. 2014](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.89.083009)), we propose a more general way to solve this problem based on Parameterized Post-Friedmann framework. For more details please refer to our paper: [J. P. Dai, J. Q. Xia. The Astrophysical Journal, 2019, 876(125).](https://iopscience.iop.org/article/10.3847/1538-4357/ab1655)

## How to use
You can install or run our package following CosmoMC. Here we provide a [guide](https://arxiv.org/pdf/1808.05080).<br>
Most of the changes are in **camb/equations_ppf.f90** and some files in **source**.<br>

The general interacting dark energy model is written as (for more details please refer to our paper): <br>
![](https://github.com/Ji-Ping-Dai/GeneralPPF/blob/master/docs/readme_fig1.PNG)<br>
Our package provides for different cases, which you can choose in **batch2/params CMB defaults.ini**
![](https://github.com/Ji-Ping-Dai/GeneralPPF/blob/master/docs/readme_fig2.PNG)<br>
