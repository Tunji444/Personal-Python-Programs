class MoneyConverter:
    """
    Class to handle money conversion operations.

    Attributes:
    - exchange_rates: dict
        A dictionary containing the exchange rates for different currencies.
        The keys are currency codes (e.g., "USD", "EUR") and the values are the exchange rates.
    """

    def __init__(self, exchange_rates: dict):
        """
        Constructor to instantiate the MoneyConverter class.

        Parameters:
        - exchange_rates: dict
            A dictionary containing the exchange rates for different currencies.
            The keys are currency codes (e.g., "USD", "EUR") and the values are the exchange rates.
        """

        self.exchange_rates = exchange_rates

    def convert(self, amount: float, from_currency: str, to_currency: str):
        """
        Converts an amount from one currency to another.

        Parameters:
        - amount: float
            The amount of money to be converted.
        - from_currency: str
            The currency code of the original currency.
        - to_currency: str
            The currency code of the target currency.

        Returns:
        - float:
            The converted amount in the target currency.

        Raises:
        - ValueError:
            Will raise an error if the exchange rate for either the original or target currency is not available.
        """

        # Checking if exchange rates are available for both currencies
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Exchange rate not available for one or both currencies.")

        # Converting the amount using the exchange rates
        converted_amount = amount * self.exchange_rates[to_currency] / self.exchange_rates[from_currency]

        return converted_amount

# Example usage of the MoneyConverter class:

# Example 1: Initializing the MoneyConverter with exchange rates
exchange_rates = {
    "USD": 1.0,  # 1 USD = 1 USD (base currency)
    "EUR": 0.85,  # 1 USD = 0.85 EUR
    "GBP": 0.73,  # 1 USD = 0.73 GBP
    "JPY": 110.0  # 1 USD = 110 JPY
}
converter = MoneyConverter(exchange_rates)

# Example 2: Converting an amount from USD to EUR
amount_usd = 100.0
converted_amount_eur = converter.convert(amount_usd, "USD", "EUR")
print(f"{amount_usd} USD is equivalent to {converted_amount_eur} EUR.")

# Example 3: Converting an amount from EUR to GBP
amount_eur = 50.0
converted_amount_gbp = converter.convert(amount_eur, "EUR", "GBP")
print(f"{amount_eur} EUR is equivalent to {converted_amount_gbp} GBP.")