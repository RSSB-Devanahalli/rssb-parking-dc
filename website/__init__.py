from flask import Flask


def rssb_parking():
    app = Flask(__name__)

    from .views import views
    from .add import add
    from .search import search
    from .about import about

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(add, url_prefix='/')
    app.register_blueprint(search, url_prefix='/')
    app.register_blueprint(about, url_prefix='/')

    return app


