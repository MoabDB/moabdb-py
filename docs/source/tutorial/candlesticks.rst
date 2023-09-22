Plotting Intraday Candlesticks
############################### 

.. image:: https://img.shields.io/pypi/v/moabdb.svg
   :target: https://pypi.python.org/pypi/moabdb
   :alt: PyPI Version

Continuing with the theme of price plotting, this guide will walk
you through how to plot intraday stock prices using MoabDB and `matplotlib`.

We'll plot candlestock charts to illustrate intraday data.

Prerequisites
=============

Prior to running this example, you should have the following:

- You will need `matplotlib` installed. If you haven't already, you can install it with:

  .. code-block:: bash

     pip install matplotlib

- For advanced plotting, ensure you've set up and authenticated with MoabDB as described in the Quick Start guide.
- The advanced plotting will assume you have a ``config.ini`` file in your working directory with the following structure: 

  .. code-block:: ini

      [Credentials]
      email = your-email@example.com
      api_key = your-secret-api-key

- Login to MoabDB using ``mdb.login()``:
  
  .. code-block:: python

        import moabdb as mdb

        # Constants defined here for flexibility
        # TIC = 'MSFT'
        # SAMPLE = '1d'
        # DAY_START = '9:30'
        # DAY_END = '16:00'

        # Read credentials from config file
        config = configparser.ConfigParser()
        config.read('config.ini')
        email = config.get("Credentials", "email")
        api_key = config.get("Credentials", "api_key")

        # MoabDB login
        mdb.login(email, api_key)



Plotting Single Stock with Daily-Level Data
===========================================

First, let's retrieve some financial data. For this example, we'll fetch historical closing prices for a given stock (e.g., `AAPL`):

Import MoabDB and fetch data
----------------------------



Plot 1 day of intraday data
---------------------------

**Simple plot**

With our data in hand, we can now plot it:

.. code-block:: python

    import configparser
    import moabdb as mdb
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    # Constants defined here for flexibility
    TIC = 'MSFT'
    SAMPLE = '1d'
    DAY_START = '9:30'
    DAY_END = '16:00'

    # Reading in credentials from config.ini file
    # Read credentials from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config.get("Credentials", "email")
    api_key = config.get("Credentials", "api_key")
    mdb.login(email, api_key)

    # Load and get price data
    data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE, intraday=True)
    price_df = data_df['Close'].between_time(DAY_START, DAY_END)

    # Plot
    price_df.plot()
    plt.show()

**Customization with Matplotlib**

The simple plot leaves a lot to be desired. Let's customize it with `matplotlib`:

.. code-block:: python

    import configparser
    import moabdb as mdb
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates

    # Constants defined here for flexibility
    TIC = 'MSFT'
    SAMPLE = '1d'
    DAY_START = '9:30'
    DAY_END = '16:00'

    # Reading in credentials from config.ini file
    # Read credentials from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config.get("Credentials", "email")
    api_key = config.get("Credentials", "api_key")
    mdb.login(email, api_key)

    # Load and get price data
    data_df = mdb.get_equity(tickers=TIC, sample=SAMPLE, intraday=True)
    price_df = data_df['Close'].between_time(DAY_START, DAY_END)

    # Plot Data Values
    x = price_df.index
    y = price_df.values

    # Plot
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, y, label=TIC, color='blue')
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price (in $)')
    ax.xaxis.set_major_formatter(
        mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    fig.autofmt_xdate()
    plt.legend()
    plt.show()




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