# Currency Converter

This is a Python-based Currency Converter application that allows users to convert amounts between different currencies using real-time exchange rates fetched from an API. The application features a graphical user interface (GUI) built with Tkinter, making it easy to use.

## Features

- **Real-time Data Fetching**: The application fetches the latest exchange rates from the `exchangerate-api`.
- **User-Friendly Interface**: A clean and simple GUI allows users to easily input amounts, select currencies, and view the converted amount.
- **Currency Swapping**: Quickly swap between "From" and "To" currencies for reverse conversions.
- **Error Handling**: Includes validation for inputs and error handling for API requests.

## Requirements

- Python 3.x
- `requests` library
- `tkinter` (comes pre-installed with Python)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/currency-converter.git
    cd currency-converter
    ```

2. **Install Dependencies**:
    Install the required Python library by running:
    ```bash
    pip install requests
    ```

3. **Run the Application**:
    ```bash
    python currency_converter.py
    ```

## Usage

1. **Input the Amount**: Enter the amount you want to convert.
2. **Select Currencies**: Choose the "From" and "To" currencies from the dropdown menus.
3. **Convert**: Click the "Convert" button to see the converted amount.
4. **Swap Currencies**: Use the "Swap" button to quickly switch between the "From" and "To" currencies.

## Example

Here's a quick example of how the application looks and works:

1. Enter an amount, e.g., `100`.
2. Select "USD" as the "From" currency and "EUR" as the "To" currency.
3. Click "Convert" to get the equivalent amount in EUR.
4. Optionally, click "Swap" to reverse the currencies and convert from EUR to USD.

## Enhancements

This project has been enhanced to include:
- A larger, more user-friendly GUI window.
- Increased font size for better readability.
- Error handling to manage invalid inputs and API errors.
- Currency swapping functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

