__author__ = 'Stuart Gordon Reid'
__email__ = 'stuartgordonreid@gmail.com'
__website__ = 'http://www.stuartreid.co.za'

"""
This file contains the logic for downloading and manipulating data-sets downloaded from Google Finance
"""

from urllib import urlretrieve
from Helpers.Switch import switch


class GoogleDownloader():
    """
    Base URL: "http://finance.google.com/finance/historical? Parameters:
    q =  stock_ticker &startdate = Jan_01_2014 &enddate = Dec_01_2014 &output = csv
    """

    def __init__(self, stock_tickers=None, start_date=None, end_date=None):
        self.stock_tickers = stock_tickers
        self.start_date = self.get_date(start_date)
        self.end_date = self.get_date(end_date)

    def download_csv(self):
        for ticker in self.stock_tickers:
            link = "http://finance.google.com/finance/historical?q=JSE:" + ticker
            if self.start_date is not None:
                link += "&startdate=" + self.start_date
            if self.end_date is not None:
                link += "&enddate=" + self.end_date
            link += "&output=csv"
            print "Download link: " + link
            # TODO: Check this method when I get home
            try:
                urlretrieve(link, "Download.csv")
            except:
                link.replace("q=JSE:", "q=")
                urlretrieve(link, "Download.csv")

    @staticmethod
    def get_date(date):
        if date is None:
            return None

        assert isinstance(date, str)
        string_values = date.split('-')

        for case in switch(string_values[1]):
            if case('01'):
                date = "Jan+"
                break
            if case('02'):
                date = "Feb+"
                break
            if case('03'):
                date = "Mar+"
                break
            if case('04'):
                date = "Apr+"
                break
            if case('05'):
                date = "May+"
                break
            if case('06'):
                date = "Jun+"
                break
            if case('07'):
                date = "Jul+"
                break
            if case('08'):
                date = "Aug+"
                break
            if case('09'):
                date = "Sep+"
                break
            if case('10'):
                date = "Oct+"
                break
            if case('11'):
                date = "Nov+"
                break
            if case('12'):
                date = "Dec+"
                break

        return date + string_values[0] + "+" + string_values[2]


if __name__ == "__main__":
    tickers = ['ANG', 'BHP', 'MTN']
    downloader = GoogleDownloader(tickers, start_date="01-01-2010", end_date="01-01-2012")
    downloader.download_csv()