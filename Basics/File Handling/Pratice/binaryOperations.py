import struct

RECORD_SIZE = 14

def func_add_player(id,name):
    with open('palyer.dat', 'ab') as file:
        name = name.encode().ljust(10)
        record = struct.pack('i10s', id, name)
        """
        i10s -> i stands for integer, s stands for String, 10 stands for 10 charcter, its for string
        denotation: 
        h -> short 2 byte
        i -> int 4 byte
        I -> unsigned int 4 byte
        l -> long 8 byte
        s -> string <depends on number of character>
        f -> float 4 byte
        d -> double 8 byte
        ? -> boolean 1 byte
        p -> character 1 byte
        """
        file.write(record)

def func_find(index):
    with open('palyer.dat', 'rb') as f:
        f.seek(index * RECORD_SIZE)
        record = f.read(RECORD_SIZE)
        if record:
            id, name = struct.unpack('i10s', record)
            print(f'Id: {id}, Name : {name.decode()}')
        else:
            print("No record at that Index")

func_add_player(14,"Smith")
func_add_player(18, "Kohli")
func_add_player(7, "Dhoni")
func_find(2)
