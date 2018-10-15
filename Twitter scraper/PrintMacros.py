#prints a line of dashes to make for a quick divider in large texts.
def drawDivider():
	print("------------------------------------------------------------------------------------------------------------------")

#macro for input value setting. used as: var1 = PrintMacros.enterValue()
def enterValue():
	return input("Waiting for your input...")

#macro for input value debugging.
def returnInput(input):
	print("Input was: " + input)

#removes the '[', ']', ''', 'b' and ',' characters from a string, as well as '\n' sets of characters
def sanitizeHTMLString(str_in):
	str_out = ""
	badChar = False

	#loop through all characters in string
	for x in range(len(str_in)):
		#removes first empty entry from the string
		if x > 5: 
			#remove all b's that come from being a list, originally
			if str_in[x] == 'b' and str_in[x + 1] == '\'' and str_in[x - 1] == ' ': 
				badChar = True
				pass

			#remove all '\n' sets from the string
			elif (str_in[x] == 'n' and str_in[x - 1] == '\\') or (str_in[x] == '\\' and str_in[x + 1] == 'n'):
				badChar = True
				pass

			#remove all other chars that come from being a list.
			elif str_in[x] == '\'' or str_in[x] == ',' or str_in[x] == ' ' or str_in[x] == ']' or str_in[x] == '[': 
				badChar = True
				pass

			#adds non-bad chars 
			elif badChar == False:
				str_out += str_in[x]
				pass
			badChar = False
			

	return str_out
