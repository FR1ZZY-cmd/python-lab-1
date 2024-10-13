# TODO Найдите количество книг, которое можно разместить на дискете
ONE_CHAR_SIZE = 4
SIZE_DISCETE = 1.44 * 1024 * 1024
book = {
    'count_pages': 100,
    'count_rows_on_page': 50,
    'count_chars_in_row': 25
}
count_books = int(SIZE_DISCETE // (book['count_pages'] * book['count_rows_on_page']* book['count_chars_in_row'] * ONE_CHAR_SIZE))

print("Количество книг, помещающихся на дискету:", count_books)
