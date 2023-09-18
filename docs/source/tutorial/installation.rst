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


Setting up without API Key
--------------------------

1. **Import MoabDB Library**:

   Once installed, configure the client library:

   .. code-block:: python

      import moabdb as mdb

2. **Test Connection**:

   Verify that the setup is successful:

   .. code-block:: python

      import moabdb as mdb
      test_df = mdb.get_equity('AAPL')
      print(test_df)

Setting up with API Key
-----------------------

Here's a simple example of retrieving financial data for a specific company:

.. code-block:: python

   import moabdb as mdb
   mdb.login('your-email', 'your-api-key')
   test_df = mdb.get_equity('AAPL',intraday=True)
   print(test_df)


Support and Further Reading
---------------------------

.. If you encounter any issues or need further assistance:

.. * Check out our `FAQ Section <link-to-faq>`_.
.. * Dive deeper into our `API Reference <link-to-api-reference>`_.
.. * For technical issues, contact our `support team <support-email>`_.

Conclusion
----------

Congratulations! You've made your first API call with MoabDB. Explore further, integrate it with your applications, and make the most out of our powerful financial data.
