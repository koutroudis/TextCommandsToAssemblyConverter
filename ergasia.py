
#Georgiadis Georgios 3199    cse63199
#Koutroudis ioannis  3258    cse63258


#to arxeio pou 8eloume na trexoume to kaloume sto terminal (python ergasia.py input4.txt)

import re
import sys



#Dhlwsh twn token_type gia eukolia wste na mhn xrhsimopoioume ston kwdika strings
programtk = 'programtk'
leftpartk = 'leftpartk'
rightpartk = 'rightpartk'
LSQBtk = 'LSQBtk'
RSQBtk = 'RSQBtk'
declaretk = 'declaretk'
iftk = 'iftk'
thentk = 'thentk'
elsetk = 'elsetk'
whiletk = 'whiletk'
doublewhiletk = 'doublewhiletk'
looptk = 'looptk'
exittk = 'exittk'
forcasetk = 'forcasetk'
incasetk = 'incasetk'
whentk = 'whentk'
defaulttk = 'defaulttk'
nottk = 'nottk'
andtk = 'andtk'
ortk = 'ortk'
functiontk = 'functiontk'
proceduretk = 'proceduretk'
calltk = 'calltk'
returntk = 'returntk'
intk = 'intk'
inouttk = 'inouttk'
inputtk = 'inputtk'
printtk = 'printtk'
leftbrachtk = 'leftbrachtk'
rightbrachtk = 'rightbrachtk'
plustk = 'plustk'
minustk = 'minustk'
multk = 'multk'
divtk = 'divtk'
semitk = 'semitk'
colontk = 'colontk'
equaltk = 'equaltk'
notequaltk = 'notequaltk'
greatertk = 'greatertk'
lesstk = 'lesstk'
greaterequaltk = 'greaterequaltk'
lessequaltk = 'lessequaltk'
colonequaltk = 'colonequaltk'
idtk = 'idtk'
constanttk = 'constanttk'
slashstartk = 'slashstartk'
starslashtk = 'starslashtk'
slashslashtk = 'slashslash'
commatk = 'commatk'
expressiontk = 'expressiontk' 

##anoigoume to arxeio kai diavazoume to prwto sumvolo
file = open('input4.txt', 'r')
#file = open(sys.argv[1],'r')
content = file.read(1)

##Dhlwsh global metablhtwn
word =""
tokens = []

counter = 0
line = 1
quadCounter =0
quad = []
Btrue = []
Bfalse = []
Qtrue = []
Qfalse = []
Rtrue = []
Rfalse = []
R = []
tempCounter = 0
token_value = 0
a = 0
b = 0
c = 0
inout = 0
d = ""
result = 0
namefunprod = ""
namefunArray = []
counterFunName = 0
#######PINAKAS SUMVOLWN
counterEpipedo = 0
pinakasSimv = []
offset = 12
offsetArray = []
#########
########TELIKOS KWDIKAS
assembly = []
counterAssembly = -1
assemblyCounterEp = 0
counterEp = -1
offsetRet = ""
flag1 = -1
########



#bohthhtikes uporoutines

#epistrefei ton ari8mo ths apomenhs tetradas
def nextquad():
    global quadCounter
    return quadCounter + 1

#dhmiourgei thn epomenh tetrada
def genquad(op,x,y,z):
    global quadCounter
    quad.append([op , x, y, z])
    quadCounter = quadCounter + 1
    
#epistrefei mia nea proswwrinh metavlhth
def newTemp():
    global tempCounter
    global offset
    tempCounter = tempCounter + 1
    temporary = ('T_'+str(tempCounter))
    #########PINAKAS SUMVOLWN
    pinakasSimv[counterEpipedo].append([temporary,offset])
    offset = offset+4             
    #########
    return temporary

#dhmiourgei mia lista etiketwn tetradwn pou periexei mono ton aritmo ths etiketas
def makelist(x):
    global quadlist
    quadlist = [x]
    return quadlist

#sunenwnei 2 listes 
def merge(list1,list2):
    global lista
    lista = []
    lista = list1 + list2
    return lista

#sumplhrwnei thn teleutaia 8esh ths tetradas an einai kenh
def backpatch(lis,z):
    for i in range(len(lis)):
        if (quad[lis[i]-1][3] == "_"):
            quad[lis[i]-1][3] = z
    


            
    

