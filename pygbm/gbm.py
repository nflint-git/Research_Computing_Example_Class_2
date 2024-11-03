import numpy as np
import matplotlib.pyplot as plt

class GeometricBrownianMotion:
    def __init__(self, V0, mu, sigma, T, n, M):
        # Initialize parameters
        self.V0 = V0         # Initial value
        self.mu = mu         # Drift coefficient
        self.sigma = sigma   # Volatility
        self.T = T           # Time in years
        self.n = n           # Number of steps
        self.M = M           # Number of simulations
        self.dt = T / n      # Time step size

    def simulate(self):
        # Generate the random component of the process
        dW = np.random.normal(0, np.sqrt(self.dt), size=(self.M, self.n)).T
        # Calculate value paths
        St = np.exp((self.mu - self.sigma ** 2 / 2) * self.dt + self.sigma * dW)
        
        # Start with an array of 1s to represent the initial stock price
        St = np.vstack([np.ones(self.M), St])
        
        # Compute the cumulative product for each path and scale by S0
        self.St = self.V0 * St.cumprod(axis=0)
        
        # Define the time interval array for plotting purposes
        self.time = np.linspace(0, self.T, self.n + 1)
        self.tt = np.full(shape=(self.M, self.n + 1), fill_value=self.time).T

    def plot(self):
        # Plot the results
        plt.plot(self.tt, self.St)
        plt.xlabel("Years $(t)$")
        plt.ylabel("Value $(V_t)$")
        plt.title(
            "Realizations of Geometric Brownian Motion\n"
            f"$dV_t = \\mu V_t dt + \\sigma V_t dW_t$\n $V_0 = {self.V0}, \\mu = {self.mu}, \\sigma = {self.sigma}$"
        )
        plt.show()


# Subclass for additional functionality
class GeometricBrownianMotionSimulation(GeometricBrownianMotion):
    def __init__(self, V0=100, mu=0.1, sigma=0.3, T=1, n=100, M=100):
        # Initialize using the parent class's constructor
        super().__init__(V0, mu, sigma, T, n, M)
        
    def run_simulation_and_plot(self):
        # Run the simulation and plot the results
        self.simulate()
        self.plot()


# Example usage:
#gbm_simulation = GeometricBrownianMotionSimulation(V0=100, mu=0.1, sigma=0.3, T=1, n=100, M=100)
#gbm_simulation.run_simulation_and_plot()
