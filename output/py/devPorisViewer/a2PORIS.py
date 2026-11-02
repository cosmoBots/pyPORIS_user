from PORIS import *

class a2PORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.prDispersion = PORISParam("Dispersion")
        self.vlDispersion_R500 = PORISValue("Dispersion_R500")
        self.vlDispersion_R1000 = PORISValue("Dispersion_R1000")
        self.vlDispersion_R2000 = PORISValue("Dispersion_R2000")
        self.mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
        self.mdDispersionMode_Fijo = PORISMode("DispersionMode_Fijo")
        self.addItem(self.prDispersion)
        self.prDispersion.ident = "n0"
        self.prDispersion.setXMLName('Dispersion')
        self.prDispersion.description = ""
        self.addItem(self.vlDispersion_R500)
        self.vlDispersion_R500.ident = "n0::n0"
        self.vlDispersion_R500.setXMLName('R500')
        self.vlDispersion_R500.description = ""
        self.prDispersion.addValue(self.vlDispersion_R500)
        self.addItem(self.vlDispersion_R1000)
        self.vlDispersion_R1000.ident = "n0::n1"
        self.vlDispersion_R1000.setXMLName('R1000')
        self.vlDispersion_R1000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R1000)
        self.addItem(self.vlDispersion_R2000)
        self.vlDispersion_R2000.ident = "n0::n2"
        self.vlDispersion_R2000.setXMLName('R2000')
        self.vlDispersion_R2000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R2000)
        self.addItem(self.mdDispersionMode_Normal)
        self.mdDispersionMode_Normal.ident = "n0::n3"
        self.mdDispersionMode_Normal.setXMLName('Normal')
        self.mdDispersionMode_Normal.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Normal)
        self.addItem(self.mdDispersionMode_Fijo)
        self.mdDispersionMode_Fijo.ident = "n0::n4"
        self.mdDispersionMode_Fijo.setXMLName('Fijo')
        self.mdDispersionMode_Fijo.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Fijo)
        # Marcamos Dispersion_R500 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R500)
        # Marcamos Dispersion_R1000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R1000)
        # Marcamos Dispersion_R2000 como elegible para DispersionMode_Normal
        self.mdDispersionMode_Normal.addValue(self.vlDispersion_R2000)
        # Marcamos Dispersion_R1000 como elegible para DispersionMode_Fijo
        self.mdDispersionMode_Fijo.addValue(self.vlDispersion_R1000)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


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

