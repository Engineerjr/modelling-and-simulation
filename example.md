# modelling-and-simulation
# RC Circuit Simulation in Python

This project models and simulates the transient response of a charging **Resistor-Capacitor (RC) circuit**. It compares the mathematical analytical solution against a numerical simulation using an Ordinary Differential Equation (ODE) solver (`scipy.integrate.odeint`).

The simulation automatically plots the voltage response over time and saves the output as a high-resolution PNG image.

---

## Theoretical Background

When a DC voltage ($V_{in}$) is applied to an RC circuit, the rate of change of the voltage across the capacitor ($V_c$) is described by the following differential equation:

$$\frac{dV_c}{dt} = \frac{V_{in} - V_c}{R \cdot C}$$

Where:
* **$R$**: Resistance in Ohms ($\Omega$)
* **$C$**: Capacitance in Farads ($F$)
* **$\tau = R \cdot C$**: The time constant of the circuit, representing the time it takes for the capacitor to charge to approximately 63.2% of its maximum voltage.

---

## Features

* **Dual Modeling:** Computes both the exact analytical solution and the dynamic numerical ODE solution.
* **Visualization:** Generates a clean plot highlighting the input voltage and the $\tau$ (tau) threshold.
* **Auto-Save:** Saves the generated chart as a crisp, presentation-ready image (`rc_circuit_response.png`) at 300 DPI.

---

## Prerequisites & Installation

To run this simulation, you will need Python 3 installed along with a few numerical and plotting libraries. 

Install the required dependencies using `pip`:

```bash
pip install numpy scipy matplotlib