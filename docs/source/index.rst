.. MoabDB documentation master file, created by
   sphinx-quickstart on Fri Dec 16 10:22:22 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.



====================================
MoabDB API and Dataset Documentation
====================================

MoabDB is a fast and easy-to-use database for financial data.
It is built with Rust for fast data retrieval and is accessible with Python for easy data manipulation.

.. seealso::

   Information on subscriptions to advnaced datasets can be found at the homepage: 
   `MoabDB.com <https://moabdb.com>`_


API Highlights
--------------

The MoabDB API offers the following features:

* Built with Rust for fast data retrieval
* Accessible with Python for easy data manipulation

.. toctree::
   :maxdepth: 2

   Documentation Home <https://docs.moabdb.com/index.html>
   MoabDB Home <https://moabdb.com>
   
.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorial/installation
   tutorial/simple_example


.. toctree::
   :maxdepth: 2
   :caption: Datasets

   datasets/equity
   datasets/interest_rates
   datasets/options
   .. datasets/financials_balancesheet
   .. datasets/financials_cashflows
   .. datasets/financialss_income

.. toctree::
   :maxdepth: 2
   :caption: API

   api/login
   api/get_equity
   api/get_rates
   api/get_options
   .. api/get_bs
   .. api/get_cf
   .. api/get_is

   
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




   .. moabdb

.. .. toctree::
..    :maxdepth: 2
..    :caption: Navigation

..    MoabDB Home <https://moabdb.com>
..    Docs Home <https://docs.moabdb.com/index.html>
..    tutorial
..    api
..    datasets
