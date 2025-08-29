import matplotlib.pyplot as plt
import pandas as pd

from jet.plotters.helpers import find_latency_col


def plot_time_series(
    csv_paths: list[str],
    labels: list[str],
    skip: int,
    log_scale: bool,
    ylim: float,
    output: str,
):
    plt.figure()
    for path, label in zip(csv_paths, labels):
        df = pd.read_csv(path)
        lat_col = find_latency_col(df)
        x = df["frame"][skip:]
        y = df[lat_col][skip:]
        plt.plot(x, y, label=label)
    plt.xlabel("Frame")
    plt.ylabel("Inference Time (ms)")
    plt.title("Per-Frame Inference Time Comparison")
    if log_scale:
        plt.yscale("log")
    if ylim:
        plt.ylim(0, ylim)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output)
    print(f"Saved time-series plot to {output}")
