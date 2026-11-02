from PORIS import *

class output_canonicalPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysSupraOutputSource = PORISSys("SupraOutputSource")
        self.setRoot(self.sysSupraOutputSource)
        self.prRecomposition = PORISParam("Recomposition")
        self.prOutputSource = PORISParam("OutputSource")
        self.mdSupraOutputSourceMode_0x2 = PORISMode("SupraOutputSourceMode_0x2")
        self.mdSupraOutputSourceMode_ALL = PORISMode("SupraOutputSourceMode_ALL")
        self.mdSupraOutputSourceMode_0x0 = PORISMode("SupraOutputSourceMode_0x0")
        self.mdSupraOutputSourceMode_0x3 = PORISMode("SupraOutputSourceMode_0x3")
        self.mdSupraOutputSourceMode_TWO = PORISMode("SupraOutputSourceMode_TWO")
        self.mdSupraOutputSourceMode_0x1 = PORISMode("SupraOutputSourceMode_0x1")
        self.mdRecompositionMode_None = PORISMode("RecompositionMode_None")
        self.mdRecompositionMode_QuadCCD = PORISMode("RecompositionMode_QuadCCD")
        self.mdRecompositionMode_QuadIR = PORISMode("RecompositionMode_QuadIR")
        self.mdRecompositionMode_CDSQuad = PORISMode("RecompositionMode_CDSQuad")
        self.mdRecompositionMode_Serial = PORISMode("RecompositionMode_Serial")
        self.mdRecompositionMode_Parallel = PORISMode("RecompositionMode_Parallel")
        self.mdRecompositionMode_HawaiiRG = PORISMode("RecompositionMode_HawaiiRG")
        self.vlRecomposition_None = PORISValue("Recomposition_None")
        self.vlRecomposition_QuadCCD = PORISValue("Recomposition_QuadCCD")
        self.vlRecomposition_QuadIR = PORISValue("Recomposition_QuadIR")
        self.vlRecomposition_CDSQuad = PORISValue("Recomposition_CDSQuad")
        self.vlRecomposition_Serial = PORISValue("Recomposition_Serial")
        self.vlRecomposition_Parallel = PORISValue("Recomposition_Parallel")
        self.vlRecomposition_HawaiiRG = PORISValue("Recomposition_HawaiiRG")
        self.mdOutputSourceMode_0x2 = PORISMode("OutputSourceMode_0x2")
        self.mdOutputSourceMode_ALL = PORISMode("OutputSourceMode_ALL")
        self.mdOutputSourceMode_0x0 = PORISMode("OutputSourceMode_0x0")
        self.mdOutputSourceMode_0x3 = PORISMode("OutputSourceMode_0x3")
        self.mdOutputSourceMode_TWO = PORISMode("OutputSourceMode_TWO")
        self.mdOutputSourceMode_0x1 = PORISMode("OutputSourceMode_0x1")
        self.vlOutputSource_0x2 = PORISValue("OutputSource_0x2")
        self.vlOutputSource_ALL = PORISValue("OutputSource_ALL")
        self.vlOutputSource_0x0 = PORISValue("OutputSource_0x0")
        self.vlOutputSource_0x3 = PORISValue("OutputSource_0x3")
        self.vlOutputSource_TWO = PORISValue("OutputSource_TWO")
        self.vlOutputSource_0x1 = PORISValue("OutputSource_0x1")
        self.mdSupraOutputSourceMode_Engineering = PORISMode("SupraOutputSourceMode_Engineering")
        self.addItem(self.sysSupraOutputSource)
        self.sysSupraOutputSource.ident = "n0"
        self.sysSupraOutputSource.setXMLName('SupraOutputSource')
        self.sysSupraOutputSource.description = ""
        self.addItem(self.prRecomposition)
        self.prRecomposition.ident = "n0::n6"
        self.prRecomposition.setXMLName('Recomposition')
        self.prRecomposition.description = ""
        self.sysSupraOutputSource.addParam(self.prRecomposition)
        self.addItem(self.prOutputSource)
        self.prOutputSource.ident = "n0::n7"
        self.prOutputSource.setXMLName('OutputSource')
        self.prOutputSource.description = ""
        self.sysSupraOutputSource.addParam(self.prOutputSource)
        self.addItem(self.mdSupraOutputSourceMode_0x2)
        self.mdSupraOutputSourceMode_0x2.ident = "n0::n0"
        self.mdSupraOutputSourceMode_0x2.setXMLName('0x2')
        self.mdSupraOutputSourceMode_0x2.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_0x2)
        self.addItem(self.mdSupraOutputSourceMode_ALL)
        self.mdSupraOutputSourceMode_ALL.ident = "n0::n1"
        self.mdSupraOutputSourceMode_ALL.setXMLName('ALL')
        self.mdSupraOutputSourceMode_ALL.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_ALL)
        self.addItem(self.mdSupraOutputSourceMode_0x0)
        self.mdSupraOutputSourceMode_0x0.ident = "n0::n2"
        self.mdSupraOutputSourceMode_0x0.setXMLName('0x0')
        self.mdSupraOutputSourceMode_0x0.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_0x0)
        self.addItem(self.mdSupraOutputSourceMode_0x3)
        self.mdSupraOutputSourceMode_0x3.ident = "n0::n3"
        self.mdSupraOutputSourceMode_0x3.setXMLName('0x3')
        self.mdSupraOutputSourceMode_0x3.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_0x3)
        self.addItem(self.mdSupraOutputSourceMode_TWO)
        self.mdSupraOutputSourceMode_TWO.ident = "n0::n4"
        self.mdSupraOutputSourceMode_TWO.setXMLName('TWO')
        self.mdSupraOutputSourceMode_TWO.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_TWO)
        self.addItem(self.mdSupraOutputSourceMode_0x1)
        self.mdSupraOutputSourceMode_0x1.ident = "n0::n5"
        self.mdSupraOutputSourceMode_0x1.setXMLName('0x1')
        self.mdSupraOutputSourceMode_0x1.description = ""
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_0x1)
        self.addItem(self.mdRecompositionMode_None)
        self.mdRecompositionMode_None.ident = "n0::n6::n0"
        self.mdRecompositionMode_None.setXMLName('None')
        self.mdRecompositionMode_None.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_None)
        self.addItem(self.mdRecompositionMode_QuadCCD)
        self.mdRecompositionMode_QuadCCD.ident = "n0::n6::n1"
        self.mdRecompositionMode_QuadCCD.setXMLName('QuadCCD')
        self.mdRecompositionMode_QuadCCD.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_QuadCCD)
        self.addItem(self.mdRecompositionMode_QuadIR)
        self.mdRecompositionMode_QuadIR.ident = "n0::n6::n2"
        self.mdRecompositionMode_QuadIR.setXMLName('QuadIR')
        self.mdRecompositionMode_QuadIR.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_QuadIR)
        self.addItem(self.mdRecompositionMode_CDSQuad)
        self.mdRecompositionMode_CDSQuad.ident = "n0::n6::n3"
        self.mdRecompositionMode_CDSQuad.setXMLName('CDSQuad')
        self.mdRecompositionMode_CDSQuad.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_CDSQuad)
        self.addItem(self.mdRecompositionMode_Serial)
        self.mdRecompositionMode_Serial.ident = "n0::n6::n4"
        self.mdRecompositionMode_Serial.setXMLName('Serial')
        self.mdRecompositionMode_Serial.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_Serial)
        self.addItem(self.mdRecompositionMode_Parallel)
        self.mdRecompositionMode_Parallel.ident = "n0::n6::n5"
        self.mdRecompositionMode_Parallel.setXMLName('Parallel')
        self.mdRecompositionMode_Parallel.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_Parallel)
        self.addItem(self.mdRecompositionMode_HawaiiRG)
        self.mdRecompositionMode_HawaiiRG.ident = "n0::n6::n6"
        self.mdRecompositionMode_HawaiiRG.setXMLName('HawaiiRG')
        self.mdRecompositionMode_HawaiiRG.description = ""
        self.prRecomposition.addMode(self.mdRecompositionMode_HawaiiRG)
        self.addItem(self.vlRecomposition_None)
        self.vlRecomposition_None.ident = "n0::n6::n7"
        self.vlRecomposition_None.setXMLName('None')
        self.vlRecomposition_None.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_None)
        self.addItem(self.vlRecomposition_QuadCCD)
        self.vlRecomposition_QuadCCD.ident = "n0::n6::n8"
        self.vlRecomposition_QuadCCD.setXMLName('QuadCCD')
        self.vlRecomposition_QuadCCD.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_QuadCCD)
        self.addItem(self.vlRecomposition_QuadIR)
        self.vlRecomposition_QuadIR.ident = "n0::n6::n9"
        self.vlRecomposition_QuadIR.setXMLName('QuadIR')
        self.vlRecomposition_QuadIR.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_QuadIR)
        self.addItem(self.vlRecomposition_CDSQuad)
        self.vlRecomposition_CDSQuad.ident = "n0::n6::n10"
        self.vlRecomposition_CDSQuad.setXMLName('CDSQuad')
        self.vlRecomposition_CDSQuad.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_CDSQuad)
        self.addItem(self.vlRecomposition_Serial)
        self.vlRecomposition_Serial.ident = "n0::n6::n11"
        self.vlRecomposition_Serial.setXMLName('Serial')
        self.vlRecomposition_Serial.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_Serial)
        self.addItem(self.vlRecomposition_Parallel)
        self.vlRecomposition_Parallel.ident = "n0::n6::n12"
        self.vlRecomposition_Parallel.setXMLName('Parallel')
        self.vlRecomposition_Parallel.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_Parallel)
        self.addItem(self.vlRecomposition_HawaiiRG)
        self.vlRecomposition_HawaiiRG.ident = "n0::n6::n13"
        self.vlRecomposition_HawaiiRG.setXMLName('HawaiiRG')
        self.vlRecomposition_HawaiiRG.description = ""
        self.prRecomposition.addValue(self.vlRecomposition_HawaiiRG)
        self.addItem(self.mdOutputSourceMode_0x2)
        self.mdOutputSourceMode_0x2.ident = "n0::n7::n0"
        self.mdOutputSourceMode_0x2.setXMLName('0x2')
        self.mdOutputSourceMode_0x2.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_0x2)
        self.addItem(self.mdOutputSourceMode_ALL)
        self.mdOutputSourceMode_ALL.ident = "n0::n7::n1"
        self.mdOutputSourceMode_ALL.setXMLName('ALL')
        self.mdOutputSourceMode_ALL.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_ALL)
        self.addItem(self.mdOutputSourceMode_0x0)
        self.mdOutputSourceMode_0x0.ident = "n0::n7::n2"
        self.mdOutputSourceMode_0x0.setXMLName('0x0')
        self.mdOutputSourceMode_0x0.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_0x0)
        self.addItem(self.mdOutputSourceMode_0x3)
        self.mdOutputSourceMode_0x3.ident = "n0::n7::n3"
        self.mdOutputSourceMode_0x3.setXMLName('0x3')
        self.mdOutputSourceMode_0x3.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_0x3)
        self.addItem(self.mdOutputSourceMode_TWO)
        self.mdOutputSourceMode_TWO.ident = "n0::n7::n4"
        self.mdOutputSourceMode_TWO.setXMLName('TWO')
        self.mdOutputSourceMode_TWO.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_TWO)
        self.addItem(self.mdOutputSourceMode_0x1)
        self.mdOutputSourceMode_0x1.ident = "n0::n7::n5"
        self.mdOutputSourceMode_0x1.setXMLName('0x1')
        self.mdOutputSourceMode_0x1.description = ""
        self.prOutputSource.addMode(self.mdOutputSourceMode_0x1)
        self.addItem(self.vlOutputSource_0x2)
        self.vlOutputSource_0x2.ident = "n0::n7::n6"
        self.vlOutputSource_0x2.setXMLName('0x2')
        self.vlOutputSource_0x2.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_0x2)
        self.addItem(self.vlOutputSource_ALL)
        self.vlOutputSource_ALL.ident = "n0::n7::n7"
        self.vlOutputSource_ALL.setXMLName('ALL')
        self.vlOutputSource_ALL.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_ALL)
        self.addItem(self.vlOutputSource_0x0)
        self.vlOutputSource_0x0.ident = "n0::n7::n8"
        self.vlOutputSource_0x0.setXMLName('0x0')
        self.vlOutputSource_0x0.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_0x0)
        self.addItem(self.vlOutputSource_0x3)
        self.vlOutputSource_0x3.ident = "n0::n7::n9"
        self.vlOutputSource_0x3.setXMLName('0x3')
        self.vlOutputSource_0x3.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_0x3)
        self.addItem(self.vlOutputSource_TWO)
        self.vlOutputSource_TWO.ident = "n0::n7::n10"
        self.vlOutputSource_TWO.setXMLName('TWO')
        self.vlOutputSource_TWO.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_TWO)
        self.addItem(self.vlOutputSource_0x1)
        self.vlOutputSource_0x1.ident = "n0::n7::n11"
        self.vlOutputSource_0x1.setXMLName('0x1')
        self.vlOutputSource_0x1.description = ""
        self.prOutputSource.addValue(self.vlOutputSource_0x1)
        self.addItem(self.mdSupraOutputSourceMode_Engineering)
        self.mdSupraOutputSourceMode_Engineering.ident = "ENG-1"
        self.mdSupraOutputSourceMode_Engineering.setXMLName('Engineering')
        self.mdSupraOutputSourceMode_Engineering.description = "SupraOutputSource_engineering_mode"
        self.sysSupraOutputSource.addMode(self.mdSupraOutputSourceMode_Engineering)
        # Marcamos RecompositionMode_None como elegible para SupraOutputSourceMode_0x2
        self.mdSupraOutputSourceMode_0x2.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_QuadCCD como elegible para SupraOutputSourceMode_ALL
        self.mdSupraOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_QuadIR como elegible para SupraOutputSourceMode_ALL
        self.mdSupraOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadIR)
        # Marcamos RecompositionMode_CDSQuad como elegible para SupraOutputSourceMode_ALL
        self.mdSupraOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_CDSQuad)
        # Marcamos RecompositionMode_None como elegible para SupraOutputSourceMode_0x0
        self.mdSupraOutputSourceMode_0x0.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para SupraOutputSourceMode_0x3
        self.mdSupraOutputSourceMode_0x3.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_Serial como elegible para SupraOutputSourceMode_TWO
        self.mdSupraOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_Parallel como elegible para SupraOutputSourceMode_TWO
        self.mdSupraOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Parallel)
        # Marcamos RecompositionMode_HawaiiRG como elegible para SupraOutputSourceMode_TWO
        self.mdSupraOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_HawaiiRG)
        # Marcamos RecompositionMode_None como elegible para SupraOutputSourceMode_0x1
        self.mdSupraOutputSourceMode_0x1.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_QuadCCD como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_QuadIR como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadIR)
        # Marcamos RecompositionMode_CDSQuad como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_CDSQuad)
        # Marcamos RecompositionMode_Serial como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_Parallel como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Parallel)
        # Marcamos RecompositionMode_HawaiiRG como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_HawaiiRG)
        # Marcamos Recomposition_None como elegible para RecompositionMode_None
        self.mdRecompositionMode_None.addValue(self.vlRecomposition_None)
        # Marcamos Recomposition_QuadCCD como elegible para RecompositionMode_QuadCCD
        self.mdRecompositionMode_QuadCCD.addValue(self.vlRecomposition_QuadCCD)
        # Marcamos Recomposition_QuadIR como elegible para RecompositionMode_QuadIR
        self.mdRecompositionMode_QuadIR.addValue(self.vlRecomposition_QuadIR)
        # Marcamos Recomposition_CDSQuad como elegible para RecompositionMode_CDSQuad
        self.mdRecompositionMode_CDSQuad.addValue(self.vlRecomposition_CDSQuad)
        # Marcamos Recomposition_Serial como elegible para RecompositionMode_Serial
        self.mdRecompositionMode_Serial.addValue(self.vlRecomposition_Serial)
        # Marcamos Recomposition_Parallel como elegible para RecompositionMode_Parallel
        self.mdRecompositionMode_Parallel.addValue(self.vlRecomposition_Parallel)
        # Marcamos Recomposition_HawaiiRG como elegible para RecompositionMode_HawaiiRG
        self.mdRecompositionMode_HawaiiRG.addValue(self.vlRecomposition_HawaiiRG)
        # Marcamos OutputSourceMode_0x2 como elegible para SupraOutputSourceMode_0x2
        self.mdSupraOutputSourceMode_0x2.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_ALL como elegible para SupraOutputSourceMode_ALL
        self.mdSupraOutputSourceMode_ALL.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para SupraOutputSourceMode_0x0
        self.mdSupraOutputSourceMode_0x0.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x3 como elegible para SupraOutputSourceMode_0x3
        self.mdSupraOutputSourceMode_0x3.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para SupraOutputSourceMode_TWO
        self.mdSupraOutputSourceMode_TWO.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x1 como elegible para SupraOutputSourceMode_0x1
        self.mdSupraOutputSourceMode_0x1.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_ALL como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x3 como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x1 como elegible para SupraOutputSourceMode_Engineering
        self.mdSupraOutputSourceMode_Engineering.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSource_0x2 como elegible para OutputSourceMode_0x2
        self.mdOutputSourceMode_0x2.addValue(self.vlOutputSource_0x2)
        # Marcamos OutputSource_ALL como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addValue(self.vlOutputSource_ALL)
        # Marcamos OutputSource_0x0 como elegible para OutputSourceMode_0x0
        self.mdOutputSourceMode_0x0.addValue(self.vlOutputSource_0x0)
        # Marcamos OutputSource_0x3 como elegible para OutputSourceMode_0x3
        self.mdOutputSourceMode_0x3.addValue(self.vlOutputSource_0x3)
        # Marcamos OutputSource_TWO como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addValue(self.vlOutputSource_TWO)
        # Marcamos OutputSource_0x1 como elegible para OutputSourceMode_0x1
        self.mdOutputSourceMode_0x1.addValue(self.vlOutputSource_0x1)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## SupraOutputSourceMode 
    def get_SupraOutputSourceMode(self)-> PORISMode:
        return self.sysSupraOutputSource.getSelectedMode()

    def set_SupraOutputSourceMode(self, mode: PORISMode)-> PORISMode :
        return self.sysSupraOutputSource.selectMode(mode)


    ## prParam Recomposition 

    # Recomposition
    def get_Recomposition(self)-> PORISValue :
        return self.prRecomposition.getSelectedValue()

    def set_Recomposition(self, value: PORISValue)-> PORISValue :
        return self.prRecomposition.setValue(value)


    ## RecompositionMode 
    def get_RecompositionMode(self)-> PORISMode:
        return self.prRecomposition.getSelectedMode()

    def set_RecompositionMode(self, mode: PORISMode)-> PORISMode :
        return self.prRecomposition.selectMode(mode)


    ## prParam OutputSource 

    # OutputSource
    def get_OutputSource(self)-> PORISValue :
        return self.prOutputSource.getSelectedValue()

    def set_OutputSource(self, value: PORISValue)-> PORISValue :
        return self.prOutputSource.setValue(value)


    ## OutputSourceMode 
    def get_OutputSourceMode(self)-> PORISMode:
        return self.prOutputSource.getSelectedMode()

    def set_OutputSourceMode(self, mode: PORISMode)-> PORISMode :
        return self.prOutputSource.selectMode(mode)

