from sys import *

tokens = list()

def open_file(filename):
    data = open(filename, "r").read()
    return(data)

def lex(filecontents):
    tok = ""
    state = 0
    string = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        
        #ignore spaces
        if tok == " ":
            if state == 0: 
                tok = ""
            else:
                tok = " "
        elif tok == "\n":
            tok = ""
            
        #if interpreter finds "PRINT", It will report thet PRINT has been found    
        elif tok == "PRINT":
            tokens.append("PRINT")
            #We need to reset the "tok" variable after each keyword is recognized. 
            tok = ""
        elif tok == "\"":
            
#The program starts with a state of 0, so the first quotation marks set the state to 1.
#this will mean that the interpreter is not looking for keywords, so should treat the following as a string.
#At the second quotation mark, which should always exist, the interpreter sets state = 0 again, meaning it is
#looking again for keywords.
            
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING: " + string + "\"")
                string =""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""
    return tokens
    #print(tokens)

def parse(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i + 1][0:6] == "PRINT STRING":
            print(toks[i+1][7:])
            i += 2
            
        
            
            
    
def run():
    data = open_file(argv[1])
    toks = lex(data)
    parse(toks)

run()
