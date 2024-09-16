from PORIS import *

class ARCGenIIIPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysARCGenIII = PORISSys("ARCGenIII")
        self.setRoot(self.sysARCGenIII)
        self.sysFirmware = PORISSys("Firmware")
        self.sysVariants = PORISSys("Variants")
        self.sysAcquisition = PORISSys("Acquisition")
        self.prShuffleLines = PORISParam("ShuffleLines")
        self.prShiftNumber = PORISParam("ShiftNumber")
        self.sysSubarrayFeature = PORISSys("SubarrayFeature")
        self.prCols = PORISParam("Cols")
        self.proffsetRow = PORISParam("offsetRow")
        self.prRows = PORISParam("Rows")
        self.proffsetCol = PORISParam("offsetCol")
        self.sysExposureCtrl = PORISSys("ExposureCtrl")
        self.sysOpenShutter = PORISSys("OpenShutter")
        self.prExpTime = PORISParam("ExpTime")
        self.sysPixelSpeed = PORISSys("PixelSpeed")
        self.prnumOfFrames = PORISParam("numOfFrames")
        self.prCalibGain = PORISParam("CalibGain")
        self.sysOutputSource = PORISSys("OutputSource")
        self.sysRecomposition = PORISSys("Recomposition")
        self.sysDimensions = PORISSys("Dimensions")
        self.pruiRows = PORISParam("uiRows")
        self.pruiCols = PORISParam("uiCols")
        self.prBinning = PORISParam("Binning")
        self.mdARCGenIIIMode_Real = PORISMode("ARCGenIIIMode_Real")
        self.mdARCGenIIIMode_Emulated = PORISMode("ARCGenIIIMode_Emulated")
        self.mdFirmwareMode_tim = PORISMode("FirmwareMode_tim")
        self.mdFirmwareMode_osiris2 = PORISMode("FirmwareMode_osiris2")
        self.mdFirmwareMode_osiris3 = PORISMode("FirmwareMode_osiris3")
        self.mdFirmwareMode_osiris4 = PORISMode("FirmwareMode_osiris4")
        self.mdFirmwareMode_osiris5 = PORISMode("FirmwareMode_osiris5")
        self.mdAcquisitionMode_Normal = PORISMode("AcquisitionMode_Normal")
        self.mdAcquisitionMode_FrameTransfer = PORISMode("AcquisitionMode_FrameTransfer")
        self.mdAcquisitionMode_Shuffling = PORISMode("AcquisitionMode_Shuffling")
        self.vlShuffleLines_Full_Range = PORISValueFloat("ShuffleLines_Full_Range",0,200,1000)
        self.mdShuffleLinesMode_Normal = PORISMode("ShuffleLinesMode_Normal")
        self.vlShiftNumber_Full_Range = PORISValueFloat("ShiftNumber_Full_Range",0,5,1000)
        self.mdShiftNumberMode_Normal = PORISMode("ShiftNumberMode_Normal")
        self.mdSubarrayFeatureMode_Off = PORISMode("SubarrayFeatureMode_Off")
        self.mdSubarrayFeatureMode_On = PORISMode("SubarrayFeatureMode_On")
        self.mdColsMode_Normal = PORISMode("ColsMode_Normal")
        self.vlCols_Full_Range = PORISValueFloat("Cols_Full_Range",0,2048,4098)
        self.mdoffsetRowMode_Normal = PORISMode("offsetRowMode_Normal")
        self.vloffsetRow_Full_Range = PORISValueFloat("offsetRow_Full_Range",0,2048,4098)
        self.mdRowsMode_Normal = PORISMode("RowsMode_Normal")
        self.vlRows_Full_Range = PORISValueFloat("Rows_Full_Range",0,2048,4098)
        self.mdoffsetColMode_Normal = PORISMode("offsetColMode_Normal")
        self.vloffsetCol_Full_Range = PORISValueFloat("offsetCol_Full_Range",0,2048,4098)
        self.mdOpenShutterMode_On = PORISMode("OpenShutterMode_On")
        self.mdOpenShutterMode_Off = PORISMode("OpenShutterMode_Off")
        self.vlExpTime_Full_Range = PORISValueFloat("ExpTime_Full_Range",0,1,4294967.295)
        self.mdExpTimeMode_Normal = PORISMode("ExpTimeMode_Normal")
        self.mdExpTimeMode_FT = PORISMode("ExpTimeMode_FT")
        self.vlExpTime_FT_Range = PORISValueFloat("ExpTime_FT_Range",0,0,360)
        self.mdPixelSpeedMode_SLW = PORISMode("PixelSpeedMode_SLW")
        self.mdPixelSpeedMode_MED = PORISMode("PixelSpeedMode_MED")
        self.mdPixelSpeedMode_FST = PORISMode("PixelSpeedMode_FST")
        self.mdExposureCtrlMode_Normal = PORISMode("ExposureCtrlMode_Normal")
        self.mdExposureCtrlMode_FT = PORISMode("ExposureCtrlMode_FT")
        self.mdnumOfFramesMode_Multiple = PORISMode("numOfFramesMode_Multiple")
        self.vlnumOfFrames_Multiple_Range = PORISValueFloat("numOfFrames_Multiple_Range",2,10,4294967295)
        self.mdnumOfFramesMode_Single = PORISMode("numOfFramesMode_Single")
        self.vlnumOfFrames_1 = PORISValue("numOfFrames_1")
        self.vlCalibGain_Normal_Range = PORISValueFloat("CalibGain_Normal_Range",0,2,15)
        self.mdCalibGainMode_Normal = PORISMode("CalibGainMode_Normal")
        self.mdExposureCtrlMode_NoShutter = PORISMode("ExposureCtrlMode_NoShutter")
        self.mdExposureCtrlMode_Calibration = PORISMode("ExposureCtrlMode_Calibration")
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
        self.mdAcquisitionMode_NormalWindow = PORISMode("AcquisitionMode_NormalWindow")
        self.vluiRows_Full_Range = PORISValueFloat("uiRows_Full_Range",0,4112,4112)
        self.mduiRowsMode_Normal = PORISMode("uiRowsMode_Normal")
        self.vluiRows_FTRange = PORISValueFloat("uiRows_FTRange",0,2056,2056)
        self.mduiRowsMode_Half = PORISMode("uiRowsMode_Half")
        self.vluiCols_Full_Range = PORISValueFloat("uiCols_Full_Range",0,4096,4096)
        self.mduiColsMode_Normal = PORISMode("uiColsMode_Normal")
        self.mdDimensionsMode_Normal = PORISMode("DimensionsMode_Normal")
        self.mdDimensionsMode_FT = PORISMode("DimensionsMode_FT")
        self.vlBinning_1x1 = PORISValue("Binning_1x1")
        self.vlBinning_1x2 = PORISValue("Binning_1x2")
        self.vlBinning_2x1 = PORISValue("Binning_2x1")
        self.vlBinning_2x2 = PORISValue("Binning_2x2")
        self.mdBinningMode_All = PORISMode("BinningMode_All")
        self.mdAcquisitionMode_Calibration = PORISMode("AcquisitionMode_Calibration")
        self.mdVariantsMode_Normal = PORISMode("VariantsMode_Normal")
        self.mdVariantsMode_Extended = PORISMode("VariantsMode_Extended")
        self.mdVariantsMode_Extended_2 = PORISMode("VariantsMode_Extended_2")
        self.addItem(self.sysARCGenIII)
        self.sysARCGenIII.ident = "ARC-0004"
        self.sysARCGenIII.description = ""
        self.addItem(self.sysFirmware)
        self.sysFirmware.ident = "ARC-0007"
        self.sysFirmware.description = ""
        self.sysARCGenIII.addSubsystem(self.sysFirmware)
        self.addItem(self.sysVariants)
        self.sysVariants.ident = "ARC-0097"
        self.sysVariants.description = ""
        self.sysFirmware.addSubsystem(self.sysVariants)
        self.addItem(self.sysAcquisition)
        self.sysAcquisition.ident = "ARC-0076"
        self.sysAcquisition.description = ""
        self.sysVariants.addSubsystem(self.sysAcquisition)
        self.addItem(self.prShuffleLines)
        self.prShuffleLines.ident = "ARC-0080"
        self.prShuffleLines.description = ""
        self.sysAcquisition.addParam(self.prShuffleLines)
        self.addItem(self.prShiftNumber)
        self.prShiftNumber.ident = "ARC-0083"
        self.prShiftNumber.description = ""
        self.sysAcquisition.addParam(self.prShiftNumber)
        self.addItem(self.sysSubarrayFeature)
        self.sysSubarrayFeature.ident = "ARC-0013"
        self.sysSubarrayFeature.description = ""
        self.sysAcquisition.addSubsystem(self.sysSubarrayFeature)
        self.addItem(self.prCols)
        self.prCols.ident = "ARC-0044"
        self.prCols.description = ""
        self.sysSubarrayFeature.addParam(self.prCols)
        self.addItem(self.proffsetRow)
        self.proffsetRow.ident = "ARC-0045"
        self.proffsetRow.description = ""
        self.sysSubarrayFeature.addParam(self.proffsetRow)
        self.addItem(self.prRows)
        self.prRows.ident = "ARC-0043"
        self.prRows.description = ""
        self.sysSubarrayFeature.addParam(self.prRows)
        self.addItem(self.proffsetCol)
        self.proffsetCol.ident = "ARC-0046"
        self.proffsetCol.description = ""
        self.sysSubarrayFeature.addParam(self.proffsetCol)
        self.addItem(self.sysExposureCtrl)
        self.sysExposureCtrl.ident = "ARC-0103"
        self.sysExposureCtrl.description = ""
        self.sysAcquisition.addSubsystem(self.sysExposureCtrl)
        self.addItem(self.sysOpenShutter)
        self.sysOpenShutter.ident = "ARC-0009"
        self.sysOpenShutter.description = ""
        self.sysExposureCtrl.addSubsystem(self.sysOpenShutter)
        self.addItem(self.prExpTime)
        self.prExpTime.ident = "ARC-0010"
        self.prExpTime.description = ""
        self.sysExposureCtrl.addParam(self.prExpTime)
        self.addItem(self.sysPixelSpeed)
        self.sysPixelSpeed.ident = "ARC-0093"
        self.sysPixelSpeed.description = ""
        self.sysExposureCtrl.addSubsystem(self.sysPixelSpeed)
        self.addItem(self.prnumOfFrames)
        self.prnumOfFrames.ident = "ARC-0001"
        self.prnumOfFrames.description = ""
        self.sysExposureCtrl.addParam(self.prnumOfFrames)
        self.addItem(self.prCalibGain)
        self.prCalibGain.ident = "ARC-0130"
        self.prCalibGain.description = ""
        self.sysExposureCtrl.addParam(self.prCalibGain)
        self.addItem(self.sysOutputSource)
        self.sysOutputSource.ident = "ARC-0086"
        self.sysOutputSource.description = ""
        self.sysAcquisition.addSubsystem(self.sysOutputSource)
        self.addItem(self.sysRecomposition)
        self.sysRecomposition.ident = "ARC-0020"
        self.sysRecomposition.description = ""
        self.sysOutputSource.addSubsystem(self.sysRecomposition)
        self.addItem(self.sysDimensions)
        self.sysDimensions.ident = "ARC-0099"
        self.sysDimensions.description = ""
        self.sysAcquisition.addSubsystem(self.sysDimensions)
        self.addItem(self.pruiRows)
        self.pruiRows.ident = "ARC-0005"
        self.pruiRows.description = ""
        self.sysDimensions.addParam(self.pruiRows)
        self.addItem(self.pruiCols)
        self.pruiCols.ident = "ARC-0006"
        self.pruiCols.description = ""
        self.sysDimensions.addParam(self.pruiCols)
        self.addItem(self.prBinning)
        self.prBinning.ident = "ARC-0008"
        self.prBinning.description = ""
        self.sysAcquisition.addParam(self.prBinning)
        self.addItem(self.mdARCGenIIIMode_Real)
        self.mdARCGenIIIMode_Real.ident = "ARC-0018"
        self.mdARCGenIIIMode_Real.description = ""
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_Real)
        self.addItem(self.mdARCGenIIIMode_Emulated)
        self.mdARCGenIIIMode_Emulated.ident = "ARC-0110"
        self.mdARCGenIIIMode_Emulated.description = ""
        self.sysARCGenIII.addMode(self.mdARCGenIIIMode_Emulated)
        self.addItem(self.mdFirmwareMode_tim)
        self.mdFirmwareMode_tim.ident = "ARC-0021"
        self.mdFirmwareMode_tim.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_tim)
        self.addItem(self.mdFirmwareMode_osiris2)
        self.mdFirmwareMode_osiris2.ident = "ARC-0062"
        self.mdFirmwareMode_osiris2.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris2)
        self.addItem(self.mdFirmwareMode_osiris3)
        self.mdFirmwareMode_osiris3.ident = "ARC-0073"
        self.mdFirmwareMode_osiris3.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris3)
        self.addItem(self.mdFirmwareMode_osiris4)
        self.mdFirmwareMode_osiris4.ident = "ARC-0074"
        self.mdFirmwareMode_osiris4.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris4)
        self.addItem(self.mdFirmwareMode_osiris5)
        self.mdFirmwareMode_osiris5.ident = "ARC-0075"
        self.mdFirmwareMode_osiris5.description = ""
        self.sysFirmware.addMode(self.mdFirmwareMode_osiris5)
        self.addItem(self.mdAcquisitionMode_Normal)
        self.mdAcquisitionMode_Normal.ident = "ARC-0077"
        self.mdAcquisitionMode_Normal.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Normal)
        self.addItem(self.mdAcquisitionMode_FrameTransfer)
        self.mdAcquisitionMode_FrameTransfer.ident = "ARC-0078"
        self.mdAcquisitionMode_FrameTransfer.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FrameTransfer)
        self.addItem(self.mdAcquisitionMode_Shuffling)
        self.mdAcquisitionMode_Shuffling.ident = "ARC-0079"
        self.mdAcquisitionMode_Shuffling.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Shuffling)
        self.addItem(self.vlShuffleLines_Full_Range)
        self.vlShuffleLines_Full_Range.ident = "ARC-0081"
        self.vlShuffleLines_Full_Range.description = ""
        self.prShuffleLines.addValue(self.vlShuffleLines_Full_Range)
        self.addItem(self.mdShuffleLinesMode_Normal)
        self.mdShuffleLinesMode_Normal.ident = "ARC-0082"
        self.mdShuffleLinesMode_Normal.description = ""
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_Normal)
        self.addItem(self.vlShiftNumber_Full_Range)
        self.vlShiftNumber_Full_Range.ident = "ARC-0084"
        self.vlShiftNumber_Full_Range.description = ""
        self.prShiftNumber.addValue(self.vlShiftNumber_Full_Range)
        self.addItem(self.mdShiftNumberMode_Normal)
        self.mdShiftNumberMode_Normal.ident = "ARC-0085"
        self.mdShiftNumberMode_Normal.description = ""
        self.prShiftNumber.addMode(self.mdShiftNumberMode_Normal)
        self.addItem(self.mdSubarrayFeatureMode_Off)
        self.mdSubarrayFeatureMode_Off.ident = "ARC-0041"
        self.mdSubarrayFeatureMode_Off.description = ""
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_Off)
        self.addItem(self.mdSubarrayFeatureMode_On)
        self.mdSubarrayFeatureMode_On.ident = "ARC-0042"
        self.mdSubarrayFeatureMode_On.description = ""
        self.sysSubarrayFeature.addMode(self.mdSubarrayFeatureMode_On)
        self.addItem(self.mdColsMode_Normal)
        self.mdColsMode_Normal.ident = "ARC-0066"
        self.mdColsMode_Normal.description = ""
        self.prCols.addMode(self.mdColsMode_Normal)
        self.addItem(self.vlCols_Full_Range)
        self.vlCols_Full_Range.ident = "ARC-0065"
        self.vlCols_Full_Range.description = ""
        self.prCols.addValue(self.vlCols_Full_Range)
        self.addItem(self.mdoffsetRowMode_Normal)
        self.mdoffsetRowMode_Normal.ident = "ARC-0068"
        self.mdoffsetRowMode_Normal.description = ""
        self.proffsetRow.addMode(self.mdoffsetRowMode_Normal)
        self.addItem(self.vloffsetRow_Full_Range)
        self.vloffsetRow_Full_Range.ident = "ARC-0067"
        self.vloffsetRow_Full_Range.description = ""
        self.proffsetRow.addValue(self.vloffsetRow_Full_Range)
        self.addItem(self.mdRowsMode_Normal)
        self.mdRowsMode_Normal.ident = "ARC-0064"
        self.mdRowsMode_Normal.description = ""
        self.prRows.addMode(self.mdRowsMode_Normal)
        self.addItem(self.vlRows_Full_Range)
        self.vlRows_Full_Range.ident = "ARC-0063"
        self.vlRows_Full_Range.description = ""
        self.prRows.addValue(self.vlRows_Full_Range)
        self.addItem(self.mdoffsetColMode_Normal)
        self.mdoffsetColMode_Normal.ident = "ARC-0070"
        self.mdoffsetColMode_Normal.description = ""
        self.proffsetCol.addMode(self.mdoffsetColMode_Normal)
        self.addItem(self.vloffsetCol_Full_Range)
        self.vloffsetCol_Full_Range.ident = "ARC-0069"
        self.vloffsetCol_Full_Range.description = ""
        self.proffsetCol.addValue(self.vloffsetCol_Full_Range)
        self.addItem(self.mdOpenShutterMode_On)
        self.mdOpenShutterMode_On.ident = "ARC-0033"
        self.mdOpenShutterMode_On.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_On)
        self.addItem(self.mdOpenShutterMode_Off)
        self.mdOpenShutterMode_Off.ident = "ARC-0034"
        self.mdOpenShutterMode_Off.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_Off)
        self.addItem(self.vlExpTime_Full_Range)
        self.vlExpTime_Full_Range.ident = "ARC-0035"
        self.vlExpTime_Full_Range.description = ""
        self.prExpTime.addValue(self.vlExpTime_Full_Range)
        self.addItem(self.mdExpTimeMode_Normal)
        self.mdExpTimeMode_Normal.ident = "ARC-0036"
        self.mdExpTimeMode_Normal.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Normal)
        self.addItem(self.mdExpTimeMode_FT)
        self.mdExpTimeMode_FT.ident = "ARC-0119"
        self.mdExpTimeMode_FT.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_FT)
        self.addItem(self.vlExpTime_FT_Range)
        self.vlExpTime_FT_Range.ident = "ARC-0120"
        self.vlExpTime_FT_Range.description = ""
        self.prExpTime.addValue(self.vlExpTime_FT_Range)
        self.addItem(self.mdPixelSpeedMode_SLW)
        self.mdPixelSpeedMode_SLW.ident = "ARC-0094"
        self.mdPixelSpeedMode_SLW.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_SLW)
        self.addItem(self.mdPixelSpeedMode_MED)
        self.mdPixelSpeedMode_MED.ident = "ARC-0095"
        self.mdPixelSpeedMode_MED.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_MED)
        self.addItem(self.mdPixelSpeedMode_FST)
        self.mdPixelSpeedMode_FST.ident = "ARC-0096"
        self.mdPixelSpeedMode_FST.description = ""
        self.sysPixelSpeed.addMode(self.mdPixelSpeedMode_FST)
        self.addItem(self.mdExposureCtrlMode_Normal)
        self.mdExposureCtrlMode_Normal.ident = "ARC-0104"
        self.mdExposureCtrlMode_Normal.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_Normal)
        self.addItem(self.mdExposureCtrlMode_FT)
        self.mdExposureCtrlMode_FT.ident = "ARC-0114"
        self.mdExposureCtrlMode_FT.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_FT)
        self.addItem(self.mdnumOfFramesMode_Multiple)
        self.mdnumOfFramesMode_Multiple.ident = "ARC-0072"
        self.mdnumOfFramesMode_Multiple.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Multiple)
        self.addItem(self.vlnumOfFrames_Multiple_Range)
        self.vlnumOfFrames_Multiple_Range.ident = "ARC-0071"
        self.vlnumOfFrames_Multiple_Range.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_Multiple_Range)
        self.addItem(self.mdnumOfFramesMode_Single)
        self.mdnumOfFramesMode_Single.ident = "ARC-0037"
        self.mdnumOfFramesMode_Single.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Single)
        self.addItem(self.vlnumOfFrames_1)
        self.vlnumOfFrames_1.ident = "ARC-0131"
        self.vlnumOfFrames_1.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_1)
        self.addItem(self.vlCalibGain_Normal_Range)
        self.vlCalibGain_Normal_Range.ident = "ARC-0124"
        self.vlCalibGain_Normal_Range.description = ""
        self.prCalibGain.addValue(self.vlCalibGain_Normal_Range)
        self.addItem(self.mdCalibGainMode_Normal)
        self.mdCalibGainMode_Normal.ident = "ARC-0125"
        self.mdCalibGainMode_Normal.description = ""
        self.prCalibGain.addMode(self.mdCalibGainMode_Normal)
        self.addItem(self.mdExposureCtrlMode_NoShutter)
        self.mdExposureCtrlMode_NoShutter.ident = "ARC-0134"
        self.mdExposureCtrlMode_NoShutter.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_NoShutter)
        self.addItem(self.mdExposureCtrlMode_Calibration)
        self.mdExposureCtrlMode_Calibration.ident = "ARC-0136"
        self.mdExposureCtrlMode_Calibration.description = ""
        self.sysExposureCtrl.addMode(self.mdExposureCtrlMode_Calibration)
        self.addItem(self.mdOutputSourceMode_0x0)
        self.mdOutputSourceMode_0x0.ident = "ARC-0087"
        self.mdOutputSourceMode_0x0.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x0)
        self.addItem(self.mdOutputSourceMode_0x1)
        self.mdOutputSourceMode_0x1.ident = "ARC-0088"
        self.mdOutputSourceMode_0x1.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x1)
        self.addItem(self.mdOutputSourceMode_0x2)
        self.mdOutputSourceMode_0x2.ident = "ARC-0089"
        self.mdOutputSourceMode_0x2.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x2)
        self.addItem(self.mdOutputSourceMode_0x3)
        self.mdOutputSourceMode_0x3.ident = "ARC-0090"
        self.mdOutputSourceMode_0x3.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_0x3)
        self.addItem(self.mdOutputSourceMode_ALL)
        self.mdOutputSourceMode_ALL.ident = "ARC-0091"
        self.mdOutputSourceMode_ALL.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_ALL)
        self.addItem(self.mdOutputSourceMode_TWO)
        self.mdOutputSourceMode_TWO.ident = "ARC-0092"
        self.mdOutputSourceMode_TWO.description = ""
        self.sysOutputSource.addMode(self.mdOutputSourceMode_TWO)
        self.addItem(self.mdRecompositionMode_None)
        self.mdRecompositionMode_None.ident = "ARC-0055"
        self.mdRecompositionMode_None.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_None)
        self.addItem(self.mdRecompositionMode_Parallel)
        self.mdRecompositionMode_Parallel.ident = "ARC-0056"
        self.mdRecompositionMode_Parallel.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Parallel)
        self.addItem(self.mdRecompositionMode_Serial)
        self.mdRecompositionMode_Serial.ident = "ARC-0057"
        self.mdRecompositionMode_Serial.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_Serial)
        self.addItem(self.mdRecompositionMode_QuadCCD)
        self.mdRecompositionMode_QuadCCD.ident = "ARC-0058"
        self.mdRecompositionMode_QuadCCD.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadCCD)
        self.addItem(self.mdRecompositionMode_QuadIR)
        self.mdRecompositionMode_QuadIR.ident = "ARC-0059"
        self.mdRecompositionMode_QuadIR.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_QuadIR)
        self.addItem(self.mdRecompositionMode_CDSQuad)
        self.mdRecompositionMode_CDSQuad.ident = "ARC-0060"
        self.mdRecompositionMode_CDSQuad.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_CDSQuad)
        self.addItem(self.mdRecompositionMode_HawaiiRG)
        self.mdRecompositionMode_HawaiiRG.ident = "ARC-0061"
        self.mdRecompositionMode_HawaiiRG.description = ""
        self.sysRecomposition.addMode(self.mdRecompositionMode_HawaiiRG)
        self.addItem(self.mdAcquisitionMode_NormalWindow)
        self.mdAcquisitionMode_NormalWindow.ident = "ARC-0126"
        self.mdAcquisitionMode_NormalWindow.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalWindow)
        self.addItem(self.vluiRows_Full_Range)
        self.vluiRows_Full_Range.ident = "ARC-0022"
        self.vluiRows_Full_Range.description = ""
        self.pruiRows.addValue(self.vluiRows_Full_Range)
        self.addItem(self.mduiRowsMode_Normal)
        self.mduiRowsMode_Normal.ident = "ARC-0023"
        self.mduiRowsMode_Normal.description = ""
        self.pruiRows.addMode(self.mduiRowsMode_Normal)
        self.addItem(self.vluiRows_FTRange)
        self.vluiRows_FTRange.ident = "ARC-0127"
        self.vluiRows_FTRange.description = ""
        self.pruiRows.addValue(self.vluiRows_FTRange)
        self.addItem(self.mduiRowsMode_Half)
        self.mduiRowsMode_Half.ident = "ARC-0128"
        self.mduiRowsMode_Half.description = ""
        self.pruiRows.addMode(self.mduiRowsMode_Half)
        self.addItem(self.vluiCols_Full_Range)
        self.vluiCols_Full_Range.ident = "ARC-0024"
        self.vluiCols_Full_Range.description = ""
        self.pruiCols.addValue(self.vluiCols_Full_Range)
        self.addItem(self.mduiColsMode_Normal)
        self.mduiColsMode_Normal.ident = "ARC-0025"
        self.mduiColsMode_Normal.description = ""
        self.pruiCols.addMode(self.mduiColsMode_Normal)
        self.addItem(self.mdDimensionsMode_Normal)
        self.mdDimensionsMode_Normal.ident = "ARC-0100"
        self.mdDimensionsMode_Normal.description = ""
        self.sysDimensions.addMode(self.mdDimensionsMode_Normal)
        self.addItem(self.mdDimensionsMode_FT)
        self.mdDimensionsMode_FT.ident = "ARC-0129"
        self.mdDimensionsMode_FT.description = ""
        self.sysDimensions.addMode(self.mdDimensionsMode_FT)
        self.addItem(self.vlBinning_1x1)
        self.vlBinning_1x1.ident = "ARC-0026"
        self.vlBinning_1x1.description = ""
        self.prBinning.addValue(self.vlBinning_1x1)
        self.addItem(self.vlBinning_1x2)
        self.vlBinning_1x2.ident = "ARC-0027"
        self.vlBinning_1x2.description = ""
        self.prBinning.addValue(self.vlBinning_1x2)
        self.addItem(self.vlBinning_2x1)
        self.vlBinning_2x1.ident = "ARC-0028"
        self.vlBinning_2x1.description = ""
        self.prBinning.addValue(self.vlBinning_2x1)
        self.addItem(self.vlBinning_2x2)
        self.vlBinning_2x2.ident = "ARC-0029"
        self.vlBinning_2x2.description = ""
        self.prBinning.addValue(self.vlBinning_2x2)
        self.addItem(self.mdBinningMode_All)
        self.mdBinningMode_All.ident = "ARC-0031"
        self.mdBinningMode_All.description = ""
        self.prBinning.addMode(self.mdBinningMode_All)
        self.addItem(self.mdAcquisitionMode_Calibration)
        self.mdAcquisitionMode_Calibration.ident = "ARC-0137"
        self.mdAcquisitionMode_Calibration.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Calibration)
        self.addItem(self.mdVariantsMode_Normal)
        self.mdVariantsMode_Normal.ident = "ARC-0098"
        self.mdVariantsMode_Normal.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Normal)
        self.addItem(self.mdVariantsMode_Extended)
        self.mdVariantsMode_Extended.ident = "ARC-0105"
        self.mdVariantsMode_Extended.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Extended)
        self.addItem(self.mdVariantsMode_Extended_2)
        self.mdVariantsMode_Extended_2.ident = "ARC-0138"
        self.mdVariantsMode_Extended_2.description = ""
        self.sysVariants.addMode(self.mdVariantsMode_Extended_2)
        # Marcamos FirmwareMode_tim como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_tim)
        # Marcamos FirmwareMode_osiris2 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris2)
        # Marcamos FirmwareMode_osiris3 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris3)
        # Marcamos FirmwareMode_osiris4 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris4)
        # Marcamos FirmwareMode_osiris5 como elegible para ARCGenIIIMode_Real
        self.mdARCGenIIIMode_Real.addSubMode(self.mdFirmwareMode_osiris5)
        # Marcamos FirmwareMode_tim como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_tim)
        # Marcamos FirmwareMode_osiris2 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris2)
        # Marcamos FirmwareMode_osiris3 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris3)
        # Marcamos FirmwareMode_osiris4 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris4)
        # Marcamos FirmwareMode_osiris5 como elegible para ARCGenIIIMode_Emulated
        self.mdARCGenIIIMode_Emulated.addSubMode(self.mdFirmwareMode_osiris5)
        # Marcamos VariantsMode_Normal como elegible para FirmwareMode_tim
        self.mdFirmwareMode_tim.addSubMode(self.mdVariantsMode_Normal)
        # Marcamos VariantsMode_Extended como elegible para FirmwareMode_osiris2
        self.mdFirmwareMode_osiris2.addSubMode(self.mdVariantsMode_Extended)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris3
        self.mdFirmwareMode_osiris3.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris4
        self.mdFirmwareMode_osiris4.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos VariantsMode_Extended_2 como elegible para FirmwareMode_osiris5
        self.mdFirmwareMode_osiris5.addSubMode(self.mdVariantsMode_Extended_2)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Normal
        self.mdVariantsMode_Normal.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Normal
        self.mdVariantsMode_Normal.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Shuffling como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Extended
        self.mdVariantsMode_Extended.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Shuffling como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Normal como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_NormalWindow como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_NormalWindow)
        # Marcamos AcquisitionMode_Calibration como elegible para VariantsMode_Extended_2
        self.mdVariantsMode_Extended_2.addSubMode(self.mdAcquisitionMode_Calibration)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLines_Full_Range como elegible para ShuffleLinesMode_Normal
        self.mdShuffleLinesMode_Normal.addValue(self.vlShuffleLines_Full_Range)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumber_Full_Range como elegible para ShiftNumberMode_Normal
        self.mdShiftNumberMode_Normal.addValue(self.vlShiftNumber_Full_Range)
        # Marcamos SubarrayFeatureMode_Off como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdSubarrayFeatureMode_Off)
        # Marcamos SubarrayFeatureMode_On como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdSubarrayFeatureMode_On)
        # Marcamos SubarrayFeatureMode_Off como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdSubarrayFeatureMode_Off)
        # Marcamos ColsMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdColsMode_Normal)
        # Marcamos Cols_Full_Range como elegible para ColsMode_Normal
        self.mdColsMode_Normal.addValue(self.vlCols_Full_Range)
        # Marcamos offsetRowMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdoffsetRowMode_Normal)
        # Marcamos offsetRow_Full_Range como elegible para offsetRowMode_Normal
        self.mdoffsetRowMode_Normal.addValue(self.vloffsetRow_Full_Range)
        # Marcamos RowsMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdRowsMode_Normal)
        # Marcamos Rows_Full_Range como elegible para RowsMode_Normal
        self.mdRowsMode_Normal.addValue(self.vlRows_Full_Range)
        # Marcamos offsetColMode_Normal como elegible para SubarrayFeatureMode_On
        self.mdSubarrayFeatureMode_On.addSubMode(self.mdoffsetColMode_Normal)
        # Marcamos offsetCol_Full_Range como elegible para offsetColMode_Normal
        self.mdoffsetColMode_Normal.addValue(self.vloffsetCol_Full_Range)
        # Marcamos ExposureCtrlMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdExposureCtrlMode_Normal)
        # Marcamos ExposureCtrlMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdExposureCtrlMode_FT)
        # Marcamos ExposureCtrlMode_NoShutter como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdExposureCtrlMode_NoShutter)
        # Marcamos ExposureCtrlMode_Normal como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdExposureCtrlMode_Normal)
        # Marcamos ExposureCtrlMode_Calibration como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdExposureCtrlMode_Calibration)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_FT como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTime_Full_Range como elegible para ExpTimeMode_Normal
        self.mdExpTimeMode_Normal.addValue(self.vlExpTime_Full_Range)
        # Marcamos ExpTime_FT_Range como elegible para ExpTimeMode_FT
        self.mdExpTimeMode_FT.addValue(self.vlExpTime_FT_Range)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos PixelSpeedMode_FST como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_FST)
        # Marcamos PixelSpeedMode_MED como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_MED)
        # Marcamos PixelSpeedMode_SLW como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdPixelSpeedMode_SLW)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_Normal
        self.mdExposureCtrlMode_Normal.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_FT
        self.mdExposureCtrlMode_FT.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_NoShutter
        self.mdExposureCtrlMode_NoShutter.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFramesMode_Single como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdnumOfFramesMode_Single)
        # Marcamos numOfFramesMode_Multiple como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdnumOfFramesMode_Multiple)
        # Marcamos numOfFrames_Multiple_Range como elegible para numOfFramesMode_Multiple
        self.mdnumOfFramesMode_Multiple.addValue(self.vlnumOfFrames_Multiple_Range)
        # Marcamos numOfFrames_1 como elegible para numOfFramesMode_Single
        self.mdnumOfFramesMode_Single.addValue(self.vlnumOfFrames_1)
        # Marcamos CalibGainMode_Normal como elegible para ExposureCtrlMode_Calibration
        self.mdExposureCtrlMode_Calibration.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGain_Normal_Range como elegible para CalibGainMode_Normal
        self.mdCalibGainMode_Normal.addValue(self.vlCalibGain_Normal_Range)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdOutputSourceMode_ALL)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x0 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x0)
        # Marcamos OutputSourceMode_0x1 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x1)
        # Marcamos OutputSourceMode_0x2 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x2)
        # Marcamos OutputSourceMode_0x3 como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_0x3)
        # Marcamos OutputSourceMode_TWO como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_TWO)
        # Marcamos OutputSourceMode_ALL como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdOutputSourceMode_ALL)
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
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdDimensionsMode_FT)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos DimensionsMode_Normal como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdDimensionsMode_Normal)
        # Marcamos uiRowsMode_Normal como elegible para DimensionsMode_Normal
        self.mdDimensionsMode_Normal.addSubMode(self.mduiRowsMode_Normal)
        # Marcamos uiRowsMode_Half como elegible para DimensionsMode_FT
        self.mdDimensionsMode_FT.addSubMode(self.mduiRowsMode_Half)
        # Marcamos uiRows_Full_Range como elegible para uiRowsMode_Normal
        self.mduiRowsMode_Normal.addValue(self.vluiRows_Full_Range)
        # Marcamos uiRows_FTRange como elegible para uiRowsMode_Half
        self.mduiRowsMode_Half.addValue(self.vluiRows_FTRange)
        # Marcamos uiColsMode_Normal como elegible para DimensionsMode_Normal
        self.mdDimensionsMode_Normal.addSubMode(self.mduiColsMode_Normal)
        # Marcamos uiColsMode_Normal como elegible para DimensionsMode_FT
        self.mdDimensionsMode_FT.addSubMode(self.mduiColsMode_Normal)
        # Marcamos uiCols_Full_Range como elegible para uiColsMode_Normal
        self.mduiColsMode_Normal.addValue(self.vluiCols_Full_Range)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_NormalWindow
        self.mdAcquisitionMode_NormalWindow.addSubMode(self.mdBinningMode_All)
        # Marcamos BinningMode_All como elegible para AcquisitionMode_Calibration
        self.mdAcquisitionMode_Calibration.addSubMode(self.mdBinningMode_All)
        # Marcamos Binning_1x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x1)
        # Marcamos Binning_1x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_1x2)
        # Marcamos Binning_2x1 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x1)
        # Marcamos Binning_2x2 como elegible para BinningMode_All
        self.mdBinningMode_All.addValue(self.vlBinning_2x2)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## ARCGenIIIMode 
    def get_ARCGenIIIMode(self)-> PORISMode:
        return self.sysARCGenIII.getSelectedMode()

    def set_ARCGenIIIMode(self, mode: PORISMode)-> PORISMode :
        return self.sysARCGenIII.selectMode(mode)


    ## FirmwareMode 
    def get_FirmwareMode(self)-> PORISMode:
        return self.sysFirmware.getSelectedMode()

    def set_FirmwareMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFirmware.selectMode(mode)


    ## VariantsMode 
    def get_VariantsMode(self)-> PORISMode:
        return self.sysVariants.getSelectedMode()

    def set_VariantsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysVariants.selectMode(mode)


    ## AcquisitionMode 
    def get_AcquisitionMode(self)-> PORISMode:
        return self.sysAcquisition.getSelectedMode()

    def set_AcquisitionMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAcquisition.selectMode(mode)


    ## prParam ShuffleLines 

    # ShuffleLines
    def get_ShuffleLines(self)-> PORISValue :
        return self.prShuffleLines.getSelectedValue()

    def set_ShuffleLines(self, value: PORISValue)-> PORISValue :
        return self.prShuffleLines.setValue(value)


    ## ShuffleLinesMode 
    def get_ShuffleLinesMode(self)-> PORISMode:
        return self.prShuffleLines.getSelectedMode()

    def set_ShuffleLinesMode(self, mode: PORISMode)-> PORISMode :
        return self.prShuffleLines.selectMode(mode)


    ## prParam Acquisition 

    # ShuffleLinesDouble  
    def get_ShuffleLinesDouble(self)-> float :
        v = self.prShuffleLines.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ShuffleLinesDouble(self, data: float)-> float :
        return self.prShuffleLines.getSelectedValue().setData(data)


    ## prParam ShiftNumber 

    # ShiftNumber
    def get_ShiftNumber(self)-> PORISValue :
        return self.prShiftNumber.getSelectedValue()

    def set_ShiftNumber(self, value: PORISValue)-> PORISValue :
        return self.prShiftNumber.setValue(value)


    ## ShiftNumberMode 
    def get_ShiftNumberMode(self)-> PORISMode:
        return self.prShiftNumber.getSelectedMode()

    def set_ShiftNumberMode(self, mode: PORISMode)-> PORISMode :
        return self.prShiftNumber.selectMode(mode)


    ## prParam Acquisition 

    # ShiftNumberDouble  
    def get_ShiftNumberDouble(self)-> float :
        v = self.prShiftNumber.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ShiftNumberDouble(self, data: float)-> float :
        return self.prShiftNumber.getSelectedValue().setData(data)


    ## SubarrayFeatureMode 
    def get_SubarrayFeatureMode(self)-> PORISMode:
        return self.sysSubarrayFeature.getSelectedMode()

    def set_SubarrayFeatureMode(self, mode: PORISMode)-> PORISMode :
        return self.sysSubarrayFeature.selectMode(mode)


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


    ## prParam SubarrayFeature 

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


    ## prParam SubarrayFeature 

    # offsetRowDouble  
    def get_offsetRowDouble(self)-> float :
        v = self.proffsetRow.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetRowDouble(self, data: float)-> float :
        return self.proffsetRow.getSelectedValue().setData(data)


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


    ## prParam SubarrayFeature 

    # RowsDouble  
    def get_RowsDouble(self)-> float :
        v = self.prRows.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RowsDouble(self, data: float)-> float :
        return self.prRows.getSelectedValue().setData(data)


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


    ## prParam SubarrayFeature 

    # offsetColDouble  
    def get_offsetColDouble(self)-> float :
        v = self.proffsetCol.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_offsetColDouble(self, data: float)-> float :
        return self.proffsetCol.getSelectedValue().setData(data)


    ## ExposureCtrlMode 
    def get_ExposureCtrlMode(self)-> PORISMode:
        return self.sysExposureCtrl.getSelectedMode()

    def set_ExposureCtrlMode(self, mode: PORISMode)-> PORISMode :
        return self.sysExposureCtrl.selectMode(mode)


    ## OpenShutterMode 
    def get_OpenShutterMode(self)-> PORISMode:
        return self.sysOpenShutter.getSelectedMode()

    def set_OpenShutterMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOpenShutter.selectMode(mode)


    ## prParam ExpTime 

    # ExpTime
    def get_ExpTime(self)-> PORISValue :
        return self.prExpTime.getSelectedValue()

    def set_ExpTime(self, value: PORISValue)-> PORISValue :
        return self.prExpTime.setValue(value)


    ## ExpTimeMode 
    def get_ExpTimeMode(self)-> PORISMode:
        return self.prExpTime.getSelectedMode()

    def set_ExpTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prExpTime.selectMode(mode)


    ## prParam ExposureCtrl 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## prParam ExposureCtrl 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## PixelSpeedMode 
    def get_PixelSpeedMode(self)-> PORISMode:
        return self.sysPixelSpeed.getSelectedMode()

    def set_PixelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPixelSpeed.selectMode(mode)


    ## prParam numOfFrames 

    # numOfFrames
    def get_numOfFrames(self)-> PORISValue :
        return self.prnumOfFrames.getSelectedValue()

    def set_numOfFrames(self, value: PORISValue)-> PORISValue :
        return self.prnumOfFrames.setValue(value)


    ## numOfFramesMode 
    def get_numOfFramesMode(self)-> PORISMode:
        return self.prnumOfFrames.getSelectedMode()

    def set_numOfFramesMode(self, mode: PORISMode)-> PORISMode :
        return self.prnumOfFrames.selectMode(mode)


    ## prParam ExposureCtrl 

    # numOfFramesDouble  
    def get_numOfFramesDouble(self)-> float :
        v = self.prnumOfFrames.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_numOfFramesDouble(self, data: float)-> float :
        return self.prnumOfFrames.getSelectedValue().setData(data)


    ## prParam CalibGain 

    # CalibGain
    def get_CalibGain(self)-> PORISValue :
        return self.prCalibGain.getSelectedValue()

    def set_CalibGain(self, value: PORISValue)-> PORISValue :
        return self.prCalibGain.setValue(value)


    ## CalibGainMode 
    def get_CalibGainMode(self)-> PORISMode:
        return self.prCalibGain.getSelectedMode()

    def set_CalibGainMode(self, mode: PORISMode)-> PORISMode :
        return self.prCalibGain.selectMode(mode)


    ## prParam ExposureCtrl 

    # CalibGainDouble  
    def get_CalibGainDouble(self)-> float :
        v = self.prCalibGain.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CalibGainDouble(self, data: float)-> float :
        return self.prCalibGain.getSelectedValue().setData(data)


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


    ## DimensionsMode 
    def get_DimensionsMode(self)-> PORISMode:
        return self.sysDimensions.getSelectedMode()

    def set_DimensionsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDimensions.selectMode(mode)


    ## prParam uiRows 

    # uiRows
    def get_uiRows(self)-> PORISValue :
        return self.pruiRows.getSelectedValue()

    def set_uiRows(self, value: PORISValue)-> PORISValue :
        return self.pruiRows.setValue(value)


    ## uiRowsMode 
    def get_uiRowsMode(self)-> PORISMode:
        return self.pruiRows.getSelectedMode()

    def set_uiRowsMode(self, mode: PORISMode)-> PORISMode :
        return self.pruiRows.selectMode(mode)


    ## prParam Dimensions 

    # uiRowsDouble  
    def get_uiRowsDouble(self)-> float :
        v = self.pruiRows.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_uiRowsDouble(self, data: float)-> float :
        return self.pruiRows.getSelectedValue().setData(data)


    ## prParam Dimensions 

    # uiRowsDouble  
    def get_uiRowsDouble(self)-> float :
        v = self.pruiRows.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_uiRowsDouble(self, data: float)-> float :
        return self.pruiRows.getSelectedValue().setData(data)


    ## prParam uiCols 

    # uiCols
    def get_uiCols(self)-> PORISValue :
        return self.pruiCols.getSelectedValue()

    def set_uiCols(self, value: PORISValue)-> PORISValue :
        return self.pruiCols.setValue(value)


    ## uiColsMode 
    def get_uiColsMode(self)-> PORISMode:
        return self.pruiCols.getSelectedMode()

    def set_uiColsMode(self, mode: PORISMode)-> PORISMode :
        return self.pruiCols.selectMode(mode)


    ## prParam Dimensions 

    # uiColsDouble  
    def get_uiColsDouble(self)-> float :
        v = self.pruiCols.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_uiColsDouble(self, data: float)-> float :
        return self.pruiCols.getSelectedValue().setData(data)


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


    ## Action trigger ARCGenIII_expose ##
    def execARCGenIII_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_init_expose ##
    def execARCGenIII_init_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_cfg_init_expose ##
    def execARCGenIII_cfg_init_expose(self, value: bool) -> bool:
        # Override this
        return True


    ## Action trigger ARCGenIII_abort ##
    def execARCGenIII_abort(self, value: bool) -> bool:
        # Override this
        return True

