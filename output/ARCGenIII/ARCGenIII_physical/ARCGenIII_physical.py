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
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())

# print(thismodel.getOrderedIdList())

# dom = thismodel.toXML()
# pretty_xml_as_string = dom.toprettyxml()

# print(pretty_xml_as_string)

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_UNKNOWN)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())


'''

x = datetime.now(tz=pytz.utc)
print(x)
mystring = PORISVALUEFORMATTER_DATE.getString(x)
print(mystring)
mydate = PORISVALUEFORMATTER_DATE.getValue(mystring)
print(mydate)
mystring = PORISVALUEFORMATTER_DATE.getString(mydate)
print(mystring)

x = x.astimezone(timezone('US/Pacific'))
print(x)
mystring = PORISVALUEFORMATTER_DATE.getString(x)
print(mystring)
mydate = PORISVALUEFORMATTER_DATE.getValue(mystring)
print(mydate)
mystring = PORISVALUEFORMATTER_DATE.getString(mydate)
print(mystring)

'''