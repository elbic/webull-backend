from django.test import TestCase
from exchange.models import Exchange  # Import the Exchange model from the models file


class TestExchangeModel(TestCase):
    def test_exchange_creation(self):
        # Create a new instance of the Exchange model with valid data
        exchange = Exchange(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )

        # Save the instance to the database
        exchange.save()

        # Check that the instance was saved correctly
        self.assertEqual(exchange.mic, "XNY")
        self.assertEqual(exchange.description, "New York Stock Exchange")
        self.assertEqual(exchange.city, "New York City")
        self.assertEqual(exchange.website, "https://www.nyse.com/")
        self.assertIsNotNone(exchange.uuid)

        # Check that the instance's status is set to active by default
        self.assertEqual(exchange.status, Exchange.STATUS.active)

    def test_exchange_update(self):
        # Create a new instance of the Exchange model with valid data
        exchange = Exchange(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )

        # Save the instance to the database
        exchange.save()

        # Update the instance's data and save it again
        exchange.mic = "XNYY"
        exchange.description = "Updated New York Stock Exchange"
        exchange.city = "New York City Updated"
        exchange.website = "https://www.nyse-updated.com/"
        exchange.save()

        # Check that the instance's data was updated correctly
        self.assertEqual(exchange.mic, "XNYY")
        self.assertEqual(exchange.description, "Updated New York Stock Exchange")
        self.assertEqual(exchange.city, "New York City Updated")
        self.assertEqual(exchange.website, "https://www.nyse-updated.com/")

    def test_exchange_status(self):
        # Create a new instance of the Exchange model with valid data
        exchange = Exchange(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )

        # Save the instance to the database
        exchange.save()

        # Check that the instance's status is set to active by default
        self.assertEqual(exchange.status, Exchange.STATUS.active)

        # Update the instance's status to disabled and save it again
        exchange.status = Exchange.STATUS.disabled
        exchange.save()

        # Check that the instance's status was updated correctly
        self.assertEqual(exchange.status, Exchange.STATUS.disabled)

    def test_exchange_str_representation(self):
        # Create a new instance of the Exchange model with valid data
        exchange = Exchange(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )

        # Save the instance to the database
        exchange.save()

        # Check that the instance's string representation is correct
        self.assertEqual(str(exchange), f"{exchange.mic} - {exchange.description}")

    def test_exchange_uuid(self):
        # Create a new instance of the Exchange model with valid data
        exchange = Exchange(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )

        # Save the instance to the database
        exchange.save()

        # Check that the instance's UUID is unique
        self.assertNotEqual(
            exchange.uuid,
            Exchange.objects.get(uuid=exchange.uuid).uuid,
        )
