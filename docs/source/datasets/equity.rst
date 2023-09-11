.. _equity-data-ref:

==================
Equity Market Data
==================

.. note::
    See :ref:`get-equity-ref` for documentation and retrieving 
    equity data using the MoabDB API.

The Equity Market Data API provides comprehensive data about 
equity markets. The data can be accessed either at the end 
of the day or the beginning of the day. 

Variables
=========

End of Day Data
---------------

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - DataFrame Column
     - Variable Description
   * - ``Symbol`` (str)
     - Ticker symbol of the equity.
   * - ``Open`` (float)
     - Opening trade price.
   * - ``High`` (float)
     - Highest trade price.
   * - ``Low`` (float)
     - Lowest trade price.
   * - ``Close`` (float)
     - Closing trade price.
   * - ``VWAP`` (float)
     - Volume-weighted average price.
   * - ``BidPrc`` (float)
     - Bid price.
   * - ``AskPrc`` (float)
     - Ask price.
   * - ``Volume`` (int)
     - Volume traded.
   * - ``Trades`` (int)
     - Number of trades.

Intraday Data
-------------

.. list-table:: 
   :widths: 25 75
   :header-rows: 1

   * - DataFrame Column
     - Variable Description
   * - ``Symbol`` (str)
     - Ticker symbol of the equity.
   * - ``Trades`` (int)
     - Number of trades.
   * - ``Volume`` (int)
     - Volume traded.
   * - ``Imbalance`` (int)
     - Buy-initiated volume minus sell-initiated volume.
   * - ``Close`` (float)
     - Closing trade price.
   * - ``VWAP`` (float)
     - Volume-weighted average price.
   * - ``BidPrc`` (float)
     - Bid price.
   * - ``AskPrc`` (float)
     - Ask price.
   * - ``BidSz`` (int)
     - Round lots available at BidPrc.
   * - ``AskSz`` (int)
     - Round lots available at AskPrc.



About the Data
==============

Exchanges
---------

Equity Market Data is sourced from leading global exchanges, 
ensuring a comprehensive coverage of major market activities. 
From the New York Stock Exchange to the Tokyo Stock Exchange, 
our data encompasses a broad spectrum of markets to offer users 
insights from different parts of the world. The integration of 
data from multiple exchanges provides users with a holistic 
view of the market, making it easier to spot global trends 
and correlations.

Trades
------

Trade data represents the core of our offering. With each trade, 
a wealth of information is produced. Beyond the basics of price 
and volume, our data captures the nuances of each transaction, 
providing insights such as the direction of the trade (buy or sell), 
the size of the trade, and the exact timestamp. Such granular 
data can be invaluable for high-frequency traders, market makers, 
and anyone interested in a deep dive into market microstructure.

Quotes and the Bid-Ask Spread
-----------------------------

In the world of finance, quotes are the lifeblood of trading. 
A quote provides the most recent price at which an asset, 
in this case equities, was traded. But beyond the last traded price, 
our data dives into the details of the bid and ask prices. 
This bid-ask spread can be an important indicator of liquidity and 
potential transaction costs. A tighter spread often indicates a more 
liquid market, while a wider spread can signify less liquidity. 
Our API not only provides the bid and ask prices but also offers the 
size (in terms of volume) associated with these quotes, further 
adding depth to your analysis.

VWAP
----

The Volume-Weighted Average Price (VWAP) is a critical metric for 
many institutional investors. Serving as a benchmark, VWAP helps 
traders understand if they received a good price for their trades 
relative to the day's trading activity. Our data provides the VWAP 
for each equity, ensuring that users can gauge their trading 
efficiency and make more informed decisions in future trades.

Data Accuracy and Integrity
===========================

Ensuring the accuracy and integrity of our data is paramount. 
With advanced algorithms and stringent quality checks, 
we ensure that the data provided is free from anomalies and 
aberrations. Any discrepancies, no matter how minor, are 
quickly identified and rectified. Our commitment to data 
quality means that users can trust the insights derived 
from our platform, making critical decisions with confidence.

Accessing Data
==============

See :ref:`get-equity-ref` for documentation and retrieving 
equity data using the MoabDB API.
