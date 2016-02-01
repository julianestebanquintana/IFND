#################### DEFINITION OF VARIABLES ######################

lista = [['To communicate with computers and make them do whatever is needed, we use programming languages; these have a different set of rules than natural languages (called a ______).', 'syntax'], 
['Internet is a network of computers, they communicate with each other through a protocol called ______, and they transfer files from one to another.', 'http'], 
['Html gives to web pages the structure; the elements in it are tree-like, meaning that there is a branching pattern. CSS is a different language, used to give ______ to the web sites.', 'style'], 
['The basic HTML element format is: < opening-tag > content < closing-tag > , although there are some tags without closing tag, called void tags. Some tags have also attributes, like class or id. In html everything is considered a box, and some boxes are inside bigger boxes (the branching pattern). There are tags that make this boxes, called block tags; but there are also tags that give structure to elements in the html without splitting it from the rectangle in which it is, and are called ______ elements.', 'inline'], 
['Span is used to select an inline element, while div forms blocks. ______ is an attribute used for multiple alike elements, while id gives name to one element and must not be repeated in the same html.', 'class'], 
['The HTML tree-like structure, where one has branches going down the document (or boxes containing other boxes, if better understood) is modeled by the ______, an API implemented in every browser to handle the structure of web pages; it models every element of an HTML document as an object, allowing the manipulation of these objects by other languages.', 'dom'], 
['Css goes down through every element (Cascading) and applies the most specific rule to it. In the computer sciences, there is an abstract concept called ______; is a mechanism by which properties asigned to an element are applied to itself and its descending elements. This idea is important, since it avoids repetition.', 'inheritance'], 
['In css we use the ______, which are called so because they permit to choose the element for style application. They are composed by the name of the tag or the dot and the name of one attribute. After it, between brackets, come the styling rules that will be applied to the selected elements.', 'selectors'], 
['There are three methods to include style: To include CSS in the html head, using the style tag. To link a css file as a separate stylesheet, using the ______ tag in the html head. To write the style inline as a tag attribute, which is not a preferred method.', 'link'], 
['Every element is considered part of a box, and every box is modeled as having, from outside to inside: ______, border, padding, content. Each of these can be modified to give the needed style.', 'margin'], 
['Computational science is about how to solve problems. Programming is the main thing in computational science. Most of the human made machines are designed to accomplish only one single work. Computers by themselves cant accomplish any labor; but computers with programs, can do a lot of different things. A computer program is a simple sequence of instructions, sequence that the computer must follow closely; these different instructions are made using a ______ language, and python is just one of them.', 'programming'], 
['Programming languages are different from natural languages in that are less verbose, less redundant and specially unambiguous, as well as space saving. Most languages today have a set of rules (a syntax) described as ______ form; they are composed by expressions, being an expression an abstract concept that has some value. The expressions can be combined by the construction <non-terminal> -> replacement, where the arrow signals an assignment operation.', 'Backus - Naur'], 
['In Backus-Naur form,every expression can be successively replaced until it gets to a ______ value, where it can be no longer replaced. Some other rules come from this construct, like expression -> expression operator expression, expression -> number or expression -> (expression).', 'terminal'], 
['A variable is a name that refers to a value. In python, a variable is assigned using the form <variable name> = expression, where = corresponds to the ______ symbol. As a convention, the first letter of the variable must be lowercase. Care must be taken to avoid confusing mathematical equal to with the = operator = used in python.', 'assignment'], 
['In python, text is represented as a ______, which is a sequence of characters (letters, digits and symbols);  can contain any number of characters and is built by surrounding text by single or double quotes.', 'string'], 
['The operator +, when used with two strings, concatenates them; also, using the operator * for multiplying a string times an integer, produces a bigger string composed of multiple times the initial string. Strings can be indexed and sliced; in python, the first component the string is indexed as ______. The method for indexation is using square brackets after the variable.', 'zero'], 
['The ______ function sends an output to the console. To manufacture a multiline string, that includes returns and spaces, triple single quotes or triple double quotes are used.', 'print'], 
['______ are procedures that are used frequently used, so instead of declaring them every time it is needed, it is defined in a generical way, and easily called when desired. To define one, we use the python reserved word def.', 'functions'], 
['To use the function, is called by the name and passing it the necessary arguments. Every function has inputs and outputs. To get an output from a function, it must ______ something.', 'return'], 
['If a variable is passed to a function, it does not get modified as a result of the function; the variables defined inside the function, that is, that are ______ to the function, are encapsulated and wont exist outside the function.', 'local'], 
['In order to make decisions, it is used the ______ construct, which evaluates a test expression and, according to its value (True or False) performs the instructions of one block or another.', 'if'], 
['The test expression is usually constructed with less than (<), more than (>), is equal to (==), is different to (!=), or and and. The end of the block is determined by ______.', 'indentation'], 
['To perform a repetitive action, the while loop is used. The block is executed while the text expression is ______, and when it changes, the block execution stops; in order to avoid that a block keeps going forever, in every iteration of the block, something must change. Sometimes, an index variable is used to keep track of the execution, and when it reaches a certain value, it makes the test expression False, so the loop execution stops.', 'true'], 
['While programming is unavoidable to have mistakes; its very important to develop a programming technique that allows to find easily the mistakes, and a method to find and correct programming mistakes systematically. The methodology to find and correct mistakes is called ______.', 'debugging'], 
['Debugging has some important steps: Read the ______ message; in python, the message gives a type of error and number of line where execution stopped; although the error can be found there, it can also be upstream.', 'error'], 
['One option is to copy a similar ______, and approach to the needed code, changing step by step, one small part every time, evaluating what happens when every small thing is changed.', 'function'], 
['Bugs that dont stop code execution are harder to find and make programs work erratically; if one is not getting the expected results, it is useful to ______ intermediate results.', 'print'], 
['Sometimes, code works partially; if one gets to a point where major changes must be done, one can screw up what is really working, so it is really important to not loose what is working well; it is preferable to comment the original code, save a copy or use version controllers, like ______.', 'git'], 
['Recapitulating the ______ strategy: error messages must be examined, work from example code doing small step modifications, get sure that code from third parties work correctly, print intermediate results, and keep and compare old versions.', 'debugging'], 
['Comments are very useful when debugging; single line comments are made with #. ______ are multiple line comments that the python interpreter retains as function documentation. Comments must be kept updated, while code is modified. The idea is that code must be concise, always consistent with the style chosen to document the code, and must give important information.', 'docstrings'], 
['String is a data type that is structured; it is a sequence of characters that can be split into smaller pieces (characters). But strings arent complex enough, not everything can be done with a string, so python implements bigger structured data types. ______ are sequences of anything; in python, they are formed with square brackets, their elements are separated by commas and are indexed in the same way that strings.', 'lists'], 
['Lists are ______, that meaning they can be modified after being created. Strings cant change after creation; elements can be appended to strings, but they form new strings, wont modify the originals. This seemingly subtle difference gets more notorious if one introduces a new variable and assigns it to same object: if a list changes with one name, also changes with the other; this is called aliasing: there are two ways to call the same object.', 'mutable']]

