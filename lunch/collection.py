from flask import Blueprint, request, jsonify


class Collection:
    def __init__(self):
        self.name = self.__class__.__name__.lower()
        self.blueprint = Blueprint(self.name, __name__)
        self._configure_blueprint()
        self._db = None

    def get_blueprint(self):
        return self.blueprint

    def configure_db(self, _db):
        self._db = _db

    @property
    def db(self):
        assert self._db, 'You need to call configure_db before using this collection.'
        return self._db

    def get(self):
        cursor = self.db.users.find()
        schema = self._get_schema(many=True)
        data = schema.dump(cursor).data
        return jsonify(data), 200

    def _get_schema(self, many=False):
        schema = self.__class__.Model(many=many)
        return schema

    def post(self):
        data = request.values
        data = self.before_post(data)
        saved = self.save(data)
        response = self.after_post(saved)
        return jsonify(response), 201

    def save(self, data):
        schema = self._get_schema()
        errors = schema.validate(data)
        if errors:
            raise Exception(errors)

        obj = schema.dump(data).data

        result = self.db.users.insert_one(obj)

        if not result.acknowledged:
            raise Exception('Could not save the object')

        obj = schema.dump(obj).data

        return obj

    def before_post(self, data):
        return data

    def after_post(self, data):
        return data

    def put(self):
        return 'put'

    def delete(self):
        return 'delete'

    def head(self):
        return 'head'

    def options(self):
        return 'options'

    def _configure_blueprint(self):

        @self.blueprint.route('/{}'.format(self.name), methods=['GET'])
        def _get():
            return self.get()

        @self.blueprint.route('/{}'.format(self.name), methods=['POST'])
        def _post():
            return self.post()

        @self.blueprint.route('/{}'.format(self.name), methods=['PUT'])
        def _put():
            return self.put()

        @self.blueprint.route('/{}'.format(self.name), methods=['DELETE'])
        def _delete():
            return self.delete()

        @self.blueprint.route('/{}'.format(self.name), methods=['OPTIONS'])
        def _options():
            return self.options()

        @self.blueprint.route('/{}'.format(self.name), methods=['HEAD'])
        def _head():
            return self.head()
