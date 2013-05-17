from vanilla import app
from flask.ext.assets import Environment, Bundle

assets = Environment(app)
assets.debug = True
assets.register('js', Bundle(
    # JavaScript
    'js/vendor/jquery-2.0.0.js',
    'js/vendor/handlebars-runtime-1.0.0.js',
    # Templates
    Bundle(
        '../src/templates/*.handlebars',
        filters='handlebars',
        output='templates-%(version)s.js',
    ),
    # Coffee
    Bundle(
        '../src/coffee/*.cs',
        filters='coffeescript',
        output='coffee-%(version)s.js',
    ),
    filters='uglifyjs',
    output='app-%(version)s.js',
))
assets.register('css', Bundle(
    # CSS
    'css/vendor/normalize-2.1.2.css',
    # SCSS
    Bundle(
        '../src/scss/style.scss',
        filters='scss',
        output='scss-%(version)s.css',
    ),
    filters='cleancss',
    output='style-%(version)s.css',
))
