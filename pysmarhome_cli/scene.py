from .graphql.request import graphql_request
from .graphql.mutations import activate_scene_mutation


def activate_scene(args):
    [id] = args.id
    graphql_request(args.host, args.api_key, activate_scene_mutation(id))
