from PORIS import *

class simplePORIS:
    def __init__(self):
        idcounter = 1
        self.sysInstrument = PORISSys("Instrument")
        self.mdInstrumentMode_UNKNOWN = PORISMode("InstrumentMode_UNKNOWN")
        self.root = self.sysInstrument
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

        self.sysInstrument.id = idcounter
        idcounter += 1
        self.sysInstrument.ident = "Instrument"
        self.sysInstrument.description = ""

        self.mdInstrumentMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdInstrumentMode_UNKNOWN.ident = "InstrumentMode_UNKNOWN"
        self.mdInstrumentMode_UNKNOWN.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_UNKNOWN)

        self.prMasks.id = idcounter
        idcounter += 1
        self.prMasks.ident = "Masks"
        self.prMasks.description = ""
        self.sysInstrument.addParam(self.prMasks)

        self.vlMasks_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlMasks_UNKNOWN.ident = "Masks_UNKNOWN"
        self.vlMasks_UNKNOWN.description = "Unknown value for Masks"
        self.prMasks.addValue(self.vlMasks_UNKNOWN)

        self.mdMasksMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdMasksMode_UNKNOWN.ident = "MasksMode_UNKNOWN"
        self.mdMasksMode_UNKNOWN.description = "Unknown mode for Masks"
        self.prMasks.addMode(self.mdMasksMode_UNKNOWN)
        self.mdMasksMode_UNKNOWN.addValue(self.vlMasks_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdMasksMode_UNKNOWN)

        self.prDispersion.id = idcounter
        idcounter += 1
        self.prDispersion.ident = "Dispersion"
        self.prDispersion.description = ""
        self.sysInstrument.addParam(self.prDispersion)

        self.vlDispersion_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlDispersion_UNKNOWN.ident = "Dispersion_UNKNOWN"
        self.vlDispersion_UNKNOWN.description = "Unknown value for Dispersion"
        self.prDispersion.addValue(self.vlDispersion_UNKNOWN)

        self.mdDispersionMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDispersionMode_UNKNOWN.ident = "DispersionMode_UNKNOWN"
        self.mdDispersionMode_UNKNOWN.description = "Unknown mode for Dispersion"
        self.prDispersion.addMode(self.mdDispersionMode_UNKNOWN)
        self.mdDispersionMode_UNKNOWN.addValue(self.vlDispersion_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdDispersionMode_UNKNOWN)

        self.sysDetector.id = idcounter
        idcounter += 1
        self.sysDetector.ident = "Detector"
        self.sysDetector.description = ""
        self.sysInstrument.addSubsystem(self.sysDetector)

        self.mdDetectorMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdDetectorMode_UNKNOWN.ident = "DetectorMode_UNKNOWN"
        self.mdDetectorMode_UNKNOWN.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_UNKNOWN)

        self.prexpTime.id = idcounter
        idcounter += 1
        self.prexpTime.ident = "expTime"
        self.prexpTime.description = ""
        self.sysDetector.addParam(self.prexpTime)

        self.vlexpTime_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlexpTime_UNKNOWN.ident = "expTime_UNKNOWN"
        self.vlexpTime_UNKNOWN.description = "Unknown value for expTime"
        self.prexpTime.addValue(self.vlexpTime_UNKNOWN)

        self.mdexpTimeMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdexpTimeMode_UNKNOWN.ident = "expTimeMode_UNKNOWN"
        self.mdexpTimeMode_UNKNOWN.description = "Unknown mode for expTime"
        self.prexpTime.addMode(self.mdexpTimeMode_UNKNOWN)
        self.mdexpTimeMode_UNKNOWN.addValue(self.vlexpTime_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdexpTimeMode_UNKNOWN)

        self.prBinning.id = idcounter
        idcounter += 1
        self.prBinning.ident = "Binning"
        self.prBinning.description = ""
        self.sysDetector.addParam(self.prBinning)

        self.vlBinning_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlBinning_UNKNOWN.ident = "Binning_UNKNOWN"
        self.vlBinning_UNKNOWN.description = "Unknown value for Binning"
        self.prBinning.addValue(self.vlBinning_UNKNOWN)

        self.mdBinningMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdBinningMode_UNKNOWN.ident = "BinningMode_UNKNOWN"
        self.mdBinningMode_UNKNOWN.description = "Unknown mode for Binning"
        self.prBinning.addMode(self.mdBinningMode_UNKNOWN)
        self.mdBinningMode_UNKNOWN.addValue(self.vlBinning_UNKNOWN)
        self.mdDetectorMode_UNKNOWN.addSubMode(self.mdBinningMode_UNKNOWN)

        self.prFilter.id = idcounter
        idcounter += 1
        self.prFilter.ident = "Filter"
        self.prFilter.description = ""
        self.sysInstrument.addParam(self.prFilter)

        self.vlFilter_UNKNOWN.id = idcounter
        idcounter += 1
        self.vlFilter_UNKNOWN.ident = "Filter_UNKNOWN"
        self.vlFilter_UNKNOWN.description = "Unknown value for Filter"
        self.prFilter.addValue(self.vlFilter_UNKNOWN)

        self.mdFilterMode_UNKNOWN.id = idcounter
        idcounter += 1
        self.mdFilterMode_UNKNOWN.ident = "FilterMode_UNKNOWN"
        self.mdFilterMode_UNKNOWN.description = "Unknown mode for Filter"
        self.prFilter.addMode(self.mdFilterMode_UNKNOWN)
        self.mdFilterMode_UNKNOWN.addValue(self.vlFilter_UNKNOWN)
        self.mdInstrumentMode_UNKNOWN.addSubMode(self.mdFilterMode_UNKNOWN)

        self.vlMasks_0_6.id = idcounter
        idcounter += 1
        self.vlMasks_0_6.ident = "Masks_0_6"
        self.vlMasks_0_6.description = ""
        self.prMasks.addValue(self.vlMasks_0_6)

        self.vlMasks_1_0.id = idcounter
        idcounter += 1
        self.vlMasks_1_0.ident = "Masks_1_0"
        self.vlMasks_1_0.description = ""
        self.prMasks.addValue(self.vlMasks_1_0)

        self.vlMasks_2_0.id = idcounter
        idcounter += 1
        self.vlMasks_2_0.ident = "Masks_2_0"
        self.vlMasks_2_0.description = ""
        self.prMasks.addValue(self.vlMasks_2_0)

        self.mdMasksMode_Spectroscopy.id = idcounter
        idcounter += 1
        self.mdMasksMode_Spectroscopy.ident = "MasksMode_Spectroscopy"
        self.mdMasksMode_Spectroscopy.description = ""
        self.prMasks.addMode(self.mdMasksMode_Spectroscopy)

        self.vlDispersion_R500.id = idcounter
        idcounter += 1
        self.vlDispersion_R500.ident = "Dispersion_R500"
        self.vlDispersion_R500.description = ""
        self.prDispersion.addValue(self.vlDispersion_R500)

        self.vlDispersion_R1000.id = idcounter
        idcounter += 1
        self.vlDispersion_R1000.ident = "Dispersion_R1000"
        self.vlDispersion_R1000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R1000)

        self.vlDispersion_R2000.id = idcounter
        idcounter += 1
        self.vlDispersion_R2000.ident = "Dispersion_R2000"
        self.vlDispersion_R2000.description = ""
        self.prDispersion.addValue(self.vlDispersion_R2000)

        self.mdDispersionMode_Normal.id = idcounter
        idcounter += 1
        self.mdDispersionMode_Normal.ident = "DispersionMode_Normal"
        self.mdDispersionMode_Normal.description = ""
        self.prDispersion.addMode(self.mdDispersionMode_Normal)

        self.vlexpTime_NormalRange.id = idcounter
        idcounter += 1
        self.vlexpTime_NormalRange.ident = "expTime_NormalRange"
        self.vlexpTime_NormalRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_NormalRange)

        self.mdexpTimeMode_Slow.id = idcounter
        idcounter += 1
        self.mdexpTimeMode_Slow.ident = "expTimeMode_Slow"
        self.mdexpTimeMode_Slow.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Slow)

        self.mdexpTimeMode_Fast.id = idcounter
        idcounter += 1
        self.mdexpTimeMode_Fast.ident = "expTimeMode_Fast"
        self.mdexpTimeMode_Fast.description = ""
        self.prexpTime.addMode(self.mdexpTimeMode_Fast)

        self.vlexpTime_FastRange.id = idcounter
        idcounter += 1
        self.vlexpTime_FastRange.ident = "expTime_FastRange"
        self.vlexpTime_FastRange.description = ""
        self.prexpTime.addValue(self.vlexpTime_FastRange)

        self.vlBinning_1x1.id = idcounter
        idcounter += 1
        self.vlBinning_1x1.ident = "Binning_1x1"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)

        self.vlBinning_2x1.id = idcounter
        idcounter += 1
        self.vlBinning_2x1.ident = "Binning_2x1"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)

        self.vlBinning_1x2.id = idcounter
        idcounter += 1
        self.vlBinning_1x2.ident = "Binning_1x2"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)

        self.vlBinning_2x2.id = idcounter
        idcounter += 1
        self.vlBinning_2x2.ident = "Binning_2x2"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)

        self.mdBinningMode_Normal.id = idcounter
        idcounter += 1
        self.mdBinningMode_Normal.ident = "BinningMode_Normal"
        self.mdBinningMode_Normal.description = ""
        self.prBinning.addMode(self.mdBinningMode_Normal)

        self.mdBinningMode_Square.id = idcounter
        idcounter += 1
        self.mdBinningMode_Square.ident = "BinningMode_Square"
        self.mdBinningMode_Square.description = ""
        self.prBinning.addMode(self.mdBinningMode_Square)

        self.mdDetectorMode_SlowFree.id = idcounter
        idcounter += 1
        self.mdDetectorMode_SlowFree.ident = "DetectorMode_SlowFree"
        self.mdDetectorMode_SlowFree.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_SlowFree)

        self.mdDetectorMode_FixedAspect.id = idcounter
        idcounter += 1
        self.mdDetectorMode_FixedAspect.ident = "DetectorMode_FixedAspect"
        self.mdDetectorMode_FixedAspect.description = ""
        self.sysDetector.addMode(self.mdDetectorMode_FixedAspect)

        self.mdInstrumentMode_Photometry.id = idcounter
        idcounter += 1
        self.mdInstrumentMode_Photometry.ident = "InstrumentMode_Photometry"
        self.mdInstrumentMode_Photometry.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Photometry)

        self.mdInstrumentMode_Spectroscopy.id = idcounter
        idcounter += 1
        self.mdInstrumentMode_Spectroscopy.ident = "InstrumentMode_Spectroscopy"
        self.mdInstrumentMode_Spectroscopy.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Spectroscopy)

        self.vlFilter_Red.id = idcounter
        idcounter += 1
        self.vlFilter_Red.ident = "Filter_Red"
        self.vlFilter_Red.description = ""
        self.prFilter.addValue(self.vlFilter_Red)

        self.vlFilter_Blue.id = idcounter
        idcounter += 1
        self.vlFilter_Blue.ident = "Filter_Blue"
        self.vlFilter_Blue.description = ""
        self.prFilter.addValue(self.vlFilter_Blue)

        self.mdFilterMode_Enabled.id = idcounter
        idcounter += 1
        self.mdFilterMode_Enabled.ident = "FilterMode_Enabled"
        self.mdFilterMode_Enabled.description = ""
        self.prFilter.addMode(self.mdFilterMode_Enabled)

        self.mdInstrumentMode_Engineering.id = idcounter
        idcounter += 1
        self.mdInstrumentMode_Engineering.ident = "InstrumentMode_Engineering"
        self.mdInstrumentMode_Engineering.description = "Instrument engineering mode"
        self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)

        self.mdDetectorMode_Engineering.id = idcounter
        idcounter += 1
        self.mdDetectorMode_Engineering.ident = "DetectorMode_Engineering"
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

