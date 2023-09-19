Plotting Intraday Stock Prices
##############################

In this guide, we will walk you through the steps to retrieve 
financial data using MoabDB and how to create a basic 
chart using the `matplotlib` library.


.. Prerequisites
.. =============

.. - For advanced plotting, ensure you've set up and authenticated with MoabDB as described in the Quick Start guide.
..   The advanced plotting will assume you have a ``config.ini`` file in your working directory with the following structure: 

..   .. code-block:: ini

..       [Credentials]
..       email = 'your-email@example.com'
..       api_key = 'your-secret-api-key'


.. - You will need `matplotlib` installed. If you haven't already, you can install it with:

..   .. code-block:: bash

..      pip install matplotlib


.. Plotting Single Stock with Daily-Level Data
.. ===========================================

.. First, let's retrieve some financial data. For this example, we'll fetch historical closing prices for a given stock (e.g., `AAPL`):

.. Import MoabDB and fetch data
.. ----------------------------

.. .. code-block:: python

..     import moabdb as mdb
..     import matplotlib.pyplot as plt

..     # Constants defined here for flexibility
..     TIC = 'MSFT'
..     SAMPLE = '5y'

..     # Load and Check Data
..     data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE)
..     print(data_df.head())


.. Visualizing Data with Matplotlib
.. --------------------------------

.. With our data in hand, we can now plot it:

.. .. code-block:: python

..     import moabdb as mdb
..     import matplotlib.pyplot as plt

..     # Constants defined here for flexibility
..     TIC = 'MSFT'
..     SAMPLE = '5y'

..     # Load and Check Data
..     data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE)
..     print(data_df.head())

..     # Creating the plot
..     x = data_df.index
..     y = data_df['Close']

..     fig, ax = plt.subplots(figsize=(6,4))
..     ax.plot(x, y, label=TIC, color='blue')
..     ax.set_xlabel('Date')
..     ax.set_ylabel('Closing Price (in $)')
..     plt.legend()
..     plt.show()



.. Plotting Multiple Stocks with Daily-Level Data
.. ==============================================

.. First, let's retrieve some financial data. For this example, we'll fetch historical closing prices for a given stock (e.g., `AAPL`):

.. Import MoabDB and fetch data
.. ----------------------------

.. .. code-block:: python

..     import moabdb as mdb
..     import matplotlib.pyplot as plt

..     # Constants defined here for flexibility
..     TICS = ['MSFT','GOOG']
..     SAMPLE = '5y'

..     # Load and Check Data
..     data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE)
..     print(data_df.head())


.. Visualizing Data with Matplotlib
.. --------------------------------

.. With our data in hand, we can now plot it:

.. .. code-block:: python

..     import moabdb as mdb
..     import matplotlib.pyplot as plt

..     # Constants defined here for flexibility
..     TICS = ['MSFT','INTC']
..     SAMPLE = '5y'

..     # Load and Check Data
..     data_df = mdb.get_equity(tickers=TICS, sample=SAMPLE)
..     print(data_df.head())

..     # Creating the plot
..     x = data_df.index
..     y = data_df['Close'][TICS] # Ensure column order matches TICS

..     fig, ax = plt.subplots(figsize=(6,4))
..     ax.plot(x, y, label=TICS)
..     ax.set_xlabel('Date')
..     ax.set_ylabel('Closing Price (in $)')
..     plt.legend()
..     plt.show()



.. With these simple steps, you've fetched financial data using [Your API Name] and visualized it with a basic chart. Explore more with different stocks, date ranges, or chart types to gain richer insights!


    .. import configparser

    .. # Reading in credentials from config.ini file
    .. config = configparser.ConfigParser()
    .. config.read('config.ini')
    .. email = config['Credentials']['email']
    .. api_key = config['Credentials']['api_key']