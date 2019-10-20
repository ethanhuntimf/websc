Web Scrapping
===============================

**[`Runnuning Scripts on Windows`](#Runnuning-Scripts-on-Windows)__,__[`Support Vector Machine`](#support-vector-machine)__,__[`Boolean`](#boolean)__,__[`Lists`](#lists)__,__[`Dictionaries`](#dictionaries)__,__ [`Tuples`](#tuples)__,__[`Sets`](#sets)__,__[`None`](#none)**

Runnuning Scripts on Windows
--------
The first line of all your Python programs should be a shebang line,              
for Windows its: #! python3                                         
To run your Python program, create a .bat batch file for running the Python program with py.exe.                      
To make a batch file, make a new text file containing a single line like the following:

```batch
@py.exe C:\path\to\your\pythonScript.py %*
```
Replace this path with the absolute path to your own program, and
save this file with a .bat file extension (for example, pythonScript.bat). This
batch file will keep you from having to type the full absolute path for the
Python program every time you want to run it. I recommend you place
all your batch and .py files in a single folder, such as C:\MyPythonScripts or
C:\Users\YourName\PythonScripts.
The C:\MyPythonScripts folder should be added to the system path on
Windows so that you can run the batch files in it from the Run dialog. To
do this, modify the PATH environment variable. Click the Start button and
type Edit environment variables for your account. This option should autocomplete
after you’ve begun
to type it. The Environment
Variables window that appears
will look like Figure B-1.
From System variables,
select the Path variable and
click Edit. In the Value text
field, append a semicolon,
type C:\MyPythonScripts,
and then click OK. Now you
can run any Python script in
the C:\MyPythonScripts folder
by simply pressing win-R and
entering the script’s name.
Running pythonScript, for
instance, will run pythonScript
.bat, which in turn will save
you from having to run the
whole command py.exe C:\MyPythonScripts\pythonScript.py
from the Run dialog.


Downloading a webpage
--------
First you need to install the requests module. As it does not come pre-installed with python.   
in cmd: 
```cmd
pip install requests
```
Downloading a webpage with requests module:
```python
>>> import requests
u >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> type(res)
<class 'requests.models.Response'>
v >>> res.status_code == requests.codes.ok
True
>>> len(res.text)
178981
>>> print(res.text[:250])
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare
This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever. You may copy it, give it away or
re-use it under the terms of the Proje
```

We can also use exception handling to display an 404 error    
```python
import requests
res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
  res.raise_for_status()
except Exception as exc:
  print('There was a problem: %s' % (exc))
```


Saving a webpage to hard disk
--------

```python
>>> import requests
>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
>>> res.raise_for_status()
>>> playFile = open('RomeoAndJuliet.txt', 'wb')
>>> for chunk in res.iter_content(100000):
playFile.write(chunk)
100000
78981
>>> playFile.close()
```
To review, here’s the complete process for downloading and saving a file:
1. Call requests.get() to download the file.
2. Call open() with 'wb' to create a new file in write binary mode.(binary because we need to maintain unicode)
3. Loop over the Response object’s iter_content() method.
4. Call write() on each iteration to write the content to the file.
5. Call close() to close the file.


Parsing HTML with the BeautifulSoup Module
--------
