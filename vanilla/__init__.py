from flask import Flask
from markdown import markdown as md

app = Flask(__name__)

# Initialise with some sensible defaults
app.config.update(
    DEBUG=True,
    SECRET_KEY='change this',
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db',
    UPLOAD_FOLDER='/tmp/vanilla_uploads',
    MAX_CONTENT_LENGTH=16 * 1024 * 1024,
)

def markdown (value):
	return Markup(md(value))

def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return value.strftime(format)

app.jinja_env.filters['markdown'] = markdown
app.jinja_env.filters['date'] = datetimeformat

from . import assets, models, views
