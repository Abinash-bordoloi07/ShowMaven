from flask_restful import Resource
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
# Create SQLAlchemy engine to connect to the database
db_connect = create_engine('sqlite:///venues.db')

# Define a parser for incoming request arguments
venue_parser = reqparse.RequestParser()
venue_parser.add_argument('name', type=str, help='Name of the venue')
venue_parser.add_argument('location', type=str, help='Location of the venue')
venue_parser.add_argument('capacity', type=int, help='Capacity of the venue')

# Define a resource for venues
class Venue(Resource):
    def get(self, venue_id):
        # Retrieve a venue by its ID
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM venues WHERE id = ?", (venue_id,))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result

    def put(self, venue_id):
        # Update a venue by its ID
        conn = db_connect.connect()
        args = venue_parser.parse_args()
        name = args['name']
        location = args['location']
        capacity = args['capacity']
        query = conn.execute("UPDATE venues SET name = ?, location = ?, capacity = ? WHERE id = ?", (name, location, capacity, venue_id))
        return {'status': 'success'}

    def delete(self, venue_id):
        # Delete a venue by its ID
        conn = db_connect.connect()
        query = conn.execute("DELETE FROM venues WHERE id = ?", (venue_id,))
        return {'status': 'success'}

# Define a resource for a list of venues
class VenueList(Resource):
    def get(self):
        # Retrieve a list of venues
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM venues")
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return result

    def post(self):
        # Add a new venue
        conn = db_connect.connect()
        args = venue_parser.parse_args()
        name = args['name']
        location = args['location']
        capacity = args['capacity']
        query = conn.execute("INSERT INTO venues (name, location, capacity) VALUES (?, ?, ?)", (name, location, capacity))
        return {'status': 'success'}
