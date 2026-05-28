from simplePORIS import *

class simple_physical(simplePORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = simple_physical()

print("Let's test our model ",thismodel.root.getName())
print("Current mode is ",thismodel.root.getSelectedMode().getName())

