from PORIS import *

class simplePORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysInstrument = PORISSys("Instrument")
        self.mdInstrumentMode_UNKNOWN = PORISMode("InstrumentMode_UNKNOWN")
        self.setRoot(self.sysInstrument)
        self.prMasks = PORISParam("Masks")
        self.mdMasksMode_UNKNOWN = PORISMode("MasksMode_UNKNOWN")
        self.vlMasks_UNKNOWN = PORISValue("Masks_UNKNOWN")
        self.prDispersion = PORISParam("Dispersion")
        self.mdDispersionMode_UNKNOWN = PORISMode("DispersionMode_UNKNOWN")
        self.vlDispersion_UNKNOWN = PORISValue("Dispersion_UNKNOWN")
        self.sysDetector = PORISSys("Detector")
        self.mdDetectorMode_UNKNOWN = PORISMode("DetectorMode_UNKNOWN")
        self.prexpTime = PORISParam("expTime")
        self.mdexpTimeMode_UNKNOWN = PORISMode("expTimeMode_UNKNOWN")
        self.vlexpTime_UNKNOWN = PORISValue("expTime_UNKNOWN")
        self.prBinning = PORISParam("Binning")
        self.mdBinningMode_UNKNOWN = PORISMode("BinningMode_UNKNOWN")
        self.vlBinning_UNKNOWN = PORISValue("Binning_UNKNOWN")
        self.prFilter = PORISParam("Filter")
        self.mdFilterMode_UNKNOWN = PORISMode("FilterMode_UNKNOWN")
        self.vlFilter_UNKNOWN = PORISValue("Filter_UNKNOWN")
        self.vlMasks_0_6 = PORISValue("Masks_0_6")
        self.vlMasks_1_0 = PORISValue("Masks_1_0")
        self.vlMasks_2_0 = PORISValue("Masks_2_0")
        self.mdMasksMode_Spectroscopy = PORISMode("MasksMode_Spectroscopy")
        self.vlDispersion_R500 = PORISValue("Dispersion_R500")
        self.vlDispersion_R1000 = PORISValue("Dispersion_R1000")
        self.vlDispersion_R2000 = PORISValue("Dispersion_R2000")
        self.mdDispersionMode_Normal = PORISMode("DispersionMode_Normal")
        self.vlexpTime_NormalRange = PORISValueFloat("expTime_NormalRange",0,1,3600)
        self.mdexpTimeMode_Slow = PORISMode("expTimeMode_Slow")
        self.mdexpTimeMode_Fast = PORISMode("expTimeMode_Fast")
        self.vlexpTime_FastRange = PORISValueFloat("expTime_FastRange",0,0.01,0.5)
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_Normal = PORISMode("BinningMode_Normal")
        self.mdBinningMode_Square = PORISMode("BinningMode_Square")
        self.mdDetectorMode_SlowFree = PORISMode("DetectorMode_SlowFree")
        self.mdDetectorMode_FixedAspect = PORISMode("DetectorMode_FixedAspect")
        self.mdInstrumentMode_Photometry = PORISMode("InstrumentMode_Photometry")
        self.mdInstrumentMode_Spectroscopy = PORISMode("InstrumentMode_Spectroscopy")
        self.vlFilter_Red = PORISValue("Filter_Red")
        self.vlFilter_Blue = PORISValue("Filter_Blue")
        self.mdFilterMode_Enabled = PORISMode("FilterMode_Enabled")
        self.mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
        self.mdDetectorMode_Engineering = PORISMode("DetectorMode_Engineering")
        self.addItem(self.sysInstrument)
        self.sysInstrument.ident = "n0"
        self.sysInstrument.description = ""
        self.addItem(self.mdInstrumentMode_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.ident = "InstrumentMode_UNKNOWN"
        self.mdInstrumentMode_UNKNOWN.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_UNKNOWN)
        self.addItem(self.prMasks)
        self.prMasks.ident = "n0::n0"
        self.prMasks.description = ""
        self.sysInstrument.addParam(self.prMasks)
        self.addItem(self.vlMasks_UNKNOWN)
        self.vlMasks_UNKNOWN.ident = "Masks_UNKNOWN"
        self.vlMasks_UNKNOWN.description = "Unknown value for Masks"
        self.prMasks.addValue(self.vlMasks_UNKNOWN)
        self.addItem(self.mdMasksMode_UNKNOWN)
        self.mdMasksMode_UNKNOWN.ident = "MasksMode_UNKNOWN"
        self.mdMasksMode_UNKNOWN.description = "Unknown mode for Masks"
        self.prMasks.addMode(self.mdMasksMode_UNKNOWN)
        self.mdMasksMode_UNKNOWN.addValue(self.vlMasks_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdMasksMode_UNKNOWN)
        self.addItem(self.prDispersion)
        self.prDispersion.ident = "n0::n1"
        self.prDispersion.description = ""
        self.sysInstrument.addParam(self.prDispersion)
        self.addItem(self.vlDispersion_UNKNOWN)
        self.vlDispersion_UNKNOWN.ident = "Dispersion_UNKNOWN"
        self.vlDispersion_UNKNOWN.description = "Unknown value for Dispersion"
        self.prDispersion.addValue(self.vlDispersion_UNKNOWN)
        self.addItem(self.mdDispersionMode_UNKNOWN)
        self.mdDispersionMode_UNKNOWN.ident = "DispersionMode_UNKNOWN"
        self.mdDispersionMode_UNKNOWN.description = "Unknown mode for Dispersion"
        self.prDispersion.addMode(self.mdDispersionMode_UNKNOWN)
        self.mdDispersionMode_UNKNOWN.addValue(self.vlDispersion_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdDispersionMode_UNKNOWN)
        self.addItem(self.sysDetector)
        self.sysDetector.ident = "n0::n2"
        self.sysDetector.description = ""
        self.sysInstrument.addSubsystem(self.sysDetector)
        self.addItem(self.mdDetectorMode_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN"
        self.mdDetectorMode_UNKNOWN.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_UNKNOWN)
        self.addItem(self.prexpTime)
        self.prexpTime.ident = "n0::n2::n0"
        self.prexpTime.description = ""
        self.sysDetector.addParam(self.prexpTime)
        self.addItem(self.vlexpTime_UNKNOWN)
        self.vlexpTime_UNKNOWN.ident = "expTime_UNKNOWN"
        self.vlexpTime_UNKNOWN.description = "Unknown value for expTime"
        self.prexpTime.addValue(self.vlexpTime_UNKNOWN)
        self.addItem(self.mdexpTimeMode_UNKNOWN)
        self.mdexpTimeMode_UNKNOWN.ident = "expTimeMode_UNKNOWN"
        self.mdexpTimeMode_UNKNOWN.description = "Unknown mode for expTime"
        self.prexpTime.addMode(self.mdexpTimeMode_UNKNOWN)
        self.mdexpTimeMode_UNKNOWN.addValue(self.vlexpTime_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdexpTimeMode_UNKNOWN)
        self.addItem(self.prBinning)
        self.prBinning.ident = "n0::n2::n1"
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)
        self.addItem(self.vlBinning_UNKNOWN)
        self.vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
        self.vlBinning_UNKNOWN.description = "Unknown value for Binning"
        self.prBinning.addValue(self.vlBinning_UNKNOWN)
        self.addItem(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
        self.mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
        self.prBinning.addMode(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.addValue(self.vlBinning_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)
        self.addItem(self.prFilter)
        self.prFilter.ident = "n0::n5"
        self.prFilter.description = ""
        self.sysInstrument.addParam(self.prFilter)
        self.addItem(self.vlFilter_UNKNOWN)
        self.vlFilter_UNKNOWN.ident = "Filter_UNKNOWN"
        self.vlFilter_UNKNOWN.description = "Unknown value for Filter"
        self.prFilter.addValue(self.vlFilter_UNKNOWN)
        self.addItem(self.mdFilterMode_UNKNOWN)
        self.mdFilterMode_UNKNOWN.ident = "FilterMode_UNKNOWN"
        self.mdFilterMode_UNKNOWN.description = "Unknown mode for Filter"
        self.prFilter.addMode(self.mdFilterMode_UNKNOWN)
        self.mdFilterMode_UNKNOWN.addValue(self.vlFilter_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdFilterMode_UNKNOWN)
        self.addItem(self.vlMasks_0_6)
        self.vlMasks_0_6.ident = "n0::n0::n0"
        self.vlMasks_0_6.description = ""
        self.prMasks.addValue(self.vlMasks_0_6)
        self.addItem(self.vlMasks_1_0)
        self.vlMasks_1_0.ident = "n0::n0::n1"
        self.vlMasks_1_0.description = ""
        self.prMasks.addValue(self.vlMasks_1_0)
        self.addItem(self.vlMasks_2_0)
        self.vlMasks_2_0.ident = "n0::n0::n2"
        self.vlMasks_2_0.description = ""
        self.prMasks.addValue(self.vlMasks_2_0)
        self.addItem(self.mdMasksMode_Spectroscopy)
        self.mdMasksMode_Spectroscopy.ident = "n0::n0::n3"
        self.mdMasksMode_Spectroscopy.description = ""
        self.prMasks.addMode(self.mdMasksMode_Spectroscopy)
        self.addItem(self.vlDispersion_R500)
        self.vlDispersion_R500.ident = "n0::n1::n0"
        self.vlDispersion_R500.description = ""
        self.prDispersion.addValue(self.vlDispersion_R500)
        self.addItem(self.vlDispersion_R1000)
        self.vlDispersion_R1000.ident = "n0::n1::n1"
        self.vlDispersion_R1000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R1000)
        self.addItem(self.vlDispersion_R2000)
        self.vlDispersion_R2000.ident = "n0::n1::n2"
        self.vlDispersion_R2000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R2000)
        self.addItem(self.mdDispersionMode_Normal)
        self.mdDispersionMode_Normal.ident = "n0::n1::n3"
        self.mdDispersionMode_Normal.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Normal)
        self.addItem(self.vlexpTime_NormalRange)
        self.vlexpTime_NormalRange.ident = "n0::n2::n0::n0"
        self.vlexpTime_NormalRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_NormalRange)
        self.addItem(self.mdexpTimeMode_Slow)
        self.mdexpTimeMode_Slow.ident = "n0::n2::n0::n1"
        self.mdexpTimeMode_Slow.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Slow)
        self.addItem(self.mdexpTimeMode_Fast)
        self.mdexpTimeMode_Fast.ident = "n0::n2::n0::n2"
        self.mdexpTimeMode_Fast.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Fast)
        self.addItem(self.vlexpTime_FastRange)
        self.vlexpTime_FastRange.ident = "n0::n2::n0::n3"
        self.vlexpTime_FastRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_FastRange)
        self.addItem(self.vlBinning_1x1)
        self.vlBinning_1x1.ident = "n0::n2::n1::n0"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)
        self.addItem(self.vlBinning_2x1)
        self.vlBinning_2x1.ident = "n0::n2::n1::n1"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)
        self.addItem(self.vlBinning_1x2)
        self.vlBinning_1x2.ident = "n0::n2::n1::n2"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)
        self.addItem(self.vlBinning_2x2)
        self.vlBinning_2x2.ident = "n0::n2::n1::n3"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)
        self.addItem(self.mdBinningMode_Normal)
        self.mdBinningMode_Normal.ident = "n0::n2::n1::n4"
        self.mdBinningMode_Normal.description = ""
        self.prBinning.addMode(self.mdBinningMode_Normal)
        self.addItem(self.mdBinningMode_Square)
        self.mdBinningMode_Square.ident = "n0::n2::n1::n5"
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)
        self.addItem(self.mdDetectorMode_SlowFree)
        self.mdDetectorMode_SlowFree.ident = "n0::n2::n2"
        self.mdDetectorMode_SlowFree.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_SlowFree)
        self.addItem(self.mdDetectorMode_FixedAspect)
        self.mdDetectorMode_FixedAspect.ident = "n0::n2::n3"
        self.mdDetectorMode_FixedAspect.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FixedAspect)
        self.addItem(self.mdInstrumentMode_Photometry)
        self.mdInstrumentMode_Photometry.ident = "n0::n3"
        self.mdInstrumentMode_Photometry.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Photometry)
        self.addItem(self.mdInstrumentMode_Spectroscopy)
        self.mdInstrumentMode_Spectroscopy.ident = "n0::n4"
        self.mdInstrumentMode_Spectroscopy.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Spectroscopy)
        self.addItem(self.vlFilter_Red)
        self.vlFilter_Red.ident = "n0::n5::n0"
        self.vlFilter_Red.description = ""
        self.prFilter.addValue(self.vlFilter_Red)
        self.addItem(self.vlFilter_Blue)
        self.vlFilter_Blue.ident = "n0::n5::n1"
        self.vlFilter_Blue.description = ""
        self.prFilter.addValue(self.vlFilter_Blue)
        self.addItem(self.mdFilterMode_Enabled)
        self.mdFilterMode_Enabled.ident = "n0::n5::n2"
        self.mdFilterMode_Enabled.description = ""
        self.prFilter.addMode(self.mdFilterMode_Enabled)
        self.addItem(self.mdInstrumentMode_Engineering)
        self.mdInstrumentMode_Engineering.ident = "ENG-1"
        self.mdInstrumentMode_Engineering.description = "Instrument engineering mode"
        self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)
        self.addItem(self.mdDetectorMode_Engineering)
        self.mdDetectorMode_Engineering.ident = "ENG-2"
        self.mdDetectorMode_Engineering.description = "Detector engineering mode"
        self.sysDetector.addMode(self.mdDetectorMode_Engineering)
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
        # Marcamos DetectorMode_FixedAspect como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdDetectorMode_FixedAspect)
        # Marcamos DetectorMode_SlowFree como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdDetectorMode_SlowFree)
        # Marcamos DetectorMode_SlowFree como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_SlowFree)
        # Marcamos DetectorMode_FixedAspect como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_FixedAspect)
        # Marcamos DetectorMode_Engineering como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdDetectorMode_Engineering)
        # Marcamos expTimeMode_Slow como elegible para DetectorMode_SlowFree
        self.mdDetectorMode_SlowFree.addSubMode(self.mdexpTimeMode_Slow)
        # Marcamos expTimeMode_Fast como elegible para DetectorMode_FixedAspect
        self.mdDetectorMode_FixedAspect.addSubMode(self.mdexpTimeMode_Fast)
        # Marcamos expTimeMode_Slow como elegible para DetectorMode_FixedAspect
        self.mdDetectorMode_FixedAspect.addSubMode(self.mdexpTimeMode_Slow)
        # Marcamos expTimeMode_Slow como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Slow)
        # Marcamos expTimeMode_Fast como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdexpTimeMode_Fast)
        # Marcamos expTime_NormalRange como elegible para expTimeMode_Slow
        self.mdexpTimeMode_Slow.addValue(self.vlexpTime_NormalRange)
        # Marcamos expTime_FastRange como elegible para expTimeMode_Fast
        self.mdexpTimeMode_Fast.addValue(self.vlexpTime_FastRange)
        # Marcamos BinningMode_Normal como elegible para DetectorMode_SlowFree
        self.mdDetectorMode_SlowFree.addSubMode(self.mdBinningMode_Normal)
        # Marcamos BinningMode_Square como elegible para DetectorMode_FixedAspect
        self.mdDetectorMode_FixedAspect.addSubMode(self.mdBinningMode_Square)
        # Marcamos BinningMode_Normal como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Normal)
        # Marcamos BinningMode_Square como elegible para DetectorMode_Engineering
        self.mdDetectorMode_Engineering.addSubMode(self.mdBinningMode_Square)
        # Marcamos Binning_1x1 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x1 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_2x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x2 como elegible para BinningMode_Normal
        self.mdBinningMode_Normal.addValue(self.vlBinning_2x2)
        # Marcamos Binning_1x1 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_1x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_Square
        self.mdBinningMode_Square.addValue(self.vlBinning_2x2)
        # Marcamos FilterMode_Enabled como elegible para InstrumentMode_Photometry
        self.mdInstrumentMode_Photometry.addSubMode(self.mdFilterMode_Enabled)
        # Marcamos FilterMode_Enabled como elegible para InstrumentMode_Spectroscopy
        self.mdInstrumentMode_Spectroscopy.addSubMode(self.mdFilterMode_Enabled)
        # Marcamos FilterMode_Enabled como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdFilterMode_Enabled)
        # Marcamos Filter_Red como elegible para FilterMode_Enabled
        self.mdFilterMode_Enabled.addValue(self.vlFilter_Red)
        # Marcamos Filter_Blue como elegible para FilterMode_Enabled
        self.mdFilterMode_Enabled.addValue(self.vlFilter_Blue)

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


    ## DetectorMode 
    def get_DetectorMode(self)-> PORISMode:
        return self.sysDetector.getSelectedMode()

    def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDetector.selectMode(mode)


    ## prParam expTime 

    # expTime
    def get_expTime(self)-> PORISValue :
        return self.prexpTime.getSelectedValue()

    def set_expTime(self, value: PORISValue)-> PORISValue :
        return self.prexpTime.setValue(value)


    ## expTimeMode 
    def get_expTimeMode(self)-> PORISMode:
        return self.prexpTime.getSelectedMode()

    def set_expTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prexpTime.selectMode(mode)


    ## prParam Detector 

    # expTimeDouble  
    def get_expTimeDouble(self)-> float :
        v = self.prexpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_expTimeDouble(self, data: float)-> float :
        return self.prexpTime.getSelectedValue().setData(data)


    ## prParam Detector 

    # expTimeDouble  
    def get_expTimeDouble(self)-> float :
        v = self.prexpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_expTimeDouble(self, data: float)-> float :
        return self.prexpTime.getSelectedValue().setData(data)


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


    ## prParam Filter 

    # Filter
    def get_Filter(self)-> PORISValue :
        return self.prFilter.getSelectedValue()

    def set_Filter(self, value: PORISValue)-> PORISValue :
        return self.prFilter.setValue(value)


    ## FilterMode 
    def get_FilterMode(self)-> PORISMode:
        return self.prFilter.getSelectedMode()

    def set_FilterMode(self, mode: PORISMode)-> PORISMode :
        return self.prFilter.selectMode(mode)