wcome_msg = [ "Hello! Welcome to 'Test your knowledge of Programming'. ", "You will be exposed to some sentences, relating to the IPND of Udacity, lessons 1 & 2.", "Write your answers in lower case, and take well care of the spelling.", "When you finish typing your answer pulse Enter. Lets go!"]

answers = []
rt_answ = 0

#################### DEFINITION OF FUNCTIONS USED IN THE GAME ######################


def get_lvl():
	''' Prompts the user to choose a game level from 1 to 3'''
	try:
		lvl = int(input("Please enter the desired level, from 1 to 3: "))
		if lvl > 0 and lvl < 4:
			print "Now, starting with the level " + str(lvl)
			return lvl
		else:
			print "Not in the desired range."
			return get_lvl()
	except:
		print("Sorry, I didn't understand that.")
		return get_lvl()

def ask_for_answ():
	''' Prompts the user to answer a question'''	
	answ = str(raw_input("What word replaces the SPACE in this sentence? "))
	return answ

def print_elem_list(lista):
	''' Receives a list and prints it, one element at a time'''
	for element in lista:
		print element


#################### THIS IS THE PART THAT INTERACTS WITH THE USER ######################
print_elem_list(wcome_msg)
level = get_lvl()

if level == 1:
	lista1 = lista[0:11]
elif level == 2:
	lista1 = lista[11:20]
else:
	lista1 = lista[20:]

for element in lista1:
	print element[0]
	print "   "
	respuesta = ask_for_answ()
	answers.append([respuesta])
	if respuesta == element[1]:
		print "Congratulations! Right answer!"
		rt_answ += 1
		print "   "
	else:
		print "Not the answer I was expecting. Moving on..."
		print "   "

print "You had " + str(rt_answ) + " right answers!" 
print "Your answers were: "
print_elem_list(answers)
print "The right answers were these: " 
for element in lista1:
	print element[1]

#################### DEVELOPED BY JULIAN QUINTANA, FROM MEDELLIN - COLOMBIA ######################
