"""Models for the update_facts function. Simplifies type hinting."""
from typing import NamedTuple

from google.cloud import bigquery, pubsub


class GCPClients(NamedTuple):
    bigquery_client: bigquery.Client
    publisher: pubsub.PublisherClient


class EnvVars(NamedTuple):
    gcp_project_id: str
    bq_facts_table_fqdn: str
    bq_staging_table_fqdn: str
    topic_update_facts_complete: str
