from PORIS import *

class osidasPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysDAS = PORISSys("DAS")
        self.setRoot(self.sysDAS)
        self.sysAcquisition = PORISSys("Acquisition")
        self.prShuffleLines = PORISParam("ShuffleLines")
        self.prShiftNumber = PORISParam("ShiftNumber")
        self.prExpTime = PORISParam("ExpTime")
        self.sysMultipleExposure = PORISSys("MultipleExposure")
        self.prnumOfFrames = PORISParam("numOfFrames")
        self.prPixelSpeed = PORISParam("PixelSpeed")
        self.sysDetector = PORISSys("Detector")
        self.prCalibGain = PORISParam("CalibGain")
        self.sysOpenShutter = PORISSys("OpenShutter")
        self.sysProcessMonitor = PORISSys("ProcessMonitor")
        self.prCurrentEllapsed = PORISParam("CurrentEllapsed")
        self.prCurrentImg = PORISParam("CurrentImg")
        self.prCurrentPct = PORISParam("CurrentPct")
        self.prOverallPct = PORISParam("OverallPct")
        self.mdAcquisitionMode_Normal = PORISMode("AcquisitionMode_Normal")
        self.mdAcquisitionMode_FrameTransfer = PORISMode("AcquisitionMode_FrameTransfer")
        self.mdAcquisitionMode_Shuffling = PORISMode("AcquisitionMode_Shuffling")
        self.vlShuffleLines_FullRange = PORISValueFloat("ShuffleLines_FullRange",0.0,200.0,1000.0)
        self.mdShuffleLinesMode_Normal = PORISMode("ShuffleLinesMode_Normal")
        self.vlShiftNumber_FullRange = PORISValueFloat("ShiftNumber_FullRange",0.0,5.0,1000.0)
        self.mdShiftNumberMode_Normal = PORISMode("ShiftNumberMode_Normal")
        self.vlExpTime_FullRange = PORISValueFloat("ExpTime_FullRange",0.0,1.0,10000.0)
        self.mdExpTimeMode_Normal = PORISMode("ExpTimeMode_Normal")
        self.mdExpTimeMode_Bias = PORISMode("ExpTimeMode_Bias")
        self.vlExpTime_0_0 = PORISValue("ExpTime_0_0")
        self.mdExpTimeMode_FT = PORISMode("ExpTimeMode_FT")
        self.vlExpTime_FTRange = PORISValueFloat("ExpTime_FTRange",0.0,0.0,360.0)
        self.mdnumOfFramesMode_Normal = PORISMode("numOfFramesMode_Normal")
        self.vlnumOfFrames_FullRange = PORISValueFloat("numOfFrames_FullRange",0.0,10.0,4294967295.0)
        self.mdMultipleExposureMode_On = PORISMode("MultipleExposureMode_On")
        self.mdMultipleExposureMode_Single = PORISMode("MultipleExposureMode_Single")
        self.vlPixelSpeed_SLW = PORISValue("PixelSpeed_SLW")
        self.vlPixelSpeed_MED = PORISValue("PixelSpeed_MED")
        self.vlPixelSpeed_FST = PORISValue("PixelSpeed_FST")
        self.mdPixelSpeedMode_All = PORISMode("PixelSpeedMode_All")
        self.mdDetectorMode_FT = PORISMode("DetectorMode_FT")
        self.mdDetectorMode_Window = PORISMode("DetectorMode_Window")
        self.mdDetectorMode_FullDetector = PORISMode("DetectorMode_FullDetector")
        self.mdDetectorMode_WindowSq = PORISMode("DetectorMode_WindowSq")
        self.mdDetectorMode_FullDetectorSq = PORISMode("DetectorMode_FullDetectorSq")
        self.mdAcquisitionMode_FTBias = PORISMode("AcquisitionMode_FTBias")
        self.mdAcquisitionMode_NormalBias = PORISMode("AcquisitionMode_NormalBias")
        self.mdAcquisitionMode_ShufflingBias = PORISMode("AcquisitionMode_ShufflingBias")
        self.mdAcquisitionMode_NormalSquare = PORISMode("AcquisitionMode_NormalSquare")
        self.mdAcquisitionMode_ShufflingSquare = PORISMode("AcquisitionMode_ShufflingSquare")
        self.mdAcquisitionMode_GainCalib = PORISMode("AcquisitionMode_GainCalib")
        self.vlCalibGain_FullRange = PORISValueFloat("CalibGain_FullRange",0.0,2.0,15.0)
        self.mdCalibGainMode_Normal = PORISMode("CalibGainMode_Normal")
        self.mdDASMode_SimpleImg = PORISMode("DASMode_SimpleImg")
        self.mdDASMode_SimpleSpec = PORISMode("DASMode_SimpleSpec")
        self.mdDASMode_ShufffingSpec = PORISMode("DASMode_ShufffingSpec")
        self.mdOpenShutterMode_On = PORISMode("OpenShutterMode_On")
        self.mdOpenShutterMode_Off = PORISMode("OpenShutterMode_Off")
        self.mdDASMode_FTImg = PORISMode("DASMode_FTImg")
        self.mdDASMode_FTDark = PORISMode("DASMode_FTDark")
        self.mdDASMode_FTBias = PORISMode("DASMode_FTBias")
        self.mdDASMode_SimpleBias = PORISMode("DASMode_SimpleBias")
        self.mdDASMode_SimpleDark = PORISMode("DASMode_SimpleDark")
        self.mdDASMode_ShufffingDark = PORISMode("DASMode_ShufffingDark")
        self.mdDASMode_ShufffingBias = PORISMode("DASMode_ShufffingBias")
        self.mdDASMode_ShufffingImage = PORISMode("DASMode_ShufffingImage")
        self.mdDASMode_SimpleCalib = PORISMode("DASMode_SimpleCalib")
        self.cmdDAS_acquire = PORISCmd("DAS_acquire")
        self.mdDASMode_GainCalib = PORISMode("DASMode_GainCalib")
        self.cmdDAS_abort = PORISCmd("DAS_abort")
        self.vlCurrentEllapsed_Range = PORISValueFloat("CurrentEllapsed_Range",0.0,0.0,10000.0)
        self.mdCurrentEllapsedMode_Normal = PORISMode("CurrentEllapsedMode_Normal")
        self.vlCurrentImg_Range = PORISValueFloat("CurrentImg_Range",0.0,0.0,10000.0)
        self.mdCurrentImgMode_Normal = PORISMode("CurrentImgMode_Normal")
        self.vlCurrentPct_Range = PORISValueFloat("CurrentPct_Range",0.0,0.0,100.0)
        self.mdCurrentPctMode_Normal = PORISMode("CurrentPctMode_Normal")
        self.vlOverallPct_Range = PORISValueFloat("OverallPct_Range",0.0,0.0,100.0)
        self.mdOverallPctMode_Normal = PORISMode("OverallPctMode_Normal")
        self.mdProcessMonitorMode_Normal = PORISMode("ProcessMonitorMode_Normal")
        self.mdDASMode_Engineering = PORISMode("DASMode_Engineering")
        self.mdAcquisitionMode_Engineering = PORISMode("AcquisitionMode_Engineering")
        self.mdMultipleExposureMode_Engineering = PORISMode("MultipleExposureMode_Engineering")
        self.mdProcessMonitorMode_Engineering = PORISMode("ProcessMonitorMode_Engineering")
        self.addItem(self.sysDAS)
        self.sysDAS.ident = "OSI-0476"
        self.sysDAS.setXMLName('DAS')
        self.sysDAS.description = ""
        self.addItem(self.sysAcquisition)
        self.sysAcquisition.ident = "OSI-0477"
        self.sysAcquisition.setXMLName('Acquisition')
        self.sysAcquisition.description = ""
        self.sysDAS.addSubsystem(self.sysAcquisition)
        self.addItem(self.prShuffleLines)
        self.prShuffleLines.ident = "OSI-0479"
        self.prShuffleLines.setXMLName('ShuffleLines')
        self.prShuffleLines.description = ""
        self.sysAcquisition.addParam(self.prShuffleLines)
        self.addItem(self.prShiftNumber)
        self.prShiftNumber.ident = "OSI-0480"
        self.prShiftNumber.setXMLName('ShiftNumber')
        self.prShiftNumber.description = ""
        self.sysAcquisition.addParam(self.prShiftNumber)
        self.addItem(self.prExpTime)
        self.prExpTime.ident = "OSI-0487"
        self.prExpTime.setXMLName('ExpTime')
        self.prExpTime.description = ""
        self.sysAcquisition.addParam(self.prExpTime)
        self.addItem(self.sysMultipleExposure)
        self.sysMultipleExposure.ident = "OSI-0488"
        self.sysMultipleExposure.setXMLName('MultipleExposure')
        self.sysMultipleExposure.description = ""
        self.sysAcquisition.addSubsystem(self.sysMultipleExposure)
        self.addItem(self.prnumOfFrames)
        self.prnumOfFrames.ident = "OSI-0489"
        self.prnumOfFrames.setXMLName('numOfFrames')
        self.prnumOfFrames.description = ""
        self.sysMultipleExposure.addParam(self.prnumOfFrames)
        self.addItem(self.prPixelSpeed)
        self.prPixelSpeed.ident = "OSI-0491"
        self.prPixelSpeed.setXMLName('PixelSpeed')
        self.prPixelSpeed.description = ""
        self.sysAcquisition.addParam(self.prPixelSpeed)
        self.addItem(self.sysDetector)
        self.sysDetector.ident = "OSI-0481"
        self.sysDetector.setXMLName('Detector')
        self.sysDetector.description = ""
        self.sysAcquisition.addSubsystem(self.sysDetector)
        self.addItem(self.prCalibGain)
        self.prCalibGain.ident = "DAS-0006"
        self.prCalibGain.setXMLName('CalibGain')
        self.prCalibGain.description = ""
        self.sysAcquisition.addParam(self.prCalibGain)
        self.addItem(self.sysOpenShutter)
        self.sysOpenShutter.ident = "OSI-0499"
        self.sysOpenShutter.setXMLName('OpenShutter')
        self.sysOpenShutter.description = ""
        self.sysDAS.addSubsystem(self.sysOpenShutter)
        self.addItem(self.sysProcessMonitor)
        self.sysProcessMonitor.ident = "DAS-0036"
        self.sysProcessMonitor.setXMLName('ProcessMonitor')
        self.sysProcessMonitor.description = ""
        self.sysDAS.addSubsystem(self.sysProcessMonitor)
        self.addItem(self.prCurrentEllapsed)
        self.prCurrentEllapsed.ident = "DAS-0037"
        self.prCurrentEllapsed.setXMLName('CurrentEllapsed')
        self.prCurrentEllapsed.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentEllapsed)
        self.addItem(self.prCurrentImg)
        self.prCurrentImg.ident = "DAS-0038"
        self.prCurrentImg.setXMLName('CurrentImg')
        self.prCurrentImg.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentImg)
        self.addItem(self.prCurrentPct)
        self.prCurrentPct.ident = "DAS-0039"
        self.prCurrentPct.setXMLName('CurrentPct')
        self.prCurrentPct.description = ""
        self.sysProcessMonitor.addParam(self.prCurrentPct)
        self.addItem(self.prOverallPct)
        self.prOverallPct.ident = "DAS-0040"
        self.prOverallPct.setXMLName('OverallPct')
        self.prOverallPct.description = ""
        self.sysProcessMonitor.addParam(self.prOverallPct)
        self.addItem(self.mdAcquisitionMode_Normal)
        self.mdAcquisitionMode_Normal.ident = "OSI-0406"
        self.mdAcquisitionMode_Normal.setXMLName('Normal')
        self.mdAcquisitionMode_Normal.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Normal)
        self.addItem(self.mdAcquisitionMode_FrameTransfer)
        self.mdAcquisitionMode_FrameTransfer.ident = "OSI-0407"
        self.mdAcquisitionMode_FrameTransfer.setXMLName('FrameTransfer')
        self.mdAcquisitionMode_FrameTransfer.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FrameTransfer)
        self.addItem(self.mdAcquisitionMode_Shuffling)
        self.mdAcquisitionMode_Shuffling.ident = "OSI-0408"
        self.mdAcquisitionMode_Shuffling.setXMLName('Shuffling')
        self.mdAcquisitionMode_Shuffling.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Shuffling)
        self.addItem(self.vlShuffleLines_FullRange)
        self.vlShuffleLines_FullRange.ident = "OSI-0409"
        self.vlShuffleLines_FullRange.setXMLName('FullRange')
        self.vlShuffleLines_FullRange.description = ""
        self.prShuffleLines.addValue(self.vlShuffleLines_FullRange)
        self.addItem(self.mdShuffleLinesMode_Normal)
        self.mdShuffleLinesMode_Normal.ident = "OSI-0410"
        self.mdShuffleLinesMode_Normal.setXMLName('Normal')
        self.mdShuffleLinesMode_Normal.description = ""
        self.prShuffleLines.addMode(self.mdShuffleLinesMode_Normal)
        self.addItem(self.vlShiftNumber_FullRange)
        self.vlShiftNumber_FullRange.ident = "OSI-0411"
        self.vlShiftNumber_FullRange.setXMLName('FullRange')
        self.vlShiftNumber_FullRange.description = ""
        self.prShiftNumber.addValue(self.vlShiftNumber_FullRange)
        self.addItem(self.mdShiftNumberMode_Normal)
        self.mdShiftNumberMode_Normal.ident = "OSI-0412"
        self.mdShiftNumberMode_Normal.setXMLName('Normal')
        self.mdShiftNumberMode_Normal.description = ""
        self.prShiftNumber.addMode(self.mdShiftNumberMode_Normal)
        self.addItem(self.vlExpTime_FullRange)
        self.vlExpTime_FullRange.ident = "OSI-0423"
        self.vlExpTime_FullRange.setXMLName('FullRange')
        self.vlExpTime_FullRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FullRange)
        self.addItem(self.mdExpTimeMode_Normal)
        self.mdExpTimeMode_Normal.ident = "OSI-0424"
        self.mdExpTimeMode_Normal.setXMLName('Normal')
        self.mdExpTimeMode_Normal.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Normal)
        self.addItem(self.mdExpTimeMode_Bias)
        self.mdExpTimeMode_Bias.ident = "OSI-0603"
        self.mdExpTimeMode_Bias.setXMLName('Bias')
        self.mdExpTimeMode_Bias.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_Bias)
        self.addItem(self.vlExpTime_0_0)
        self.vlExpTime_0_0.ident = "OSI-0604"
        self.vlExpTime_0_0.setXMLName('0.0')
        self.vlExpTime_0_0.description = ""
        self.prExpTime.addValue(self.vlExpTime_0_0)
        self.addItem(self.mdExpTimeMode_FT)
        self.mdExpTimeMode_FT.ident = "OSI-0436"
        self.mdExpTimeMode_FT.setXMLName('FT')
        self.mdExpTimeMode_FT.description = ""
        self.prExpTime.addMode(self.mdExpTimeMode_FT)
        self.addItem(self.vlExpTime_FTRange)
        self.vlExpTime_FTRange.ident = "OSI-0437"
        self.vlExpTime_FTRange.setXMLName('FTRange')
        self.vlExpTime_FTRange.description = ""
        self.prExpTime.addValue(self.vlExpTime_FTRange)
        self.addItem(self.mdnumOfFramesMode_Normal)
        self.mdnumOfFramesMode_Normal.ident = "OSI-0425"
        self.mdnumOfFramesMode_Normal.setXMLName('Normal')
        self.mdnumOfFramesMode_Normal.description = ""
        self.prnumOfFrames.addMode(self.mdnumOfFramesMode_Normal)
        self.addItem(self.vlnumOfFrames_FullRange)
        self.vlnumOfFrames_FullRange.ident = "OSI-0426"
        self.vlnumOfFrames_FullRange.setXMLName('FullRange')
        self.vlnumOfFrames_FullRange.description = ""
        self.prnumOfFrames.addValue(self.vlnumOfFrames_FullRange)
        self.addItem(self.mdMultipleExposureMode_On)
        self.mdMultipleExposureMode_On.ident = "OSI-0428"
        self.mdMultipleExposureMode_On.setXMLName('On')
        self.mdMultipleExposureMode_On.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_On)
        self.addItem(self.mdMultipleExposureMode_Single)
        self.mdMultipleExposureMode_Single.ident = "OSI-0427"
        self.mdMultipleExposureMode_Single.setXMLName('Single')
        self.mdMultipleExposureMode_Single.description = ""
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Single)
        self.addItem(self.vlPixelSpeed_SLW)
        self.vlPixelSpeed_SLW.ident = "OSI-0431"
        self.vlPixelSpeed_SLW.setXMLName('SLW')
        self.vlPixelSpeed_SLW.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_SLW)
        self.addItem(self.vlPixelSpeed_MED)
        self.vlPixelSpeed_MED.ident = "OSI-0432"
        self.vlPixelSpeed_MED.setXMLName('MED')
        self.vlPixelSpeed_MED.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_MED)
        self.addItem(self.vlPixelSpeed_FST)
        self.vlPixelSpeed_FST.ident = "OSI-0433"
        self.vlPixelSpeed_FST.setXMLName('FST')
        self.vlPixelSpeed_FST.description = ""
        self.prPixelSpeed.addValue(self.vlPixelSpeed_FST)
        self.addItem(self.mdPixelSpeedMode_All)
        self.mdPixelSpeedMode_All.ident = "OSI-0646"
        self.mdPixelSpeedMode_All.setXMLName('All')
        self.mdPixelSpeedMode_All.description = ""
        self.prPixelSpeed.addMode(self.mdPixelSpeedMode_All)
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
        self.addItem(self.mdAcquisitionMode_FTBias)
        self.mdAcquisitionMode_FTBias.ident = "OSI-0607"
        self.mdAcquisitionMode_FTBias.setXMLName('FTBias')
        self.mdAcquisitionMode_FTBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_FTBias)
        self.addItem(self.mdAcquisitionMode_NormalBias)
        self.mdAcquisitionMode_NormalBias.ident = "OSI-0608"
        self.mdAcquisitionMode_NormalBias.setXMLName('NormalBias')
        self.mdAcquisitionMode_NormalBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalBias)
        self.addItem(self.mdAcquisitionMode_ShufflingBias)
        self.mdAcquisitionMode_ShufflingBias.ident = "OSI-0609"
        self.mdAcquisitionMode_ShufflingBias.setXMLName('ShufflingBias')
        self.mdAcquisitionMode_ShufflingBias.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingBias)
        self.addItem(self.mdAcquisitionMode_NormalSquare)
        self.mdAcquisitionMode_NormalSquare.ident = "OSI-0637"
        self.mdAcquisitionMode_NormalSquare.setXMLName('NormalSquare')
        self.mdAcquisitionMode_NormalSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_NormalSquare)
        self.addItem(self.mdAcquisitionMode_ShufflingSquare)
        self.mdAcquisitionMode_ShufflingSquare.ident = "OSI-0638"
        self.mdAcquisitionMode_ShufflingSquare.setXMLName('ShufflingSquare')
        self.mdAcquisitionMode_ShufflingSquare.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_ShufflingSquare)
        self.addItem(self.mdAcquisitionMode_GainCalib)
        self.mdAcquisitionMode_GainCalib.ident = "DAS-0002"
        self.mdAcquisitionMode_GainCalib.setXMLName('GainCalib')
        self.mdAcquisitionMode_GainCalib.description = ""
        self.sysAcquisition.addMode(self.mdAcquisitionMode_GainCalib)
        self.addItem(self.vlCalibGain_FullRange)
        self.vlCalibGain_FullRange.ident = "DAS-0003"
        self.vlCalibGain_FullRange.setXMLName('FullRange')
        self.vlCalibGain_FullRange.description = ""
        self.prCalibGain.addValue(self.vlCalibGain_FullRange)
        self.addItem(self.mdCalibGainMode_Normal)
        self.mdCalibGainMode_Normal.ident = "DAS-0004"
        self.mdCalibGainMode_Normal.setXMLName('Normal')
        self.mdCalibGainMode_Normal.description = ""
        self.prCalibGain.addMode(self.mdCalibGainMode_Normal)
        self.addItem(self.mdDASMode_SimpleImg)
        self.mdDASMode_SimpleImg.ident = "OSI-0439"
        self.mdDASMode_SimpleImg.setXMLName('SimpleImg')
        self.mdDASMode_SimpleImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleImg)
        self.addItem(self.mdDASMode_SimpleSpec)
        self.mdDASMode_SimpleSpec.ident = "OSI-0455"
        self.mdDASMode_SimpleSpec.setXMLName('SimpleSpec')
        self.mdDASMode_SimpleSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleSpec)
        self.addItem(self.mdDASMode_ShufffingSpec)
        self.mdDASMode_ShufffingSpec.ident = "OSI-0639"
        self.mdDASMode_ShufffingSpec.setXMLName('ShufffingSpec')
        self.mdDASMode_ShufffingSpec.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingSpec)
        self.addItem(self.mdOpenShutterMode_On)
        self.mdOpenShutterMode_On.ident = "OSI-0468"
        self.mdOpenShutterMode_On.setXMLName('On')
        self.mdOpenShutterMode_On.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_On)
        self.addItem(self.mdOpenShutterMode_Off)
        self.mdOpenShutterMode_Off.ident = "OSI-0469"
        self.mdOpenShutterMode_Off.setXMLName('Off')
        self.mdOpenShutterMode_Off.description = ""
        self.sysOpenShutter.addMode(self.mdOpenShutterMode_Off)
        self.addItem(self.mdDASMode_FTImg)
        self.mdDASMode_FTImg.ident = "OSI-0500"
        self.mdDASMode_FTImg.setXMLName('FTImg')
        self.mdDASMode_FTImg.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTImg)
        self.addItem(self.mdDASMode_FTDark)
        self.mdDASMode_FTDark.ident = "OSI-0610"
        self.mdDASMode_FTDark.setXMLName('FTDark')
        self.mdDASMode_FTDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTDark)
        self.addItem(self.mdDASMode_FTBias)
        self.mdDASMode_FTBias.ident = "OSI-0611"
        self.mdDASMode_FTBias.setXMLName('FTBias')
        self.mdDASMode_FTBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_FTBias)
        self.addItem(self.mdDASMode_SimpleBias)
        self.mdDASMode_SimpleBias.ident = "OSI-0613"
        self.mdDASMode_SimpleBias.setXMLName('SimpleBias')
        self.mdDASMode_SimpleBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleBias)
        self.addItem(self.mdDASMode_SimpleDark)
        self.mdDASMode_SimpleDark.ident = "OSI-0614"
        self.mdDASMode_SimpleDark.setXMLName('SimpleDark')
        self.mdDASMode_SimpleDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleDark)
        self.addItem(self.mdDASMode_ShufffingDark)
        self.mdDASMode_ShufffingDark.ident = "OSI-0616"
        self.mdDASMode_ShufffingDark.setXMLName('ShufffingDark')
        self.mdDASMode_ShufffingDark.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingDark)
        self.addItem(self.mdDASMode_ShufffingBias)
        self.mdDASMode_ShufffingBias.ident = "OSI-0617"
        self.mdDASMode_ShufffingBias.setXMLName('ShufffingBias')
        self.mdDASMode_ShufffingBias.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingBias)
        self.addItem(self.mdDASMode_ShufffingImage)
        self.mdDASMode_ShufffingImage.ident = "OSI-0467"
        self.mdDASMode_ShufffingImage.setXMLName('ShufffingImage')
        self.mdDASMode_ShufffingImage.description = ""
        self.sysDAS.addMode(self.mdDASMode_ShufffingImage)
        self.addItem(self.mdDASMode_SimpleCalib)
        self.mdDASMode_SimpleCalib.ident = "DAS-0005"
        self.mdDASMode_SimpleCalib.setXMLName('SimpleCalib')
        self.mdDASMode_SimpleCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_SimpleCalib)
        self.addItem(self.cmdDAS_acquire)
        self.cmdDAS_acquire.setActionName("acquire")
        self.cmdDAS_acquire.setHandlerName("execDAS_acquire")
        self.cmdDAS_acquire.setTracePath("sysDAS.acquire")
        self.cmdDAS_acquire.ident = "DAS-0012"
        self.cmdDAS_acquire.setXMLName('acquire')
        self.cmdDAS_acquire.description = ""
        self.sysDAS.addCommand(self.cmdDAS_acquire)
        self.addItem(self.mdDASMode_GainCalib)
        self.mdDASMode_GainCalib.ident = "DAS-0018"
        self.mdDASMode_GainCalib.setXMLName('GainCalib')
        self.mdDASMode_GainCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_GainCalib)
        self.addItem(self.cmdDAS_abort)
        self.cmdDAS_abort.setActionName("abort")
        self.cmdDAS_abort.setHandlerName("execDAS_abort")
        self.cmdDAS_abort.setTracePath("sysDAS.abort")
        self.cmdDAS_abort.ident = "DAS-0025"
        self.cmdDAS_abort.setXMLName('abort')
        self.cmdDAS_abort.description = ""
        self.sysDAS.addCommand(self.cmdDAS_abort)
        self.addItem(self.vlCurrentEllapsed_Range)
        self.vlCurrentEllapsed_Range.ident = "DAS-0026"
        self.vlCurrentEllapsed_Range.setXMLName('Range')
        self.vlCurrentEllapsed_Range.description = ""
        self.prCurrentEllapsed.addValue(self.vlCurrentEllapsed_Range)
        self.addItem(self.mdCurrentEllapsedMode_Normal)
        self.mdCurrentEllapsedMode_Normal.ident = "DAS-0027"
        self.mdCurrentEllapsedMode_Normal.setXMLName('Normal')
        self.mdCurrentEllapsedMode_Normal.description = ""
        self.prCurrentEllapsed.addMode(self.mdCurrentEllapsedMode_Normal)
        self.addItem(self.vlCurrentImg_Range)
        self.vlCurrentImg_Range.ident = "DAS-0028"
        self.vlCurrentImg_Range.setXMLName('Range')
        self.vlCurrentImg_Range.description = ""
        self.prCurrentImg.addValue(self.vlCurrentImg_Range)
        self.addItem(self.mdCurrentImgMode_Normal)
        self.mdCurrentImgMode_Normal.ident = "DAS-0029"
        self.mdCurrentImgMode_Normal.setXMLName('Normal')
        self.mdCurrentImgMode_Normal.description = ""
        self.prCurrentImg.addMode(self.mdCurrentImgMode_Normal)
        self.addItem(self.vlCurrentPct_Range)
        self.vlCurrentPct_Range.ident = "DAS-0030"
        self.vlCurrentPct_Range.setXMLName('Range')
        self.vlCurrentPct_Range.description = ""
        self.prCurrentPct.addValue(self.vlCurrentPct_Range)
        self.addItem(self.mdCurrentPctMode_Normal)
        self.mdCurrentPctMode_Normal.ident = "DAS-0031"
        self.mdCurrentPctMode_Normal.setXMLName('Normal')
        self.mdCurrentPctMode_Normal.description = ""
        self.prCurrentPct.addMode(self.mdCurrentPctMode_Normal)
        self.addItem(self.vlOverallPct_Range)
        self.vlOverallPct_Range.ident = "DAS-0032"
        self.vlOverallPct_Range.setXMLName('Range')
        self.vlOverallPct_Range.description = ""
        self.prOverallPct.addValue(self.vlOverallPct_Range)
        self.addItem(self.mdOverallPctMode_Normal)
        self.mdOverallPctMode_Normal.ident = "DAS-0033"
        self.mdOverallPctMode_Normal.setXMLName('Normal')
        self.mdOverallPctMode_Normal.description = ""
        self.prOverallPct.addMode(self.mdOverallPctMode_Normal)
        self.addItem(self.mdProcessMonitorMode_Normal)
        self.mdProcessMonitorMode_Normal.ident = "DAS-0034"
        self.mdProcessMonitorMode_Normal.setXMLName('Normal')
        self.mdProcessMonitorMode_Normal.description = ""
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Normal)
        self.addItem(self.mdDASMode_Engineering)
        self.mdDASMode_Engineering.ident = "ENG-1"
        self.mdDASMode_Engineering.setXMLName('Engineering')
        self.mdDASMode_Engineering.description = "DAS engineering mode"
        self.sysDAS.addMode(self.mdDASMode_Engineering)
        self.addItem(self.mdAcquisitionMode_Engineering)
        self.mdAcquisitionMode_Engineering.ident = "ENG-2"
        self.mdAcquisitionMode_Engineering.setXMLName('Engineering')
        self.mdAcquisitionMode_Engineering.description = "Acquisition engineering mode"
        self.sysAcquisition.addMode(self.mdAcquisitionMode_Engineering)
        self.addItem(self.mdMultipleExposureMode_Engineering)
        self.mdMultipleExposureMode_Engineering.ident = "ENG-3"
        self.mdMultipleExposureMode_Engineering.setXMLName('Engineering')
        self.mdMultipleExposureMode_Engineering.description = "MultipleExposure engineering mode"
        self.sysMultipleExposure.addMode(self.mdMultipleExposureMode_Engineering)
        self.addItem(self.mdProcessMonitorMode_Engineering)
        self.mdProcessMonitorMode_Engineering.ident = "ENG-4"
        self.mdProcessMonitorMode_Engineering.setXMLName('Engineering')
        self.mdProcessMonitorMode_Engineering.description = "ProcessMonitor engineering mode"
        self.sysProcessMonitor.addMode(self.mdProcessMonitorMode_Engineering)
        # Marcamos AcquisitionMode_NormalSquare como elegible para DASMode_SimpleImg
        self.mdDASMode_SimpleImg.addSubMode(self.mdAcquisitionMode_NormalSquare)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleSpec
        self.mdDASMode_SimpleSpec.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_ShufffingSpec
        self.mdDASMode_ShufffingSpec.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_FTImg
        self.mdDASMode_FTImg.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_FTDark
        self.mdDASMode_FTDark.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_FTBias como elegible para DASMode_FTBias
        self.mdDASMode_FTBias.addSubMode(self.mdAcquisitionMode_FTBias)
        # Marcamos AcquisitionMode_NormalBias como elegible para DASMode_SimpleBias
        self.mdDASMode_SimpleBias.addSubMode(self.mdAcquisitionMode_NormalBias)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleDark
        self.mdDASMode_SimpleDark.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_ShufffingDark
        self.mdDASMode_ShufffingDark.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_ShufflingBias como elegible para DASMode_ShufffingBias
        self.mdDASMode_ShufffingBias.addSubMode(self.mdAcquisitionMode_ShufflingBias)
        # Marcamos AcquisitionMode_ShufflingSquare como elegible para DASMode_ShufffingImage
        self.mdDASMode_ShufffingImage.addSubMode(self.mdAcquisitionMode_ShufflingSquare)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_SimpleCalib
        self.mdDASMode_SimpleCalib.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_GainCalib como elegible para DASMode_GainCalib
        self.mdDASMode_GainCalib.addSubMode(self.mdAcquisitionMode_GainCalib)
        # Marcamos AcquisitionMode_Normal como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Normal)
        # Marcamos AcquisitionMode_FrameTransfer como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_FrameTransfer)
        # Marcamos AcquisitionMode_Shuffling como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Shuffling)
        # Marcamos AcquisitionMode_FTBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_FTBias)
        # Marcamos AcquisitionMode_NormalBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_NormalBias)
        # Marcamos AcquisitionMode_ShufflingBias como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_ShufflingBias)
        # Marcamos AcquisitionMode_NormalSquare como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_NormalSquare)
        # Marcamos AcquisitionMode_ShufflingSquare como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_ShufflingSquare)
        # Marcamos AcquisitionMode_GainCalib como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_GainCalib)
        # Marcamos AcquisitionMode_Engineering como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdAcquisitionMode_Engineering)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLinesMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShuffleLinesMode_Normal)
        # Marcamos ShuffleLines_FullRange como elegible para ShuffleLinesMode_Normal
        self.mdShuffleLinesMode_Normal.addValue(self.vlShuffleLines_FullRange)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumberMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdShiftNumberMode_Normal)
        # Marcamos ShiftNumber_FullRange como elegible para ShiftNumberMode_Normal
        self.mdShiftNumberMode_Normal.addValue(self.vlShiftNumber_FullRange)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_Normal)
        # Marcamos ExpTimeMode_Bias como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_Bias)
        # Marcamos ExpTimeMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdExpTimeMode_FT)
        # Marcamos ExpTime_FullRange como elegible para ExpTimeMode_Normal
        self.mdExpTimeMode_Normal.addValue(self.vlExpTime_FullRange)
        # Marcamos ExpTime_0_0 como elegible para ExpTimeMode_Bias
        self.mdExpTimeMode_Bias.addValue(self.vlExpTime_0_0)
        # Marcamos ExpTime_FTRange como elegible para ExpTimeMode_FT
        self.mdExpTimeMode_FT.addValue(self.vlExpTime_FTRange)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_On como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_On)
        # Marcamos MultipleExposureMode_Single como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_Single)
        # Marcamos MultipleExposureMode_Engineering como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdMultipleExposureMode_Engineering)
        # Marcamos numOfFramesMode_Normal como elegible para MultipleExposureMode_On
        self.mdMultipleExposureMode_On.addSubMode(self.mdnumOfFramesMode_Normal)
        # Marcamos numOfFramesMode_Normal como elegible para MultipleExposureMode_Engineering
        self.mdMultipleExposureMode_Engineering.addSubMode(self.mdnumOfFramesMode_Normal)
        # Marcamos numOfFrames_FullRange como elegible para numOfFramesMode_Normal
        self.mdnumOfFramesMode_Normal.addValue(self.vlnumOfFrames_FullRange)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeedMode_All como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdPixelSpeedMode_All)
        # Marcamos PixelSpeed_FST como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_FST)
        # Marcamos PixelSpeed_MED como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_MED)
        # Marcamos PixelSpeed_SLW como elegible para PixelSpeedMode_All
        self.mdPixelSpeedMode_All.addValue(self.vlPixelSpeed_SLW)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_Normal
        self.mdAcquisitionMode_Normal.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_FrameTransfer
        self.mdAcquisitionMode_FrameTransfer.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Shuffling
        self.mdAcquisitionMode_Shuffling.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_FTBias
        self.mdAcquisitionMode_FTBias.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_NormalBias
        self.mdAcquisitionMode_NormalBias.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_ShufflingBias
        self.mdAcquisitionMode_ShufflingBias.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos DetectorMode_WindowSq como elegible para AcquisitionMode_NormalSquare
        self.mdAcquisitionMode_NormalSquare.addSubMode(self.mdDetectorMode_WindowSq)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_ShufflingSquare
        self.mdAcquisitionMode_ShufflingSquare.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_FT como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FT)
        # Marcamos DetectorMode_Window como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_Window)
        # Marcamos DetectorMode_FullDetector como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FullDetector)
        # Marcamos DetectorMode_WindowSq como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_WindowSq)
        # Marcamos DetectorMode_FullDetectorSq como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdDetectorMode_FullDetectorSq)
        # Marcamos CalibGainMode_Normal como elegible para AcquisitionMode_GainCalib
        self.mdAcquisitionMode_GainCalib.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGainMode_Normal como elegible para AcquisitionMode_Engineering
        self.mdAcquisitionMode_Engineering.addSubMode(self.mdCalibGainMode_Normal)
        # Marcamos CalibGain_FullRange como elegible para CalibGainMode_Normal
        self.mdCalibGainMode_Normal.addValue(self.vlCalibGain_FullRange)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleImg
        self.mdDASMode_SimpleImg.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleSpec
        self.mdDASMode_SimpleSpec.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_ShufffingSpec
        self.mdDASMode_ShufffingSpec.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_FTImg
        self.mdDASMode_FTImg.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_FTDark
        self.mdDASMode_FTDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_FTBias
        self.mdDASMode_FTBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_SimpleBias
        self.mdDASMode_SimpleBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_SimpleDark
        self.mdDASMode_SimpleDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_ShufffingDark
        self.mdDASMode_ShufffingDark.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_ShufffingBias
        self.mdDASMode_ShufffingBias.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos OpenShutterMode_On como elegible para DASMode_ShufffingImage
        self.mdDASMode_ShufffingImage.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_SimpleCalib
        self.mdDASMode_SimpleCalib.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_GainCalib
        self.mdDASMode_GainCalib.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_On como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdOpenShutterMode_On)
        # Marcamos OpenShutterMode_Off como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdOpenShutterMode_Off)
        # Marcamos ProcessMonitorMode_Normal como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdProcessMonitorMode_Normal)
        # Marcamos ProcessMonitorMode_Engineering como elegible para DASMode_Engineering
        self.mdDASMode_Engineering.addSubMode(self.mdProcessMonitorMode_Engineering)
        # Marcamos CurrentEllapsedMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentEllapsedMode_Normal)
        # Marcamos CurrentEllapsedMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentEllapsedMode_Normal)
        # Marcamos CurrentEllapsed_Range como elegible para CurrentEllapsedMode_Normal
        self.mdCurrentEllapsedMode_Normal.addValue(self.vlCurrentEllapsed_Range)
        # Marcamos CurrentImgMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentImgMode_Normal)
        # Marcamos CurrentImgMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentImgMode_Normal)
        # Marcamos CurrentImg_Range como elegible para CurrentImgMode_Normal
        self.mdCurrentImgMode_Normal.addValue(self.vlCurrentImg_Range)
        # Marcamos CurrentPctMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdCurrentPctMode_Normal)
        # Marcamos CurrentPctMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdCurrentPctMode_Normal)
        # Marcamos CurrentPct_Range como elegible para CurrentPctMode_Normal
        self.mdCurrentPctMode_Normal.addValue(self.vlCurrentPct_Range)
        # Marcamos OverallPctMode_Normal como elegible para ProcessMonitorMode_Normal
        self.mdProcessMonitorMode_Normal.addSubMode(self.mdOverallPctMode_Normal)
        # Marcamos OverallPctMode_Normal como elegible para ProcessMonitorMode_Engineering
        self.mdProcessMonitorMode_Engineering.addSubMode(self.mdOverallPctMode_Normal)
        # Marcamos OverallPct_Range como elegible para OverallPctMode_Normal
        self.mdOverallPctMode_Normal.addValue(self.vlOverallPct_Range)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## DASMode 
    def get_DASMode(self)-> PORISMode:
        return self.sysDAS.getSelectedMode()

    def set_DASMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDAS.selectMode(mode)


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


    ## prParam Acquisition 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## prParam Acquisition 

    # ExpTimeDouble  
    def get_ExpTimeDouble(self)-> float :
        v = self.prExpTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExpTimeDouble(self, data: float)-> float :
        return self.prExpTime.getSelectedValue().setData(data)


    ## MultipleExposureMode 
    def get_MultipleExposureMode(self)-> PORISMode:
        return self.sysMultipleExposure.getSelectedMode()

    def set_MultipleExposureMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMultipleExposure.selectMode(mode)


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


    ## prParam MultipleExposure 

    # numOfFramesDouble  
    def get_numOfFramesDouble(self)-> float :
        v = self.prnumOfFrames.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_numOfFramesDouble(self, data: float)-> float :
        return self.prnumOfFrames.getSelectedValue().setData(data)


    ## prParam PixelSpeed 

    # PixelSpeed
    def get_PixelSpeed(self)-> PORISValue :
        return self.prPixelSpeed.getSelectedValue()

    def set_PixelSpeed(self, value: PORISValue)-> PORISValue :
        return self.prPixelSpeed.setValue(value)


    ## PixelSpeedMode 
    def get_PixelSpeedMode(self)-> PORISMode:
        return self.prPixelSpeed.getSelectedMode()

    def set_PixelSpeedMode(self, mode: PORISMode)-> PORISMode :
        return self.prPixelSpeed.selectMode(mode)


    ## DetectorMode 
    def get_DetectorMode(self)-> PORISMode:
        return self.sysDetector.getSelectedMode()

    def set_DetectorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDetector.selectMode(mode)


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


    ## prParam Acquisition 

    # CalibGainDouble  
    def get_CalibGainDouble(self)-> float :
        v = self.prCalibGain.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CalibGainDouble(self, data: float)-> float :
        return self.prCalibGain.getSelectedValue().setData(data)


    ## OpenShutterMode 
    def get_OpenShutterMode(self)-> PORISMode:
        return self.sysOpenShutter.getSelectedMode()

    def set_OpenShutterMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOpenShutter.selectMode(mode)


    ## ProcessMonitorMode 
    def get_ProcessMonitorMode(self)-> PORISMode:
        return self.sysProcessMonitor.getSelectedMode()

    def set_ProcessMonitorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysProcessMonitor.selectMode(mode)


    ## prParam CurrentEllapsed 

    # CurrentEllapsed
    def get_CurrentEllapsed(self)-> PORISValue :
        return self.prCurrentEllapsed.getSelectedValue()

    def set_CurrentEllapsed(self, value: PORISValue)-> PORISValue :
        return self.prCurrentEllapsed.setValue(value)


    ## CurrentEllapsedMode 
    def get_CurrentEllapsedMode(self)-> PORISMode:
        return self.prCurrentEllapsed.getSelectedMode()

    def set_CurrentEllapsedMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentEllapsed.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentEllapsedDouble  
    def get_CurrentEllapsedDouble(self)-> float :
        v = self.prCurrentEllapsed.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentEllapsedDouble(self, data: float)-> float :
        return self.prCurrentEllapsed.getSelectedValue().setData(data)


    ## prParam CurrentImg 

    # CurrentImg
    def get_CurrentImg(self)-> PORISValue :
        return self.prCurrentImg.getSelectedValue()

    def set_CurrentImg(self, value: PORISValue)-> PORISValue :
        return self.prCurrentImg.setValue(value)


    ## CurrentImgMode 
    def get_CurrentImgMode(self)-> PORISMode:
        return self.prCurrentImg.getSelectedMode()

    def set_CurrentImgMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentImg.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentImgDouble  
    def get_CurrentImgDouble(self)-> float :
        v = self.prCurrentImg.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentImgDouble(self, data: float)-> float :
        return self.prCurrentImg.getSelectedValue().setData(data)


    ## prParam CurrentPct 

    # CurrentPct
    def get_CurrentPct(self)-> PORISValue :
        return self.prCurrentPct.getSelectedValue()

    def set_CurrentPct(self, value: PORISValue)-> PORISValue :
        return self.prCurrentPct.setValue(value)


    ## CurrentPctMode 
    def get_CurrentPctMode(self)-> PORISMode:
        return self.prCurrentPct.getSelectedMode()

    def set_CurrentPctMode(self, mode: PORISMode)-> PORISMode :
        return self.prCurrentPct.selectMode(mode)


    ## prParam ProcessMonitor 

    # CurrentPctDouble  
    def get_CurrentPctDouble(self)-> float :
        v = self.prCurrentPct.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CurrentPctDouble(self, data: float)-> float :
        return self.prCurrentPct.getSelectedValue().setData(data)


    ## prParam OverallPct 

    # OverallPct
    def get_OverallPct(self)-> PORISValue :
        return self.prOverallPct.getSelectedValue()

    def set_OverallPct(self, value: PORISValue)-> PORISValue :
        return self.prOverallPct.setValue(value)


    ## OverallPctMode 
    def get_OverallPctMode(self)-> PORISMode:
        return self.prOverallPct.getSelectedMode()

    def set_OverallPctMode(self, mode: PORISMode)-> PORISMode :
        return self.prOverallPct.selectMode(mode)


    ## prParam ProcessMonitor 

    # OverallPctDouble  
    def get_OverallPctDouble(self)-> float :
        v = self.prOverallPct.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_OverallPctDouble(self, data: float)-> float :
        return self.prOverallPct.getSelectedValue().setData(data)


    ## Action trigger DAS_acquire ##
    def execDAS_acquire(self, *args, **kwargs) -> bool:
        return self.cmdDAS_acquire.defaultExecute(*args, **kwargs)


    ## Action trigger DAS_abort ##
    def execDAS_abort(self, *args, **kwargs) -> bool:
        return self.cmdDAS_abort.defaultExecute(*args, **kwargs)

