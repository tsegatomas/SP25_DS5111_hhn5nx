{{ config(materialized = "table") }}

select
  EN,
  FR
from {{ ref('numbers') }}
