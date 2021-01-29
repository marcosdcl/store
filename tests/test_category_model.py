import sys
sys.path.append('')

from models.categorty_model import Category
import pytest


def test_category_model_instance():
    category = Category('Test Name', 'Test Desciption')
    assert isinstance(category, Category)

def test_category_model_contructor():
    name = 'Test Name'
    description = 'Test Desciption'
    category = Category(name, description)
    assert category.name is name
    assert category.description is description

@pytest.mark.parametrize("name, description", [
    (10, 'Desc Categoria'),
    (10.5, 'Desc Categoria'),
    (False, 'Desc Categoria')
])
def test_category_model_name_not_str_exception(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)

@pytest.mark.parametrize("name, description", [
    ('Desc nome', None),
    ('Desc nome', 10.5),
    ('Desc nome', False)
])
def test_category_model_description_not_str_exception(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)

def test_category_model_name_empty_exception():
    with pytest.raises(ValueError):
        category = Category('   ', 'description')

def test_category_model_name_bigger_than_100_characters_exception():
    with pytest.raises(ValueError):
        category = Category('i'*101, 'description')

def test_category_model_description_bigger_than_255_characters_exception():
    with pytest.raises(ValueError):
        category = Category('name', 'i'*256)

