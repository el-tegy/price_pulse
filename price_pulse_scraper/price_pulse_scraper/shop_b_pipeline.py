# pylint: disable=import-error

"""
This module contains a function to extract series information from a given link and 
a script to apply this function to a sample dataframe and save the resulting dataframe 
to a CSV file.

Functions:
    extract_series(link):
        Extracts the series information from a given link.

Scripts:
    shopB_pipeline.py:
        - Reads a sample dataframe from a CSV file.
        - Applies the extract_series function to the "link" column of the dataframe 
        and adds the resulting series information to a new "series" column.
        - Saves the resulting dataframe to a CSV file.
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
    pattern = r"/apple-([\w\-]+)\.html"
    match = re.search(pattern, link)

    if match:
        return match.group(1)
    return None


# Sample dataframe
df_shop_B = pd.read_csv("./data/raw/shopB.csv")
df_shop_B["series"] = df_shop_B["link"].apply(extract_series)

# Save dataframe to a CSV file
df_shop_B.to_csv("./data/silver/shopB_silver.csv")
