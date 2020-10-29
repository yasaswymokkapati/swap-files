def swapFile() :
    file_1 = input('Enter file 1 name (including extension)')
    file_2 = input('Enter file 2 name (including extension)')
    with open(file_1, 'r') as first_file :
        data_1 = first_file.read()
    with open(file_2, 'r') as second_file :
        data_2 = second_file.read()
    with open(file_1, 'w') as first_file:
        first_file.write(data_2)
    with open(file_2, 'w') as second_file:
        second_file.write(data_1)

swapFile()

input('Enter to exit')