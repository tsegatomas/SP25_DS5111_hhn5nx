{{ config(materialized = "table") }}

select message
from {{ ref('yahoo_gainers_20250411_185406') }}

union all

select message
from {{ ref('wsj_gainers_20250411_185406') }}
