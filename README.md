# Fast Orbit Propagation with Deep Neural Networks. Final Year Project for Imperial College London, Aeronautics Dept.

## Author: Vlad Marascu
## Date: 1st of June 2021
## Supervisor: Dr Davide Amato

**Abstract:** This paper aims to conduct a preliminary feasibility study in the development and application of Recurrent Neural Networks, with the scope of modeling perturbed orbits, effectively providing a fast and generalized method of approximating the Differential Equations that stand at the base of the perturbed Equations of Motion.
This task was approached from a Deep Learning perspective: three different LSTM-based models were successfully implemented with the aim of predicting the 6 positional and velocity [r, v] features in time. The baseline Uni-variate model trains and predicts each of the 6 features separately, considering them as stand-alone time-series. The more complicated Multi-variate model introduces inter-dependency between the features, thus considering all the other features when making a prediction. The Autoencoder propagates all the features in the same time, thus behaving like a Numerical Integrator. The obtained results revealed that the models have an impressive precision, the Multi-variate LSTM Model being the most accurate overall, followed closely by the Uni-variate architecture. These models predicted some of the features with an accuracy competitive with the Numerical Integrator's, attaining mean relative errors as low as 0.05% and 0.15% and mean absolute errors in the region of 1.5%, clearly revealing the fact that LSTM-based models are capable of approximating Differential Equations and predicting perturbed trajectories in time. 

**Summary:** Trained RNNs (LSTM) that are used in predicting how Orbital Elements will evolve in time, using only a fraction of the computational power of numerical methods. 
