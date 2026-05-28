from ARCGenIIIPORIS import *
from xml.dom import minidom

class ARCGenIII_physical(ARCGenIIIPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = ARCGenIII_physical(13)
'''
print("Let's test our model ",thismodel.getRoot().getName())
print("")
print("Initial mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Initial Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("Initial binning value is",thismodel.prBinning.getSelectedValue().getName())
print("")

print("----- BEGIN --------- XML dump of the model ------------------")
print("")
'''
dom = thismodel.toXML()
'''
pretty_xml_as_string = dom.toprettyxml(encoding="UTF-8")
print("----- BEGIN --------- XML dump of the model ------------------")
# print(pretty_xml_as_string.decode('utf-8')) )
print("")
print("-----  END  --------- XML dump of the model ------------------")

print("Let's parse")
'''
othermodel = PORISDoc(2)
othermodel.fromXML(dom)

# print("Let's dump")
dom2 = othermodel.toXML()
pretty_xml_as_string = dom2.toprettyxml(encoding="UTF-8")
print(pretty_xml_as_string.decode('utf-8')) 

'''
print("")

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("Current binning value is",thismodel.prBinning.getSelectedValue().getName())
print("")
print("We will add 2x1 to the Binnning_1x1 mode")
binning1x1mode = thismodel.prBinning.getSelectedMode()
binning1x1mode.addValue(thismodel.vlBinning_2x1)

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_UNKNOWN)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("After change, Current binning value is",thismodel.prBinning.getSelectedValue().getName())

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("Current binning value is",thismodel.prBinning.getSelectedValue().getName())

print("We will select 2x1 as the default value for the Binnning_1x1 mode")
binning1x1mode.setDefaultValue(thismodel.vlBinning_2x1)

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_UNKNOWN)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("After change, Current binning value is",thismodel.prBinning.getSelectedValue().getName())

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("Current binning value is",thismodel.prBinning.getSelectedValue().getName())
print("Current Acquisition mode is ",thismodel.sysAcquisition.getSelectedMode().getName())

print("We will select NormalWindow as the default acquisition mode")
thismodel.sysAcquisition.setDefaultMode(thismodel.mdAcquisitionMode_NormalWindow)

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_UNKNOWN)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("After change, Current binning value is",thismodel.prBinning.getSelectedValue().getName())

thismodel.set_ARCGenIIIMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current Binning mode is ",thismodel.prBinning.getSelectedMode().getName())
print("Current binning value is",thismodel.prBinning.getSelectedValue().getName())
print("Current Acquisition mode is ",thismodel.sysAcquisition.getSelectedMode().getName())

print("")

print("----- BEGIN --------- XML dump of the model ------------------")
print("")

dom = thismodel.toXML()
pretty_xml_as_string = dom.toprettyxml(encoding="utf-8")
print(pretty_xml_as_string)
print("")
print("-----  END  --------- XML dump of the model ------------------")

print("")
'''

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