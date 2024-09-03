from ARCGenIIIPORIS import *
from xml.dom import minidom

class ARCGenIII_physical(ARCGenIIIPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = ARCGenIII_physical(13)

print("Let's test our model ",thismodel.getRoot().getName())
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())

# thismodel.list_nodes()

dom = thismodel.toXML()
pretty_xml_as_string = dom.toprettyxml()

print(pretty_xml_as_string)
