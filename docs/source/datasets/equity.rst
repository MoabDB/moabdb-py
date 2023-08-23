==================
Equity Market Data
==================

The Equity Market Data API provides comprehensive data about equity markets. The data can be accessed either at the end of the day or the beginning of the day. 

When accessed, the following dataframes are returned:

End of Day Data
===============

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
=============

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

