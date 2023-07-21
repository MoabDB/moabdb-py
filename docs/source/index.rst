.. MoabDB documentation master file, created by
   sphinx-quickstart on Fri Dec 16 10:22:22 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. .. image:: ../source/_static/images/MoabDB.jpg
..   :width: 400
..   :alt: Logo


MoabDB API and Dataset Documentation

|release|
=========

MoabDB is a fast and easy-to-use database for financial data. 
For subscriptions visit the homepage: `MoabDB.com <https://moabdb.com>`_

API Highlights
--------------

The MoabDB API offers the following features:

* Built with Rust for fast data retrieval
* Accessible with Python for easy data manipulation

Data Provided by MoabDB
-----------------------

MoabDB provides the following data:

* Equities: Daily-level and Second-by-second
* Options: Daily-level and Minute-by-minute
* Interest Rates
* Financial Statements

```python
import moabdb as mdb
mdb.get_equity("AAPL")
# something idk docs
```

Source code
-----------

The source code is available on GitHub at: `MoabDB GitHub Repository <https://github.com/MoabDB/moabdb-py>`_

Data Retrieval
-------------

.. toctree::
   :maxdepth: 2
   :caption: Get Data Functions

   api/get_equity
   api/get_rates

Datasets
-------------
.. toctree::
   :maxdepth: 2
   :caption: Datasets

   datasets/rates
   datasets/equity

..   moabdb
