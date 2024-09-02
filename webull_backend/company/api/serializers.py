import json
from typing import cast

from polygon import RESTClient  # API client for interacting with Polygon APIs
from rest_framework import serializers
from urllib3 import HTTPResponse

from webull_backend.company.models import Company
from webull_backend.company.models import Ticker
from webull_backend.company.utils import get_current_date
from webull_backend.company.utils import get_current_date_minus_n_days

# Initialize a RESTClient instance with an API key (not shown here)
client = RESTClient()


class TickerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Ticker model.

    Attributes:
        symbol: The unique identifier for the company's stock (e.g., "AAPL").
    """

    class Meta:
        model = Ticker
        fields = ["symbol"]


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for the Company model.

    Attributes:
        uuid: A unique identifier for the company.
        name: The human-readable name of the company (e.g., "Apple Inc.').
        description: A brief description of the company.
        ticker: The corresponding Ticker instance (see TickerSerializer).
    """

    # Include a nested serializer for the Ticker model
    ticker = TickerSerializer(many=False)

    class Meta:
        model = Company
        fields = ["uuid", "name", "description", "ticker"]

    def create(self, validated_data):
        """
        Creates a new Company instance with a corresponding Ticker instance.

        Args:
            validated_data: The validated data for the Company instance to be created.

        Returns:
            A newly created Company instance.
        """
        # Extract the ticker data and remove it from the validated data
        ticker_data = validated_data.pop("ticker")

        # Get the corresponding Ticker instance using the symbol
        ticker = Ticker.objects.get(symbol=ticker_data["symbol"])

        # Add the Ticker's UUID to the validated data
        validated_data["ticker_id"] = ticker.uuid

        # Create a new Company instance and save it to the database
        company = Company.objects.create(**validated_data)
        company.save()

        return company

    def update(self, instance, validated_data):
        """
        Updates an existing Company instance with a corresponding Ticker instance.

        Args:
            instance: The Company instance to be updated.
            validated_data: The validated data for the Company instance to be updated.

        Returns:
            The updated Company instance.
        """
        # Update the company's name and description (if provided)
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)

        # Extract the ticker data and remove it from the validated data
        ticker_data = validated_data.pop("ticker")

        # Get the corresponding Ticker instance using the symbol
        ticker = Ticker.objects.get(symbol=ticker_data["symbol"])

        # Update the company's Ticker instance
        instance.ticker = ticker

        # Save the updated Company instance to the database
        instance.save()

        return instance


class CompanyDetailSerializer(serializers.BaseSerializer):
    """
    Custom serializer for the Company model, providing additional details.

    Attributes:
        uuid: A unique identifier for the company.
        name: The human-readable name of the company (e.g., "Apple Inc.').
        description: A brief description of the company.
        ticker: The corresponding Ticker instance with its own details.
            - name: The human-readable name of the stock (e.g., "AAPL').
            - symbol: The unique identifier for the company's stock (e.g., "AAPL').
            - history: The historical data for the stock, retrieved from the Polygon
            API
    """

    def to_representation(self, instance):
        """
        Returns a dictionary representation of the Company instance with additional
        details.

        Args:
            instance: The Company instance to be represented.

        Returns:
            A dictionary containing the company's details and its corresponding Ticker
            instance.
        """
        # Retrieve historical data for the stock using the Polygon API
        aggs = cast(
            HTTPResponse,
            client.get_aggs(
                instance.ticker.symbol,  # Hardcoded symbol, should be replaced with a
                # dynamic value
                1,  # Time period (not specified in the code)
                "day",
                get_current_date_minus_n_days(7),
                get_current_date(),
                raw=True,
            ),
        )

        # Return a dictionary representation of the Company instance with additional
        # details
        return {
            "uuid": instance.uuid,
            "name": instance.name,
            "description": instance.description,
            "ticker": {
                "name": instance.ticker.company_name,  # Not clear where this value
                # comes from
                "symbol": instance.ticker.symbol,
                "history": json.loads(aggs.data),  # Historical data for the stock
            },
        }
