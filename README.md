Web Scrapping
===============================

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


requests module
--------
First you need to install the requests module. As it does not come pre-installed with python.
in cmd: pip install requests            
