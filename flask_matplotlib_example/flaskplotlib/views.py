import io

from flask import (
    Blueprint,
    render_template,
    abort,
    current_app,
    make_response
    )
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

client = Blueprint('client', __name__, template_folder='templates', static_url_path='/static')

@client.route('/<int:points>', methods=['GET'])
def home(points):
    title = current_app.config['TITLE']
    plot = plot_points(points)
    return render_template('index.html', title=title, plot=plot)

def plot_points(points):
    """Generate a plot with a varying number of randomly generated points

    Args:
    points (int): a number of points to plot

    Returns: An svg plot with <points> data points
    """
    # data for plotting
    data = np.random

    data = np.random.normal(loc=150, scale=5, size=points)

    fig = Figure()
    FigureCanvas(fig)

    ax = fig.add_subplot(111)

    ax.hist(data, bins = 50, color='green')

    ax.set_xlabel('Horsepower of cars', fontsize=15)
    ax.set_ylabel('Frequency (number of cars)', fontsize=15)
    ax.set_title(f'There are {points} used cars in this histogram!')
    ax.grid(True)

    img = io.StringIO()
    fig.savefig(img, format='svg')
    #clip off the xml headers from the image
    svg_img = '<svg' + img.getvalue().split('<svg')[1]
    
    return svg_img


