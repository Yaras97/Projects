from operator import *
def arithmetic_operation(operation):
    slv = {"+": add,
          "-": sub,
          "*": mul,
          "/": truediv}
    return slv[operation]