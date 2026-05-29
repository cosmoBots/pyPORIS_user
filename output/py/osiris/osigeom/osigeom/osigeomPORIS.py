from PORIS import *

class osigeomPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysDetector = PORISSys("Detector")
        self.setRoot(self.sysDetector)
        self.sysOutputSource = PORISSys("OutputSource")
        self.sysRecomposition = PORISSys("Recomposition")
        self.prBinning = PORISParam("Binning")
        self.sysWindow = PORISSys("Window")
        self.prRows = PORISParam("Rows")
        self.prCols = PORISParam("Cols")
        self.proffsetRow = PORISParam("offsetRow")
        self.proffsetCol = PORISParam("offsetCol")
        self.mdDetectorMode_FT = PORISMode("DetectorMode_FT")
        self.mdDetectorMode_Window = PORISMode("DetectorMode_Window")
        self.mdOutputSourceMode_0x0 = PORISMode("OutputSourceMode_0x0")
        self.mdOutputSourceMode_0x1 = PORISMode("OutputSourceMode_0x1")
        self.mdOutputSourceMode_0x2 = PORISMode("OutputSourceMode_0x2")
        self.mdOutputSourceMode_0x3 = PORISMode("OutputSourceMode_0x3")
        self.mdOutputSourceMode_ALL = PORISMode("OutputSourceMode_ALL")
        self.mdOutputSourceMode_TWO = PORISMode("OutputSourceMode_TWO")
        self.mdRecompositionMode_None = PORISMode("RecompositionMode_None")
        self.mdRecompositionMode_Serial = PORISMode("RecompositionMode_Serial")
        self.mdRecompositionMode_QuadCCD = PORISMode("RecompositionMode_QuadCCD")
        self.mdDetectorMode_FullDetector = PORISMode("DetectorMode_FullDetector")
        self.mdDetectorMode_WindowSq = PORISMode("DetectorMode_WindowSq")
        self.mdDetectorMode_FullDetectorSq = PORISMode("DetectorMode_FullDetectorSq")
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_All = PORISMode("BinningMode_All")
        self.mdBinningMode_Square = PORISMode("BinningMode_Square")
        self.mdBinningMode_Off = PORISMode("BinningMode_Off")
        self.mdWindowMode_Enabled = PORISMode("WindowMode_Enabled")
        self.mdRowsMode_Normal = PORISMode("RowsMode_Normal")
        self.vlRows_FullRange = PORISValueFloat("Rows_FullRange",0.0,2056.0,4112.0)
        self.mdColsMode_Normal = PORISMode("ColsMode_Normal")
        self.vlCols_FullRange = PORISValueFloat("Cols_FullRange",0.0,2048.0,4096.0)
        self.mdoffsetRowMode_Normal = PORISMode("offsetRowMode_Normal")
        self.vloffsetRow_FullRange = PORISValueFloat("offsetRow_FullRange",0.0,1028.0,4112.0)
        self.mdoffsetColMode_Normal = PORISMode("offsetColMode_Normal")
        self.vloffsetCol_FullRange = PORISValueFloat("offsetCol_FullRange",0.0,1024.0,4096.0)
        self.mdWindowMode_Disabled = PORISMode("WindowMode_Disabled")
        self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
        self.mdOutputSourceMode_Engineering = PORISMode("OutputSourceMode_Engineering")
        self.mdWindowMode_Engineering = PORISMode("WindowMode_Engineering")
        self.addItem(self.sysDetector)
        self.sysDetector.ident = "OSI-0481"
        self.sysDetector.setXMLName('Detector')
        self.sysDetector.description = ""
        self.addItem(self.sysOutputSource)
        self.sysOutputSource.ident = "OSI-0493"
        self.sysOutputSource.setXMLName('OutputSource')
        self.sysOutputSource.description = ""
        self.sysDetector.addSubsystem(self.sysOutputSource)
        self.addItem(self.sysRecomposition)
        self.sysRecomposition.ident = "OSI-0494"
        self.sysRecomposition.setXMLName('Recomposition')
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)
        self.addItem(self.prBinning)
        self.prBinning.ident = "OSI-0641"
        self.prBinning.setXMLName('Binning')
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)
        self.addItem(self.sysWindow)
        self.sysWindow.ident = "OSI-0640"
        self.sysWindow.setXMLName('Window')
        self.sysWindow.description = ""
        self.sysDetector.addSubsystem(self.sysWindow)
        self.addItem(self.prRows)
        self.prRows.ident = "OSI-0484"
        self.prRows.setXMLName('Rows')
        self.prRows.description = ""
        self.sysWindow.addParam(self.prRows)
        self.addItem(self.prCols)
        self.prCols.ident = "OSI-0482"
        self.prCols.setXMLName('Cols')
        self.prCols.description = ""
        self.sysWindow.addParam(self.prCols)
        self.addItem(self.proffsetRow)
        self.proffsetRow.ident = "OSI-0483"
        self.proffsetRow.setXMLName('offsetRow')
        self.proffsetRow.description = ""
        self.sysWindow.addParam(self.proffsetRow)
        self.addItem(self.proffsetCol)
        self.proffsetCol.ident = "OSI-0485"
        self.proffsetCol.setXMLName('offsetCol')
        self.proffsetCol.description = ""
        self.sysWindow.addParam(self.proffsetCol)
        self.addItem(self.mdDetectorMode_FT)
        self.mdDetectorMode_FT.ident = "OSI-0606"
        self.mdDetectorMode_FT.setXMLName('FT')
        self.mdDetectorMode_FT.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FT)
        self.addItem(self.mdDetectorMode_Window)
        self.mdDetectorMode_Window.ident = "OSI-0414"
        self.mdDetectorMode_Window.setXMLName('Window')
        self.mdDetectorMode_Window.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_Window)
        self.addItem(self.mdOutputSourceMode_0x0)
        self.mdOutputSourceMode_0x0.ident = "OSI-0440"
        self.mdOutputSourceMode_0x0.setXMLName('0x0')
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)
        self.addItem(self.mdOutputSourceMode_0x1)
        self.mdOutputSourceMode_0x1.ident = "OSI-0441"
        self.mdOutputSourceMode_0x1.setXMLName('0x1')
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)
        self.addItem(self.mdOutputSourceMode_0x2)
        self.mdOutputSourceMode_0x2.ident = "OSI-0442"
        self.mdOutputSourceMode_0x2.setXMLName('0x2')
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)
        self.addItem(self.mdOutputSourceMode_0x3)
        self.mdOutputSourceMode_0x3.ident = "OSI-0443"
        self.mdOutputSourceMode_0x3.setXMLName('0x3')
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)
        self.addItem(self.mdOutputSourceMode_ALL)
        self.mdOutputSourceMode_ALL.ident = "OSI-0444"
        self.mdOutputSourceMode_ALL.setXMLName('ALL')
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)
        self.addItem(self.mdOutputSourceMode_TWO)
        self.mdOutputSourceMode_TWO.ident = "OSI-0445"
        self.mdOutputSourceMode_TWO.setXMLName('TWO')
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)
        self.addItem(self.mdRecompositionMode_None)
        self.mdRecompositionMode_None.ident = "OSI-0446"
        self.mdRecompositionMode_None.setXMLName('None')
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)
        self.addItem(self.mdRecompositionMode_Serial)
        self.mdRecompositionMode_Serial.ident = "OSI-0448"
        self.mdRecompositionMode_Serial.setXMLName('Serial')
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)
        self.addItem(self.mdRecompositionMode_QuadCCD)
        self.mdRecompositionMode_QuadCCD.ident = "OSI-0449"
        self.mdRecompositionMode_QuadCCD.setXMLName('QuadCCD')
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)
        self.addItem(self.mdDetectorMode_FullDetector)
        self.mdDetectorMode_FullDetector.ident = "OSI-0413"
        self.mdDetectorMode_FullDetector.setXMLName('FullDetector')
        self.mdDetectorMode_FullDetector.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetector)
        self.addItem(self.mdDetectorMode_WindowSq)
        self.mdDetectorMode_WindowSq.ident = "OSI-0628"
        self.mdDetectorMode_WindowSq.setXMLName('WindowSq')
        self.mdDetectorMode_WindowSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_WindowSq)
        self.addItem(self.mdDetectorMode_FullDetectorSq)
        self.mdDetectorMode_FullDetectorSq.ident = "OSI-0629"
        self.mdDetectorMode_FullDetectorSq.setXMLName('FullDetectorSq')
        self.mdDetectorMode_FullDetectorSq.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FullDetectorSq)
        self.addItem(self.vlBinning_1x1)
        self.vlBinning_1x1.ident = "OSI-0630"
        self.vlBinning_1x1.setXMLName('1x1')
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)
        self.addItem(self.vlBinning_1x2)
        self.vlBinning_1x2.ident = "OSI-0631"
        self.vlBinning_1x2.setXMLName('1x2')
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)
        self.addItem(self.vlBinning_2x1)
        self.vlBinning_2x1.ident = "OSI-0632"
        self.vlBinning_2x1.setXMLName('2x1')
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)
        self.addItem(self.vlBinning_2x2)
        self.vlBinning_2x2.ident = "OSI-0633"
        self.vlBinning_2x2.setXMLName('2x2')
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)
        self.addItem(self.mdBinningMode_All)
        self.mdBinningMode_All.ident = "OSI-0634"
        self.mdBinningMode_All.setXMLName('All')
        self.mdBinningMode_All.description = ""
        self.prBinning.addMode(self.mdBinningMode_All)
        self.addItem(self.mdBinningMode_Square)
        self.mdBinningMode_Square.ident = "OSI-0635"
        self.mdBinningMode_Square.setXMLName('Square')
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)
        self.addItem(self.mdBinningMode_Off)
        self.mdBinningMode_Off.ident = "OSI-0636"
        self.mdBinningMode_Off.setXMLName('Off')
        self.mdBinningMode_Off.description = ""
        self.prBinning.addMode(self.mdBinningMode_Off)
        self.addItem(self.mdWindowMode_Enabled)
        self.mdWindowMode_Enabled.ident = "OSI-0460"
        self.mdWindowMode_Enabled.setXMLName('Enabled')
        self.mdWindowMode_Enabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Enabled)
        self.addItem(self.mdRowsMode_Normal)
        self.mdRowsMode_Normal.ident = "OSI-0419"
        self.mdRowsMode_Normal.setXMLName('Normal')
        self.mdRowsMode_Normal.description = ""
        self.prRows.addMode(self.mdRowsMode_Normal)
        self.addItem(self.vlRows_FullRange)
        self.vlRows_FullRange.ident = "OSI-0420"
        self.vlRows_FullRange.setXMLName('FullRange')
        self.vlRows_FullRange.description = ""
        self.prRows.addValue(self.vlRows_FullRange)
        self.addItem(self.mdColsMode_Normal)
        self.mdColsMode_Normal.ident = "OSI-0415"
        self.mdColsMode_Normal.setXMLName('Normal')
        self.mdColsMode_Normal.description = ""
        self.prCols.addMode(self.mdColsMode_Normal)
        self.addItem(self.vlCols_FullRange)
        self.vlCols_FullRange.ident = "OSI-0416"
        self.vlCols_FullRange.setXMLName('FullRange')
        self.vlCols_FullRange.description = ""
        self.prCols.addValue(self.vlCols_FullRange)
        self.addItem(self.mdoffsetRowMode_Normal)
        self.mdoffsetRowMode_Normal.ident = "OSI-0417"
        self.mdoffsetRowMode_Normal.setXMLName('Normal')
        self.mdoffsetRowMode_Normal.description = ""
        self.proffsetRow.addMode(self.mdoffsetRowMode_Normal)
        self.addItem(self.vloffsetRow_FullRange)
        self.vloffsetRow_FullRange.ident = "OSI-0418"
        self.vloffsetRow_FullRange.setXMLName('FullRange')
        self.vloffsetRow_FullRange.description = ""
        self.proffsetRow.addValue(self.vloffsetRow_FullRange)
        self.addItem(self.mdoffsetColMode_Normal)
        self.mdoffsetColMode_Normal.ident = "OSI-0421"
        self.mdoffsetColMode_Normal.setXMLName('Normal')
        self.mdoffsetColMode_Normal.description = ""
        self.proffsetCol.addMode(self.mdoffsetColMode_Normal)
        self.addItem(self.vloffsetCol_FullRange)
        self.vloffsetCol_FullRange.ident = "OSI-0422"
        self.vloffsetCol_FullRange.setXMLName('FullRange')
        self.vloffsetCol_FullRange.description = ""
        self.proffsetCol.addValue(self.vloffsetCol_FullRange)
        self.addItem(self.mdWindowMode_Disabled)
        self.mdWindowMode_Disabled.ident = "GEOM-0002"
        self.mdWindowMode_Disabled.setXMLName('Disabled')
        self.mdWindowMode_Disabled.description = ""
        self.sysWindow.addMode(self.mdWindowMode_Disabled)
        self.addItem(self.mdDetectorMode_Engineering)
        self.mdDetectorMode_Engineering.ident = "ENG-1"
        self.mdDetectorMode_Engineering.setXMLName('Engineering')
        self.mdDetectorMode_Engineering.description = "Detector_engineering_mode"
        self.sysDetector.addMode(self.mdDetectorMode_Engineering)
        self.addItem(self.mdOutputSourceMode_Engineering)
        self.mdOutputSourceMode_Engineering.ident = "ENG-2"
        self.mdOutputSourceMode_Engineering.setXMLName('Engineering')
        self.mdOutputSourceMode_Engineering.description = "OutputSource_engineering_mode"
        self.sysOutputSource.addMode(self.mdOutputSourceMode_Engineering)
        self.addItem(self.mdWindowMode_Engineering)
        self.mdWindowMode_Engineering.ident = "ENG-3"
        self.mdWindowMode_Engineering.setXMLName('Engineering')
        self.mdWindowMode_Engineering.description = "Window_engineering_mode"
        self.sysWindow.addMode(self.mdWindowMode_Engineering)
        # Marcamos OutputSourceMode_TWO como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_ALL como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_TWO como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_Engineering como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdOutputSourceMode_Engineering)
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
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_TWO
        self.mdOutputSourceMode_TWO.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos RecompositionMode_None como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_None)
        # Marcamos RecompositionMode_Serial como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_Serial)
        # Marcamos RecompositionMode_QuadCCD como elegible para OutputSourceMode_Engineering
        self.mdOutputSourceMode_Engineering.addSubMode(self.mdRecompositionMode_QuadCCD)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_All como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_Square como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_All como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Off como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Off)
        # Marcamos Binning_1x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Off
        self.mdBinningMode_Off.addValue(self.vlBinning_1x1)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_FT
        self.mdDetectorMode_FT.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_Window
        self.mdDetectorMode_Window.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FullDetector
        self.mdDetectorMode_FullDetector.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_WindowSq
        self.mdDetectorMode_WindowSq.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_FullDetectorSq
        self.mdDetectorMode_FullDetectorSq.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Enabled como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Enabled)
        # Marcamos WindowMode_Disabled como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Disabled)
        # Marcamos WindowMode_Engineering como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdWindowMode_Engineering)
        # Marcamos RowsMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdRowsMode_Normal)
        # Marcamos RowsMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdRowsMode_Normal)
        # Marcamos Rows_FullRange como elegible para RowsMode_Normal
        self.mdRowsMode_Normal.addValue(self.vlRows_FullRange)
        # Marcamos ColsMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdColsMode_Normal)
        # Marcamos ColsMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdColsMode_Normal)
        # Marcamos Cols_FullRange como elegible para ColsMode_Normal
        self.mdColsMode_Normal.addValue(self.vlCols_FullRange)
        # Marcamos offsetRowMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRowMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRow_FullRange como elegible para offsetRowMode_Normal
        self.mdoffsetRowMode_Normal.addValue(self.vloffsetRow_FullRange)
        # Marcamos offsetColMode_Normal como elegible para WindowMode_Enabled
        self.mdWindowMode_Enabled.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetColMode_Normal como elegible para WindowMode_Engineering
        self.mdWindowMode_Engineering.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetCol_FullRange como elegible para offsetColMode_Normal
        self.mdoffsetColMode_Normal.addValue(self.vloffsetCol_FullRange)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## DetectorMode 
    def get_DetectorMode(self)-> PORISMode:
        return self.sysDetector.getSelectedMode()

    def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDetector.selectMode(mode)


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


    ## prParam Binning 

    # Binning
    def get_Binning(self)-> PORISValue :
        return self.prBinning.getSelectedValue()

    def set_Binning(self, value: PORISValue)-> PORISValue :
        return self.prBinning.setValue(value)


    ## BinningMode 
    def get_BinningMode(self)-> PORISMode:
        return self.prBinning.getSelectedMode()

    def set_BinningMode(self, mode: PORISMode)-> PORISMode :
        return self.prBinning.selectMode(mode)


    ## WindowMode 
    def get_WindowMode(self)-> PORISMode:
        return self.sysWindow.getSelectedMode()

    def set_WindowMode(self, mode: PORISMode)-> PORISMode :
        return self.sysWindow.selectMode(mode)


    ## prParam Rows 

    # Rows
    def get_Rows(self)-> PORISValue :
        return self.prRows.getSelectedValue()

    def set_Rows(self, value: PORISValue)-> PORISValue :
        return self.prRows.setValue(value)


    ## RowsMode 
    def get_RowsMode(self)-> PORISMode:
        return self.prRows.getSelectedMode()

    def set_RowsMode(self, mode: PORISMode)-> PORISMode :
        return self.prRows.selectMode(mode)


    ## prParam Window 

    # RowsDouble  
    def get_RowsDouble(self)-> float :
        v = self.prRows.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RowsDouble(self, data: float)-> float :
        return self.prRows.getSelectedValue().setData(data)


    ## prParam Cols 

    # Cols
    def get_Cols(self)-> PORISValue :
        return self.prCols.getSelectedValue()

    def set_Cols(self, value: PORISValue)-> PORISValue :
        return self.prCols.setValue(value)


    ## ColsMode 
    def get_ColsMode(self)-> PORISMode:
        return self.prCols.getSelectedMode()

    def set_ColsMode(self, mode: PORISMode)-> PORISMode :
        return self.prCols.selectMode(mode)


    ## prParam Window 

    # ColsDouble  
    def get_ColsDouble(self)-> float :
        v = self.prCols.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ColsDouble(self, data: float)-> float :
        return self.prCols.getSelectedValue().setData(data)


    ## prParam offsetRow 

    # offsetRow
    def get_offsetRow(self)-> PORISValue :
        return self.proffsetRow.getSelectedValue()

    def set_offsetRow(self, value: PORISValue)-> PORISValue :
        return self.proffsetRow.setValue(value)


    ## offsetRowMode 
    def get_offsetRowMode(self)-> PORISMode:
        return self.proffsetRow.getSelectedMode()

    def set_offsetRowMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetRow.selectMode(mode)


    ## prParam Window 

    # offsetRowDouble  
    def get_offsetRowDouble(self)-> float :
        v = self.proffsetRow.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetRowDouble(self, data: float)-> float :
        return self.proffsetRow.getSelectedValue().setData(data)


    ## prParam offsetCol 

    # offsetCol
    def get_offsetCol(self)-> PORISValue :
        return self.proffsetCol.getSelectedValue()

    def set_offsetCol(self, value: PORISValue)-> PORISValue :
        return self.proffsetCol.setValue(value)


    ## offsetColMode 
    def get_offsetColMode(self)-> PORISMode:
        return self.proffsetCol.getSelectedMode()

    def set_offsetColMode(self, mode: PORISMode)-> PORISMode :
        return self.proffsetCol.selectMode(mode)


    ## prParam Window 

    # offsetColDouble  
    def get_offsetColDouble(self)-> float :
        v = self.proffsetCol.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetColDouble(self, data: float)-> float :
        return self.proffsetCol.getSelectedValue().setData(data)

