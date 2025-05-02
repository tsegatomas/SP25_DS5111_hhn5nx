{{ config(materialized = "table") }}

select
  EN,
  DE
from {{ ref('numbers') }}