#Lexical analyzer
class Lexer():
  
    
    def tokenize(self):
        global line
        global content
        word =""
        tokens = []

        #oso to stoixeio einai keno , tab, newline 8a diavazoume to epomeno stoixeio
        while content ==" " or content == "\n" or content == "\t":
            if content =="\n":
                #pros8eth 1 ka8e fora pou allazei grammh gia na xeroume se poia grammh vriskomaste
                line = line + 1
            #diavazei to epomeno sumvolo
            content = file.read(1)

        #koitame an an to sumvolo einai gramma kai an einai diavazoume ta epomena stoixeia oso auta einai grammata h ari8moi.
        if(content.isalpha()):
            # sto word pros8etoume sumvolo sumvolo kai dhmiourgoume oloklhrh thn lexh.
            word +=content
            content = file.read(1)
            while content.isalpha() or content.isdigit():
                word +=content
                content = file.read(1)
                
            #elenxoume tis eidikes lexeis kai tis pros8etoume sto tokens
            if word == "and":
                tokens.append(['andtk', word])
            elif word == "or":
                tokens.append(['ortk', word])
            elif word == "not":
                tokens.append(['nottk', word])
            elif word == "in":
                tokens.append(['intk', word])
            elif word == "inout":
                tokens.append(['inouttk', word])
            elif word == "input":
                tokens.append(['inputtk', word])
            elif word == "print":
                tokens.append(['printtk', word])
            elif word == "call":
                tokens.append(['calltk', word])
            elif word == "return":
                tokens.append(['returntk', word])
            elif word == "incase":
                tokens.append(['incasetk', word])
            elif word == "forcase":
                tokens.append(['forcasetk', word])
            elif word == "when":
                tokens.append(['whentk', word])
            elif word == "default":
                tokens.append(['defaulttk', word])
            elif word == "exit":
                tokens.append(['exittk', word])
            elif word == "loop":
                tokens.append(['looptk', word])
            elif word == "doublewhile":
                tokens.append(['doublewhiletk', word])
            elif word == "else":
                tokens.append(['elsetk', word])
            elif word == "while":
                tokens.append(['whiletk', word])
            elif word == "then":
                tokens.append(['thentk', word])
            elif word == "function":
                tokens.append(['functiontk', word])
            elif word == "procedure":
                tokens.append(['proceduretk', word])
            elif word == "declare":
                tokens.append(['declaretk', word])
            elif word == "program":
                tokens.append(['programtk', word])
            elif word == "if":
                tokens.append(['iftk', word])
            elif word == "then":
                tokens.append(['thentk', word])
            #Id
            else:   
                tokens.append(['idtk', word])
        
        #koitame an to sumvolo einai ari8mos kai an einai diavazoume ta epomena stoixeio oso auta einai ari8moi
        elif(content.isdigit()):
            word +=content
            content = file.read(1)
            while content.isdigit():
                word +=content
                content = file.read(1)
            tokens.append(['constanttk', word])
        
        #elenxoume an to sumvolo einai (+,-,*,/) kai epishs elenxoume an exoume sxolia , wste na mhn ta lavoume upopshn mas
        elif content == "+":
            word +=content
            content = file.read(1)
            tokens.append(['plustk', word])
        elif content == "-":
            word +=content
            content = file.read(1)
            tokens.append(['minustk', word])
        elif content == "*":
            word +=content
            content = file.read(1)
            tokens.append(['multk', word])
        elif content == "/":
            word +=content
            content = file.read(1)
            if content == "*":
                word +=content
                tokens.append(['leftComment', word])
                while True:
                    word = ""
                    content = file.read(1)
                    if content == "*":
                        word +=content
                        content = file.read(1)
                        if content == "/":
                            word +=content
                            tokens.append(['rightComment', word])
                            break
            elif content == "/":
                word +=content
                while True:
                    content = file.read(1)
                    if content == "\n":
                        lex = Lexer()
                        lex.tokenize()
                        break
                        
            else:
                tokens.append(['divtk', word])
        #elenxoume an to sumvolo einai (<,<=,>,>=,<>,=)
        elif content == "<":
            word +=content
            content = file.read(1)
            if content == "=":
                word +=content
                content = file.read(1)
                tokens.append(['lessequaltk', word])
            elif content == ">":
                word +=content
                content = file.read(1)
                tokens.append(['notequaltk', word])
            else:
                word +=content
                tokens.append(['lesstk', word])
        elif content == ">":
            word +=content
            content = file.read(1)
            if content == "=":
                word +=content
                content = file.read(1)
                tokens.append(['greaterequaltk', word])
            else:
                word +=content
                tokens.append(['greatertk', word])
        elif content == "=":
            word +=content
            content = file.read(1)
            tokens.append(['equaltk', word])
        #elenxoume an to sumvolo einai (:=,:)
        elif content == ":":
            word +=content
            content = file.read(1)
            if content == "=":
                word +=content
                content = file.read(1)
                tokens.append(['colonequaltk', word])
            else:
                word +=content
                tokens.append(['colontk', word])
        #elenxoume an to sumvolo einai (;,',')
        elif content == ";":
            word +=content
            content = file.read(1)
            tokens.append(['semitk', word])
        elif content == ",":
            word +=content
            content = file.read(1)
            tokens.append(['commatk', word])
        

        #elenxoume an to sumvolo einai ('(',')',[,],{,})
        elif content == "(":
            word +=content
            content = file.read(1)
            tokens.append(['leftpartk', word])
        elif content == ")":
            word +=content
            content = file.read(1)
            tokens.append(['rightpartk', word])
        elif content == "[":
            word +=content
            content = file.read(1)
            tokens.append(['LSQBtk', word])
        elif content == "]":
            word +=content
            content = file.read(1)
            tokens.append(['RSQBtk', word])
        elif content == "{":
            word +=content
            content = file.read(1)
            tokens.append(['leftbrachtk', word])
        elif content == "}":
            word +=content
            content = file.read(1)
            tokens.append(['rightbrachtk', word])
        
            
           
        #an den diavasei tipota apo ola auta tote teleiwnoume to programma kai tupwnoume "end of program"    
        else:
            print("end of program")
            return 0
        
        #spame to token se 2 8eseis dhladh ston tupo tou kai thn timh tou
        #apo8ukeuoume to eidos token ths lexhs h tou sumvolou pou anagnwrisame
        token_type = tokens[0][0]
        global token_value
        #apo8hkeuoume thn lexh h to sumvolo  pou anagnwrisame 
        token_value = tokens[0][1]

        #tupwnoume to eidos tou token ths ka8e lexhs h symvolou kai ta tupwnoume mazi me ton ari8mo ths etiketas tous
        global counter
        #print(counter,":",token_type)
        counter = counter + 1
        
        #epistrefoume to eidos tou token ths ka8e lexhs h sumvolou
        return(token_type)
        
        


