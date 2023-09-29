.. MoabDB documentation master file, created by
   sphinx-quickstart on Fri Dec 16 10:22:22 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================
MoabDB API Documentation
========================


.. image:: https://img.shields.io/pypi/v/moabdb.svg
   :target: https://pypi.python.org/pypi/moabdb

.. '<strong>{project}</strong> <i>{release}</i>'

MoabDB is a fast and easy-to-use database for financial data.
It is built with Rust for fast data retrieval and is accessible with Python for easy data manipulation.

.. note::

   If you're looking for subscriptions options, they are found at  
   `MoabDB.com <https://moabdb.com>`_


API Highlights
--------------

The MoabDB API offers the following features:

* Built with Rust for fast data retrieval
* Easily accessible with Python
* Simple and intuitive
* Robust data offerings
* Customizable requests


Data Provided by MoabDB
-----------------------

MoabDB provides the following data:

* Equities: Daily-level and Second-by-second
* Options: Daily-level and Minute-by-minute
* Interest Rates
* Financial Statements


.. toctree::
   :maxdepth: 2

   Documentation Home <https://docs.moabdb.com/index.html>
   MoabDB Home <https://moabdb.com>
   tutorial/quickstart

API Documentation
-----------------

.. toctree::
   :maxdepth: 1
   :caption: API calls

   api/login
   api/get_equity
   api/get_rates
   api/get_options
   api/get_bs
   api/get_is
   api/get_cf
   
Dataset Documentation
---------------------

.. toctree::
   :maxdepth: 2
   :caption: Datasets

   datasets/equity
   datasets/options
   datasets/financials_balancesheet
   datasets/financials_income
   datasets/financials_cashflows
   datasets/interest_rates
   

Examples and Guides
-------------------

.. toctree::
   :maxdepth: 2
   :caption: Simple Tutorials
 
   tutorial/simple_plot
   tutorial/return_distributions
   tutorial/calc_beta

.. .. toctree::
..    :maxdepth: 2
..    :caption: Intraday Tutorials

..    tutorial/quickstart
..    tutorial/simple_plot
..    tutorial/return_distributions
..    tutorial/candlesticks


.. .. toctree::
..    :maxdepth: 2
..    :caption: Advanced Tutorials

..    tutorial/quickstart
..    tutorial/simple_plot
..    tutorial/return_distributions
..    tutorial/candlesticks






Source code
-----------

The source code is available on GitHub at: `MoabDB GitHub Repository <https://github.com/MoabDB/moabdb-py>`_




.. ```python
.. import moabdb as mdb
.. mdb.get_equity("AAPL")
.. # something idk docs
.. ```
