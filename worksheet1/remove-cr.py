
'''
The script contains CR (carriage return) characters. 
The shell interprets these CR characters as arguments.
Solution: Remove the CR characters from the script using the following script.
Why this happened: Windows use CR, LF for line ending. 
                   Need to change back to LF for Unix 

The other way to solve this:
Open the file in vim or vi, and administer the following command:
:set ff=unix
Save and exit:
:wq
Done!

Explanation
ff stands for file format, and can accept the values of unix (\n), dos (\r\n) and mac (\r) (only meant to be used on pre-intel macs, on modern macs use unix).

To read more about the ff command:
:help ff
:wq stands for Write and Quit, a faster equivalent is Shift+zz (i.e. hold down Shift then press z twice).
'''


with open('hello.py', 'rb+') as f:
    content = f.read()
    f.seek(0)
    f.write(content.replace(b'\r', b''))
    f.truncate()