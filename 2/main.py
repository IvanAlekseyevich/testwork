import json
import os
import uuid

DATA_FILE = 'library.json'
STATUS_CHOICE = {'в наличии', 'выдана'}
SEARCH_CHOICE = {'title', 'author', 'year'}


def load_data() -> dict:
    '''Загрузка данных из файла'''
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_data(data: dict) -> None:
    """Сохранение данных в файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def generate_book_id() -> str:
    '''Генерация id книги'''
    return str(uuid.uuid4())


def add_book(data: dict, title: str, author: str, year: str) -> None:
    '''Добавление книги'''
    if not year.isdigit():
        print('Неверно указан год.')
        return
    new_book_id = generate_book_id()
    new_book = {
        'title': title,
        'author': author,
        'year': year,
        'status': 'в наличии'
    }
    data[new_book_id] = new_book
    save_data(data)
    print("Книга добавлена!")


def delete_book(data: dict, book_id: str) -> None:
    '''Удаление книги'''
    if book_id in data:
        data.pop(book_id)
        save_data(data)
        print("Книга удалена!")
        return
    print("Книга с указанным id не найдена.")


def search_books(data: dict, query: str, field: str) -> list:
    '''Поиск книги'''
    if not field in SEARCH_CHOICE:
        print('Неверно выбран тип поиска.')
        return
    result = []
    for book_id, book_data in data.items():
        if book_data[field].lower() == query.lower():
            result.append(
                f"id: {book_id}, "
                f"title: {book_data['title']}, "
                f"author: {book_data['author']}, "
                f"year: {book_data['year']} "
                f"status: {book_data['status']}"
            )
    return result


def display_books(data: dict) -> None:
    '''Вывод всех книг'''
    if not data:
        print("Библиотека пуста.")
    for book_id, book_data in data.items():
        print(f"id: {book_id}", *[f"{k}: {v}" for k, v in book_data.items()])


def update_status(data: dict, book_id: str, new_status: str) -> None:
    '''Изменение статуса книги'''
    if new_status not in STATUS_CHOICE:
        print("Введен неверный статус!")
    elif book_id in data:
        data[book_id]['status'] = new_status
        save_data(data)
        print("Статус книги обновлен!")
    else:
        print("Книга с указанным id не найдена.")


def main() -> None:
    '''Главное меню'''
    data = load_data()
    while True:
        print("\nМеню")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        choice = input("> ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            add_book(data, title, author, year)
        elif choice == '2':
            book_id = input("Введите id книги для удаления: ")
            delete_book(data, book_id)
        elif choice == '3':
            field = input("Искать по (title, author, year): ")
            query = input("Введите поисковый запрос: ")
            results = search_books(data, query, field)
            if results:
                print(*results, sep='\n')
            else:
                print("Книги не найдены.")
        elif choice == '4':
            display_books(data)
        elif choice == '5':
            book_id = input("Введите id книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            update_status(data, book_id, new_status)
        elif choice == '6':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
