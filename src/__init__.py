from flask import Flask, session
from src.routes import Routes
from flask_bootstrap import Bootstrap

# the root of the appliction and the routes

app = Flask(__name__)
app.secret_key = "secret"
bootstrap = Bootstrap(app)


routes = Routes(app, session)
routes.initRoutes()
