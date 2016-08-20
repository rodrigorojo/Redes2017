from Calculator import *
from Constants.Constants import *

class ScientificCalculator(Calculator):

    expresion = ""


    def __init__(self, expresion):
        self.expresion = expresion
        Calculator.__init__(self, self.expresion)

    def scientific_calculate(self):
        c = Calculator(self.expresion)
        tok = c.tokenizer(self.expresion)
        if (tok[1] == Constants().MULT_SYMBOL):
            return float(tok[0])*float(tok[2])
        elif (tok[1] == Constants().DIV_SYMBOL):
            try:
                return float(tok[0])/float(tok[2])
            except ZeroDivisionError:
                return Constants().ZERO_DIVISION_ERR
        elif (tok[1] == Constants().MOD_SYMBOL):
            return float(tok[0])%float(tok[2])
        elif (tok[1] == Constants().POW_SYMBOL):
            return float(tok[0])**float(tok[2])
        else:
            return c.calculate(tok)

    #def save_user(self, username, password):
