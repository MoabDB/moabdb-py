
====================
Quickstart
====================

.. image:: https://img.shields.io/pypi/v/moabdb.svg
   :target: https://pypi.python.org/pypi/moabdb
   :alt: PyPI Version
   
Welcome to the MoabDB documentation! If you're new to MoabDB, 
this guide will help you set up and make your first API call.

Install and Load Library
------------------------

You can install the MoabDB library using ``pip``.

.. code-block:: bash

   pip install moabdb

Once installed, you can load the library in your Python code

.. code-block:: python

    import moabdb as mdb


Access Data Without an API Key
------------------------------

MoabDB provides a robust selection of free daily-level data.
This data is available without an API key or subscription.

A feature of MoabDB is that both free and premium data can be accessed using the same API.
This allows you to easily upgrade to premium data when you're ready. 
To access the data, we will use the ``get_equity()`` function to end-of-day stock data.

**Simple Example to Access MoabDB Data**

.. code-block:: python

    import moabdb as mdb

    test_df = mdb.get_equity('AAPL')

MoabDB will return a Pandas DataFrame:

.. code-block:: python

    print(test_df.head())

                Symbol    Open    High     Low   Close    VWAP  BidPrc  AskPrc     Volume   Trades
    Date
    2023-08-21   AAPL  175.22  179.14  173.74  175.60  175.31  175.55  175.60  109463191  1104760
    2023-08-22   AAPL  176.83  184.13  167.00  177.07  177.03  177.06  177.10   92263173   987877
    2023-08-23   AAPL  177.64  181.67  177.22  180.85  180.69  180.81  180.97  117742371  1156742
    2023-08-24   AAPL  181.70  183.08  172.76  176.08  177.50  176.05  176.08  129308295  1201840
    2023-08-25   AAPL  176.97  179.14  175.28  178.57  177.98  178.50  178.58  114993736  1098505

.. note::

    The daily-level ``get_equity()`` function currently returns prices based on after-market hours. 
    In a future release this will be updated to return prices based on regular market hours.


.. _login-example:

Using ``mdb.login()`` for Advanced Data Access
----------------------------------------------

Prerequisites
^^^^^^^^^^^^^

To access advanced data:

* Sign up for an account at `MoabDB.com <https://moabdb.com>`_.
* Ensure you have your API key on hand. You can find this in your account dashboard.

With your API key and active subscription, intraday data and other advanced datasets are available. 
You can login and access advanced data in two ways:

1. Manually enter your email and API key in the ``mdb.login()`` function.
2. Using a ``config.ini`` file and the ``configparser`` library. Then use the ``mdb.login()`` function.


Manually Entering API Credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Entering your email and API key in the ``mdb.login()`` function is the simplest way to access advanced data.

.. code-block:: python

    import moabdb as mdb

    mdb.login('your-email', 'your-api-key')
    test_df = mdb.get_equity('AAPL', intraday=True)

The intraday data is returned as a Pandas DataFrame:

.. code-block:: python
    
        print(test_df.head())

                            Symbol  Trades   Volume  Imbalance   Close    VWAP  BidPrc  AskPrc  BidSz  AskSz
        Time
        2023-08-21 08:00:01   AAPL    82.0   6846.0    -4438.0  175.22  175.21  175.41  175.44    1.0    2.0
        2023-08-21 08:00:02   AAPL   155.0  14020.0   -13940.0  175.24  175.19  175.41  175.44    1.0    1.0
        2023-08-21 08:00:03   AAPL   235.0  16678.0   -16598.0  175.25  175.21  175.41  175.48    1.0   12.0
        2023-08-21 08:00:04   AAPL   149.0   7073.0    -7045.0  175.27  175.28  175.41  175.48    1.0   11.0
        2023-08-21 08:00:05   AAPL   143.0   4555.0    -4327.0  175.27  175.26  175.41  175.46    1.0    1.0


However, depending on your use case, frequently entering the API key can be tedious. 
An alternative is to use a ``config.ini`` file to store your credentials.


Using ``config.ini`` File to Store API Credentials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Instead of hardcoding your email and API key in the code, a safer practice is to store them in a configuration file. 
This method prevents the accidental exposure of sensitive credentials, especially if sharing or publishing your code.

**Create the Config File**

Create a file named ``config.ini`` and structure it as follows:

.. code-block:: ini

    [Credentials]
    email = your-email@example.com
    api_key = your-secret-api-key

**Read Config File, Login, and Access Data**

If the ``config.ini`` file is in the same directory as your Python script, 
you can use the ``configparser`` library to read the file and access the credentials as follows:

.. code-block:: python

    import configparser
    import moabdb as mdb

    # Read credentials from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config.get("Credentials","email")
    api_key = config.get("Credentials","api_key")

    # Login and access data
    mdb.login(email, api_key)
    test_df = mdb.get_equity('AAPL', intraday=True)

.. note::

    * The ``config.ini`` file must be in the same directory as your Python script.
    * If you are using a Jupyter Notebook, ensure the ``config.ini`` file is in the same directory as the notebook.
    * If you store the ``config.ini`` file in a different directory, you must specify the path to the file in the ``config.read()`` function.



**Security Notes**

- Ensure your ``config.ini`` file is kept secure and out of the reach of unauthorized users.
- Never commit the ``config.ini`` file to public version control repositories to prevent exposure of your credentials.


Conclusion
----------

Congratulations! You've made your first API call with MoabDB. Explore further, integrate it with your applications, and make the most out of our powerful financial data.
