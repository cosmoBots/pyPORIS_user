from PORIS import *

class osirisPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysOsiris = PORISSys("Osiris")
        self.setRoot(self.sysOsiris)
        self.sysObservingModes = PORISSys("ObservingModes")
        self.sysAcquisitionModes = PORISSys("AcquisitionModes")
        self.sysPreOptics = PORISSys("PreOptics")
        self.sysDAS = PORISSys("DAS")
        self.sysFPE = PORISSys("FPE")
        self.mdOsirisMode_Imaging = PORISMode("OsirisMode_Imaging")
        self.mdOsirisMode_Spectroscopy = PORISMode("OsirisMode_Spectroscopy")
        self.mdOsirisMode_Calibration = PORISMode("OsirisMode_Calibration")
        self.mdAcquisitionModesMode_aBBI = PORISMode("AcquisitionModesMode_aBBI")
        self.mdAcquisitionModesMode_aTFI = PORISMode("AcquisitionModesMode_aTFI")
        self.mdAcquisitionModesMode_aLSSpec = PORISMode("AcquisitionModesMode_aLSSpec")
        self.mdAcquisitionModesMode_aMOS = PORISMode("AcquisitionModesMode_aMOS")
        self.mdAcquisitionModesMode_aFastBBI = PORISMode("AcquisitionModesMode_aFastBBI")
        self.mdAcquisitionModesMode_aFrTrBBI = PORISMode("AcquisitionModesMode_aFrTrBBI")
        self.mdAcquisitionModesMode_aFastLSSpec = PORISMode("AcquisitionModesMode_aFastLSSpec")
        self.mdPreOpticsMode_NoDispersion = PORISMode("PreOpticsMode_NoDispersion")
        self.mdPreOpticsMode_RTF = PORISMode("PreOpticsMode_RTF")
        self.mdPreOpticsMode_GrismR = PORISMode("PreOpticsMode_GrismR")
        self.mdPreOpticsMode_BTF = PORISMode("PreOpticsMode_BTF")
        self.mdPreOpticsMode_GrismB = PORISMode("PreOpticsMode_GrismB")
        self.mdPreOpticsMode_GrismBMOS = PORISMode("PreOpticsMode_GrismBMOS")
        self.mdPreOpticsMode_RTFCalib = PORISMode("PreOpticsMode_RTFCalib")
        self.mdPreOpticsMode_BTFCalib = PORISMode("PreOpticsMode_BTFCalib")
        self.mdAcquisitionModesMode_aFastTFImage = PORISMode("AcquisitionModesMode_aFastTFImage")
        self.mdAcquisitionModesMode_aFrTrTFI = PORISMode("AcquisitionModesMode_aFrTrTFI")
        self.mdAcquisitionModesMode_aBias = PORISMode("AcquisitionModesMode_aBias")
        self.mdAcquisitionModesMode_aDark = PORISMode("AcquisitionModesMode_aDark")
        self.mdAcquisitionModesMode_aDomeFlat = PORISMode("AcquisitionModesMode_aDomeFlat")
        self.mdAcquisitionModesMode_aSkyFlat = PORISMode("AcquisitionModesMode_aSkyFlat")
        self.mdAcquisitionModesMode_aSpectralFlat = PORISMode("AcquisitionModesMode_aSpectralFlat")
        self.mdAcquisitionModesMode_aCalibLamp = PORISMode("AcquisitionModesMode_aCalibLamp")
        self.mdAcquisitionModesMode_aTFCalib = PORISMode("AcquisitionModesMode_aTFCalib")
        self.mdDASMode_SimpleImg = PORISMode("DASMode_SimpleImg")
        self.mdDASMode_SimpleSpec = PORISMode("DASMode_SimpleSpec")
        self.mdDASMode_ShufffingSpec = PORISMode("DASMode_ShufffingSpec")
        self.mdDASMode_FTImg = PORISMode("DASMode_FTImg")
        self.mdDASMode_FTDark = PORISMode("DASMode_FTDark")
        self.mdDASMode_FTBias = PORISMode("DASMode_FTBias")
        self.mdDASMode_SimpleBias = PORISMode("DASMode_SimpleBias")
        self.mdDASMode_SimpleDark = PORISMode("DASMode_SimpleDark")
        self.mdDASMode_ShufffingDark = PORISMode("DASMode_ShufffingDark")
        self.mdDASMode_ShufffingBias = PORISMode("DASMode_ShufffingBias")
        self.mdDASMode_ShufffingImage = PORISMode("DASMode_ShufffingImage")
        self.mdDASMode_SimpleCalib = PORISMode("DASMode_SimpleCalib")
        self.mdDASMode_GainCalib = PORISMode("DASMode_GainCalib")
        self.mdAcquisitionModesMode_Throughslit = PORISMode("AcquisitionModesMode_Throughslit")
        self.mdFPEMode_NoFPE = PORISMode("FPEMode_NoFPE")
        self.mdFPEMode_MOSmask = PORISMode("FPEMode_MOSmask")
        self.mdFPEMode_FastPhotometryMask = PORISMode("FPEMode_FastPhotometryMask")
        self.mdFPEMode_FrameTransferMask = PORISMode("FPEMode_FrameTransferMask")
        self.mdFPEMode_LSMask = PORISMode("FPEMode_LSMask")
        self.mdObservingModesMode_BBI = PORISMode("ObservingModesMode_BBI")
        self.mdObservingModesMode_TFI = PORISMode("ObservingModesMode_TFI")
        self.mdObservingModesMode_LSSpec = PORISMode("ObservingModesMode_LSSpec")
        self.mdObservingModesMode_MOS = PORISMode("ObservingModesMode_MOS")
        self.mdObservingModesMode_FastBBI = PORISMode("ObservingModesMode_FastBBI")
        self.mdObservingModesMode_FrTrBBI = PORISMode("ObservingModesMode_FrTrBBI")
        self.mdObservingModesMode_FastLSSpec = PORISMode("ObservingModesMode_FastLSSpec")
        self.mdObservingModesMode_FastTFImage = PORISMode("ObservingModesMode_FastTFImage")
        self.mdObservingModesMode_FrTrTFI = PORISMode("ObservingModesMode_FrTrTFI")
        self.mdObservingModesMode_Bias = PORISMode("ObservingModesMode_Bias")
        self.mdObservingModesMode_Dark = PORISMode("ObservingModesMode_Dark")
        self.mdObservingModesMode_DomeFlat = PORISMode("ObservingModesMode_DomeFlat")
        self.mdObservingModesMode_SkyFlat = PORISMode("ObservingModesMode_SkyFlat")
        self.mdObservingModesMode_SpectralFlat = PORISMode("ObservingModesMode_SpectralFlat")
        self.mdObservingModesMode_CalibLamp = PORISMode("ObservingModesMode_CalibLamp")
        self.mdObservingModesMode_TFCalib = PORISMode("ObservingModesMode_TFCalib")
        self.mdOsirisMode_Engineering = PORISMode("OsirisMode_Engineering")
        self.mdObservingModesMode_Engineering = PORISMode("ObservingModesMode_Engineering")
        self.mdAcquisitionModesMode_Engineering = PORISMode("AcquisitionModesMode_Engineering")
        self.addItem(self.sysOsiris)
        self.sysOsiris.ident = "OSI-0474"
        self.sysOsiris.setXMLName('Osiris')
        self.sysOsiris.description = ""
        self.addItem(self.sysObservingModes)
        self.sysObservingModes.ident = "OSI-0733"
        self.sysObservingModes.setXMLName('ObservingModes')
        self.sysObservingModes.description = ""
        self.sysOsiris.addSubsystem(self.sysObservingModes)
        self.addItem(self.sysAcquisitionModes)
        self.sysAcquisitionModes.ident = "OSI-0133"
        self.sysAcquisitionModes.setXMLName('AcquisitionModes')
        self.sysAcquisitionModes.description = ""
        self.sysObservingModes.addSubsystem(self.sysAcquisitionModes)
        self.addItem(self.sysPreOptics)
        self.sysPreOptics.ident = "OSI-0136"
        self.sysPreOptics.setXMLName('PreOptics')
        self.sysPreOptics.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysPreOptics)
        self.addItem(self.sysDAS)
        self.sysDAS.ident = "OSI-0476"
        self.sysDAS.setXMLName('DAS')
        self.sysDAS.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysDAS)
        self.addItem(self.sysFPE)
        self.sysFPE.ident = "FP-0006"
        self.sysFPE.setXMLName('FPE')
        self.sysFPE.description = ""
        self.sysAcquisitionModes.addSubsystem(self.sysFPE)
        self.addItem(self.mdOsirisMode_Imaging)
        self.mdOsirisMode_Imaging.ident = "OSI-0471"
        self.mdOsirisMode_Imaging.setXMLName('Imaging')
        self.mdOsirisMode_Imaging.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Imaging)
        self.addItem(self.mdOsirisMode_Spectroscopy)
        self.mdOsirisMode_Spectroscopy.ident = "OSI-0472"
        self.mdOsirisMode_Spectroscopy.setXMLName('Spectroscopy')
        self.mdOsirisMode_Spectroscopy.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Spectroscopy)
        self.addItem(self.mdOsirisMode_Calibration)
        self.mdOsirisMode_Calibration.ident = "OSI-0473"
        self.mdOsirisMode_Calibration.setXMLName('Calibration')
        self.mdOsirisMode_Calibration.description = ""
        self.sysOsiris.addMode(self.mdOsirisMode_Calibration)
        self.addItem(self.mdAcquisitionModesMode_aBBI)
        self.mdAcquisitionModesMode_aBBI.ident = "OSI-0001"
        self.mdAcquisitionModesMode_aBBI.setXMLName('aBBI')
        self.mdAcquisitionModesMode_aBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBBI)
        self.addItem(self.mdAcquisitionModesMode_aTFI)
        self.mdAcquisitionModesMode_aTFI.ident = "OSI-0002"
        self.mdAcquisitionModesMode_aTFI.setXMLName('aTFI')
        self.mdAcquisitionModesMode_aTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFI)
        self.addItem(self.mdAcquisitionModesMode_aLSSpec)
        self.mdAcquisitionModesMode_aLSSpec.ident = "OSI-0003"
        self.mdAcquisitionModesMode_aLSSpec.setXMLName('aLSSpec')
        self.mdAcquisitionModesMode_aLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aLSSpec)
        self.addItem(self.mdAcquisitionModesMode_aMOS)
        self.mdAcquisitionModesMode_aMOS.ident = "OSI-0004"
        self.mdAcquisitionModesMode_aMOS.setXMLName('aMOS')
        self.mdAcquisitionModesMode_aMOS.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aMOS)
        self.addItem(self.mdAcquisitionModesMode_aFastBBI)
        self.mdAcquisitionModesMode_aFastBBI.ident = "OSI-0005"
        self.mdAcquisitionModesMode_aFastBBI.setXMLName('aFastBBI')
        self.mdAcquisitionModesMode_aFastBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastBBI)
        self.addItem(self.mdAcquisitionModesMode_aFrTrBBI)
        self.mdAcquisitionModesMode_aFrTrBBI.ident = "OSI-0006"
        self.mdAcquisitionModesMode_aFrTrBBI.setXMLName('aFrTrBBI')
        self.mdAcquisitionModesMode_aFrTrBBI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrBBI)
        self.addItem(self.mdAcquisitionModesMode_aFastLSSpec)
        self.mdAcquisitionModesMode_aFastLSSpec.ident = "OSI-0007"
        self.mdAcquisitionModesMode_aFastLSSpec.setXMLName('aFastLSSpec')
        self.mdAcquisitionModesMode_aFastLSSpec.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastLSSpec)
        self.addItem(self.mdPreOpticsMode_NoDispersion)
        self.mdPreOpticsMode_NoDispersion.ident = "OSI-0014"
        self.mdPreOpticsMode_NoDispersion.setXMLName('NoDispersion')
        self.mdPreOpticsMode_NoDispersion.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_NoDispersion)
        self.addItem(self.mdPreOpticsMode_RTF)
        self.mdPreOpticsMode_RTF.ident = "OSI-0015"
        self.mdPreOpticsMode_RTF.setXMLName('RTF')
        self.mdPreOpticsMode_RTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTF)
        self.addItem(self.mdPreOpticsMode_GrismR)
        self.mdPreOpticsMode_GrismR.ident = "OSI-0146"
        self.mdPreOpticsMode_GrismR.setXMLName('GrismR')
        self.mdPreOpticsMode_GrismR.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismR)
        self.addItem(self.mdPreOpticsMode_BTF)
        self.mdPreOpticsMode_BTF.ident = "OSI-0016"
        self.mdPreOpticsMode_BTF.setXMLName('BTF')
        self.mdPreOpticsMode_BTF.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTF)
        self.addItem(self.mdPreOpticsMode_GrismB)
        self.mdPreOpticsMode_GrismB.ident = "OSI-0394"
        self.mdPreOpticsMode_GrismB.setXMLName('GrismB')
        self.mdPreOpticsMode_GrismB.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismB)
        self.addItem(self.mdPreOpticsMode_GrismBMOS)
        self.mdPreOpticsMode_GrismBMOS.ident = "OSI-0501"
        self.mdPreOpticsMode_GrismBMOS.setXMLName('GrismBMOS')
        self.mdPreOpticsMode_GrismBMOS.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_GrismBMOS)
        self.addItem(self.mdPreOpticsMode_RTFCalib)
        self.mdPreOpticsMode_RTFCalib.ident = "OP-0105"
        self.mdPreOpticsMode_RTFCalib.setXMLName('RTFCalib')
        self.mdPreOpticsMode_RTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_RTFCalib)
        self.addItem(self.mdPreOpticsMode_BTFCalib)
        self.mdPreOpticsMode_BTFCalib.ident = "OP-0106"
        self.mdPreOpticsMode_BTFCalib.setXMLName('BTFCalib')
        self.mdPreOpticsMode_BTFCalib.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_BTFCalib)
        self.addItem(self.mdAcquisitionModesMode_aFastTFImage)
        self.mdAcquisitionModesMode_aFastTFImage.ident = "OSI-0395"
        self.mdAcquisitionModesMode_aFastTFImage.setXMLName('aFastTFImage')
        self.mdAcquisitionModesMode_aFastTFImage.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFastTFImage)
        self.addItem(self.mdAcquisitionModesMode_aFrTrTFI)
        self.mdAcquisitionModesMode_aFrTrTFI.ident = "OSI-0396"
        self.mdAcquisitionModesMode_aFrTrTFI.setXMLName('aFrTrTFI')
        self.mdAcquisitionModesMode_aFrTrTFI.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aFrTrTFI)
        self.addItem(self.mdAcquisitionModesMode_aBias)
        self.mdAcquisitionModesMode_aBias.ident = "OSI-0397"
        self.mdAcquisitionModesMode_aBias.setXMLName('aBias')
        self.mdAcquisitionModesMode_aBias.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aBias)
        self.addItem(self.mdAcquisitionModesMode_aDark)
        self.mdAcquisitionModesMode_aDark.ident = "OSI-0398"
        self.mdAcquisitionModesMode_aDark.setXMLName('aDark')
        self.mdAcquisitionModesMode_aDark.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDark)
        self.addItem(self.mdAcquisitionModesMode_aDomeFlat)
        self.mdAcquisitionModesMode_aDomeFlat.ident = "OSI-0399"
        self.mdAcquisitionModesMode_aDomeFlat.setXMLName('aDomeFlat')
        self.mdAcquisitionModesMode_aDomeFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aDomeFlat)
        self.addItem(self.mdAcquisitionModesMode_aSkyFlat)
        self.mdAcquisitionModesMode_aSkyFlat.ident = "OSI-0400"
        self.mdAcquisitionModesMode_aSkyFlat.setXMLName('aSkyFlat')
        self.mdAcquisitionModesMode_aSkyFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSkyFlat)
        self.addItem(self.mdAcquisitionModesMode_aSpectralFlat)
        self.mdAcquisitionModesMode_aSpectralFlat.ident = "OSI-0401"
        self.mdAcquisitionModesMode_aSpectralFlat.setXMLName('aSpectralFlat')
        self.mdAcquisitionModesMode_aSpectralFlat.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aSpectralFlat)
        self.addItem(self.mdAcquisitionModesMode_aCalibLamp)
        self.mdAcquisitionModesMode_aCalibLamp.ident = "OSI-0402"
        self.mdAcquisitionModesMode_aCalibLamp.setXMLName('aCalibLamp')
        self.mdAcquisitionModesMode_aCalibLamp.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aCalibLamp)
        self.addItem(self.mdAcquisitionModesMode_aTFCalib)
        self.mdAcquisitionModesMode_aTFCalib.ident = "OSI-0403"
        self.mdAcquisitionModesMode_aTFCalib.setXMLName('aTFCalib')
        self.mdAcquisitionModesMode_aTFCalib.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_aTFCalib)
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
        self.addItem(self.mdDASMode_GainCalib)
        self.mdDASMode_GainCalib.ident = "DAS-0018"
        self.mdDASMode_GainCalib.setXMLName('GainCalib')
        self.mdDASMode_GainCalib.description = ""
        self.sysDAS.addMode(self.mdDASMode_GainCalib)
        self.addItem(self.mdAcquisitionModesMode_Throughslit)
        self.mdAcquisitionModesMode_Throughslit.ident = "OSI-0772"
        self.mdAcquisitionModesMode_Throughslit.setXMLName('Throughslit')
        self.mdAcquisitionModesMode_Throughslit.description = ""
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Throughslit)
        self.addItem(self.mdFPEMode_NoFPE)
        self.mdFPEMode_NoFPE.ident = "OSI-0116"
        self.mdFPEMode_NoFPE.setXMLName('NoFPE')
        self.mdFPEMode_NoFPE.description = ""
        self.sysFPE.addMode(self.mdFPEMode_NoFPE)
        self.addItem(self.mdFPEMode_MOSmask)
        self.mdFPEMode_MOSmask.ident = "OSI-0130"
        self.mdFPEMode_MOSmask.setXMLName('MOSmask')
        self.mdFPEMode_MOSmask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_MOSmask)
        self.addItem(self.mdFPEMode_FastPhotometryMask)
        self.mdFPEMode_FastPhotometryMask.ident = "OSI-0131"
        self.mdFPEMode_FastPhotometryMask.setXMLName('FastPhotometryMask')
        self.mdFPEMode_FastPhotometryMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FastPhotometryMask)
        self.addItem(self.mdFPEMode_FrameTransferMask)
        self.mdFPEMode_FrameTransferMask.ident = "OSI-0132"
        self.mdFPEMode_FrameTransferMask.setXMLName('FrameTransferMask')
        self.mdFPEMode_FrameTransferMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_FrameTransferMask)
        self.addItem(self.mdFPEMode_LSMask)
        self.mdFPEMode_LSMask.ident = "OSI-0142"
        self.mdFPEMode_LSMask.setXMLName('LSMask')
        self.mdFPEMode_LSMask.description = ""
        self.sysFPE.addMode(self.mdFPEMode_LSMask)
        self.addItem(self.mdObservingModesMode_BBI)
        self.mdObservingModesMode_BBI.ident = "OSI-0717"
        self.mdObservingModesMode_BBI.setXMLName('BBI')
        self.mdObservingModesMode_BBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_BBI)
        self.addItem(self.mdObservingModesMode_TFI)
        self.mdObservingModesMode_TFI.ident = "OSI-0718"
        self.mdObservingModesMode_TFI.setXMLName('TFI')
        self.mdObservingModesMode_TFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFI)
        self.addItem(self.mdObservingModesMode_LSSpec)
        self.mdObservingModesMode_LSSpec.ident = "OSI-0719"
        self.mdObservingModesMode_LSSpec.setXMLName('LSSpec')
        self.mdObservingModesMode_LSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_LSSpec)
        self.addItem(self.mdObservingModesMode_MOS)
        self.mdObservingModesMode_MOS.ident = "OSI-0720"
        self.mdObservingModesMode_MOS.setXMLName('MOS')
        self.mdObservingModesMode_MOS.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_MOS)
        self.addItem(self.mdObservingModesMode_FastBBI)
        self.mdObservingModesMode_FastBBI.ident = "OSI-0721"
        self.mdObservingModesMode_FastBBI.setXMLName('FastBBI')
        self.mdObservingModesMode_FastBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastBBI)
        self.addItem(self.mdObservingModesMode_FrTrBBI)
        self.mdObservingModesMode_FrTrBBI.ident = "OSI-0722"
        self.mdObservingModesMode_FrTrBBI.setXMLName('FrTrBBI')
        self.mdObservingModesMode_FrTrBBI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrBBI)
        self.addItem(self.mdObservingModesMode_FastLSSpec)
        self.mdObservingModesMode_FastLSSpec.ident = "OSI-0723"
        self.mdObservingModesMode_FastLSSpec.setXMLName('FastLSSpec')
        self.mdObservingModesMode_FastLSSpec.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastLSSpec)
        self.addItem(self.mdObservingModesMode_FastTFImage)
        self.mdObservingModesMode_FastTFImage.ident = "OSI-0724"
        self.mdObservingModesMode_FastTFImage.setXMLName('FastTFImage')
        self.mdObservingModesMode_FastTFImage.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FastTFImage)
        self.addItem(self.mdObservingModesMode_FrTrTFI)
        self.mdObservingModesMode_FrTrTFI.ident = "OSI-0725"
        self.mdObservingModesMode_FrTrTFI.setXMLName('FrTrTFI')
        self.mdObservingModesMode_FrTrTFI.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_FrTrTFI)
        self.addItem(self.mdObservingModesMode_Bias)
        self.mdObservingModesMode_Bias.ident = "OSI-0726"
        self.mdObservingModesMode_Bias.setXMLName('Bias')
        self.mdObservingModesMode_Bias.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Bias)
        self.addItem(self.mdObservingModesMode_Dark)
        self.mdObservingModesMode_Dark.ident = "OSI-0727"
        self.mdObservingModesMode_Dark.setXMLName('Dark')
        self.mdObservingModesMode_Dark.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_Dark)
        self.addItem(self.mdObservingModesMode_DomeFlat)
        self.mdObservingModesMode_DomeFlat.ident = "OSI-0728"
        self.mdObservingModesMode_DomeFlat.setXMLName('DomeFlat')
        self.mdObservingModesMode_DomeFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_DomeFlat)
        self.addItem(self.mdObservingModesMode_SkyFlat)
        self.mdObservingModesMode_SkyFlat.ident = "OSI-0729"
        self.mdObservingModesMode_SkyFlat.setXMLName('SkyFlat')
        self.mdObservingModesMode_SkyFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SkyFlat)
        self.addItem(self.mdObservingModesMode_SpectralFlat)
        self.mdObservingModesMode_SpectralFlat.ident = "OSI-0730"
        self.mdObservingModesMode_SpectralFlat.setXMLName('SpectralFlat')
        self.mdObservingModesMode_SpectralFlat.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_SpectralFlat)
        self.addItem(self.mdObservingModesMode_CalibLamp)
        self.mdObservingModesMode_CalibLamp.ident = "OSI-0731"
        self.mdObservingModesMode_CalibLamp.setXMLName('CalibLamp')
        self.mdObservingModesMode_CalibLamp.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_CalibLamp)
        self.addItem(self.mdObservingModesMode_TFCalib)
        self.mdObservingModesMode_TFCalib.ident = "OSI-0732"
        self.mdObservingModesMode_TFCalib.setXMLName('TFCalib')
        self.mdObservingModesMode_TFCalib.description = ""
        self.sysObservingModes.addMode(self.mdObservingModesMode_TFCalib)
        self.addItem(self.mdOsirisMode_Engineering)
        self.mdOsirisMode_Engineering.ident = "ENG-1"
        self.mdOsirisMode_Engineering.setXMLName('Engineering')
        self.mdOsirisMode_Engineering.description = "Osiris_engineering_mode"
        self.sysOsiris.addMode(self.mdOsirisMode_Engineering)
        self.addItem(self.mdObservingModesMode_Engineering)
        self.mdObservingModesMode_Engineering.ident = "ENG-2"
        self.mdObservingModesMode_Engineering.setXMLName('Engineering')
        self.mdObservingModesMode_Engineering.description = "ObservingModes_engineering_mode"
        self.sysObservingModes.addMode(self.mdObservingModesMode_Engineering)
        self.addItem(self.mdAcquisitionModesMode_Engineering)
        self.mdAcquisitionModesMode_Engineering.ident = "ENG-3"
        self.mdAcquisitionModesMode_Engineering.setXMLName('Engineering')
        self.mdAcquisitionModesMode_Engineering.description = "AcquisitionModes_engineering_mode"
        self.sysAcquisitionModes.addMode(self.mdAcquisitionModesMode_Engineering)
        # Marcamos ObservingModesMode_FastBBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FastBBI)
        # Marcamos ObservingModesMode_TFI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_TFI)
        # Marcamos ObservingModesMode_BBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_BBI)
        # Marcamos ObservingModesMode_FrTrTFI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FrTrTFI)
        # Marcamos ObservingModesMode_FastTFImage como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FastTFImage)
        # Marcamos ObservingModesMode_FrTrBBI como elegible para OsirisMode_Imaging
        self.mdOsirisMode_Imaging.addSubMode(self.mdObservingModesMode_FrTrBBI)
        # Marcamos ObservingModesMode_FastLSSpec como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_FastLSSpec)
        # Marcamos ObservingModesMode_MOS como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_MOS)
        # Marcamos ObservingModesMode_LSSpec como elegible para OsirisMode_Spectroscopy
        self.mdOsirisMode_Spectroscopy.addSubMode(self.mdObservingModesMode_LSSpec)
        # Marcamos ObservingModesMode_CalibLamp como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_CalibLamp)
        # Marcamos ObservingModesMode_TFCalib como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_TFCalib)
        # Marcamos ObservingModesMode_SkyFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_SkyFlat)
        # Marcamos ObservingModesMode_SpectralFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_SpectralFlat)
        # Marcamos ObservingModesMode_Bias como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_Bias)
        # Marcamos ObservingModesMode_Dark como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_Dark)
        # Marcamos ObservingModesMode_DomeFlat como elegible para OsirisMode_Calibration
        self.mdOsirisMode_Calibration.addSubMode(self.mdObservingModesMode_DomeFlat)
        # Marcamos ObservingModesMode_BBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_BBI)
        # Marcamos ObservingModesMode_TFI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_TFI)
        # Marcamos ObservingModesMode_LSSpec como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_LSSpec)
        # Marcamos ObservingModesMode_MOS como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_MOS)
        # Marcamos ObservingModesMode_FastBBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastBBI)
        # Marcamos ObservingModesMode_FrTrBBI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FrTrBBI)
        # Marcamos ObservingModesMode_FastLSSpec como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastLSSpec)
        # Marcamos ObservingModesMode_FastTFImage como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FastTFImage)
        # Marcamos ObservingModesMode_FrTrTFI como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_FrTrTFI)
        # Marcamos ObservingModesMode_Bias como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Bias)
        # Marcamos ObservingModesMode_Dark como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Dark)
        # Marcamos ObservingModesMode_DomeFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_DomeFlat)
        # Marcamos ObservingModesMode_SkyFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_SkyFlat)
        # Marcamos ObservingModesMode_SpectralFlat como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_SpectralFlat)
        # Marcamos ObservingModesMode_CalibLamp como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_CalibLamp)
        # Marcamos ObservingModesMode_TFCalib como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_TFCalib)
        # Marcamos ObservingModesMode_Engineering como elegible para OsirisMode_Engineering
        self.mdOsirisMode_Engineering.addSubMode(self.mdObservingModesMode_Engineering)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_BBI
        self.mdObservingModesMode_BBI.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_aTFI como elegible para ObservingModesMode_TFI
        self.mdObservingModesMode_TFI.addSubMode(self.mdAcquisitionModesMode_aTFI)
        # Marcamos AcquisitionModesMode_aLSSpec como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_aLSSpec)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_LSSpec
        self.mdObservingModesMode_LSSpec.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aMOS como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_aMOS)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_MOS
        self.mdObservingModesMode_MOS.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aFastBBI como elegible para ObservingModesMode_FastBBI
        self.mdObservingModesMode_FastBBI.addSubMode(self.mdAcquisitionModesMode_aFastBBI)
        # Marcamos AcquisitionModesMode_aFrTrBBI como elegible para ObservingModesMode_FrTrBBI
        self.mdObservingModesMode_FrTrBBI.addSubMode(self.mdAcquisitionModesMode_aFrTrBBI)
        # Marcamos AcquisitionModesMode_aFastLSSpec como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_aFastLSSpec)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_FastLSSpec
        self.mdObservingModesMode_FastLSSpec.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_aFastTFImage como elegible para ObservingModesMode_FastTFImage
        self.mdObservingModesMode_FastTFImage.addSubMode(self.mdAcquisitionModesMode_aFastTFImage)
        # Marcamos AcquisitionModesMode_aFrTrTFI como elegible para ObservingModesMode_FrTrTFI
        self.mdObservingModesMode_FrTrTFI.addSubMode(self.mdAcquisitionModesMode_aFrTrTFI)
        # Marcamos AcquisitionModesMode_aBias como elegible para ObservingModesMode_Bias
        self.mdObservingModesMode_Bias.addSubMode(self.mdAcquisitionModesMode_aBias)
        # Marcamos AcquisitionModesMode_aDark como elegible para ObservingModesMode_Dark
        self.mdObservingModesMode_Dark.addSubMode(self.mdAcquisitionModesMode_aDark)
        # Marcamos AcquisitionModesMode_aDomeFlat como elegible para ObservingModesMode_DomeFlat
        self.mdObservingModesMode_DomeFlat.addSubMode(self.mdAcquisitionModesMode_aDomeFlat)
        # Marcamos AcquisitionModesMode_aSkyFlat como elegible para ObservingModesMode_SkyFlat
        self.mdObservingModesMode_SkyFlat.addSubMode(self.mdAcquisitionModesMode_aSkyFlat)
        # Marcamos AcquisitionModesMode_aSpectralFlat como elegible para ObservingModesMode_SpectralFlat
        self.mdObservingModesMode_SpectralFlat.addSubMode(self.mdAcquisitionModesMode_aSpectralFlat)
        # Marcamos AcquisitionModesMode_aCalibLamp como elegible para ObservingModesMode_CalibLamp
        self.mdObservingModesMode_CalibLamp.addSubMode(self.mdAcquisitionModesMode_aCalibLamp)
        # Marcamos AcquisitionModesMode_aTFCalib como elegible para ObservingModesMode_TFCalib
        self.mdObservingModesMode_TFCalib.addSubMode(self.mdAcquisitionModesMode_aTFCalib)
        # Marcamos AcquisitionModesMode_aBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aBBI)
        # Marcamos AcquisitionModesMode_aTFI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aTFI)
        # Marcamos AcquisitionModesMode_aLSSpec como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aLSSpec)
        # Marcamos AcquisitionModesMode_aMOS como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aMOS)
        # Marcamos AcquisitionModesMode_aFastBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastBBI)
        # Marcamos AcquisitionModesMode_aFrTrBBI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFrTrBBI)
        # Marcamos AcquisitionModesMode_aFastLSSpec como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastLSSpec)
        # Marcamos AcquisitionModesMode_aFastTFImage como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFastTFImage)
        # Marcamos AcquisitionModesMode_aFrTrTFI como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aFrTrTFI)
        # Marcamos AcquisitionModesMode_aBias como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aBias)
        # Marcamos AcquisitionModesMode_aDark como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aDark)
        # Marcamos AcquisitionModesMode_aDomeFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aDomeFlat)
        # Marcamos AcquisitionModesMode_aSkyFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aSkyFlat)
        # Marcamos AcquisitionModesMode_aSpectralFlat como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aSpectralFlat)
        # Marcamos AcquisitionModesMode_aCalibLamp como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aCalibLamp)
        # Marcamos AcquisitionModesMode_aTFCalib como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_aTFCalib)
        # Marcamos AcquisitionModesMode_Throughslit como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_Throughslit)
        # Marcamos AcquisitionModesMode_Engineering como elegible para ObservingModesMode_Engineering
        self.mdObservingModesMode_Engineering.addSubMode(self.mdAcquisitionModesMode_Engineering)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismBMOS como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdPreOpticsMode_GrismBMOS)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_RTFCalib como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdPreOpticsMode_RTFCalib)
        # Marcamos PreOpticsMode_BTFCalib como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdPreOpticsMode_BTFCalib)
        # Marcamos PreOpticsMode_NoDispersion como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_NoDispersion)
        # Marcamos PreOpticsMode_RTF como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_RTF)
        # Marcamos PreOpticsMode_GrismR como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismR)
        # Marcamos PreOpticsMode_BTF como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_BTF)
        # Marcamos PreOpticsMode_GrismB como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismB)
        # Marcamos PreOpticsMode_GrismBMOS como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_GrismBMOS)
        # Marcamos PreOpticsMode_RTFCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_RTFCalib)
        # Marcamos PreOpticsMode_BTFCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdPreOpticsMode_BTFCalib)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_ShufffingSpec como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdDASMode_ShufffingSpec)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_ShufffingBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_ShufffingBias)
        # Marcamos DASMode_SimpleBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_SimpleBias)
        # Marcamos DASMode_FTBias como elegible para AcquisitionModesMode_aBias
        self.mdAcquisitionModesMode_aBias.addSubMode(self.mdDASMode_FTBias)
        # Marcamos DASMode_ShufffingDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_ShufffingDark)
        # Marcamos DASMode_SimpleDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_SimpleDark)
        # Marcamos DASMode_FTDark como elegible para AcquisitionModesMode_aDark
        self.mdAcquisitionModesMode_aDark.addSubMode(self.mdDASMode_FTDark)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aDomeFlat
        self.mdAcquisitionModesMode_aDomeFlat.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aDomeFlat
        self.mdAcquisitionModesMode_aDomeFlat.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_aSkyFlat
        self.mdAcquisitionModesMode_aSkyFlat.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_aSkyFlat
        self.mdAcquisitionModesMode_aSkyFlat.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_aSpectralFlat
        self.mdAcquisitionModesMode_aSpectralFlat.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_GainCalib como elegible para AcquisitionModesMode_aCalibLamp
        self.mdAcquisitionModesMode_aCalibLamp.addSubMode(self.mdDASMode_GainCalib)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_Throughslit
        self.mdAcquisitionModesMode_Throughslit.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_SimpleImg como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleImg)
        # Marcamos DASMode_SimpleSpec como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleSpec)
        # Marcamos DASMode_ShufffingSpec como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingSpec)
        # Marcamos DASMode_FTImg como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTImg)
        # Marcamos DASMode_FTDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTDark)
        # Marcamos DASMode_FTBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_FTBias)
        # Marcamos DASMode_SimpleBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleBias)
        # Marcamos DASMode_SimpleDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleDark)
        # Marcamos DASMode_ShufffingDark como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingDark)
        # Marcamos DASMode_ShufffingBias como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingBias)
        # Marcamos DASMode_ShufffingImage como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_ShufffingImage)
        # Marcamos DASMode_SimpleCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_SimpleCalib)
        # Marcamos DASMode_GainCalib como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdDASMode_GainCalib)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aBBI
        self.mdAcquisitionModesMode_aBBI.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aTFI
        self.mdAcquisitionModesMode_aTFI.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_aLSSpec
        self.mdAcquisitionModesMode_aLSSpec.addSubMode(self.mdFPEMode_LSMask)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_aMOS
        self.mdAcquisitionModesMode_aMOS.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_aFastBBI
        self.mdAcquisitionModesMode_aFastBBI.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_aFrTrBBI
        self.mdAcquisitionModesMode_aFrTrBBI.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_aFastLSSpec
        self.mdAcquisitionModesMode_aFastLSSpec.addSubMode(self.mdFPEMode_LSMask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_aFastTFImage
        self.mdAcquisitionModesMode_aFastTFImage.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_aFrTrTFI
        self.mdAcquisitionModesMode_aFrTrTFI.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_aTFCalib
        self.mdAcquisitionModesMode_aTFCalib.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_Throughslit
        self.mdAcquisitionModesMode_Throughslit.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_NoFPE como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_NoFPE)
        # Marcamos FPEMode_MOSmask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_MOSmask)
        # Marcamos FPEMode_FastPhotometryMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_FastPhotometryMask)
        # Marcamos FPEMode_FrameTransferMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_FrameTransferMask)
        # Marcamos FPEMode_LSMask como elegible para AcquisitionModesMode_Engineering
        self.mdAcquisitionModesMode_Engineering.addSubMode(self.mdFPEMode_LSMask)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## OsirisMode 
    def get_OsirisMode(self)-> PORISMode:
        return self.sysOsiris.getSelectedMode()

    def set_OsirisMode(self, mode: PORISMode)-> PORISMode :
        return self.sysOsiris.selectMode(mode)


    ## ObservingModesMode 
    def get_ObservingModesMode(self)-> PORISMode:
        return self.sysObservingModes.getSelectedMode()

    def set_ObservingModesMode(self, mode: PORISMode)-> PORISMode :
        return self.sysObservingModes.selectMode(mode)


    ## AcquisitionModesMode 
    def get_AcquisitionModesMode(self)-> PORISMode:
        return self.sysAcquisitionModes.getSelectedMode()

    def set_AcquisitionModesMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAcquisitionModes.selectMode(mode)


    ## PreOpticsMode 
    def get_PreOpticsMode(self)-> PORISMode:
        return self.sysPreOptics.getSelectedMode()

    def set_PreOpticsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPreOptics.selectMode(mode)


    ## DASMode 
    def get_DASMode(self)-> PORISMode:
        return self.sysDAS.getSelectedMode()

    def set_DASMode(self, mode: PORISMode)-> PORISMode :
        return self.sysDAS.selectMode(mode)


    ## FPEMode 
    def get_FPEMode(self)-> PORISMode:
        return self.sysFPE.getSelectedMode()

    def set_FPEMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFPE.selectMode(mode)

