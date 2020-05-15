"""Module to work with Python's logging module.
Python 3 >= 3.6.
"""

# Standard library imports.
import logging
import logging.config
import os
import time

# Third party imports.
import yaml

# Local applicaton imports.
from . import sub_module


def get_config(config_file):
    """Reads a YAML file with logging configuration.

    Args:
        config_file (str): path and name to the config file.

    Returns:
        dict: configuration to pass to logging.config.dictconfig.
    """
    with open(config_file, "r") as f:
        config = yaml.safe_load(f.read())
    return config


def run():
    """Execute this module and the submodule."""
    # Path of this script.
    script_path = os.path.dirname(os.path.abspath(__file__))
    # Logging module configuration file.
    config_file = os.path.join(script_path, 'config.yaml')
    # Configure the logging module.
    # This configuration will be used by all logger objects of the project.
    logging.config.dictConfig(config=get_config(config_file))
    # Logger object for this module.
    logger = logging.getLogger(__name__)
    # Work with the logger.
    logger.debug('Main módule')
    time.sleep(0.2)
    logger.debug('Log 2')
    # Run submodule.
    sub_module.run()
