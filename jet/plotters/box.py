import matplotlib.pyplot as plt
import pandas as pd

from jet.plotters.helpers import find_latency_col


def plot_box(csv_paths, labels, skip, output):
    data = {}
    for path, label in zip(csv_paths, labels):
        df = pd.read_csv(path)
        lat_col = find_latency_col(df)
        data[label] = df[lat_col][skip:].values
    fig, ax = plt.subplots()
    pd.DataFrame(data).plot.box(ax=ax)
    ax.set_ylabel("Inference Time (ms)")
    ax.set_title("Latency Distribution by Method")
    plt.tight_layout()
    plt.savefig(output)
    print(f"Saved box-plot to {output}")
