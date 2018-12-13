"""
These are my data analysis functions
used to download and process some
temperature time series from Berkeley
Earth.
"""
import numpy as np
import requests


def generate_url(location):
    url = f
    'http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/{location.lower()}-TAVG-Trend.txt'
    return url


def download_data(location):
    """
    Download data for the given
    location.
    """
    url = generate_url(location)
    # Download the content of the URL
    response = requests.get(url)

    data = np.loadtxt(
        response.iter_lines(),
        comments="%")
    return data


def moving_average(data, width):
    """
    Computes the moving average.
    :param data: Input data array.
    :param width: Width in samples.
    """
    moving_avg = np.full(data.size, np.nan)
    for i in range(width, moving_avg.size - width):
        moving_avg[i] = np.mean(data[i:i + width])
    return moving_avg