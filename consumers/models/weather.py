"""Contains functionality related to Weather"""
import json
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        logger.info("weather process_message is incomplete - skipping")
        weather = message.value()
        self.temperature = weather['temperature']
        self.status = weather['status']
        weather = json.loads(message.value())
        try:
            self.temperature = weather['temperature']
            self.status = weather['status']
        except KeyError as e:
            logger.debug(f"failed to unpack message {e}")
