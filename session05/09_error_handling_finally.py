def read_file_content(address):
    file = open(address)
    
    try:
        return file.read()
    except:
        print("error")
    finally:
        file.close()


print(read_file_content("09_error_handling_finally.txt"))
print(read_file_content("09_error_handling_finally.txt"))
print(read_file_content("09_error_handling_finally.txt"))
