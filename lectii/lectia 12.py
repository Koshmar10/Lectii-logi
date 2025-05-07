#fisiere
# 1. Deschiderea fisierului (mai multe moduri)

# [ r, w, a, r+, w+, a+]
# r - doar citim din fisier 
# w - scriem in fisier dar starge continutul anterior sau creaza  fisier in caz ca incercam 
# sa citim din fisier care nu exista
# a - scrie in continuarea continutului ce exista deja 
# r+ - //---// + scriere
# w+ - //---// + citire
# a+ - //---// + citire

# 2. Citire/scriere ()
# 3. Inchiderea fisierului

def file_reader():
    file = open("lectii/lectia12.txt", "r")
    content = file.read(8)
    file.close()
    print(content)

def file_line_reader(file_name):
    file = open(file_name, "r", encoding="utf-8")
    content = file.readlines()
    file.close()
    #print(content)
    #prima solutie
    for row in content: # row = fiecare string din lista
        print(row, end="")
    #a doua solutie
    #for row in content:
    #    print(row.strip())
def write_to_file(msg):
    file = open("lectii/lectia12.txt", "w")
    file.write(msg)
    file.close

def append_to_file(msg):
    file = open("lectii/lectia12.txt", "a")
    #content = file.read()
    file.write("\n" + msg)
    file.close()

def read_with_offset(offset):
    file = open("lectii/lectia12.txt", 'r')
    file.seek(offset)
    content = file.read(10)
    print(content)
    file.close()

def create_file(file_name, file_content):
    file = open(file_name + ".txt", "w")
    file.write(file_content)
    file.close()


#write_to_file("Sunteti tacuti")
#append_to_file("Vorbiti mai mult")
#read_with_offset(10)
create_file("lectii/test", "A FUNCIONAT!!!!!!!")
file_line_reader("test.txt")