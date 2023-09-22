
=================================
Analyzing Return Distributions 
=================================

In this guide, we'll demonstrate how to fetch financial data using the `moabdb` API, 
calculate daily returns, and then visualize the
 return distributions using the popular `matplotlib` and `seaborn` libraries.

Prerequisites
-------------

- You will need `matplotlib`, `seaborn`, and `numpy` installed. Install them with:

  .. code-block:: bash

     pip install matplotlib seaborn numpy

Fetching Data from MoabDB
------------------------

First, let's retrieve historical closing prices for a given stock (e.g., `AAPL`):

.. code-block:: python

   import moabdb as mdb

   # Constants for flexibility
   TICS = ['AAPL','MSFT','TSLA','NVDA']
   SAMPLE = '5y'

   # Fetching data
   data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE)

Calculate Daily Returns
-----------------------

To understand return distributions, we then need to calculate daily returns:

.. code-block:: python

   # Calculate daily returns
   return_df = data_df['Close'].pct_change().dropna()

Visualizing Return Distributions
--------------------------------

With the daily returns we can plot their distribution:

.. code-block:: python

   import matplotlib.pyplot as plt
   import seaborn as sns

   # Set style
   sns.set_style('whitegrid')

   # Histogram of daily returns
   plt.figure(figsize=(10,6))
   sns.histplot(data_df['Daily_Return'].dropna(), bins=100, color='blue')
   plt.title('Distribution of Daily Returns for ' + TIC)
   plt.xlabel('Daily Return')
   plt.ylabel('Frequency')
   plt.tight_layout()
   plt.show()

This visualization offers insights into the volatility and risk associated with the stock. A wider distribution implies more volatility.

Considerations
--------------

- The daily return distribution can be useful for understanding risk and return characteristics.
- Always be cautious when interpreting these visualizations; past performance is not indicative of future results.

