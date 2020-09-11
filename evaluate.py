import math
from simpleeval import simple_eval
class evalexp():
    def evalexpr(self,expression):
        return simple_eval(expression,functions={
                        "cos": lambda x:math.cos(x),
                        "tan": lambda x:math.tan(x),
                        "sin": lambda x:math.sin(x),
                        "cosec":lambda x:1/math.sin(x),
                        "sec":lambda x:1/math.cos(x),
                        "cot":lambda x:1/math.tan(x),
                        "cosh": lambda x:math.cosh(x),
                        "tanh": lambda x:math.tanh(x),
                        "sinh": lambda x:math.sinh(x),
                        "sech": lambda x:1/math.cosh(x),
                        "cosech": lambda x:1/math.sinh(x),
                        "coth": lambda x:1/math.tanh(x),
                        "exp":lambda x:math.exp(x),
                        "expm1":lambda x:math.expm1(x),
                        "ln":lambda x:math.log(x),
                        "lg10":lambda x:math.log10(x),
                        "lg2":lambda x:math.log2(x),
                        "ceil":lambda x:math.ceil(x),
                        "erf":lambda x:math.erf(x),
                        "erfc":lambda x:math.erfc(x),
                        "abs":lambda x:math.fabs(x),
                        "factorial":lambda x:math.factorial(x),
                        "gamma":lambda x:math.gamma(x),
                        "pow":lambda x,y:math.pow(x,y)})

# exp=evalexp()
# mexp=input("enter the math exp\n")
# expr=input("enter the value of j\n")
# f_exp=mexp.replace("j",expr)
# print(exp.evalexpr(f_exp))
# print(mexp)