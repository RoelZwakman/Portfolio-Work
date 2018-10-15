import PrintMacros
import WebInteraction
import ToDoList

url = "twitter.com" #URL and /-addition. This is to make the code more reusable for stuff that isn't twitter searches.
urladdition = "/search?f=tweets&vertical=news&q=abc&src=typd" #q=abc should be replaced with the query you want

divfilter = ["<li", "data-permalink-path"] #two entries because of twitter search page's HTML divs setup

#start
#for initialising stuff that might be needed here
print("Initialising...")
PrintMacros.drawDivider()
#end

#start
#checks input and prints it back out
inputprompt = PrintMacros.enterValue()
PrintMacros.returnInput(inputprompt)
PrintMacros.drawDivider()
#end

#gets html from url and urladdition and prints it out listed by divs
htmlAsStringList = WebInteraction.httpsGETRequestSplit(url, urladdition)

#header ascii print for the received html
PrintMacros.drawDivider()
PrintMacros.drawDivider()
print("HTML AS LIST OF STRINGS BASED ON DIVS: ")
PrintMacros.drawDivider()
PrintMacros.drawDivider()

#prints all divs
for x in htmlAsStringList:

	#save sanitized string to print into variable because we have to check against it twice anyway
	sanstring = PrintMacros.sanitizeHTMLString(x) 
	
	#checks if this div contains one of the two filters
	if divfilter[0] in sanstring or divfilter[1] in sanstring:
		PrintMacros.drawDivider()
		print(sanstring) #prints div if it passes the filter
		PrintMacros.drawDivider()

#end of program
PrintMacros.drawDivider()
ToDoList.printToDoList()
quitprompt = input("Enter any input to close this window.")
	