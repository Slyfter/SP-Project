import matplotlib.pyplot as plt
import numpy as np

def create_plot(n):
    x = np.random.randn(n)
    y = np.random.randn(n)

    fig, ax = plt.subplots()
    ax.scatter(x, y)
    return fig

create_plot(100)