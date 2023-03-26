from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

@pytest.fixture(scope='function')
def Books_Collector():
    return BooksCollector()

name_book = '1984'
worth_name = '1989' 
    
# Добавляем одну и ту же книгу дважды    
def test_add_theSameBook_not_add_in_list():
    Books_Collector.add_new_book(name_book)
    Books_Collector.add_new_book(name_book)
    assert Books_Collector.books_rating == {name_book: 1}

# Проверяем рейтинг, если меньше 1:
def test_set_rating_less_than_one_cant_set(Books_Collector):
    Books_Collector.add_new_book(name_book)
    Books_Collector.set_book_rating(name_book, 0)
    assert Books_Collector.favorites == []
    assert Books_Collector.books_rating == {name_book: 1}
 
 # Проверяем рейтинг, если больше 10:
def test_set_rating_more_than_ten_cant_set(Books_Collector):
    Books_Collector.add_new_book(name_book)
    Books_Collector.set_book_rating(name_book, 11)
    assert Books_Collector.favorites == []
    assert Books_Collector.books_rating == {name_book: 10}
 
# Проверяем на добавление книги в избранное
def test_add_to_favorites_add_to_favorites(Books_Collector):
    Books_Collector.add_new_book(name_book)
    Books_Collector.add_book_in_favorites(name_book)
    assert Books_Collector.favorites == [name_book]
    assert Books_Collector.books_rating == {name_book: 1}
 
# Проверяем на добавление книги в избранное без рейтинга
def test_add_to_favorites_without_ratings_not_add(Books_Collector):
    Books_Collector.add_book_in_favorites(name_book)
    assert Books_Collector.favorites == []
    assert Books_Collector.books_rating == {}
 
# Проверяем удалание книги из избранного
def test_delete_from_favorites_delete(Books_Collector):
    Books_Collector.add_new_book(name_book)
    Books_Collector.add_book_in_favorites(name_book)
    Books_Collector.delete_book_from_favorites(name_book)
    assert Books_Collector.favorites == []
    assert Books_Collector.books_rating == {name_book: 1}
 
# Проверяем список избранных книг 
def test_get_list_of_favorites_books_get(Books_Collector):
    Books_Collector.add_new_book(name_book)
    Books_Collector.add_book_in_favorites(name_book)
    assert Books_Collector.get_list_of_favorites_books() == [name_book]
 
# Проверяем рейтинг книги по её имени 
def test_get_books_rating_get(Books_Collector):
    Books_Collector.add_new_book(name_book)
    assert Books_Collector.get_books_rating() == {name_book: 1}

# Проверяем рейтинг книги с несуществующим рейтингом   
def test_get_books_with_specific_rating_fails_if_wrong_rating(Books_Collector):
    Books_Collector.add_new_book(name_book)
    result = Books_Collector.get_books_with_specific_rating(0)
    assert [] == result

# Проверяем отсуствующию книгу
def test_add_other_book_has_no_rating(Books_Collector):
    Books_Collector.add_new_book(name_book)
    rating = Books_Collector.get_book_rating(worth_name)
    assert rating is None
    