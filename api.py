from collections import OrderedDict
from flask_restful import Resource
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from models import db, Show, Venue
from flask import jsonify
from flask import Flask

app = Flask(__name__)
api = Api(app)


# class VenueAPI(Resource):
#     def get(self, venue_id):
#         venue = Venue.query.filter_by(id=venue_id).first()
#         if venue:
#             return jsonify(venue.to_dict())
#         else:
#             return {'error': 'Venue not found'}, 404

#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True, help='Venue name is required')
#         parser.add_argument('city', type=str, required=True, help='Venue city is required')
#         parser.add_argument('state', type=str, required=True, help='Venue state is required')
#         args = parser.parse_args()

#         venue = Venue(name=args['name'], city=args['city'], state=args['state'])
#         db.session.add(venue)
#         db.session.commit()

#         return {'message': 'Venue added successfully'}, 201

#     def put(self, venue_id):
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str)
#         parser.add_argument('city', type=str)
#         parser.add_argument('state', type=str)
#         args = parser.parse_args()

#         venue = Venue.query.filter_by(id=venue_id).first()
#         if venue:
#             if args['name']:
#                 venue.name = args['name']
#             if args['city']:
#                 venue.city = args['city']
#             if args['state']:
#                 venue.state = args['state']
#             db.session.commit()

#             return {'message': 'Venue updated successfully'}
#         else:
#             return {'error': 'Venue not found'}, 404

#     def delete(self, venue_id):
#         venue = Venue.query.filter_by(id=venue_id).first()
#         if venue:
#             db.session.delete(venue)
#             db.session.commit()

#             return {'message': 'Venue deleted successfully'}
#         else:
#             return {'error': 'Venue not found'}, 404

# Create SQLAlchemy engine to connect to the database
# db_connect = create_engine('sqlite:///venues.db')

# Define a parser for incoming request arguments
# venue_parser = reqparse.RequestParser()
# venue_parser.add_argument('name', type=str, help='Name of the venue')
# venue_parser.add_argument('location', type=str, help='Location of the venue')
# venue_parser.add_argument('capacity', type=int, help='Capacity of the venue')

# # Define a resource for venues
# class VenueAPI(Resource):
#     def get(self, venue_id):
#         # Retrieve a venue by its ID
#         conn = db_connect.connect()
#         query = conn.execute("SELECT * FROM venues WHERE id = ?", (venue_id,))
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return result

#     def put(self, venue_id):
#         # Update a venue by its ID
#         conn = db_connect.connect()
#         args = venue_parser.parse_args()
#         name = args['name']
#         location = args['location']
#         capacity = args['capacity']
#         query = conn.execute("UPDATE venues SET name = ?, location = ?, capacity = ? WHERE id = ?", (name, location, capacity, venue_id))
#         return {'status': 'success'}

#     def delete(self, venue_id):
#         # Delete a venue by its ID
#         conn = db_connect.connect()
#         query = conn.execute("DELETE FROM venues WHERE id = ?", (venue_id,))
#         return {'status': 'success'}

# # Define a resource for a list of venues
# class VenueList(Resource):
#     def get(self):
#         # Retrieve a list of venues
#         conn = db_connect.connect()
#         query = conn.execute("SELECT * FROM venues")
#         result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
#         return result

#     def post(self):
#         # Add a new venue
#         conn = db_connect.connect()
#         args = venue_parser.parse_args()
#         name = args['name']
#         location = args['location']
#         capacity = args['capacity']
#         query = conn.execute("INSERT INTO venues (name, location, capacity) VALUES (?, ?, ?)", (name, location, capacity))
#         return {'status': 'success'}

 
class VenueAPI(Resource):
    def get(self, venue_id):
        venue = Venue.query.filter_by(id=venue_id).first()
        if venue:
            return jsonify(venue.to_dict())
        else:
            return {'error': 'Venue not found'}, 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Venue name is required')
        parser.add_argument('city', type=str, required=True, help='Venue city is required')
        parser.add_argument('state', type=str, required=True, help='Venue state is required')
        args = parser.parse_args()

        venue = Venue(name=args['name'], city=args['city'], state=args['state'])
        db.session.add(venue)
        db.session.commit()

        return {'message': 'Venue added successfully'}, 201

    def put(self, venue_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('city', type=str)
        parser.add_argument('state', type=str)
        args = parser.parse_args()

        venue = Venue.query.filter_by(id=venue_id).first()
        if venue:
            if args['name']:
                venue.name = args['name']
            if args['city']:
                venue.city = args['city']
            if args['state']:
                venue.state = args['state']
            db.session.commit()

            return {'message': 'Venue updated successfully'}
        else:
            return {'error': 'Venue not found'}, 404

    def delete(self, venue_id):
        venue = Venue.query.filter_by(id=venue_id).first()
        if venue:
            db.session.delete(venue)
            db.session.commit()

            return {'message': 'Venue deleted successfully'}
        else:
            return {'error': 'Venue not found'}, 404

 
class ShowAPI(Resource):
    def get(self, show_id):
        show = Show.query.get_or_404(show_id)
        return {'id': show.id, 'title': show.title, 'start_time': show.start_time.isoformat()}

    def put(self, show_id):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('start_time', type=str, required=True, help='Start time is required')
        args = parser.parse_args()

        show = Show.query.get_or_404(show_id)
        show.title = args['title']
        show.start_time = args['start_time']
        db.session.commit()

        return {'id': show.id, 'title': show.title, 'start_time': show.start_time.isoformat()}

    def delete(self, show_id):
        show = Show.query.get_or_404(show_id)
        db.session.delete(show)
        db.session.commit()
        return {'message': 'Show deleted successfully'}

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True, help='Title is required')
        parser.add_argument('start_time', type=str, required=True, help='Start time is required')
        parser.add_argument('venue_id', type=int, required=True, help='Venue ID is required')
        args = parser.parse_args()

        show = Show(title=args['title'], start_time=args['start_time'], venue_id=args['venue_id'])
        db.session.add(show)
        db.session.commit()

        return {'id': show.id, 'title': show.title, 'start_time': show.start_time.isoformat()}
    
    if __name__ == '__main__':
        app.run(debug=True)