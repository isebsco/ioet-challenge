# ioet-challenge
This is a repository with Sebastian's solution to the python challenge.

Challenge: I was asked to create a payment calculator that receives a .txt file with some sets of data that must be processed.

Solution: 

I decided to build a simple Python app that allows us to input a txt file with the set of data in the files folder, then our app
will receive the name of the file and performs all calculations calling the modules, methods and properties created to interact
between them.

Architecture: Tha calculator has a simple architecture that starts with its main folder tha contains 2 folders: files and modules, a
main.py file that runs the code, gitignore and readme files.

- The files folder contains a file called testFile.txt which contains 2 sets of data to perform a test. Important! Within this folder we 
must store the txt file that contains the sets of data that we want to process. The data must in the txt file in the format given in the instructions:
         'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
Every set of data must be a new line!

- The modules folder contains all the utilities developed to perform the calculation, these modules contains functions and arrays of data that allows us to
  call them when needed, ensuring a clean and organized code. 

- There are the most functions with single responsibility as possible: 
    - readtxt(fileName) is a function in fileReader method that read the text within the given file and returns an array of lines (every single line is a set of data, it means a single employee with her/his worked hours). This function must receive the name of the file as a parameter.
    - calculate(employees) is a function that receives a list, as the one returned by readtxt, and processes it calling other functions.
    - processHours(hours) is the last function and this receives the days and hours worked by an employee with the next format: MO10:00-12:00,TU10:00-12:00, splits the string and process day by day and calculating the final price of the work and returns this value.

Tests: I've used the doctest module to perform some simple unit tests. These tests run in the main fail when is called, if there is something wrong it will stop the execution an return what the wrong output and the one that is expected, otherwise, it will run normally. The 3 functions named before have been tested there.

How to run it? It must be runned in 3 simple steps:
    1. Save the txt file in the files folder.
    2. Run the main.py file.
    3. Write down in the console the name of the file without its extension.
    4. The code will run, the tests will be performed and the results will appear in the console.

Note: I've saved in the files folder a file named "employesscharge" with 10 sets of datam, if you want, avoid the first step and used this file to test the code.


TODO: Some exceptions handler if for any reason data is given in a wrong format. We are assuming all data is right.