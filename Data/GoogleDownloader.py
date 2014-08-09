__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains the logic for downloading and manipulating data-sets downloaded from Google Finance
"""

from urllib import urlretrieve
import os


class GoogleSettings():
    """
    This class contains the logic to specify settings for the Google Finance downloader. The classes contained within
    this file are specifically designed to extract data (mostly related to the JSE) from Google Finance
    """
    def __init__(self, start_date=None, end_date=None):
        pass


class GoogleDownloader():
    """
    This class contains the higher level logic for downloading data-sets from Google Finance
    """
    def __init__(self, settings=None, tickers=None):
        pass
