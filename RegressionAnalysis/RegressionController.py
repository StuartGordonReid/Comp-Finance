__author__ = 'Stuart Gordon Reid'

import numpy as np
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std


class RegressionSettings():
    """
    This class contains settings for the statsmodels package, settings include,
    * exponent:int - when equal to one this is a straight line, when >1 this is a curve
    * confidence:boolean - specifies whether confidence lines should be calculated and plotted
    """

    def __init__(self, exponent=1, confidence=False):
        """
        This initialization method constructs a new StatsModelSettings object
        """
        self.exponent = exponent
        self.confidence = confidence
        pass


class RegressionAnalysis():
    """
    This class contain the logic for calculating the regression analysis given a Quandl data-set name, a QuandlSettings
    object, and a StatsModelsSettings object. The resulting regression analysis is returned.
    """

    def __init__(self, quandl_downloader, statsmodels_settings, color='r'):
        """
        This initialization method constructs a new RegressionAnalysis object
        """
        self.color = color
        self.data_set = quandl_downloader.quandl_data_set_name
        self.dates, self.prices = quandl_downloader.get_quandl_data()

        # Only calculate and return confidence lines if setting = True
        if statsmodels_settings.confidence:
            self.regression, self.lower, self.upper = self.run_ordinary_least_squares(self.dates, self.prices,
                                                                                      statsmodels_settings)
        else:
            self.regression = self.run_ordinary_least_squares(self.dates, self.prices, statsmodels_settings)
        pass

    @staticmethod
    def run_ordinary_least_squares(ols_dates, ols_data, statsmodels_settings):
        """
        This method receives the dates and prices of a Quandl data-set as well as settings for the StatsModels package,
        it then calculates the regression lines and / or the confidence lines are returns the objects
        """
        intercept = np.column_stack((ols_dates, ols_dates ** statsmodels_settings.exponent))
        constant = sm.add_constant(intercept)
        statsmodel_regression = sm.OLS(ols_data, constant).fit()
        print(statsmodel_regression.summary())
        if statsmodels_settings.confidence:
            prstd, lower, upper = wls_prediction_std(statsmodel_regression)
            return statsmodel_regression, lower, upper
        else:
            return statsmodel_regression
