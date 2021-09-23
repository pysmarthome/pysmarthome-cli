from .graphql.request import graphql_request
from .graphql.mutations import dev_mutation


def trigger_action(args):
    [id, action_id, *action_args] = args.action
    graphql_request(args.host, args.api_key, dev_mutation(id, action_id, *action_args))
