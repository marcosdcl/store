from dao.base_dao import BaseDao
from models.category_model import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
