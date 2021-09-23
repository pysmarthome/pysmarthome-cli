from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport


def graphql_request(addr, api_key, query):
    transport = AIOHTTPTransport(url=addr, headers={'Authorization': api_key})
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client.execute(gql(query))
