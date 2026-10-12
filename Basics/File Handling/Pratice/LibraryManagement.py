from venv import logger
import struct as st

class BookNotFoundError(Exception):
    pass

fileName = 'library_stock.dat'
id = 0
title = 1
author = 2
stock = 3
RECORD_SIZE = 68

def fun_libraryMenu():
    print("\n" * 5)
    print('*' * 5, end="")
    print('Library Menu', end="")
    print('*' * 5)
    print('1. Add Book')
    print('2. Search Book')
    print('3. View All Book')
    print('4. Delete a Book')

def func_user_operation():
    fun_libraryMenu()
    try:
        option = int(input('Choose Option (1-5)'))
        while option != 5:
            if option > 4 or option < 1:
                print('Choose Option fom 1-4')
            elif option == 1:
                func_check_and_add_book()
            elif option == 2:
                fun_read_entries()
            # elif option == 3:
            #     fun_read_entries()
            # else:
            #     fun_search_entry()
            fun_libraryMenu()
            option = int(input('Choose Option (1-5)'))
    except Exception as e:
        logger.exception(e)
        func_user_operation()

def fun_read_entries():
    with open(fileName, 'rb') as file:
        while True:
            record = file.read(RECORD_SIZE)
            if not record:  # b'' means end of file
                break
            book = func_unpack(record)
            print(f'Id: {book[id]}, Title: {book[title].decode().strip()}, '
                  f'Author: {book[author].decode().strip()}, Stock Unit: {book[stock]}')

def fun_get_entries():
    books = []
    with open(fileName, 'rb') as file:
        while True:
            record = file.read(RECORD_SIZE)
            if not record:  # b'' means end of file
                break
            books.append(record)
    return books

def func_check_and_add_book():
    try:
        book_id = int(input('Enter id of the book'))
    except Exception as e:
        print('No Book Id give, will search with Title')
        book_id = None
    book_title = input('Enter Title of the book (50 char Max)')
    book_author = input('Enter Author of the Book (10 Char Max)')

    existing_record = func_search_book(input_id=book_id, input_title=book_title)
    if existing_record:
        func_update_stock_by_index(existing_record[4], existing_record[stock] + 1)
    else:
        id = fun_read_bookid_incremental()
        func_add_book(id, book_title, book_author, 1)

def func_add_book(book_id, book_title, book_author, book_stock):
    with open(fileName, 'ab') as file:
        file.write(func_pack(int(book_id), book_title.ljust(50).encode(), book_author.ljust(10).encode(), int(book_stock)))

def fun_read_bookid_incremental():
    with open('book_id.txt', 'r+') as file:
        current_id = file.read()
        next_id = int(current_id) + 1
        file.seek(0,0)
        file.write(str(next_id))
        return int(current_id)

def func_update_stock_by_index(index, updated_stock):
    global id, title, author, stock
    with open(fileName, 'r+b') as file:
        file.seek(index * RECORD_SIZE)
        book = func_unpack(file.read(RECORD_SIZE))
        book_title = book[title].decode().strip()
        book_author = book[author].decode().strip()
        record = func_pack(int(book[id]), book_title.ljust(50).encode(), book_author.ljust(10).encode(), int(updated_stock))
        file.seek(index * RECORD_SIZE)       # read() moved the cursor forward, so go back
        file.write(record)


def func_unpack(record):
    book_id, book_title, book_author, book_stock = st.unpack('i50s10si', record)
    return book_id, book_title, book_author, book_stock

def func_pack(book_id, book_title, book_author, book_stock):
    book_record = st.pack('i50s10si', book_id, book_title, book_author, book_stock)
    return book_record

def func_search_book(*, input_id=None, input_title=None):
    global id, author, title, stock
    try:
        with open(fileName, 'rb') as file:
            records = fun_get_entries()
            if input_id != None:
                index = 0
                for record in records:
                    book = func_unpack(record)
                    if book[id] == input_id:
                        return id, book[title].decode().strip(), book[author].decode().strip(), book[stock], index
                    index += 1
                else:
                    raise BookNotFoundError("No book present with give Id")
            elif input_title != None:
                index = 0
                for record in records:
                    book = func_unpack(record)
                    book_title = book[title].decode().strip()
                    if book_title == input_title:
                        return book[id], book_title, book[author].decode().strip(), book[stock], index
                    index += 1
                else:
                    raise BookNotFoundError("No book present with give Id")
            else:
                return None
    except Exception as e:
        return None

func_user_operation()