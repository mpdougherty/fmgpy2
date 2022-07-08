"""
The check module contains functions for checking input dataframes for valid data.
"""


def check_plot_id(i:int) -> int:
    """
    Checks for a valid plot_id.
    :param i: The plot id to check.
    :return: A valid plot id.
    """
    out_i = i + 1
    return out_i

def check_prism_fixed(j):
    """
    Checks for a valid prism fixed plot.
    :param j: The prism plot to check.
    :return: A valid prism plot.
    """
    out_j = check_plot_id(j)
    return out_j