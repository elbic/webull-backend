"""
This management command is used to extract tickers from a CSV file.
It creates or updates exchanges in the database if they do not exist,
and then populates the Ticker model with data from the CSV file.

Usage:
    python manage.py extract_tickers <exchanges>

Where `<exchanges>` is a comma-separated list of exchange MICs
(e.g. NYSE, NASDAQ, etc.).

Example:
    python manage.py extract_tickers NYSE,NASDAQ
"""

import csv

from django.core.management.base import BaseCommand

from webull_backend.exchanges.models import Exchange
from webull_backend.tickers.models import Ticker


class Command(BaseCommand):
    """
    A management command to extract tickers from a CSV file.
    """

    help = "Extracts tickers from a CSV file"

    def add_arguments(self, parser):
        """
        Adds arguments to the command.

        Args:
            exchanges (list): A list of exchange MICs
        """
        parser.add_argument(
            "exchanges",
            nargs="+",
            type=str,
            help="A comma-separated list of exchange MICs",
        )

    def handle(self, *args, **options):
        """
        Handles the command by extracting tickers from a CSV file.

        Args:
            options (dict): The parsed command arguments

        Returns:
            None
        """

        # Iterate over each exchange specified in the argument
        for exchange in options["exchanges"]:
            try:
                # Try to get the Exchange instance with the given MIC
                exchange_mic = Exchange.objects.get(mic=exchange)
            except Exchange.DoesNotExist:
                # If it does not exist, create a new one and save it
                self.stdout.write(
                    self.style.WARNING(
                        'Exchange "%s" does not exist. Creating...' % exchange,
                    ),
                )
                exchange_mic = Exchange.objects.create(
                    mic=exchange,
                    status="active",
                )
                exchange_mic.save()

            # Open the CSV file and read its contents
            with open(
                "/app/webull_backend/tickers/management/commands/nyse.csv",
            ) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                line_count = 0

                # Iterate over each row in the CSV file
                for row in csv_reader:
                    # Create a new Ticker instance with data from the CSV row
                    ticker = Ticker.objects.create(
                        exchange=exchange_mic,
                        company_name=row[0][:50],
                        symbol=row[1][:50].strip(),
                        status="active",
                    )
                    ticker.save()

                # Print the number of lines processed
                print(f"Processed {line_count} lines.")

            # Print a success message for each exchange
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully finished extracting data for %s " % exchange,
                ),
            )
