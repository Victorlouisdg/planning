import ompl
from ompl import base, control, geometric, tools, util

class PyBulletValidityChecker(ompl.base.StateValidityChecker):
    def __init__(self):
        print("INIT!")

    def isValid(self, state):
        print("isValid!")
        return True
    
checker = PyBulletValidityChecker()