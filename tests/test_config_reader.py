"""Module to test the config_reader module.
Python 3.
"""

import os
import pytest
import sys

import yaml

# Type of config_yaml is dict.
from files.config_yaml import config as config_yaml

# Path of this script.
script_path = os.path.dirname(os.path.abspath(__file__))

class TestConfigReader:
    """Test the config_reader module."""

    def test_config_reader(self):
        """Test that the config file is readed correctly."""
        config_file = os.path.join(script_path, 'files', 'config.yaml')
        # Read config file for tests.
        with open(config_file, "r") as f:
            config = yaml.safe_load(f.read())
        # Desired values retrieved after read the file.
        assert config == config_yaml


if __name__ == '__main__':
    print(__doc__)
