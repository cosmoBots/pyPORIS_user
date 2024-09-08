from PORIS import *
from xml.dom import minidom

dom = minidom.parse("instrument.xml")
thismodel = PORISDoc(2)
thismodel.fromXML(dom)
dom2 = thismodel.toXML()
pretty_xml_as_string = dom2.toprettyxml()
print(pretty_xml_as_string) 

