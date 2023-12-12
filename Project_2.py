#!/usr/bin/env python
# coding: utf-8

# # Project 2 ChE 2410
# ### Replication of the study: A general kinetic model for the hydrothermal liquefaction of microalgae
# 
# _Peter J. Valdez, Vincent J. Tocco, Phillip E. Savage_ 
# 
# 2014, Bioresource Journal

# 
# $\dot{x}_{1_p} = -(k_{1_p} + k_{2_p}) \cdot x_{1_p} $
# 
# $\dot{x}_{1_1} = -(k_{1_1} + k_{2_1}) \cdot x_{1_1} $
# 
# $\dot{x}_{1_c} = -(k_{1_c} + k_{2_c}) \cdot x_{1_c} $
# 
# $\dot{x}_2 = -(k_4 + k_5) \cdot x_2 + k_{1_p} \cdot x_{1_p} + k_{1_1} \cdot x_{1_1} + k_{1_c} \cdot x_{1_c} + k_3 \cdot x_3 $
# 
# $\dot{x}_3 = -(k_3 + k_6) \cdot x_3 + k_{2_p} \cdot x_{1_p} + k_{2_1} \cdot x_{1_1} + k_{2_c} \cdot x_{1_c} + k_4 \cdot x_2 $
# 
# $\dot{x}_4 = k_5 \cdot x_2 + k_6 \cdot x_3 $
# 
# $x_1 = x_{1_p} + x_{1_1} + x_{1_c}$
# 

# In[2]:


import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# In[10]:


#data for 350 °C and scenedesmus
time = np.array([0, 10, 20, 40, 60])
solids = np.array([0, 14, 15, 19, 9.5])
aqueous = np.array([0, 48, 47, 47, 49])
biocrude = np.array([0, 39, 38, 41, 34])
gas = np.array([0, 0.0063, 0, 0, 7.7])

plt.plot(time, solids, label='Solids', marker='o')
plt.plot(time, aqueous, label='Aqueous', marker='s')
plt.plot(time, biocrude, label='Biocrude', marker='^')
plt.plot(time, gas, label='Gas', marker='d')

plt.title('Product Evolution Over Time')
plt.xlabel('Time (min)')
plt.ylabel('Product Yield (wt%)')
plt.legend()
plt.show()


# The behavior of solids does not make any sense, because at time equals zero, the concentration of solids must be higher. This is the data reported in the paper but the plot is different.

# In[ ]:


def MyODEs(t, y, k1_p, k2_p, k1_1, k2_1, k1_c, k2_c, k4, k5, k3, k6):
    x1_p, x1_1, x1_c, x2, x3 = y

    dx1_pdt = -(k1_p + k2_p) * x1_p
    dx1_1dt = -(k1_1 + k2_1) * x1_1
    dx1_cdt = -(k1_c + k2_c) * x1_c
    dx2dt = -(k4 + k5) * x2 + k1_p * x1_p + k1_1 * x1_1 + k1_c * x1_c + k3 * x3
    dx3dt = -(k3 + k6) * x3 + k2_p * x1_p + k2_1 * x1_1 + k2_c * x1_c + k4 * x2
    dx4dt = k5 * x2 + k6 * x3

    return [dx1_pdt, dx1_1dt, dx1_cdt, dx2dt, dx3dt, dx4dt]


# In[ ]:


t_steps = np.arange(0,20,1)
wp_0 = 50 #%wt
wc_0 = 31 #%wt
wl_0 = 8 #%wt
wa_0 = 11#%wt 
def RMSE_MyODEs(params):
    k1_p, k2_p, k1_1, k2_1, k1_c, k2_c, k4, k5, k3, k6 = params
    ODE_output = odeint(MyODEs, ic_3, t_steps, args=(k1_p, k2_p, k1_1, k2_1, k1_c, k2_c, k4, k5, k3, k6))
    err = training_data - ODE_output
    return np.sqrt(np.sum(err**2))


# In[ ]:


from scipy.optimize import minimize
initial_guess = [initial_value_for_k1_p, initial_value_for_k2_p, initial_value_for_k1_1, 
                  initial_value_for_k2_1, initial_value_for_k1_c, initial_value_for_k2_c, 
                  initial_value_for_k4, initial_value_for_k5, initial_value_for_k3, 
                  initial_value_for_k6]

result = minimize(RMSE_MyODEs, initial_guess, method='L-BFGS-B')
optimized_params = result.x
print("Optimized Parameters:", optimized_params)

