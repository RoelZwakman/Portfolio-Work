import http.client
import time
import PrintMacros

#function source: https://docs.python.org/3/library/http.client.html
def httpsGETRequestRaw(base, addition):
	print("SENDING HTTPS REQUEST...")
	connection = http.client.HTTPSConnection(base)
	connection.request("GET", addition)
	return connection.getresponse().read()

#split into lines for readability
def httpsGETRequestSplit(base, addition):
	
	#set up a get-request
	print("SENDING HTTPS REQUEST...")
	connection = http.client.HTTPSConnection(base)
	connection.request("GET", addition)

	responseLines = [""] #list with single empty string to store all string lines
	currentLine = [''] #current line of chars returned from response

	#gets response from the get request
	response = connection.getresponse()

	manualbytecounter = 0 #amount of bytes read. this is a bit of a hack but twitter search is nearly infinite so you gotta do what you gotta do
	manualbytelimit = 1000000 #amount of bytes allowed to be read in total for a request
	
	while not response.closed:
		responseread = response.read(1) #reads the response
		manualbytecounter += 1
		currentLine.append(responseread)
		
		if ">" in str(responseread):
			responseLines.append(str(currentLine))
			currentLine = ['']
		elif manualbytecounter == manualbytelimit:
			response.close()

	return responseLines 
