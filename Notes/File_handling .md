## Python File handling:
- Python supports file handling and allows users to handle files i.e., to read and write files, along with many other file handling options, to operate on files
## Text file
- Methods in file handling
   - read, write, append, seek, tell, read(n), readline, readlines(), writelines(list
1. Open a file
   - f= open('File_name_with_extension', 'mode')
2. Do the operation on file 
3. Close the file
   - f.close()
   
#### syntax:
  - f = open(filename, mode)

#### Following mode is supported   
- r: open an existing file for a read operation.
- w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
- a:  open an existing file for append operation. It won’t override existing data. r+:  To read and write data into the file. The previous data in the file will be overridden.
- w+: To write and read data. It will override existing data.
- a+: To append and read data from the file. It won’t override existing data.

**read mode:**
- If file exists then it will open a file into read mode and place the cursor at the beginning of the file
- If file does not exist then it will give **FileNotFoundError**
- This mode allowed only to read from the file, not allowed to do other methods
- syntax:
  - f = open(filename, 'r')
  - f.read()
  - f.tell()
  - f.seek()
  - f.close()
  
- tell() function returns the value of cursor position in the file
- seek() function places the cursor to the mentioned position in the file.
  
**write mode**
- If the file exists then it will open a file in write mode and delete the content of the file.
- If file does not exist, then it will create a file with the mentioned name.
- This mode allows you to write into the file, and not allowed to read from the file.
- syntax:
  - f = open(filename, 'w')
  - f.write(write the content of the file)
  - f.tell()
  - f.seek()
  - f.close()

**append mode**
- If the file exists then it will open a file in write mode and places the cursor at the end of the file
- If file does not exist, then it will create a file with the mentioned name.
- This mode allows you to write into the file, and not allowed to read from the file.
- syntax:
  - f = open(filename, 'a')
  - f.write(write the content of the file)
  - f.tell() # in append mode, tell function the last position value of cursor from the file
  - f.close()

   
**read and write mode: r+**
- If file exists then it will open a file into read mode and place the cursor at the beginning of the file
- If file does not exist then it will give **FileNotFoundError**
- This mode allowed only to read from the file and write in the file
- syntax:
  - f = open(filename, 'r+')
  - f.read()
  - f.seek(len(f.read())
  - f.write(write the content of the file)
  - f.seek(0) 
  - f.close()
   **write and read mode: 'w+'**
   -- If the file exists then it will open a file in write mode and delete the content of the file.
- If file does not exist, then it will create a file with the mentioned name.
- This mode allows you to write into the file, and to read from the file.
- syntax:
  - f = open(filename, 'w+')
  - f.read() # gives an empty file
  - f.write(write the content of the file)
  - f.seek(0)
  - f.read()
  - f.close()

**append and read mode: 'a+'**
- If the file exists then it will open a file in write mode and place the cursor at the end of the file
- If file does not exist, then it will create a file with the mentioned name.
- This mode allows you to write into the file and allowed to read from the file.
- syntax:
  - f = open(filename, 'a+')
  - f.write(write the content of the file)
  - f.seek(0)
  - f.read()
  - f.close()
## Binary Files 
- for example => Images,pdf, audio
- read - **rb**
- write -**wb**
- append - **ab**
- read and write - **r+b/ rb+**
- write and read - **w+b/wb+**
- append and read - **a+b/ab+**
