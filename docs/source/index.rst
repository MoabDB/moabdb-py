---
title: MoabDB Documentation
---

::::{grid}
:reverse:
:gutter: 2 1 1 1
:margin: 4 4 1 1

:::{grid-item}
:columns: 4

```{image} ./_static/favicons/android-chrome-192x192.png
:width: 150px
```
:::

:::{grid-item}
:columns: 8
:class: sd-fs-3

MoabDB API and Dataset Documentation

|release|
=========

:::

::::

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
