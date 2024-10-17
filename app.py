from flask_restful import Resource
from models import Episode, Guest, Appearance
from flask import jsonify, make_response, request
from config import api, db, app


class EpisodeListResource(Resource):
    def get(self):
        episodes = [episode.to_dict() for episode in Episode.query.all()]
        return make_response(jsonify(episodes), 200)


class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found"}, 404
        return {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": [
                {
                    "id": appearance.id,
                    "rating": appearance.rating,
                    "guest_id": appearance.guest_id,
                    "guest": appearance.guest.to_dict(),
                    "episode_id": appearance.episode_id,
                }
                for appearance in episode.appearances
            ],
        }, 200


class EpisodeResource(Resource):
    def get(self, id):
        episode = Episode.query.filter_by(id=id).first()
        return make_response(jsonify(episode.to_dict()), 200)


class GuestListResource(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200


class AppearanceResource(Resource):
    def post(self):
        data = request.get_json()
        new_appearance = Appearance(
            rating=data["rating"],
            episode_id=data["episode_id"],
            guest_id=data["guest_id"],
        )
        db.session.add(new_appearance)
        db.session.commit()

        return new_appearance.to_dict(), 201


api.add_resource(EpisodeListResource, "/episodes")
api.add_resource(EpisodeResource, "/episodes/<int:id>")
api.add_resource(GuestListResource, "/guests")
api.add_resource(AppearanceResource, "/appearances")


if __name__ == "__main__":
    app.run(port=5555, debug=True)
