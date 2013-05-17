from vanilla import app
from flask.ext.mongoengine import MongoEngine

db = MongoEngine(app)
