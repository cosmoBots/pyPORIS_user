from PORIS import *

class output_alternativePORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysOutputSource = PORISSys("OutputSource")
        self.setRoot(self.sysOutputSource)
        self.sysRecomposition = PORISSys("Recomposition")
        self.mdOutputSourceMode_0x0 = PORISMode("OutputSourceMode_0x0")
        self.mdOutputSourceMode_0x1 = PORISMode("OutputSourceMode_0x1")
        self.mdOutputSourceMode_0x2 = PORISMode("OutputSourceMode_0x2")
        self.mdOutputSourceMode_0x3 = PORISMode("OutputSourceMode_0x3")
        self.mdOutputSourceMode_ALL = PORISMode("OutputSourceMode_ALL")
        self.mdOutputSourceMode_TWO = PORISMode("OutputSourceMode_TWO")
        self.mdRecompositionMode_None = PORISMode("RecompositionMode_None")
        self.mdRecompositionMode_Parallel = PORISMode("RecompositionMode_Parallel")
        self.mdRecompositionMode_Serial = PORISMode("RecompositionMode_Serial")
        self.mdRecompositionMode_QuadCCD = PORISMode("RecompositionMode_QuadCCD")
        self.mdRecompositionMode_QuadIR = PORISMode("RecompositionMode_QuadIR")
        self.mdRecompositionMode_CDSQuad = PORISMode("RecompositionMode_CDSQuad")
        self.mdRecompositionMode_HawaiiRG = PORISMode("RecompositionMode_HawaiiRG")
        self.mdOutputSourceMode_Engineering = PORISMode("OutputSourceMode_Engineering")
        self.addItem(self.sysOutputSource)
        self.sysOutputSource.ident = "ARC-0086"
        self.sysOutputSource.setXMLName('OutputSource')
        self.sysOutputSource.description = ""
        self.addItem(self.sysRecomposition)
        self.sysRecomposition.ident = "ARC-0020"
        self.sysRecomposition.setXMLName('Recomposition')
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)
        self.addItem(self.mdOutputSourceMode_0x0)
        self.mdOutputSourceMode_0x0.ident = "ARC-0087"
        self.mdOutputSourceMode_0x0.setXMLName('0x0')
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)
        self.addItem(self.mdOutputSourceMode_0x1)
        self.mdOutputSourceMode_0x1.ident = "ARC-0088"
        self.mdOutputSourceMode_0x1.setXMLName('0x1')
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)
        self.addItem(self.mdOutputSourceMode_0x2)
        self.mdOutputSourceMode_0x2.ident = "ARC-0089"
        self.mdOutputSourceMode_0x2.setXMLName('0x2')
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)
        self.addItem(self.mdOutputSourceMode_0x3)
        self.mdOutputSourceMode_0x3.ident = "ARC-0090"
        self.mdOutputSourceMode_0x3.setXMLName('0x3')
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)
        self.addItem(self.mdOutputSourceMode_ALL)
        self.mdOutputSourceMode_ALL.ident = "ARC-0091"
        self.mdOutputSourceMode_ALL.setXMLName('ALL')
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)
        self.addItem(self.mdOutputSourceMode_TWO)
        self.mdOutputSourceMode_TWO.ident = "ARC-0092"
        self.mdOutputSourceMode_TWO.setXMLName('TWO')
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)
        self.addItem(self.mdRecompositionMode_None)
        self.mdRecompositionMode_None.ident = "ARC-0055"
        self.mdRecompositionMode_None.setXMLName('None')
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)
        self.addItem(self.mdRecompositionMode_Parallel)
        self.mdRecompositionMode_Parallel.ident = "ARC-0056"
        self.mdRecompositionMode_Parallel.setXMLName('Parallel')
        self.mdRecompositionMode_Parallel.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Parallel)
        self.addItem(self.mdRecompositionMode_Serial)
        self.mdRecompositionMode_Serial.ident = "ARC-0057"
        self.mdRecompositionMode_Serial.setXMLName('Serial')
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)
        self.addItem(self.mdRecompositionMode_QuadCCD)
        self.mdRecompositionMode_QuadCCD.ident = "ARC-0058"
        self.mdRecompositionMode_QuadCCD.setXMLName('QuadCCD')
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)
        self.addItem(self.mdRecompositionMode_QuadIR)
        self.mdRecompositionMode_QuadIR.ident = "ARC-0059"
        self.mdRecompositionMode_QuadIR.setXMLName('QuadIR')
        self.mdRecompositionMode_QuadIR.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadIR)
        self.addItem(self.mdRecompositionMode_CDSQuad)
        self.mdRecompositionMode_CDSQuad.ident = "ARC-0060"
        self.mdRecompositionMode_CDSQuad.setXMLName('CDSQuad')
        self.mdRecompositionMode_CDSQuad.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_CDSQuad)
        self.addItem(self.mdRecompositionMode_HawaiiRG)
        self.mdRecompositionMode_HawaiiRG.ident = "ARC-0061"
        self.mdRecompositionMode_HawaiiRG.setXMLName('HawaiiRG')
        self.mdRecompositionMode_HawaiiRG.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_HawaiiRG)
        self.addItem(self.mdOutputSourceMode_Engineering)
        self.mdOutputSourceMode_Engineering.ident = "ENG-1"
        self.mdOutputSourceMode_Engineering.setXMLName('Engineering')
        self.mdOutputSourceMode_Engineering.description = "OutputSource_engineering_mode"
        self.sysOutputSource.addMode(self.mdOutputSourceMode_Engineering)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x0
        self.mdOutputSourceMode_0x0.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x1
        self.mdOutputSourceMode_0x1.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x2
        self.mdOutputSourceMode_0x2.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_0x3
        self.mdOutputSourceMode_0x3.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_QuadIR como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_QuadIR)
        # Marcamos RecompositionMode_CDSQuad como elegible para OutputSourceMode_ALL
        self.mdOutputSourceMode_ALL.addSubMode(self.mdRecompositionMode_CDSQuad)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_Parallel como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Parallel)
        # Marcamos RecompositionMode_HawaiiRG como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_HawaiiRG)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_Parallel como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Parallel)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_QuadIR como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadIR)
        # Marcamos RecompositionMode_CDSQuad como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_CDSQuad)
        # Marcamos RecompositionMode_HawaiiRG como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_HawaiiRG)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## OutputSourceMode 
    def get_OutputSourceMode(self)-> PORISMode:
        return self.sysOutputSource.getSelectedMode()

    def set_OutputSourceMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOutputSource.selectMode(mode)


    ## RecompositionMode 
    def get_RecompositionMode(self)-> PORISMode:
        return self.sysRecomposition.getSelectedMode()

    def set_RecompositionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysRecomposition.selectMode(mode)

