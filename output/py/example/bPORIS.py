from PORIS import *

class bPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysInstrument = PORISSys("Instrument")
        self.setRoot(self.sysInstrument)
        self.mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
        self.mdInstrumentMode_Spectroscopy = PORISMode("InstrumentMode_Spectroscopy")
        self.addItem(self.sysInstrument)
        self.sysInstrument.ident = "n0"
        self.sysInstrument.setXMLName('Instrument')
        self.sysInstrument.description = ""
        self.addItem(self.mdInstrumentMode_Photometry)
        self.mdInstrumentMode_Photometry.ident = "n0::n0"
        self.mdInstrumentMode_Photometry.setXMLName('Photometry')
        self.mdInstrumentMode_Photometry.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Photometry)
        self.addItem(self.mdInstrumentMode_Spectroscopy)
        self.mdInstrumentMode_Spectroscopy.ident = "n0::n1"
        self.mdInstrumentMode_Spectroscopy.setXMLName('Spectroscopy')
        self.mdInstrumentMode_Spectroscopy.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Spectroscopy)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## InstrumentMode 
    def get_InstrumentMode(self)-> PORISMode:
        return self.sysInstrument.getSelectedMode()

    def set_InstrumentMode(self, mode: PORISMode)-> PORISMode :
        return self.sysInstrument.selectMode(mode)

