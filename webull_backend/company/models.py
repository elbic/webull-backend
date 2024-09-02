"""
Module for defining Company model.

This module imports necessary libraries and defines the Company model using Django's
ORM.
"""

from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.fields import UUIDField

# Import Ticker model from webull_backend.tickers.models
from webull_backend.tickers.models import Ticker


class Company(models.Model):
    """
    Represents a company with its details.
    """

    # Define possible statuses for a company
    STATUS = Choices("active", "disabled")

    # Unique identifier for the company
    uuid = UUIDField(
        primary_key=True,  # Set as primary key
        version=4,  # Use random version 4 UUIDs
        editable=False,  # Not editable by users
    )

    # Associate a Ticker instance with this Company
    ticker = models.OneToOneField(
        Ticker,
        on_delete=models.CASCADE,
        related_name="company",  # Optional related name for the OneToOneField
    )

    # Company details
    name = models.CharField(
        max_length=50,  # Maximum length of 50 characters
        blank=True,  # Allow blank values
        verbose_name=_("Company Name"),  # Translation-friendly field name
        help_text=_("Company Name"),  # Help text for users
    )

    description = models.CharField(max_length=50, blank=True)

    # Timestamps for creation and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Status of the company (active or disabled)
    status = StatusField(
        choices_name="STATUS",  # Use STATUS Choices
    )

    def __str__(self):
        """
        Returns a string representation of this Company instance.

        :return: String representation of the company.
        """
        return f"{self.name} - {self.description}"
