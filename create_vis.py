import itertools
import os

import numpy as np
import pandas as pd

from itertools import count

# The PHYLIP matrix as a pandas dataframe
PHYLIP_DF: pd.DataFrame = None

NAME_ENUM: dict = {}


def load_dataframe(phylip_path: str):
    """
    Load the phylip matrix as a pandas dataframe.

    Return:
        Returns the matrix as a pandas dataframe.
    """

    global PHYLIP_DF

    n = 0
    df = None

    with open(phylip_path, 'r') as phylip_file:

        # Get the expected dimension size of the matrix
        n = int(next(phylip_file).strip())

        df = pd.read_csv(phylip_file, engine='python',
                         sep=None, header=None, index_col=0)

    df.index = list(map(str.strip, df.index))
    df.columns = df.index

    rows, cols = df.shape

    # Make sure the rows and columns have the expected number of dimensions
    if (rows != n) or (cols != n):
        raise ValueError(
            "Matrix does not have expected number of dimensions (" + str(n) + ")")

    PHYLIP_DF = df

    return df


def enumerate_names():
    """
    Enumerates the names of the genomes extracted from the matrix.
    """

    global PHYLIP_DF
    global NAME_ENUM

    enum: dict = dict(zip(count(), PHYLIP_DF.index))

    NAME_ENUM = enum

    return enum


def create_name_list() -> list:
    """
    Returns a sorted list dictionaries containing the names of the genomes.
    """

    global PHYLIP_DF
    global NAME_ENUM

    names_list = [{"name": name} for name in PHYLIP_DF.index]

    return names_list


def create_links_list() -> list:
    """
    Returns a list of all the links between different nodes.
    """

    global PHYLIP_DF

    links_list = []

    combs = itertools.combinations(range(PHYLIP_DF.shape[0]), 2)
    combs = [(v1, v2) if v1 > v2 else (v2, v1) for v1, v2 in combs]

    for v1, v2 in combs:

        link_dict = {}

        link_dict["source"] = v1
        link_dict["target"] = v2

        # NOTE: Remember to convert from distance to similarity
        link_dict["value"] = max(10 - PHYLIP_DF.iloc[v1, v2], 0)

        links_list.append(link_dict)

    return links_list


def main():

    phylip_path = os.path.join(os.getcwd(), "data", "michael_dist_matrix.txt")
    load_dataframe(phylip_path)

    # enumerate_names()

    create_links_list()


if __name__ == '__main__':
    main()
