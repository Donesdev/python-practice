""" The first thing we have in every programming language is what's called reserved words.
  IF we use these words they must mean what python expects them to mean. 
  We can'tuse them elsewhere. We can't make up a variable name inport, we can't make a variable name assert, these 
  words mean something very specific to python. RESERVE WORDS are : False ,None ,True ,and ,as ,assert ,async ,await ,break
,class  ,continue ,def ,del ,elif ,else ,except ,finally ,for ,from ,global ,if ,import ,in ,is ,lambda ,nonlocal ,not ,or ,pass ,raise ,return ,try
,while ,with ,yield
Sentenses are lines. When we write a program, we're wrtting a text file, and we put a line on another line and another line and we construct a paragraph
out of a series of lines. 
  """

x = 2
x = x + 1
print(x)

""" Program steps or program flow
Like a recipe or installation instructions, a program is a sequense of steps to be dones in order. 
- Some steps are conditional - They may be skipped - Sometimes a step or group of steps is to be repeated
- Sometimes we store a set of steps to be used over as needed several places throughout the program.
"""
# ( Sequentia Steps ) 

x = 2 
print(x)
x = x + 2 
print(x)


# ( Conditional Steps )

x = 5
if x < 10: # if has a T/F question and ends with an :
    print('Smaller') # This is a conditional statement
if x > 20:
    print('Bigger')
print('Finis')


# ( Repeat Steps )

n = 5
while n > 5:
    print(n)
    n = n - 1
print('Blastoff') # Loops ( repeated steps ) have iteration variables that change each time through a loop.


name = input('Enter File:')
handle = open (name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.item():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)


""" 
Why are reserved words not used as variable names in Python? - They have predefined meanings in Python
What defines a script in Python ? - A stored set of instructions in a text file. 
What pattern involves repeating a series of steps in programming ? - Repeat Pattern
What is the concept of placing one loop or conditonal inside another in programming ? Nesting
What is the basic pattern where actions are performed one after another in programming ? - Sequential Pattern
What does an assignment statement do in Python ? - Assings a value to a variable
How are avtions performed based on conditions in programming ? - Conditional Steps
When Python ( >>> ) what question is Python asking ? - What Python statement would you like me run
What is the file extension for Python scripts ( files ) ? - .py
What is the proper way to say 'Good-Bye' to Python ? - quit()
Which part of a computer executes the program instructions ? - Central Processing Unit ( CPU )
What is " Code " in the context of this course ? - A sequense of instructions in a programming language
A USB memore stick is an example of which of ? - Secondary Memory
What is the best way to think about a " Symtax Error " while programming ? - The computer did not understand the statement that you entered.
What is the fetch execute cycle ? - Process of retrieving and executing instructions.
What is the primary function of the CPU in a computer ? - To perform arithmetic and logical operations on data 
What best describes programming as a process ? - A sequense of instructions executed by a computer
What is the role of main memory in a computers hardware architecture ? - To store data that is actively being used by the CPU
"""