
import re 

def isValid(s): 
	
	# 
	Pattern = re.compile("^\d{4}\s\d{4}\s\d{4}$") 
	return Pattern.match(s) 


s = "347873923408"
if (isValid(s)): 
	print ("Valid Number")	 
else : 
	print ("Invalid Number") 
