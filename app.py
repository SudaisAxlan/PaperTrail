from flask import Flask
from Routes.AllRoutes import routes

app=Flask(__name__)

app.register_blueprint(routes)






if __name__ == "__main__":
    app.run(debug=True)