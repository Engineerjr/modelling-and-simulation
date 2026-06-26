import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# --- 1. Circuit Parameters ---
R = 1000.0  # Resistance in Ohms (1 kΩ)
C = 1e-6    # Capacitance in Farads (1 µF)
V_in = 5.0  # Input voltage (5V)
tau = R * C # Time constant (seconds)

# Time vector for simulation (0 to 5 time constants)
t = np.linspace(0, 5 * tau, 500)

# --- 2. Analytical Solution ---
V_c_analytical = V_in * (1 - np.exp(-t / tau))

# --- 3. Numerical Solution (ODE Solving) ---
def rc_circuit(Vc, t, R, C, Vin):
    # dVc/dt = (Vin - Vc) / (R * C)
    return (Vin - Vc) / (R * C)

# Initial condition: capacitor is completely discharged (0V)
Vc_0 = 0.0

# Solve the ODE
V_c_numerical = odeint(rc_circuit, Vc_0, t, args=(R, C, V_in))

# --- 4. Plotting the Results ---
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, V_c_analytical, label='Analytical Solution', linewidth=2)
plt.plot(t * 1000, V_c_numerical, '--', label='Numerical Solution (odeint)', linewidth=2)
plt.axhline(V_in, color='r', linestyle=':', label='Input Voltage ($V_{in}$)')

# Highlight the time constant (tau)
plt.axvline(tau * 1000, color='g', linestyle='--', alpha=0.7)
plt.text(tau * 1000 * 1.1, V_in * 0.5, f'τ = {tau*1000:.1f} ms\n(63.2% Charged)', color='g')

plt.title('RC Circuit Charging Response')
plt.xlabel('Time (ms)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.grid(True)
plt.show()