# Project 2 ChE 2410 - Hydrothermal Liquefaction of Microalgae
## Overview
This project aims to replicate and expand upon the study titled "A general kinetic model for the hydrothermal liquefaction of microalgae" by Peter J. Valdez, Vincent J. Tocco, and Phillip E. Savage, published in the Bioresource Journal in 2014. The primary focus is on developing a mathematical model based on two or more differential equations to describe the hydrothermal liquefaction process of microalgae, as proposed in the referenced paper.

## Mathematical Model
The mathematical model for the hydrothermal liquefaction system is represented by the following set of differential equations:

$\dot{x}{1_p} = -(k{1_p} + k_{2_p}) \cdot x_{1_p} $
$\dot{x}{1_1} = -(k{1_1} + k_{2_1}) \cdot x_{1_1} $
$\dot{x}{1_c} = -(k{1_c} + k_{2_c}) \cdot x_{1_c} $
$\dot{x}2 = -(k_4 + k_5) \cdot x_2 + k{1_p} \cdot x_{1_p} + k_{1_1} \cdot x_{1_1} + k_{1_c} \cdot x_{1_c} + k_3 \cdot x_3 $
$\dot{x}3 = -(k_3 + k_6) \cdot x_3 + k{2_p} \cdot x_{1_p} + k_{2_1} \cdot x_{1_1} + k_{2_c} \cdot x_{1_c} + k_4 \cdot x_2 $
$\dot{x}_4 = k_5 \cdot x_2 + k_6 \cdot x_3 $
$x_1 = x_{1_p} + x_{1_1} + x_{1_c}$
Here, the variables $x_{1_p}$, $x_{1_1}$, $x_{1_c}$, $x_2$, $x_3$, and $x_4$ represent different components of the microalgae, and the coefficients $k_i$ denote the rate constants associated with various reactions.

