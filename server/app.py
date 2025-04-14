from models import db, Episode, Guest, Appearance
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route("/")
def index():
    return "<h1>Late Show Code Challenge</h1>"

@app.route("/episodes")
def get_episodes():
    episodes=db.session.query(Episode).all()
    response=[episode.to_dict(only=("id", "date", "number")) for episode in episodes]

    return jsonify(response)

@app.route("/episodes/<int:id>")
def get_episode_by_id(id):
    episode=db.session.query(Episode).filter_by(id=id).first()

    if episode:
        return jsonify({
            'id':episode.id,
            'date':episode.date,
            'number':episode.number,
            "appearances": [
                {
                    "episode_id": appearance.id,
                    "guest": {
                        "id": appearance.guest.id,
                        "name": appearance.guest.name,
                        "occupation": appearance.guest.occupation
                    },
                    "guest_id": appearance.guest_id,
                    "id": appearance.guest.id,
                    "rating": appearance.rating,
                } 
                for appearance in episode.appearances
            ]
        })
    else:
        return jsonify({"error": "Episode not found"}), 404

@app.route("/guests")
def get_guests():
    guests=db.session.query(Guest).all()
    response=[guest.to_dict(only=("id", "name", "occupation")) for guest in guests]
    return jsonify(response)

@app.route("/appearances", methods=["POST"])
def post_appearance():
    data=request.get_json()
    rating=data.get("rating")
    episode_id=data.get("episode_id")
    guest_id=data.get("guest_id")

    guest = db.session.query(Guest).filter_by(id=guest_id).first()
    episode = db.session.query(Episode).filter_by(id=episode_id).first()

    errors=[]
    if not guest:
        errors.append("Invalid guest_id: Guest not found")
    if not episode:
        errors.append("Invalid episode_id: Episode not found")

    if errors:
        return jsonify({"errors": errors}), 400
    
    new_appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        "id": new_appearance.id,
        "rating": new_appearance.rating,
        "guest_id": new_appearance.guest_id,
        "episode_id": new_appearance.episode_id,
        "episode": episode.to_dict(only=("id", "date", "number")),
        "guest": guest.to_dict(only=("id", "name", "occupation"))
        
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
