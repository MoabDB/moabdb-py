Quickstart
##########

Getting Started with MoabDB
===========================

Welcome to the MoabDB documentation! If you're new to MoabDB, this guide will help you set up and make your first API call.

Prerequisites
-------------

Before you begin:

* If you want advanced data, sign up for an account at `MoabDB.com <https://moabdb.com>`_.
* Ensure you have your API key on hand. You can find this in your account dashboard.



Install and Load Library
========================

You can install the MoabDB library using ``pip``.

.. code-block:: bash

   pip install moabdb

Once installed, you can load the library in your Python code.

.. code-block:: python

    import moabdb as mdb



Data Access without API Key
===========================

To access basic data, you do not need an API key.
The ``get_equity()`` function can be used to 
access end-of-day stock data.

**Simple Example to Access MoabDB Data**

.. code-block:: python
    :linenos:

    import moabdb as mdb

    test_df = mdb.get_equity('AAPL')
    print(test_df)


Advanced Data Access with API Key
=================================

With an API key and subscription, intraday data and other
advanced datasets are available. 
As an example, to access intraday data you can enter your 
credentials by either:

1. Manually enter your email and API key in the code.
2. Using a ``config.ini`` file: 

You then can use the ``mdb.login()`` function to login with your credentials.

Manually Entering Credentials
-----------------------------

To access advanced data you must first login with your API key.

.. code-block:: python

    import moabdb as mdb

    mdb.login('your-email', 'your-api-key')
    test_df = mdb.get_equity('AAPL', intraday=True)
    print(test_df)


Using ``config.ini`` File for Credentials
-----------------------------------------

Instead of hardcoding your email and API key in the code, a safer practice is to store them in a configuration file. 
This method prevents the accidental exposure of sensitive credentials, especially if sharing or publishing your code.

**Create Config File**

Create a file named ``config.ini`` and structure it as follows:

.. code-block:: ini

    [Credentials]
    email = 'your-email@example.com'
    api_key = 'your-secret-api-key'

**Read Config File, Login, and Access Data**

.. code-block:: python

    import configparser
    import moabdb as mdb

    # Read credentials from config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    email = config['Credentials']['email']
    api_key = config['Credentials']['api_key']

    # Login and access data
    mdb.login(email, api_key)
    test_df = mdb.get_equity('AAPL', intraday=True)
    print(test_df)

**Security Notes**

- Ensure your ``config.ini`` file is kept secure and out of the reach of unauthorized users.
- Never commit the ``config.ini`` file to public version control repositories to prevent exposure of your credentials.


Conclusion
----------

Congratulations! You've made your first API call with MoabDB. Explore further, integrate it with your applications, and make the most out of our powerful financial data.
