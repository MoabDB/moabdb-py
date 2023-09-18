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


Installation
------------

Download the client library:

.. code-block:: bash

   pip install moabdb


Access data without API Key
---------------------------

1. **Import MoabDB Library**:

   Once installed, import the MoabDB library.

   .. code-block:: python

      import moabdb as mdb

2. **Test Connection**:

   Verify that the setup is successful:

   .. code-block:: python

      import moabdb as mdb

      test_df = mdb.get_equity('AAPL')
      print(test_df)


Access data with API Key
------------------------

1. **Example 1: Manually Enter Credentials**:

    With an API key and subscription, intraday data is available. To access intraday data, you must first login with your API key:

    .. code-block:: python

        import moabdb as mdb

        mdb.login('your-email', 'your-api-key')
        test_df = mdb.get_equity('AAPL',intraday=True)
        print(test_df)


2. **Example 2: Use Config File for API Credentials**:

    Instead of hardcoding your email and API key in the code, a safer practice is to store them in a configuration file. This method prevents the accidental exposure of sensitive credentials, especially if sharing or publishing your code.

    Config File Setup
    ^^^^^^^^^^^^^^^^^

    Create a file named ``config.ini`` and structure it as follows:

    .. code-block:: ini
        [Credentials]
        email = your-email@example.com
        api_key = your-secret-api-key

    Using Credentials from the Config File in Python
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    With an API key and subscription, intraday data is available. 
    To access intraday data, you must first retrieve your 
    credentials from the config file and then login with your API key:

    .. code-block:: python

        import configparser
        import moabdb as mdb

        # Read credentials from config file
        config = configparser.ConfigParser()
        config.read('config.ini')
        email = config['Credentials']['email']
        api_key = config['Credentials']['api_key']

        mdb.login(email, api_key)
        test_df = mdb.get_equity('AAPL', intraday=True)
        print(test_df)

    Security Notes
    ^^^^^^^^^^^^^^

    - Ensure your ``config.ini`` file is kept secure and out of the reach of unauthorized users.
    - Never commit the ``config.ini`` file to public version control repositories to prevent exposure of your credentials.



    .. With an API key and subscription, intraday data is available. To access intraday data, you must first login with your API key:

    .. .. code-block:: python

    ..     import moabdb as mdb

    ..     mdb.login('your-email', 'your-api-key')
    ..     test_df = mdb.get_equity('AAPL',intraday=True)
    ..     print(test_df)









.. Support and Further Reading
.. ---------------------------

.. If you encounter any issues or need further assistance:

.. * Check out our `FAQ Section <link-to-faq>`_.
.. * Dive deeper into our `API Reference <link-to-api-reference>`_.
.. * For technical issues, contact our `support team <support-email>`_.

Conclusion
----------

Congratulations! You've made your first API call with MoabDB. Explore further, integrate it with your applications, and make the most out of our powerful financial data.
