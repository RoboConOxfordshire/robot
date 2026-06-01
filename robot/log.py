"""Logging configuration for the robot package."""
import logging

logger = logging.getLogger("robot")
logger.addHandler(logging.NullHandler())