#Syntax analyzer
class Parser():
    
                  
    #ulopoihsh ths gramatikhs
    def program(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        
        par = Parser()
        lex = Lexer()
        global tokens
        #kaloume ton lexer wste na anagnwrisoume to eidos tou token ths epomenhs lexhs h sumvolou
        tokens = lex.tokenize()
        if tokens == programtk :
            tokens = lex.tokenize()
            if tokens == idtk:
                ########PINAKAS SUMVOLWN
                counterEpipedo = 0
                pinakasSimv.append([[counterEpipedo]])
                ########
                #apo8hkeuoume to onoma tou programatos wste na to tupwsoume stis tetrades
                name = token_value
                tokens = lex.tokenize()
                if tokens == leftbrachtk:
                    tokens = lex.tokenize()
                    #kaloume thn genquad me ta antistoixa orismata
                    genquad("begin_block",name,"_","_")
                    par.block()
                    genquad("halt","_","_","_")
                    genquad("end_block",name,"_","_")
                    if tokens == rightbrachtk:
                        tokens = lex.tokenize()
                    else:
                        #tupwnoume to error mas kai thn antistoixh grammh sthn opoia vrisketai
                        print("line",line,": right brach expected")
                        return 0
                else:
                    print("line",line,": left brach expeceted")
                    return 0
            else:
                print("line",line,": program name expected")
                return 0
        else:
            print("line",line,": the keyword 'program' was expected")
            return 0
    

    def block(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        par = Parser()
        lex = Lexer()
        par.declarations()
        par.subprograms()
        par.statements()


    def declarations(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        while tokens == declaretk:  
            par.varlist()
            if tokens == semitk:
                tokens = lex.tokenize()
            else:
                print("line",line,": semi ';' expected")
                return 0
        

    
    def varlist(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        tokens = lex.tokenize()
        if tokens == idtk:
            ########PINAKAS SUMVOLWN
            pinakasSimv[counterEpipedo].append([token_value,offset])
            offset = offset +4
            ########
            tokens = lex.tokenize()
            while tokens == commatk:
                tokens = lex.tokenize()
                if tokens == idtk:
                    ########PINAKAS SUMVOLWN
                    pinakasSimv[counterEpipedo].append([token_value,offset])
                    offset = offset +4
                    #print(token_value)
                    #print(offset)
                    ########
                    tokens = lex.tokenize()
                else:
                    print("line",line,": varlist id expected or comma expected")
                    return 0
        else:
            print("line",line,": varlist id expected")
            return 0
                    
            



    def subprograms(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        while tokens == functiontk or tokens == proceduretk:
            par.subprogram()
            


    def subprogram(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        global assembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global namefunprod
        if tokens == functiontk:
            tokens = lex.tokenize()
            if tokens == idtk:
                #apo8hkeuoume to onoma ths function
                namefunprod = token_value
                
                ########PINAKAS SUMVOLWN
                pinakasSimv[counterEpipedo].append([namefunprod])

                offsetArray.append(offset)
                
                
                counterEpipedo = counterEpipedo+1
                pinakasSimv.append([[counterEpipedo]])
                
                offset = 12
                ########
                tokens = lex.tokenize()
                par.funcbody()
            else:
                print("line",line,": subprogram name expected")
                return 0
        elif tokens == proceduretk:
            tokens = lex.tokenize()
            if tokens == idtk:
                #apo8hkeuoume to onoma ths procedure
                namefunprod = token_value
                ########PINAKAS SUMVOLWN
                pinakasSimv[counterEpipedo].append([namefunprod])

                offsetArray.append([offset])
                
                counterEpipedo = counterEpipedo+1
                pinakasSimv.append([counterEpipedo])
                offset = 12
                ########
                tokens = lex.tokenize()
                par.funcbody()
            else:
                print("line",line,": subprogram name expected")
                return 0
        else:
            print("line",line,": the keywords 'function or procedure' were expected")
            return 0
                  


    def funcbody(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global quadCounter
        global offsetArray
        global counterAssembly
        global assembly
        global namefunArray
        global counterFunName
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global namefunprod
        par.formalpars()
        if tokens == leftbrachtk:
            tokens = lex.tokenize()
            #print(pinakasSimv)
            namefunArray.append(namefunprod)
            genquad("begin_block",namefunArray[counterFunName],"_","_")
            counterFunName = counterFunName + 1



            
            
            #########PINAKAS SUMVOLWN
            g = len(pinakasSimv[counterEpipedo-1])
            pinakasSimv[counterEpipedo-1][g-1].append(quadCounter+1)
            #########
            
            par.block()
            counterFunName = counterFunName - 1
            genquad("end_block",namefunArray[counterFunName],"_","_")
            
            if tokens == rightbrachtk:
                #########PINAKAS SUMVOLWN
                #print(offset)
                #pinakasSimv.pop(counterEpipedo)
                
                counterEpipedo = counterEpipedo-1
                g = len(pinakasSimv[counterEpipedo])
                #print(g)
                pinakasSimv[counterEpipedo][g-1].append(offset)
                offset = offsetArray[counterEpipedo]
                #########
                tokens = lex.tokenize()
            else:
                #print("line",line,": right brach expected")
                return 0
        


    def formalpars(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == leftpartk:
            tokens = lex.tokenize()
            par.formalparlist()
            if tokens == rightpartk:
                tokens = lex.tokenize()
                
            else:
                print("line",line,": right brachet expected")
                return 0
            

    def formalparlist(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == intk or tokens == inouttk:
            
            par.formalparitem()
            while tokens == commatk:
                tokens = lex.tokenize()
                par.formalparitem()
        else:
            print("line",line,": the keywords 'in or inout' were expected")
            return 0
        


    def formalparitem(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == intk:
            tokens = lex.tokenize()
            if tokens == idtk:
                ########PINAKAS SUMVOLWN
                g = len(pinakasSimv[counterEpipedo-1])
                pinakasSimv[counterEpipedo-1][g-1].append("in")
                
                pinakasSimv[counterEpipedo].append([token_value,offset,"CV"])
                offset = offset + 4
                ########
                tokens = lex.tokenize()
            else:
                print("line",line,": formalparitem id expected")
                return 0
        elif tokens == inouttk:
            tokens = lex.tokenize()
            if tokens == idtk:
                ########PINAKAS SUMVOLWN
                g = len(pinakasSimv[counterEpipedo-1])
                pinakasSimv[counterEpipedo-1][g-1].append("inout")
                
                pinakasSimv[counterEpipedo].append([token_value,offset,"REF"])
                offset = offset + 4
                ########
                tokens = lex.tokenize()
            else:
                print("line",line,": formalparitem id expected")
                return 0
        else:
            print("line",line,": the keywords 'in or inout' were expected")
            return 0
        


    def statements(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        
        if tokens == leftbrachtk:
            tokens = lex.tokenize()
            
            par.statement()
            while tokens == semitk:
                
                tokens = lex.tokenize()
                par.statement()
            
            if tokens == rightbrachtk:
                tokens = lex.tokenize()
            else:
                print("line",line,": right brachet expected")
                return 0
        else:
            par.statement()
        
        
            
        
    
        


    def statement(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == idtk:
            par.assignment_stat()
        elif tokens == iftk:
            tokens = lex.tokenize()
            par.if_stat()
        elif tokens == whiletk:
            par.while_stat()
        elif tokens == doublewhiletk:
            par.doublewhile_stat()
        elif tokens == looptk:
            par.loop_stat()
        elif tokens == exittk:
            par.exit_stat()
        elif tokens == forcasetk:
            par.forcase_stat()
        elif tokens == incasetk:
            par.incase_stat()
        elif tokens == calltk:
            par.call_stat()
        elif tokens == returntk:
            par.return_stat()
        elif tokens == inputtk:
            par.input_stat()
        elif tokens == printtk:
            par.print_stat()


    def assignment_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == idtk:
            #apo8hkeuoume thn lexh pou anagnwrisame,kai thn xrhsimopoioume argotera 
            d = token_value
            tokens = lex.tokenize()
            if tokens == colonequaltk:
                tokens = lex.tokenize()
                par.expression()
                
                genquad(":=",a,"_",d)
            else:
                print("line",line,": colonegual expected")
                return 0
        else:
            print("line",line,": assignmentStat id expected")
            return 0
            


    def if_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == leftpartk:
            tokens = lex.tokenize()
            par.condition()
            if tokens == rightpartk:
                tokens = lex.tokenize()
            else:
                print("line",line,": right brachet expected")
                return 0
        if tokens==thentk:
            tokens=lex.tokenize()
            #kaloume thn backpatch wste na sumplhrwsoume to teleutaio orisma apo oles tis tetrades pou einai apo8hkeumenes sthn lista Btrue
            backpatch(Btrue,nextquad())
            par.statements()
            #apo8hkeuoume mesa sto ifList thn etiketa ths epomenhs tetradas topo8ethmenh mesa se pinaka,wste na sumplhrwsoume meta to teleutaio orisma ths antistoixeis tetradas
            ifList = makelist(nextquad())
            genquad("jump","_","_","_")
            #kaloume thn backpatch wste na sumplhrwsoume to teleutaio orisma apo oles tis tetrades pou einai apo8hkeumenes sthn lista Btrue
            backpatch(Bfalse,nextquad())
            par.elsepart()
            backpatch(ifList,nextquad())
        else:
            print("line",line,": the keyword ‘then’ was expected")
            return 0
        
                    


    def elsepart(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == elsetk:
            tokens = lex.tokenize()
            par.statements()
        

    def while_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == whiletk:
            
            tokens = lex.tokenize()
            Bquad = nextquad()
            if tokens == leftpartk:
                tokens = lex.tokenize()
                par.condition()
                if tokens == rightpartk:
                    tokens = lex.tokenize()
                    backpatch(Btrue,nextquad())
                    ##############
                    #apo8hkeuoume to twrino Bfalse sto Btest giati an perasei apo to statements() uparxei periptwsh to Bfalse na allaxei kai na xa8ei to twrino Bfalse
                    Btest = Bfalse
                    ##############
                    par.statements()
                    genquad("jump","_","_",Bquad)
                    backpatch(Bfalse,nextquad())
                    ###########################
                    backpatch(Btest,nextquad())
                    ###########################
                else:
                    print("line",line,": right brachet expected")
                    return 0
        else:
            print("line",line,": the keyword ‘while’ was expected")
            return 0


    '''
    def doublewhile_stat(self):
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == doublewhiletk:
            tokens =lex.tokenize()
            if tokens == leftpartk:
                tokens = lex.tokenize()
                par.condition()
                if tokens == rightpartk:
                    tokens = lex.tokenize()
                    par.statements()
                
                    if tokens == elsetk:
                        tokens = lex.tokenize()
                        par.statements()
                    else:
                        print("The keyword 'else' expected")
                else:
                    print("right brachet expected")
        else:
            print("The keyword 'doublewhile'  expected")
    
    
    def loop_stat(self):
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == looptk:
            tokens = lex.tokenize()
            par.statements()
        else:
            print("the keyword ‘loop’ was expected")
    
    def exit_stat(self):
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == exittk:
            tokens = lex.tokenize()
            print("exit the program")
    
    
    def incase_stat(self):
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == incasetk:
            tokens = lex.tokenize()
            while tokens == whentk:
                if tokens == leftpartk:
                    tokens = lex.tokenize()
                    par.condition()
                    if tokens == rightpartk:
                        tokens = lex.tokenize()
                        if tokens == colontk:
                            tokens = lex.tokenize()
                            par.statements()
                        else:
                            print("colon ':' expected")
                    else:
                        print("right bracket expected")
        else:
            print("the keyword ‘incase’ was expected")
        '''


    def forcase_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == forcasetk:
            tokens = lex.tokenize()
            while tokens == whentk:
                tokens = lex.tokenize()
                #apo8hkeuoume sthn Bquad1 ton ari8mo ths etiketas tis epomenhs tetradas pou 8a parax8ei
                #wste otan teleiwsei h when na epanalamvanoume oloi thn diadikasia mexri ta condition ths when na mhn isxuoun
                Bquad1 = nextquad()
                if tokens == leftpartk:
                    tokens = lex.tokenize()
                    par.condition()
                    if tokens == rightpartk:
                        tokens = lex.tokenize()
                        #kaloume thn backpatch gia thn Btrue wste na upodeixoume se poia tetrada na metavei an isxuoun ta conditions
                        backpatch(Btrue,nextquad())
                        #apo8hkeuoume sthn Btest1 thn twrinh Bfalse ,wste na mhn xa8ei kai na sumplhrwsoume argotera to teleutaio stoixeio
                        Btest1 = Bfalse
                        if tokens == colontk:
                            tokens = lex.tokenize()
                            par.statements()
                            #kaloume thn sugkekrimenh henquad wste na ginetai sunexeia epanalhpsh 
                            genquad("jump","_","_",Bquad1)
                            backpatch(Bfalse,nextquad())
                            backpatch(Btest1,nextquad())
                        else:
                            print("line",line,": colon ':' expected")
                            return 0
                    else:
                        print("line",line,": right bracket expected")
                        return 0
            if tokens == defaulttk:
                tokens = lex.tokenize()
                if tokens == colontk:
                    tokens = lex.tokenize()
                    par.statements()
                else:
                    print("line",line,": colon ':' expected")
                    return 0
            else:
                print("line",line,": the keyword ‘default’ was expected")
                return 0
        else:
            print("line",line,": the keyword ‘forcase’ was expected")
            return 0
                    
                    
                
    

    def return_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        
        if tokens == returntk:
            tokens = lex.tokenize()
            
            par.expression()
            genquad("retv" , a , "_","_")
        else:
            
            print("line",line,": the keyword ‘return’ was expected")
            return 0
            

    def call_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global a
        global inout
        
        if tokens == calltk:
            tokens = lex.tokenize()
            if tokens == idtk:
                nameid = token_value
                tokens = lex.tokenize()
                
                par.actualpars()
                if(a.isdigit() == False):
                    genquad("par",a,"CV","_")
                if(inout != 0):
                    genquad("par",inout,"REF","_")
                genquad("call",nameid,"_","_")
            else:
                print("line",line,": callStat id expected")
                return 0
        else:
            print("line",line,": the keyword ‘call’ was expected")
            return 0
            

    def print_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == printtk:
            tokens = lex.tokenize()
            if tokens == leftpartk:
                tokens = lex.tokenize()
                par.expression()
                if tokens == rightpartk:
                    tokens = lex.tokenize()
                    genquad("out",a,"_","_")
                else:
                    print("line",line,": right bracket expected")
                    return 0
        else:
            print("line",line,": the keyword ‘print’ was expected")
            return 0

    def input_stat(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == inputtk:
            tokens == lex.tokenize()
            if tokens == leftpartk:
                tokens = lex.tokenize()
                if tokens == idtk:
                    idname = token_value
                    tokens = lex.tokenize()
                    if tokens == rightpartk:
                        tokens = lex.tokenize()
                        genquad("inp",idname,"_","_")
                    else:
                        print("line",line,": right bracket expected")
                        return 0
                else:
                    print("line",line,": inputStat id expected")
                    return 0
        else:
            print("line",line,": the keyword ‘input’ was expected")
            return 0

    def actualpars(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == leftpartk:
            tokens = lex.tokenize()
            
            par.actualparlist()
            if tokens == rightpartk:
                tokens = lex.tokenize()
            else:
                print("line",line,": right bracket expected")
                return 0

    def actualparlist(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == intk or tokens == inouttk:
            par.actualparitem()
            while tokens == commatk:
                tokens = lex.tokenize()
                par.actualparitem()
                
        else:
            print("line",line,": the keywords ‘in' or 'inout’ were expected")
            return 0
        

    def actualparitem(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global inout
        inout = 0
        if tokens == intk:
            tokens = lex.tokenize()
            par.expression()
        elif tokens == inouttk:
            tokens = lex.tokenize()
            if tokens == idtk:
                inout = token_value
                tokens = lex.tokenize()
            else:
                print("line",line,": actualParItem id expected")
                return 0
        else:
            print("line",line,": the keywords 'in' or 'inout' expected")
            return 0
       

    def condition(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global Btrue
        global Bfalse
        par.boolterm()
        Btrue = Qtrue
        Bfalse = Qfalse
        
        while tokens == ortk:
            backpatch(Bfalse , nextquad())
            tokens = lex.tokenize()
            par.boolterm()
            Btrue =  merge(Btrue, Qtrue)
            Bfalse = Qfalse
        
        
     

    def boolterm(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global Qtrue
        global Qfalse
        global tokens
        par.boolfactor()
        Qtrue = Rtrue
        Qfalse = Rfalse
        
        while tokens == andtk:
            
            backpatch(Qtrue,nextquad())
            tokens = lex.tokenize()
            par.boolfactor()
            
            Qfalse = merge(Qfalse,Rfalse)
            
            Qtrue = Rtrue
        

    def boolfactor(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global Rtrue
        global Rfalse
        global tokens
        if tokens == nottk:
            tokens = lex.tokenize()
            if tokens == LSQBtk:
                tokens = lex.tokenize()
                par.condition()
                if tokens == RSQBtk:
                    tokens = lex.tokenize()
                else:
                    print("line",line,": right RSQB expected")
                    return 0
        elif tokens == LSQBtk:
            tokens = lex.tokenize()
            par.condition()
            if tokens == RSQBtk:
                tokens = lex.tokenize()
            else:
                print("line",line,": right RSQB expected")
                return 0
        else:
            par.expression()
            e = a
            
            par.relational_oper()
            par.expression()
            Rtrue = makelist(nextquad())
            
            if d == equaltk:
                genquad("=",e , a , "_")
            elif d == lessequaltk:
                genquad("<=",e , a , "_")
            elif d == greaterequaltk:
                genquad(">=",e , a , "_")
            elif d == greatertk:
                genquad(">",e , a , "_")
            elif d == lesstk:
                genquad("<",e , a , "_")
            elif d == notequaltk:
                genquad("<>",e , a , "_")


            
            Rfalse = makelist(nextquad())
            genquad("jump" , "_" , "_" , "_")


    
   
    def expression(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global a
        global b
        global c
        global result
        global E
        
        par.optional_sign()
        E = a
        a = token_value
        par.term()
        
        
        while tokens == plustk or tokens == minustk:
            
            if(tokens == minustk):
                par.add_oper()
                
                par.term()
                
                w = newTemp()
                genquad("-",a , b , w)
                a = w
            elif(tokens == plustk):
                par.add_oper()
                
                par.term()
                
                w = newTemp()
                genquad("+",a , b , w)
                
                a = w
        ###
        result = a
        
        
        

    def term(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global a
        global b
        global c
        global E
        
        par.factor()
        
        while tokens == multk or tokens == divtk:
            if(tokens == multk):
                par.mul_oper()
                par.factor()
                
                w = newTemp()
                genquad("*",a , b , w)
                a = w
            elif(tokens == divtk):
                par.mul_oper()
                par.factor()
                w = newTemp()
                genquad("/",a , b , w)
                a = w
        ###
        mulresult = a

        

    def factor(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        
        global a
        global b
        global c
        global E
        
        if tokens == constanttk:
            b = token_value
            tokens = lex.tokenize()
        elif tokens == leftpartk:
            tokens = lex.tokenize()
            
            par.expression()
            
            if tokens == rightpartk:
                
                tokens = lex.tokenize()
                b = E
                
            else:
                print("line",line,": right brachet expected")
                return 0
        elif tokens == idtk:
            b = token_value
            tokens = lex.tokenize()
            par.idtail()
        else:
            print("line",line,": factor id or constant expected")
            return 0
        


    def idtail(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global c
        global a
        
        if tokens == leftpartk:
            c = b
            par.actualpars()
            genquad("par",a,"CV","_")
            genquad("par",inout,"REF","_")
            w = newTemp()
            a = w
            genquad("par",a,"RET","_")
            genquad("call",c,"_","_")
            
            
            

    def relational_oper(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        global d
        d = tokens
        if tokens == equaltk:
            tokens = lex.tokenize()
        elif tokens == lessequaltk:
            tokens = lex.tokenize()
        elif tokens == greaterequaltk:     
            tokens = lex.tokenize()
        elif tokens == greatertk:
            tokens = lex.tokenize()
        elif tokens == lesstk:
            tokens = lex.tokenize()
        elif tokens == notequaltk:
            tokens = lex.tokenize()
            
        else:
            print("line",line,": Relational operations expected")
            return 0

    def add_oper(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == plustk:
            tokens =lex.tokenize()
        elif tokens == minustk:
            tokens = lex.tokenize()
        else:
            print("line",line,": Add operators expected")
            return 0

    def mul_oper(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == multk:
            tokens =lex.tokenize()
        elif tokens == divtk:
            tokens = lex.tokenize()
        else:
            print("line",line,": Mul operators expected")
            return 0

    def optional_sign(self):
        #########PINAKAS SUMVOLWN
        global counterEpipedo
        global pinakasSimv
        global offset
        global offsetArray
        global counterAssembly
        #########
        par = Parser()
        lex = Lexer()
        global tokens
        if tokens == plustk or tokens == minustk:
            par.add_oper()



################ASSEMBLY
def countAssembly():
    global assembly
    global counterAssembly
    counterAssembly =counterAssembly+1
    SL = "L"+str(counterAssembly)+":"
    assembly.append(["L"+str(counterAssembly)+":"])
    

def findOffset(a):
    global counterEp
    global pinakasSimv
    helpOffset = " "
    for i in range(counterEp+1):
        for j in range(len(pinakasSimv[i])-1):
            if(a==pinakasSimv[i][j+1][0]):
                helpOffset = pinakasSimv[i][j+1][1]
    if(helpOffset == " "):      
        print("undeclared variable:"+"  "+str(a))
        sys.exit()
    return helpOffset


class assembly1():
    
    def kalos(self):
        offset = 0
        
        ##########
        global flag1
        global counterEp
        global pinakasSimv
        global quad
        global assembly
        global counterAssembly
        global offsetRet
        ##########
        
        for i in range(len(quad)):
            if(quad[i][0] == 'begin_block'):
                flag1 = flag1+1
                counterEp = counterEp +1
                countAssembly()
                if(flag1 ==0):
                    for j in range(counterEp+1):
                        for k in range(len(pinakasSimv[j])):
                            if(len(pinakasSimv[j][k])>3):
                                    d = len(pinakasSimv[j][k])-1
                                    assembly[counterAssembly].append(["addi","$sp","$sp",str(pinakasSimv[j][k][d]+4)])
                                    assembly[counterAssembly].append(["move","$s0","$sp"])
                    
                     
                else:
                    assembly[counterAssembly].append(["sw","$ra","-0($sp)"]) 
                    
                    
                    
                    
                    
                    

            elif(quad[i][0] == 'end_block'):
                flag1 = flag1-1
                counterEp = counterEp -1
                countAssembly()
                #pinakasSimv.pop(counterEpipedo)
                if(flag1 <0):
                    print("")
                    
                else:
                    assembly[counterAssembly].append(["lw","$ra","-0($sp)"])
                    assembly[counterAssembly].append(["jr","$ra"])
                    
            elif(quad[i][0] == 'halt'):
                countAssembly()

                    
            elif(quad[i][0] == "+" or quad[i][0] == "-" or quad[i][0] == "*" or quad[i][0] == "/"):
                countAssembly()
                if(quad[i][0] == "+"):
                    for j in range(1,3):
                        if(quad[i][j].isdigit() == False):
                            helpOffset = findOffset(quad[i][j])
                            assembly[counterAssembly].append(["lw","$t"+str(j),"-"+str(helpOffset)+"($sp)"])
                        elif(quad[i][j].isdigit() == True):
                            assembly[counterAssembly].append(["li","$t"+str(j),str(quad[i][j])])
                    assembly[counterAssembly].append(["add","$t1","$t1","$t2"])
                    helpOffset = findOffset(quad[i][3])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($sp)"])
            
                elif(quad[i][0] == "-"):
                    for j in range(1,3):
                        if(quad[i][j].isdigit() == False):
                            helpOffset = findOffset(quad[i][j])
                            assembly[counterAssembly].append(["lw","$t"+str(j),"-"+str(helpOffset)+"($sp)"])
                        elif(quad[i][j].isdigit() == True):
                            assembly[counterAssembly].append(["li","$t"+str(j),str(quad[i][j])])
                    assembly[counterAssembly].append(["sub","$t1","$t1","$t2"])
                    helpOffset = findOffset(quad[i][3])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($sp)"])          
        

                elif(quad[i][0] == "*"):
                    for j in range(1,3):
                        if(quad[i][j].isdigit() == False):
                            helpOffset = findOffset(quad[i][j])
                            assembly[counterAssembly].append(["lw","$t"+str(j),"-"+str(helpOffset)+"($sp)"])
                        elif(quad[i][j].isdigit() == True):
                            assembly[counterAssembly].append(["li","$t"+str(j),str(quad[i][j])])
                    assembly[counterAssembly].append(["mul","$t1","$t1","$t2"])
                    helpOffset = findOffset(quad[i][3])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($sp)"])         

                elif(quad[i][0] == "/"):
                    for j in range(1,3):
                        if(quad[i][j].isdigit() == False):
                            helpOffset = findOffset(quad[i][j])
                            assembly[counterAssembly].append(["lw","$t"+str(j),"-"+str(helpOffset)+"($sp)"])
                        elif(quad[i][j].isdigit() == True):
                            assembly[counterAssembly].append(["li","$t"+str(j),str(quad[i][j])])
                    assembly[counterAssembly].append(["div","$t1","$t1","$t2"])
                    helpOffset = findOffset(quad[i][3])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($sp)"])
                    
            elif(quad[i][0] == ":="):
                countAssembly()
                if(quad[i][1].isdigit() == False):
                    helpOffset = findOffset(quad[i][1])
                    
                    assembly[counterAssembly].append(["lw","$t1","-"+str(helpOffset)+"($sp)"])
                    helpOffset = findOffset(quad[i][3])
                    
                    assembly[counterAssembly].append(["lw","$t0","-"+str(helpOffset)+"($sp)"])
                    assembly[counterAssembly].append(["sw","$t1","($t0)"])
                else:
                    assembly[counterAssembly].append(["li","$t1",str(quad[i][1])])
                    helpOffset = findOffset(quad[i][3])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($s0)"])
            
            elif(quad[i][0] == "retv"):
                countAssembly()
                helpOffset = findOffset(quad[i][1])
                
                assembly[counterAssembly].append(["lw","$t0","-"+str(helpOffset)+"($sp)"])
                assembly[counterAssembly].append(["lw","$t1","($t0)"])
                assembly[counterAssembly].append(["lw","$t0","-8($sp)"])
                assembly[counterAssembly].append(["sw","$t1","($t0)"])
            
            elif(quad[i][0] == "par"):
                countAssembly()
                if(quad[i][2] == "CV"):
                    pros = ""
                    flag = 0
                    met = i+1
                    while(quad[met][0] =="par"):
                        if(quad[met][2]=="RET"):
                            flag = 1
                            pros = quad[met][1]
                            offsetRet = findOffset(pros)
                        met = met + 1
                    if(flag == 0):
                        for d in range(counterEp):
                            for y in range(len(pinakasSimv[d])):
                                if(len(pinakasSimv[d][y])>3):
                                    dLabel = len(pinakasSimv[d][y])-1
                                    Label = pinakasSimv[d][y][dLabel] +4
                                    offsetRet = Label
                                    
                        
                    assembly[counterAssembly].append(["addi","$fp","$sp",str(offsetRet)])
                    helpOffset = findOffset(quad[i][1])
                    assembly[counterAssembly].append(["lw","$t1","-"+str(helpOffset)+"($sp)"])
                    assembly[counterAssembly].append(["sw","$t1","-"+str(helpOffset)+"($fp)"])
                elif(quad[i][2] == "REF"):
                    helpOffset = findOffset(quad[i][1])
                    ##############################################
                    assembly[counterAssembly].append(["addi","$t0","$sp","-"+str(helpOffset)])
                    assembly[counterAssembly].append(["sw","$t0","-"+str(helpOffset)+"($fp)"])
                elif(quad[i][2] == "RET"):
                    helpOffset = findOffset(quad[i][1])
                    
                    assembly[counterAssembly].append(["addi","$t0","$sp","-"+str(helpOffset)])
                    assembly[counterAssembly].append(["sw","$t0","-8($fp)"])

            
            elif(quad[i][0] == "call"):
                countAssembly()
                assembly[counterAssembly].append(["sw","$sp","-4($fp)"])
                assembly[counterAssembly].append(["addi","$sp","$sp",str(offsetRet)])
                for d in range(counterEp+1):
                    for y in range(len(pinakasSimv[d])):
                        if(len(pinakasSimv[d][y])>3):
                            if(pinakasSimv[d][y][0] == quad[i][1]):
                                dLabel = len(pinakasSimv[d][y])-2
                                Label = pinakasSimv[d][y][dLabel]
                                assembly[counterAssembly].append(["jal","L"+str(Label)])
                assembly[counterAssembly].append(["addi","$sp","$sp","-"+str(offsetRet)])
                
            

            
            elif(quad[i][0] == "out"):
                countAssembly()
                
                helpOffset = findOffset(quad[i][1])
                
                assembly[counterAssembly].append(["lw","$t1","-"+str(helpOffset)+"($sp)"])
                assembly[counterAssembly].append(["li","$v0","1"])
                assembly[counterAssembly].append(["move","$a0","$t1"])
                assembly[counterAssembly].append(["syscall"])


                
            elif(quad[i][0] == "=" or quad[i][0] == "<=" or quad[i][0] == ">=" or quad[i][0] == ">" or quad[i][0] == "<" or quad[i][0] == "<>"):     
                countAssembly()
                if(quad[i][1].isdigit() == False):
                    helpOffset = findOffset(quad[i][1])
                    assembly[counterAssembly].append(["lw","$t1","-"+str(helpOffset)+"($sp)"])
                    
                else:
                    assembly[counterAssembly].append(["li","$t1",str(quad[i][1])])
                if(quad[i][2].isdigit() == False):
                        helpOffset = findOffset(quad[i][2])
                        assembly[counterAssembly].append(["lw","$t2","-"+str(helpOffset)+"($sp)"])
                else:
                    assembly[counterAssembly].append(["li","$t2",str(quad[i][2])]) 
                    
                if(quad[i][0] == "="):
                    assembly[counterAssembly].append(["beq","$t1","$t2","L"+str(quad[i][3])])
                elif(quad[i][0] == "<"):
                    assembly[counterAssembly].append(["blt","$t1","$t2","L"+str(quad[i][3])])
                elif(quad[i][0] == ">"):
                    assembly[counterAssembly].append(["bgt","$t1","$t2","L"+str(quad[i][3])])
                elif(quad[i][0] == "<="):
                    assembly[counterAssembly].append(["ble","$t1","$t2","L"+str(quad[i][3])])
                elif(quad[i][0] == ">="):
                    assembly[counterAssembly].append(["bge","$t1","$t2","L"+str(quad[i][3])])
                elif(quad[i][0] == "<>"):
                    assembly[counterAssembly].append(["bne","$t1","$t2","L"+str(quad[i][3])])

            elif(quad[i][0] == "jump"):
                countAssembly()
                assembly[counterAssembly].append(["j","L"+str(quad[i][3])])



            
        #print(pinakasSimv)
                     
                    
                
                
                #######




#kaloume thn program() apo thn class Parser()
obj = Parser()
obj.program()



los = assembly1()
los.kalos()
'''
print(pinakasSimv)
for j in range(len(assembly)):
    for k in range(len(assembly[j])):
        print(assembly[j][k])
'''
#tupwnoume to plh8os ton tetradwn pou exoun dhmiourgh8ei
#print("plh8os tetradwn:",len(quad))
#anoigoume ena arxeio ,wste na apo8hkeusoume tis tetrades mas ws (.int) arxeio
output = open('out.int','w')
#tupwnoume oles tis tetrades mia mia vazontas mprosta kai ton ari8mo ths etiketas tous
for i in range(len(quad)):
    print(i+1,":",quad[i])
    #tupwnoume ton ari8mo ths etiketas ths tetradas kai sthn sunexeia thn tetrada
    output.write(str(i+1))
    output.write(":")
    output.write(str(quad[i]))
    output.write("\n")
#kleinoume to arxeio pou dhmiourghsame    
output.close() 
#######

#tupwnoume oles tis entoles tis assembly
outputAssembly = open('assembly.asm','w')

for k in range(len(assembly)):
    for j in range(len(assembly[k])):
        if(j == 0):
            outputAssembly.write(assembly[k][j])
        else:
            for h in range(len(assembly[k][j])):
                outputAssembly.write(assembly[k][j][h])
                if(h <len(assembly[k][j])-1):
                    outputAssembly.write(",")
            outputAssembly.write("\n")
        outputAssembly.write("\n")
    
outputAssembly.close()




