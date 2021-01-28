from models.categorty_model import Category


def test_model_instance():
    category = Category('Test Name', 'Test Desciption')
    assert isinstance(category, Category)
