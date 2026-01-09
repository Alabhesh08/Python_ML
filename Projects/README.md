

## Title

Simulation and Preprocessing of a Noisy Biomedical Signal using NumPy

## Overview

This project demonstrates the generation, noise modeling, statistical analysis, and preprocessing of a synthetic biomedical time-series signal using NumPy.

- ### Signal Generation

A sine-based periodic signal was generated to act as a surrogate biomedical signal sampled at a fixed rate.

- ### Noise Modeling

Gaussian noise was added to simulate sensor noise, along with uniform noise to approximate quantization effects commonly introduced during digitization.

- ### Statistical Analysis

Basic statistical measures (mean, standard deviation, variance, extrema) were computed for both clean and noisy signals to study the effect of noise.

- ### Preprocessing

Z-score normalization was applied to standardize the signal scale, followed by clipping at ±3 standard deviations to limit extreme outliers.
Threshold-based filtering was *intentionally not applied*, as the signal is continuous and crosses zero naturally, making amplitude thresholding inappropriate.

## Results

Plots demonstrate the impact of noise and the effect of normalization and clipping on signal robustness.

## Tools Used

NumPy
Matplotlib