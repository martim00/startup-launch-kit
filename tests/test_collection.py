from lunch.collection import Collection


class Books(Collection):
    pass


def test_collection_should_be_named():
    collection = Books()
    assert collection.name == 'books'


def test_collection_should_generate_endpoints():
    collection = Books()
    blueprint = collection.get_blueprint()
    assert len(blueprint.deferred_functions) == 6


def test_collection_should_save_new_item():
    collection = Books()
    collection.post()
