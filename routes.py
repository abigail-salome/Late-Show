from flask_restful import Api
from app import (
    EpisodeListResource,
    EpisodeResource,
    GuestListResource,
    AppearanceResource,
)


def initialize_routes(api):
    api.add_resource(EpisodeListResource, "/episodes")
    api.add_resource(EpisodeResource, "/episodes/<int:id>")
    api.add_resource(GuestListResource, "/guests")
    api.add_resource(AppearanceResource, "/appearances")
