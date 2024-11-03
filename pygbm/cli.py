import argparse
import datetime
from pygbm import GeometricBrownianMotionSimulation

def main():
    # Initialize the argument parser
    parser = argparse.ArgumentParser(description="Simulate Geometric Brownian Motion for stock prices.")
    
    # Add arguments for each parameter with default values
    parser.add_argument("--V0", type=float, default=100, help="Initial Value (default: 100)")
    parser.add_argument("--mu", type=float, default=0.1, help="Drift coefficient (default: 0.1)")
    parser.add_argument("--sigma", type=float, default=0.3, help="Volatility (default: 0.3)")
    parser.add_argument("--T", type=float, default=1, help="Time in years (default: 1)")
    parser.add_argument("--n", type=int, default=100, help="Number of time steps (default: 100)")
    parser.add_argument("--M", type=int, default=100, help="Number of simulations (default: 100)")
    
    # Parse the arguments
    args = parser.parse_args()

    # Create an instance of the GeometricBrownianMotionSimulation class with the parsed arguments
    simulation = GeometricBrownianMotionSimulation(
        V0=args.V0,
        mu=args.mu,
        sigma=args.sigma,
        T=args.T,
        n=args.n,
        M=args.M
    )

    # Run the simulation and plot the results
    simulation.run_simulation_and_plot()

if __name__ == "__main__":
    main()
