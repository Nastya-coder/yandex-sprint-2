import pytest
from main import BooksCollector


@pytest.fixture(scope='function')
def Books_Collector():
    return BooksCollector()
