from venv import logger

fileName = 'Data1.txt'

def fun_journalMenu():
    print("\n" * 5)
    print('*' * 5, end="")
    print('File Journal Menu', end="")
    print('*' * 5)
    print('1. Add Entry')
    print('1. Read All Entries')
    print('1. Search Entries')
    print('1. Exit')

def func_user_operation():
    fun_journalMenu()
    try:
        option = int(input('Choose Option (1-4)'))
        while option != 4:
            if option > 3 or option < 1:
                print('Choose Option fom 1-4')
            elif option == 1:
                fun_add_entry()
            elif option == 2:
                fun_read_entries()
            else:
                fun_search_entry()
            fun_journalMenu()
            option = int(input('Choose Option (1-4)'))
    except Exception as e:
        logger.exception(e)
        func_user_operation()


def fun_add_entry():
    entry = input("Enter the entry to be added")
    file = open(fileName, 'a')
    entry = "\n" + entry
    file.writelines(entry)
    file.close()


def fun_read_entries():
    file = open(fileName, 'r')
    data = file.read()
    print(data)
    file.close()

def fun_search_entry():
    entry = input("Enter the entry to be Searched")
    file = open(fileName, 'r')
    data = file.readlines()
    for line in data:
        if entry.lower() in line.lower():
            print(line.strip())
            return
    else:
        print("Keyword not found")
    file.close()

func_user_operation()