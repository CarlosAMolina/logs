"""Module to test the logger module.

Python 3.
"""

import logging
import os
import pytest
import sys

from logs import main_module

class TestModules:
    """Class to test the logger module."""

    # Root logger without handlers if the module logger is not configured yet.
    # Inside a test function it cannot be checked because pytest has root logger 
    # configured.
    assert logging.root.hasHandlers() is False

    def test_modules(self):
        """Run the modules with loggers.

        This function checks too if the logging module is configured.
        """
        # Run modules with loggers.
        main_module.run()
        # The logging module has been configured.
        assert logging.root.hasHandlers() is True

if __name__ == '__main__':
    print(__doc__)
