try:
    with open('sample.txt', 'r') as file:
        contents = file.read()
        print('File contents: ')
        print(contents)
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    if 'file' in locals():
        file.close()