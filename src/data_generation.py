# data_generation.py

import os
import pandas as pd
import numpy as np

def generate_synthetic_revenue(
    periods: int = 48,
    start_date: str = "2020-01-01",
    freq: str = "M",
    seed: int = 42,
    trend_start: float = 1000.0,
    trend_slope: float = 5.0,
    seasonal_amplitude: float = 100.0,
    noise_std: float = 50.0,
    output_path: str = "data/test_data.csv"
) -> None:
    """
    Generates synthetic monthly revenue data with trend, seasonality, and noise,
    then writes it to a CSV file at `output_path`.
    """
    # Ensure reproducibility
    np.random.seed(seed)

    # Create date index
    date_index = pd.date_range(start=start_date, periods=periods, freq=freq)

    # Generate components
    trend = trend_start + trend_slope * np.arange(periods)
    seasonal = seasonal_amplitude * np.sin(2 * np.pi * np.arange(periods) / 12)
    noise = np.random.normal(loc=0.0, scale=noise_std, size=periods)

    # Build revenue series
    revenue = trend + seasonal + noise

    # Assemble DataFrame
    df = pd.DataFrame({
        "date": date_index,
        "revenue": revenue
    })

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Write to CSV
    df.to_csv(output_path, index=False)
    print(f"Synthetic data saved to '{output_path}'")

if __name__ == "__main__":
    generate_synthetic_revenue()
