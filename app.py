from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

# Flask Configs
app = Flask(__name__)
app.url_map.strict_slashes = False
api = Api(app)

# MongoDB Configs
app.config['MONGO_URI'] = 'mongodb://localhost:27017/movie-bag'

# Initialize App
initialize_db(app)
initialize_routes(api)

app.run(debug=True)
