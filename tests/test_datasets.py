import unittest

import pandas.util.testing as pdt
import recordlinkage
import numpy as np
import pandas as pd

from recordlinkage import datasets


class TestDatasets(unittest.TestCase):

    def test_datasets_existance(self):

        # Load all datasets
        datasets.load_febrl1()
        datasets.load_febrl2()
        datasets.load_febrl3()
        datasets.load_febrl4()

