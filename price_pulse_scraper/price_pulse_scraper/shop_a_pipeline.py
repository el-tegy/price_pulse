# pylint: disable=import-error

"""
This module contains a function to extract series information from
a given link and applies it to a sample dataframe.
The extracted series information is saved to a CSV file.

Functions:
    extract_series(link):
        Extracts the series information from a given link.

"""
import re

import pandas as pd


def extract_series(link):
    """
    Extracts the series information from a given link.

    Args:
        link (str): The link to extract the series information from.

    Returns:
        str: The extracted series information, or None if no match was found.
    """
    # The regex pattern captures the series information
    pattern = r"/fr/fr/([\w\-]+)-\d+\.html"
    match = re.search(pattern, link)

    if match:
        return match.group(1)
    return None


# Sample dataframe
df_shop_A = pd.read_csv("./data/raw/shopA.csv")
df_shop_A["series"] = df_shop_A["link"].apply(extract_series)

# Save dataframe to a CSV file
df_shop_A.to_csv("./data/silver/shopA_silver.csv")
