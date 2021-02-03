import sys
sys.path.append('')

from controllers.base_controller import BaseController
from controllers.category_controller import CategoryController
from models.category_model import Category
import pytest


@pytest.fixture
def create_instance():
    controller = CategoryController()
    return controller

def test_category_controller_instance(create_instance):

    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)


def test_read_all_should_return_list(create_instance):

    result = create_instance.read_all()

    assert isinstance(result, list)


def test_create_category(create_instance):
    name = 'Name test'
    description = 'Description test'
    category = Category(name, description)

    result = create_instance.create(category)

    assert result.id_ is not None
    assert result.name == name
    assert result.description == description

    create_instance.delete(result)


def test_update_category(create_instance):
    name = 'Name test'
    description = 'Description test'
    category = Category(name, description)
    created = create_instance.create(category)

    created.name = 'Name test 2'
    created.description = 'Description test 2'
    result = create_instance.update(created)

    assert result.id_ is not None
    assert result.name == 'Name test 2'
    assert result.description == 'Description test 2'

    create_instance.delete(result)


def test_delete_category(create_instance):
    name = 'Name test'
    description = 'Description test'
    category = Category(name, description)
    created = create_instance.create(category)

    create_instance.delete(created)

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id_)
        assert exc.value == 'Object not found in database.'


def test_read_by_id_should_return_category(create_instance):
    name = 'Name test'
    description = 'Description test'
    category = Category(name, description)
    created = create_instance.create(category)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Category)
    assert result.name == name
    assert result.description == description

    create_instance.delete(created)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = CategoryController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(57842395)
        assert exc.value == 'Object not found in database.'
