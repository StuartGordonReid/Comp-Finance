__author__ = 'stuartreid'

from RegressionController import RegressionAnalysis
from RegressionController import RegressionSettings
from Data.QuandlController import QuandlDownloader
from Data.QuandlController import QuandlSettings
from Visualization import SimplePlotter


def investing_example():
    """
    This method creates a set of regression analyses based on fundamental trading (revenues)
    """
    # b: blue, g: green, r: red, c: cyan, m: magenta, y: yellow, k: black, w: white
    statsmodels_args_inv = RegressionSettings(2, False)
    quandl_args_inv = QuandlSettings(5, 1, "yearly")

    regressions_inv = [RegressionAnalysis(QuandlDownloader("DMDRN/GOOG_REV_LAST", quandl_args_inv),
                                          statsmodels_args_inv, 'b'),
                       RegressionAnalysis(QuandlDownloader("DMDRN/YHOO_REV_LAST", quandl_args_inv),
                                          statsmodels_args_inv, 'g'),
                       RegressionAnalysis(QuandlDownloader("DMDRN/AAPL_REV_LAST", quandl_args_inv),
                                          statsmodels_args_inv, 'k')]
    SimplePlotter.plot_regression_line(regressions_inv)


def trading_example():
    """
    This method creates a set of regression analyses based on technical trading details (price)
    """
    # b: blue, g: green, r: red, c: cyan, m: magenta, y: yellow, k: black, w: white
    statsmodels_args_trade = RegressionSettings(1, True)
    quandl_args_trade = QuandlSettings(350, 4, "weekly")

    regressions_trade = [RegressionAnalysis(QuandlDownloader("GOOG/NASDAQ_GOOG", quandl_args_trade),
                                            statsmodels_args_trade, 'b'),
                         RegressionAnalysis(QuandlDownloader("GOOG/NASDAQ_YHOO", quandl_args_trade),
                                            statsmodels_args_trade, 'g')]
    SimplePlotter.plot_regression_line(regressions_trade)


def economics_example():
    """
    This method creates a set of regression analyses based on economics GDP's of the BRICS nations,
    """
    # b: blue, g: green, r: red, c: cyan, m: magenta, y: yellow, k: black, w: white
    statsmodels_args = RegressionSettings(1, False)
    quandl_args_prices = QuandlSettings(15, 1, "yearly")

    # South Africa, China, Brazil, India, Russia
    regressions = [RegressionAnalysis(QuandlDownloader("WORLDBANK/ZAF_NY_GDP_MKTP_KN", quandl_args_prices),
                                      statsmodels_args, 'b'),
                   RegressionAnalysis(QuandlDownloader("WORLDBANK/CHN_NY_GDP_MKTP_KN", quandl_args_prices),
                                      statsmodels_args, 'g'),
                   RegressionAnalysis(QuandlDownloader("WORLDBANK/BRA_NY_GDP_MKTP_KN", quandl_args_prices),
                                      statsmodels_args, 'k'),
                   RegressionAnalysis(QuandlDownloader("WORLDBANK/IND_NY_GDP_MKTP_KN", quandl_args_prices),
                                      statsmodels_args, 'm'),
                   RegressionAnalysis(QuandlDownloader("WORLDBANK/RUS_NY_GDP_MKTP_KN", quandl_args_prices),
                                      statsmodels_args, 'c')]
    SimplePlotter.plot_regression_line(regressions)


if __name__ == "__main__":
    # This main method run the regression analysis program
    trading_example()


