# Currency Converter

## Overview

The **Currency Converter** is a Python-based application that will perform currency conversion using data fetched from an open-source API: https://www.frankfurter.app/ . The goal of this app is to display the current conversion rate between 2 currency codes at a specific date or for the latest date. It will also calculate the inverse conversion rate between these 2 currencies.

---

## Objectives

- Extracting the list of all available currency codes.

- Extracting the latest conversion rate for the specified currency codes.

- Extracting the historical conversion rate for the specified currency codes and a given date.

---

## Setup Instructions

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/zhea-son/web-news-aggregator.git
   cd web-news-aggregator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the application using Streamlit:
```
streamlit run app.py
```

This will start the web app locally and open it in your default browser.

## Dependencies

- pandas
- plotly
- seaborn
- wordcloud
- textblob
- nltk
- matplotlib
- dateutil
- streamlit

Make sure to install all dependencies listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.