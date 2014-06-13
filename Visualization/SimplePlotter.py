__author__ = 'stuartreid'

import matplotlib.pyplot as plot


def plot_regression_line(regression_analyses):
    """
    This global method is a front-end to the MatplotLib library which receives a set of regression analyses and plots
    each one of them onto the canvas.
    """
    title = ""
    fig, ax = plot.subplots()
    # Plot each regression analysis in the set
    for regression_i in regression_analyses:
        ax.plot(regression_i.dates, regression_i.prices, regression_i.color, label="Values " + regression_i.data_set)
        ax.plot(regression_i.dates, regression_i.regression.fittedvalues, regression_i.color + '.',
                label="Regression line " + regression_i.data_set)
        if regression_i.lower is not None:
            ax.plot(regression_i.dates, regression_i.lower, regression_i.color + '--')
        if regression_i.upper is not None:
            ax.plot(regression_i.dates, regression_i.upper, regression_i.color + '--')
        plot.xlabel('Time')
        plot.ylabel('Normalized Values')
        title += regression_i.data_set + ", "

    plot.title('Regression Analysis of ' + title)
    ax.legend(loc='best')
    plot.grid(True)
    plot.show()