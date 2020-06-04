# GeneralPPF Readme
This package is based on [CosmoMC](https://github.com/cmbant/CosmoMC) (version: Jun2016), a Fortran 2008 parallelized MCMC sampler. We aim to provide a general solution to solve the large-scale instability problem at the early universe when considering the interacting dark energy models (see more details in [Väliviita et al. 2008](https://iopscience.iop.org/article/10.1088/1475-7516/2008/07/020)). Based on the previous work ([Li et al. 2014](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.89.083009)), we propose a more general way to solve this problem based on Parameterized Post-Friedmann framework. For more detials please refer to our paper: [J. P. Dai, J. Q. Xia. Revisiting the Instability Problem of the Interacting Dark Energy Model in the Parameterized Post-Friedmann Framework. The Astrophysical Journal, 2019, 876(125).](https://iopscience.iop.org/article/10.3847/1538-4357/ab1655)

## How to use
You can install or run our package following CosmoMC. Here we provide a [guide](https://arxiv.org/pdf/1808.05080).<br>
Most of the changes are in **camb/equations_ppf.f90** and some files in **source**.<br>

The general interacting dark energy model is written as: <br>
![](http://latex.codecogs.com/gif.latex?\\\tf_{t,d}=1+log(tf_{t,d}\))

$$\begin{equation}\begin{array}{l}
Q_{d e}=-Q_{c}=C_{1} \rho_{c}+C_{2} \rho_{d e} \\
\delta Q_{d e}=-\delta Q_{c}=C_{1}\left(\delta \rho_{c}\right)+C_{2}\left(\delta \rho_{d e}\right) \\
Q_{d e}(v-B)+f_{d e}=-Q_{c}(v-B)-f_{c}=D_{1}\left(\rho_{c}+p_{c}\right)\left(v_{c}-B\right)+D_{2}\left(\rho_{d e}+p_{d e}\right)\left(v_{d e}-B\right)
\end{array}\end{equation}$$
