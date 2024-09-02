"""
Module for defining Exchange model.

This module imports necessary libraries and defines the Exchange model using Django's
ORM.
"""

from django.db import models
from django.utils.translation import gettext as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.fields import UUIDField


class Exchange(models.Model):
    """
    Represents an exchange with its details.
    """

    # Define possible statuses for an exchange
    STATUS = Choices("active", "disabled")

    # Unique identifier for the exchange
    uuid = UUIDField(
        primary_key=True,  # Set as primary key
        version=4,  # Use random version 4 UUIDs
        editable=False,  # Not editable by users
    )

    # Market Identifier Code of the exchange
    mic = models.CharField(
        max_length=50,  # Maximum length of 50 characters
        blank=True,  # Allow blank values
        verbose_name=_("Market Identifier Code"),  # Translation-friendly field name
        help_text=_("Market Identifier Code"),  # Help text for users
    )

    # Description of the exchange
    description = models.CharField(
        max_length=50,  # Maximum length of 50 characters
        blank=True,  # Allow blank values
        help_text=_("MARKET NAME-INSTITUTION DESCRIPTION"),  # Help text for users
    )

    # City where the exchange is located
    city = models.CharField(max_length=50, blank=True)
    website = models.URLField(
        blank=True,  # Allow blank values
        help_text=_("Website"),  # Help text for users
    )

    # Timestamps for creation and update
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Status of the exchange (active or disabled)
    status = StatusField(
        choices_name="STATUS",  # Use STATUS Choices
    )

    def __str__(self):
        """
        Returns a string representation of this Exchange instance.

        :return: String representation of the exchange.
        """
        return f"{self.mic} - {self.description}"
