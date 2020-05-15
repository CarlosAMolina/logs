"""Module to test the logger module.
Python 3.
"""

# Standard library imports.
import logging
import os
import sys
import unittest

# Add workdir to the sys.path.
sys.path.append(os.getcwd())

# Local application imports.
from logs import main_module


class TestModules(unittest.TestCase):
    """Test the modules with loggers."""

    def test_modules(self):
        """Run the modules with loggers.

        This function checks too if the logging module is configured.
        """
        # Checks if the logging module has been configured.
        # If the module logger has not been configured yet, the logger won't
        # have handlers.
        self.assertFalse(logging.root.hasHandlers())
        # Run modules with loggers.
        main_module.run()
        # The logging module has been configured.
        self.assertTrue(logging.root.hasHandlers())


if __name__ == '__main__':
    unittest.main()
