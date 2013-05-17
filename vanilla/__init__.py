from flask import Flask

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='change this',
    MONGODB_SETTINGS={
        'DB': 'default'
    }
)

import vanilla.assets
import vanilla.models
import vanilla.views
