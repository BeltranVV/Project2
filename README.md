# Project 2 ChE 2410 - Hydrothermal Liquefaction of Microalgae
## Overview
This project aims to replicate and expand upon the study titled "A general kinetic model for the hydrothermal liquefaction of microalgae" by Peter J. Valdez, Vincent J. Tocco, and Phillip E. Savage, published in the Bioresource Journal in 2014. The primary focus is on developing a mathematical model based on two or more differential equations to describe the hydrothermal liquefaction process of microalgae, as proposed in the referenced paper.

## Motivation of the study

During my undergraduate thesis, I discovered a lack of information regarding the kinetics of hydrothermal liquefaction. Although many researchers have developed parameters, they vary significantly depending on the type of microalgae. Due to the variability in biomass composition, predicting these parameters becomes challenging. Therefore, it is beneficial to develop a mathematical model to determine the kinetic parameters of the hydrothermal liquefaction reaction using experimental data specific to the species of microalgae used in my previous work. This model can aid in improving future steps, such as constructing a pilot setup for this reaction.

# 1. Information used from the paper:

## 1.1 Mathematical Model

The reaction network is represented by the following paths: 

<div align="center">
  <img src="Reaction_network.JPG" alt="data" width="400">
  <p style="font-weight:bold;"> Figure 1. HTL reaction network </p>
</div>

The mathematical model for the hydrothermal liquefaction system is represented by the following set of differential equations:

$\dot{x} _ {1_p} = -(k_{1_p} + k_{2_p}) \cdot x_{1_p} $

$\dot{x} _ {1_1} = -(k_{1_1} + k_{2_1}) \cdot x_{1_1} $

$\dot{x} _ {1_c} = -(k_{1_c} + k_{2_c}) \cdot x_{1_c} $

$\dot{x} _ 2 = -(k_4 + k_5) \cdot x_2 + k_{1_p} \cdot x_{1_p} + k_{1_1} \cdot x_{1_1} + k_{1_c} \cdot x_{1_c} + k_3 \cdot x_3 $

$\dot{x} _ 3 = -(k_3 + k_6) \cdot x_3 + k_{2_p} \cdot x_{1_p} + k_{2_1} \cdot x_{1_1} + k_{2_c} \cdot x_{1_c} + k_4 \cdot x_2 $

$\dot{x}_4 = k_5 \cdot x_2 + k_6 \cdot x_3 $

$x_1 = x_{1_p} + x_{1_1} + x_{1_c}$

Here, the variables $x_{1_p}$, $x_{1_1}$, $x_{1_c}$, $x_2$, $x_3$, and $x_4$ represent different components of the microalgae, and the coefficients $k_i$ denote the rate constants associated with various reactions.

## 1.2 Data

The information provided in the paper pertains to the percentages of solids, aqueous phase, gas phase, and biocrude. However, Figure 1 illustrates that the reaction does not solely depend on solids as an individual component but rather on their percentage in macromolecules. Therefore, the concentration of each of these macromolecules was determined based on the composition of the microalgae under study.

<div align="center">
  <p><b>Composition of Microalgae</b></p>

  | Component     | Percentage (%)|
  |---------------|------------|
  | Protein       | 56       |
  | Carbohydrates | 32       |
  | Lipids        | 9       |
  | Ash           | 3       |
</div>

<div align="center">
  <img src="plot.JPG" alt="data" width="400">
  <p style="font-weight:bold;"> Figure 2. Original data from the paper. Experimental (discrete points) and calculated (continuous curves) product fraction yields from HTL at     300 C. (a) Nannochloropsis sp </p>
</div>

## 2 Results from this study


