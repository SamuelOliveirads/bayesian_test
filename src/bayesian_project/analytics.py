import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_plot(data_experiment):
    data = pd.read_csv("data/01_raw/data_experiment.csv")

    data["click"] = data["click"].astype(int)
    data["visit"] = data["visit"].astype(int)

    x1 = np.arange(len(data["group"] == "control"))
    y1 = (
        data.loc[data["group"] == "control", "click"].cumsum()
        / data.loc[data["group"] == "control", "visit"].cumsum()
    )

    plt.cla()
    plt.plot(x1, y1, label="Control Group")
    plt.legend(loc="upper left")
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate_plot, interval=1000)

plt.tight_layout()
plt.show()
