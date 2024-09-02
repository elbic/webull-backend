"""
Module for defining Ticker model.

This module imports necessary libraries and defines the Ticker model using Django's ORM.
"""

from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.fields import UUIDField

# Import Exchange model from exchanges app
from webull_backend.exchanges.models import Exchange


class Ticker(models.Model):
    """
    Represents a stock ticker with its details.
    """

    # Define possible statuses for a ticker
    STATUS = Choices("active", "disabled")

    # Unique identifier for the ticker
    uuid = UUIDField(
        primary_key=True,  # Set as primary key
        version=4,  # Use random version 4 UUIDs
        editable=False,  # Not editable by users
    )

    # Foreign key referencing the Exchange instance
    exchange = models.ForeignKey(
        Exchange,
        on_delete=models.CASCADE,  # Cascade delete related Exchange instances
    )

    # Name of the company associated with the ticker
    company_name = models.CharField(
        max_length=50,  # Maximum length of 50 characters
        blank=True,  # Allow blank values
        verbose_name=_("Company Name"),  # Translation-friendly field name
        help_text=_("Company Name"),  # Help text for users
    )

    # Symbol or code for the ticker
    symbol = models.CharField(
        max_length=50,  # Maximum length of 50 characters
        blank=True,  # Allow blank values
        help_text=_("Symbol"),  # Help text for users
    )

    # Timestamps for creation and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Status of the ticker (active or disabled)
    status = StatusField(
        choices_name="STATUS",  # Use STATUS Choices
    )

    def __str__(self):
        """
        Returns a string representation of this Ticker instance.

        :return: String representation of the ticker.
        """
        return f"{self.company_name} - {self.symbol}"
