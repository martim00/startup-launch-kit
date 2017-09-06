from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_webpack import Webpack
from marshmallow import Schema, fields

from lunch import Lunch
from lunch.collection import Collection

app = Flask(__name__)
mongo = PyMongo(app)

lunch = Lunch(app)

app.config['WEBPACK_MANIFEST_PATH'] = 'build/manifest.json'
webpack = Webpack()

webpack.init_app(app)


@app.route("/")
def hello():
    return "jkn !"


# auth
# serialization rest
# serialization db
# callbacks
# more methods (put, delete, etc)

class BaseSchema(Schema):
    _id = fields.Str(dump_to='id')


class Users(Collection):

    class Model(BaseSchema):
        name = fields.Str()
        login = fields.Email()
        password = fields.Str()

    # def get(self):
    #     return 'override'

        # def post(self):
        #     pass
        #
        # def put(self):
        #     pass
        #
        # def delete(self):
        #     pass
        #
        # def validate(self):
        #     pass


lunch.register(Users())


@app.route('/api')
def api():
    online_users = mongo.db.users.find()
    return render_template('index.html', online_users=online_users)


if __name__ == '__main__':
    app.run(debug=True)
