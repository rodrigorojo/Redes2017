import sys,getopt

class Calculator:
    expresion = ""
    resultado = 0.0
    def __init__(self, expresion = None):
        self.expresion = expresion

    def calculator(self):
        tok = self.tokenizer(self.expresion)
        return self.calculate(tok)

    def calculate(self, tok):
        if(tok[1] == "+"):
            return  float(tok[0])+float(tok[2])
        elif (tok[1] == "-"):
            return float(tok[0])-float(tok[2])
        else :
            print "Operacion no definida"

    def tokenizer(self,exp):
        token1 = ""
        token2 = ""
        token3 = ""
        is_the_first_number = True
        tokens = []
        for n in exp:
            if self.is_number(n) and is_the_first_number:
                token1 += n
            elif self.is_number(n)and not is_the_first_number:
                token3 += n
            else:
                token2 += n
                is_the_first_number = False

        tokens.append(token1)
        tokens.append(token2)
        tokens.append(token3)
        return tokens

    def is_number(self, n):
        numbers = ["0","1","2","3","4","5","6","7","8","9","."]
        if n in numbers:
            return True
        return False

    def is_symbol(self, n):
        symbols = ["+","-"]
        if n in symbols:
            return True
        return False
