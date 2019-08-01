def ORRECTOR(string): 
	string=" "+string+" "
	string=string.lower() 
	ph = ('b','c','d','đ','g','h','k','l','m','n','p','q','r','s','t','v','x')  
	for index, x in enumerate(string):
		if x in ph:
			if (string[index+1]==" " and string[index-1]==" "):
				string = string[:index] +' '+ string[index+1:]
        		#string[index]='1'
	string=string.replace('...', '')
	string=string.replace('?', '.')
	string=string.replace('!', '.')
	string=string.replace('@', '')
	string=string.replace('&', '')
	string=string.replace(';', ',')
	string=string.replace('  ',' ')
	string=string.replace(')',' ')
	string=string.replace('(',' ')
	string=string.replace('"',' ')
	string=string.replace('\\',' ')
	string=string.replace('|',' ')
	string=string[1:]
	string=string.strip()
	return string

