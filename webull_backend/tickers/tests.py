import datetime

from django.test import TestCase
from exchanges.models import Ticker  # Import the Ticker model from the models file

from webull_backend.exchanges.models import Exchange  # Import the Exchange model


class TestTickerModel(TestCase):
    def setUp(self):
        self.exchange = Exchange.objects.create(
            mic="XNY",
            description="New York Stock Exchange",
            city="New York City",
            website="https://www.nyse.com/",
        )
        self.ticker = Ticker.objects.create(
            exchange=self.exchange,
            company_name="Company Name",
            symbol="Symbol",
        )

    def test_ticker_creation(self):
        # Check that the ticker was created correctly
        self.assertEqual(self.ticker.exchange, self.exchange)
        self.assertEqual(self.ticker.company_name, "Company Name")
        self.assertEqual(self.ticker.symbol, "Symbol")

    def test_ticker_uuid(self):
        # Check that the UUID is unique and correct
        self.assertIsNotNone(self.ticker.uuid)
        self.assertIsInstance(self.ticker.uuid, str)

    def test_ticker_status(self):
        # Check that the status field is set to active by default
        self.assertEqual(self.ticker.status, Ticker.STATUS.active)

    def test_ticker_status_update(self):
        # Update the status and check it was updated correctly
        self.ticker.status = Ticker.STATUS.disabled
        self.ticker.save()
        self.assertEqual(self.ticker.status, Ticker.STATUS.disabled)

    def test_ticker_company_name_update(self):
        # Update the company name and check it was updated correctly
        self.ticker.company_name = "New Company Name"
        self.ticker.save()
        self.assertEqual(self.ticker.company_name, "New Company Name")

    def test_ticker_symbol_update(self):
        # Update the symbol and check it was updated correctly
        self.ticker.symbol = "New Symbol"
        self.ticker.save()
        self.assertEqual(self.ticker.symbol, "New Symbol")

    def test_ticker_created_at(self):
        # Check that the created at field is populated correctly
        self.assertIsInstance(self.ticker.created_at, datetime.datetime)

    def test_ticker_updated_at(self):
        # Check that the updated at field is populated correctly
        self.assertIsInstance(self.ticker.updated_at, datetime.datetime)
