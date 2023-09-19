How to Read and Plot Stock Prices
#################################

In this guide, we will walk you through the steps to retrieve 
financial data using MoabDB and how to create a basic 
chart using the `matplotlib` library.


Prerequisites
=============

- For advanced plotting, ensure you've set up and authenticated with MoabDB as described in the Quick Start guide.
  The advanced plotting will assume you have a `config.json` file in your working directory with the following contents: 

.. code-block:: ini

    [Credentials]
    email = 'your-email@example.com'
    api_key = 'your-secret-api-key'


- You will need `matplotlib` installed. If you haven't already, you can install it with:

  .. code-block:: bash

     pip install matplotlib


Fetching Data from the API
==========================

First, let's retrieve some financial data. For this example, we'll fetch historical closing prices for a given stock (e.g., `AAPL`):

.. code-block:: python

   import moabdb as mdb

   mdb.login('your-email-from-config', 'your-api-key-from-config')
   data_df = mdb.get_equity('AAPL', columns=['Date', 'Close'])

Visualizing Data with Matplotlib
================================

With our data in hand, we can now plot it:

.. code-block:: python
    :linenos:

   import matplotlib.pyplot as plt

   # Extracting date and closing price data
   dates = data_df['Date'].tolist()
   closing_prices = data_df['Close'].tolist()

   # Creating the plot
   plt.figure(figsize=(10,6))
   plt.plot(dates, closing_prices, label='AAPL Closing Prices', color='blue')
   plt.title('AAPL Historical Closing Prices')
   plt.xlabel('Date')
   plt.ylabel('Closing Price (in $)')
   plt.grid(True)
   plt.legend()
   plt.tight_layout()
   plt.xticks(dates[::10])  # Show every 10th date for clarity
   plt.show()

With these simple steps, you've fetched financial data using [Your API Name] and visualized it with a basic chart. Explore more with different stocks, date ranges, or chart types to gain richer insights!

