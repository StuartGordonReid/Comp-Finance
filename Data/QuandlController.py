__author__ = 'stuartreid'

import Quandl
import numpy as np


class QuandlSettings():
    """
    This class contains settings for the quandl integration package, settings include,
    * rows:int - specifies the amount of historical data to extract in [frequency]
    * column:int - specifies the column in the data-set to use for the regression analysis
    * frequency:String - select between ("daily"|weekly"|"monthly"|"quarterly"|"annual")
    * transformation:String - select the numerical transformation ("diff"|"rdiff"|"normalize"|"cumul")
    * order:String - select order of data between ("asc"|"desc")
    """
    rows = 0
    column = 1
    frequency = "weekly"
    transformation = "normalize"
    order = "desc"

    def __init__(self, rows, column, frequency="weekly", transformation="normalize", order="desc"):
        """
        This initialization method constructs a new QuandlSettings object
        """
        self.rows = rows
        self.column = column
        self.frequency = frequency
        self.transformation = transformation
        self.order = order
        pass


class QuandlDownloader():
    """
    This class contains the logic for downloading and transforming Quandl data sets. It receives,
    * A QuandlSetting object as a parameter which determines how to download the data set
    * The name of a Quandl data set to be downloaded
    """

    quandl_data_set = np.array
    quandl_data_set_name = ""
    quandl_settings = QuandlSettings(500, 1)
    quandl_dates = []
    quandl_data = []
    fetched = False
    # ^ This is a default quandl settings object

    def __init__(self, quandl_data_set_name, quandl_settings=QuandlSettings(500, 1)):
        self.quandl_data_set_name = quandl_data_set_name
        self.quandl_settings = quandl_settings
        self.quandl_dates, self.quandl_data = self.get_quandl_data()
        pass

    def get_quandl_data(self):
        """
        This method retrieves the quandl data set given the settings specified in the quandl_settings object. For more
        information about these settings see documentation from the QuandlSettings class
        """
        if not self.fetched:
            self.quandl_data_set = Quandl.get(self.quandl_data_set_name,
                                              returns="numpy",
                                              rows=self.quandl_settings.rows,
                                              sort_order=self.quandl_settings.order,
                                              collapse=self.quandl_settings.frequency,
                                              transformation=self.quandl_settings.transformation,)
            self.quandl_dates = np.arange(1, self.quandl_settings.rows + 1, 1)
            self.quandl_data = zip(*self.quandl_data_set)[self.quandl_settings.column]
            self.quandl_data = self.quandl_data[::-1]
            self.fetched = True
        return self.quandl_dates, self.quandl_data
