"""Plot E[T] and E[N] for an M/M/1 queue as a function of utilization ρ."""

import numpy as np
import matplotlib.pyplot as plt
from main_mm1 import main

# Constants
SERVICE_RATE = 50.0   #  Service rate (clients per second)
SIM_DURATION = 10_000  # Duration of the simulation (seconds)

def simulate_mm1_vs_utilization():
    """Run M/M/1 simulations for all integer from 1 to SERVICE_RATE."""
    results = {}

    for lam in range(1, int(SERVICE_RATE)):
        rho = lam / SERVICE_RATE
        print(f"Running simulation for ρ={rho:.2f} (λ={lam}, μ={SERVICE_RATE})...")
        results[rho] = main(arrival_rate=lam, service_rate=SERVICE_RATE, sim_duration=SIM_DURATION)

    return results


def plot_results(results):
    """Generate and save the plots for E[T] and E[N]."""
    # --- Plot E[T] ---
    plt.figure(figsize=(8, 5))
    plt.plot(np.array(sorted(results.keys())), [r['E[T]'] for r in results.values()], 'o-', label='Simulation')
    plt.xlabel('Utilization ρ = λ/μ')
    plt.ylabel('Mean Response Time E[T] (s)')
    plt.title('M/M/1 Queue: Mean Response Time vs Utilization')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../images/mm1_t.png')
    print("Saved plot: mm1_t.png")

    # --- Plot E[N] ---
    plt.figure(figsize=(8, 5))
    plt.plot(np.array(sorted(results.keys())), [r['E[N]'] for r in results.values()], 'o-', label='Simulation',
             color='tab:orange')
    plt.xlabel('Utilization ρ = λ/μ')
    plt.ylabel('Mean Number of Clients E[N]')
    plt.title('M/M/1 Queue: Mean Number of Clients vs Utilization')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig('../images/mm1_n.png')
    print("Saved plot: mm1_n.png")


if __name__ == "__main__":
    results = simulate_mm1_vs_utilization()
    plot_results(results)
