from PORIS import *

class cPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysInstrument = PORISSys("Instrument")
        self.setRoot(self.sysInstrument)
        self.prMasks = PORISParam("Masks")
        self.prDispersion = PORISParam("Dispersion")
        self.mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
        self.mdInstrumentMode_Spectroscopy = PORISMode("InstrumentMode_Spectroscopy")
        self.vlMasks_0_6 = PORISValue("Masks_0_6")
        self.vlMasks_1_0 = PORISValue("Masks_1_0")
        self.vlMasks_2_0 = PORISValue("Masks_2_0")
        self.mdMasksMode_Spectroscopy = PORISMode("MasksMode_Spectroscopy")
        self.vlDispersion_R500 = PORISValue("Dispersion_R500")
        self.vlDispersion_R1000 = PORISValue("Dispersion_R1000")
        self.vlDispersion_R2000 = PORISValue("Dispersion_R2000")
        self.mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
        self.mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
        self.addItem(self.sysInstrument)
        self.sysInstrument.ident = "n0"
        self.sysInstrument.setXMLName('Instrument')
        self.sysInstrument.description = ""
        self.addItem(self.prMasks)
        self.prMasks.ident = "n0::n2"
        self.prMasks.setXMLName('Masks')
        self.prMasks.description = ""
        self.sysInstrument.addParam(self.prMasks)
        self.addItem(self.prDispersion)
        self.prDispersion.ident = "n0::n3"
        self.prDispersion.setXMLName('Dispersion')
        self.prDispersion.description = ""
        self.sysInstrument.addParam(self.prDispersion)
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
        self.addItem(self.vlMasks_0_6)
        self.vlMasks_0_6.ident = "n0::n2::n0"
        self.vlMasks_0_6.setXMLName('0.6')
        self.vlMasks_0_6.description = ""
        self.prMasks.addValue(self.vlMasks_0_6)
        self.addItem(self.vlMasks_1_0)
        self.vlMasks_1_0.ident = "n0::n2::n1"
        self.vlMasks_1_0.setXMLName('1.0')
        self.vlMasks_1_0.description = ""
        self.prMasks.addValue(self.vlMasks_1_0)
        self.addItem(self.vlMasks_2_0)
        self.vlMasks_2_0.ident = "n0::n2::n2"
        self.vlMasks_2_0.setXMLName('2.0')
        self.vlMasks_2_0.description = ""
        self.prMasks.addValue(self.vlMasks_2_0)
        self.addItem(self.mdMasksMode_Spectroscopy)
        self.mdMasksMode_Spectroscopy.ident = "n0::n2::n3"
        self.mdMasksMode_Spectroscopy.setXMLName('Spectroscopy')
        self.mdMasksMode_Spectroscopy.description = ""
        self.prMasks.addMode(self.mdMasksMode_Spectroscopy)
        self.addItem(self.vlDispersion_R500)
        self.vlDispersion_R500.ident = "n0::n3::n0"
        self.vlDispersion_R500.setXMLName('R500')
        self.vlDispersion_R500.description = ""
        self.prDispersion.addValue(self.vlDispersion_R500)
        self.addItem(self.vlDispersion_R1000)
        self.vlDispersion_R1000.ident = "n0::n3::n1"
        self.vlDispersion_R1000.setXMLName('R1000')
        self.vlDispersion_R1000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R1000)
        self.addItem(self.vlDispersion_R2000)
        self.vlDispersion_R2000.ident = "n0::n3::n2"
        self.vlDispersion_R2000.setXMLName('R2000')
        self.vlDispersion_R2000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R2000)
        self.addItem(self.mdDispersionMode_Normal)
        self.mdDispersionMode_Normal.ident = "n0::n3::n3"
        self.mdDispersionMode_Normal.setXMLName('Normal')
        self.mdDispersionMode_Normal.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Normal)
        self.addItem(self.mdInstrumentMode_Engineering)
        self.mdInstrumentMode_Engineering.ident = "ENG-1"
        self.mdInstrumentMode_Engineering.setXMLName('Engineering')
        self.mdInstrumentMode_Engineering.description = "Instrument engineering mode"
        self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)
        # Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdMasksMode_Spectroscopy)
        # Marcamos MasksMode_Spectroscopy como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdMasksMode_Spectroscopy)
        # Marcamos Masks_0_6 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_0_6)
        # Marcamos Masks_2_0 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_2_0)
        # Marcamos Masks_1_0 como elegible para MasksMode_Spectroscopy
        self.mdMasksMode_Spectroscopy.addValue(self.vlMasks_1_0)
        # Marcamos DispersionMode_Normal como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdDispersionMode_Normal)
        # Marcamos DispersionMode_Normal como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDispersionMode_Normal)
        # Marcamos Dispersion_R500 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R500)
        # Marcamos Dispersion_R1000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R1000)
        # Marcamos Dispersion_R2000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R2000)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## InstrumentMode 
    def get_InstrumentMode(self)-> PORISMode:
        return self.sysInstrument.getSelectedMode()

    def set_InstrumentMode(self, mode: PORISMode)-> PORISMode :
        return self.sysInstrument.selectMode(mode)


    ## prParam Masks 

    # Masks
    def get_Masks(self)-> PORISValue :
        return self.prMasks.getSelectedValue()

    def set_Masks(self, value: PORISValue)-> PORISValue :
        return self.prMasks.setValue(value)


    ## MasksMode 
    def get_MasksMode(self)-> PORISMode:
        return self.prMasks.getSelectedMode()

    def set_MasksMode(self, mode: PORISMode)-> PORISMode :
        return self.prMasks.selectMode(mode)


    ## prParam Dispersion 

    # Dispersion
    def get_Dispersion(self)-> PORISValue :
        return self.prDispersion.getSelectedValue()

    def set_Dispersion(self, value: PORISValue)-> PORISValue :
        return self.prDispersion.setValue(value)


    ## DispersionMode 
    def get_DispersionMode(self)-> PORISMode:
        return self.prDispersion.getSelectedMode()

    def set_DispersionMode(self, mode: PORISMode)-> PORISMode :
        return self.prDispersion.selectMode(mode)

