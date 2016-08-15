from Calculator import *

class ScientificCalculator(Calculator):

    expresion = ""


    def __init__(self, expresion):
        self.expresion = expresion
        Calculator.__init__(self, self.expresion)

    def scientific_calculate(self):
        c = Calculator(self.expresion)
        tok = c.tokenizer(self.expresion)
        if (tok[1] == "*"):
            return float(tok[0])*float(tok[2])
        elif (tok[1] == "/"):
            return float(tok[0])/float(tok[2])
        elif (tok[1] == "mod"):
            return float(tok[0])%float(tok[2])
        elif (tok[1] == "^"):
            return float(tok[0])**float(tok[2])
        else:
            return c.calculate(tok)

    #def save_user(self, username, password):


if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "l", ["local="])
    x = args[0]
    c = ScientificCalculator(x)
#    print c.scientific_calculate()
    #print c.resultado
