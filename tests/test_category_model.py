import sys
sys.path.append('')

from models.categorty_model import Category


def test_category_model_instance():
    category = Category('Test Name', 'Test Desciption')
    assert isinstance(category, Category)

def test_category_model_contructor():
    category = Category('Test Name', 'Test Desciption')
    assert category.name == 'Test Name'
    assert category.description == 'Test Desciption'

def test_category_model_name_exception_if_type_not_string():
    try:
        category = Category(None, 'description')
        raise NotImplementedError('The expected exception was not raised.')
    except Exception as error:
        assert isinstance(error, TypeError)

def test_category_model_name_exception_if_string_is_empty():
    try:
        category = Category('   ', 'description')
        raise NotImplementedError('The expected exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)

def test_category_model_name_exception_if_string_is_bigger_than_100_characters():
    try:
        category = Category('i'*100, 'description')
        raise NotImplementedError('The expected exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)
