__author__ = 'stuartreid'

import Quandl
import numpy as np


class QuandlSettings():
    """
    This class contains settings for the quandl integration package, settings include,
    """

    def __init__(self, rows, column, frequency="weekly", transformation="normalize", order="desc"):
        """
        This initialization method constructs a new QuandlSettings object
        :param rows: the number of rows of data to download from Quandl
        :param column: which column of the downloaded data to extract
        :param frequency: daily, weekly, monthly, quarterly, yearly
        :param transformation: normalize, rdiff, etc.
        :param order: which order to sort into w.r.t date
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

    def __init__(self, quandl_data_set_name, quandl_settings=QuandlSettings(500, 1)):
        """
        Initialization method for the Quandl Downloader object
        :param quandl_data_set_name: this is a string which contains the name of the data set to download
        :param quandl_settings: this is a setting object
        """
        self.fetched = False
        self.quandl_data_set = np.array
        self.quandl_settings = quandl_settings
        self.quandl_data_set_name = quandl_data_set_name
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
