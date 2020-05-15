"""Submodule that works with a logging module configured at other module.
Python 3 >= 3.6.
"""

# Standard library imports.
import logging


def run():
    """Execute this module."""
    # Logger for this module.
    logger = logging.getLogger(__name__)
    logger.debug('Submodule')
