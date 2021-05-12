######################################################################################################
#    Constant
######################################################################################################
T_plus ='+'
T_sub = '-'
T_div = '/'
T_mul = '*'
T_lpar ='('
T_rpar =')'
digits= '0123456789.'

######################################################################################################
#    Token Class
######################################################################################################
class Token:
    def __init__(self,tokentype,curchr):
        self.curchr=curchr 
        self.tokentype=tokentype 
    
    def __repr__(self):
        return "[Type:{} , val:{}]".format(self.tokentype,self.curchr)
######################################################################################################
#    Error Class
######################################################################################################
class Error:
    def __init__(self,error,filename,pos,ln,curchr):
        self.error=error
        self.errorchr=curchr
        self.filename=filename 
        self.pos=pos
        self.ln=ln 

    
    def __repr__(self):
        return "Error type:{} , filename:{} , lineno:{} , pos:{} , errorchr:{}".format(self.error,self.filename,self.ln,self.pos,self.errorchr)
    

class IllegalCharError(Error):
    def __init__(self,error,filename,pos,ln,curchr):
        #Error.__init__(error)
        super().__init__(error,filename,pos,ln,curchr)

    

######################################################################################################
#    Lexer Class
######################################################################################################

class Lexer:
    def __init__(self,txt,filename):
        self.txt=txt
        self.pos=-1
        self.curchr = None
        self.ln=0
        self.filename=filename
        print("filename:{}".format(self.filename))
        #return self.tokenize(self.txt)
    def tokenize(self):
        txt=self.txt
        token=[]
        error=None
        self.advance()

        while(self.pos<len(txt)):
            if self.curchr == '\n':
                self.ln+=1
            if self.curchr == T_plus:
                token.append(Token(self.curchr,'PLUS'))
            elif self.curchr == T_sub:
                token.append(Token(self.curchr,'SUBSTRACT'))
            elif self.curchr == T_div:
                token.append(Token(self.curchr,'DIV'))
            elif self.curchr == T_mul:
                token.append(Token(self.curchr,'MUL'))
            elif self.curchr == T_plus:
                token.append(Token(self.curchr,'PLUS'))
            elif self.curchr == T_lpar:
                token.append(Token(self.curchr,'lpar'))
            elif self.curchr == T_rpar:
                token.append(Token(self.curchr,'rpar'))

            elif self.curchr == ' ' or self.curchr=='\t':
                pass 
            elif self.curchr in digits:
                dot=0
                num=''
                while(self.pos<len(txt) and self.curchr in digits):
                    if self.curchr=='.':
                        if dot==1:
                            print('yes')
                            return token,IllegalCharError('IllegalCharError',self.filename,self.pos,self.ln,self.curchr)
                        dot+=1
                    num+=self.curchr
                    self.advance()
                if dot==0:
                    token.append(Token('INT',int(num)))
                else:
                    token.append(Token('FLOAT',float(num)))
                continue
            else:
                error=IllegalCharError('IllegalCharError',self.filename,self.pos,self.ln,self.curchr)
                break
            self.advance()

        return token,error
    
    
    def advance(self):
        self.pos+=1
        self.curchr= self.txt[self.pos] if self.pos<len(self.txt) else None

    

