# Lab 08 – Stock Gainer / Candlestick Data ER Diagram

The goal is to turn one week of raw “gainer” CSVs into tables that answer simple questions for non‑financial stakeholders:

* **Which symbols appear repeatedly during the week?**
* **What are the basic daily price‑range stats (open / high / low / close)?**

```mermaid
erDiagram
    RAW_GAINERS {
        string   SYMBOL
        float    PRICE
        int      VOLUME
        datetime INGEST_TS
    }
    CLEAN_GAINERS {
        string   SYMBOL
        date     TRADE_DATE
        float    OPEN
        float    HIGH
        float    LOW
        float    CLOSE
        int      VOLUME
    }
    SYMBOL_REPEAT_SUMMARY {
        string   SYMBOL
        int      DAYS_APPEARED
        int      TOTAL_VOLUME
    }
    PRICE_DISTRIBUTION {
        date     TRADE_DATE
        float    MIN_PRICE
        float    MAX_PRICE
        float    AVG_PRICE
    }

    RAW_GAINERS     ||--|{ CLEAN_GAINERS          : "cleaned to"
    CLEAN_GAINERS   ||--o{ SYMBOL_REPEAT_SUMMARY  : "aggregates"
    CLEAN_GAINERS   ||--o{ PRICE_DISTRIBUTION     : "aggregates"

