from PORIS import *

class spieinstrPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysInstrument = PORISSys("Instrument")
        self.setRoot(self.sysInstrument)
        self.sysCamera = PORISSys("Camera")
        self.prExposureTime = PORISParam("ExposureTime")
        self.prHalf_field_mask = PORISParam("Half_field_mask")
        self.vlExposureTime_NormalRange = PORISValueFloat("ExposureTime_NormalRange",0.0,1.0,3600.0)
        self.mdExposureTimeMode_Normal = PORISMode("ExposureTimeMode_Normal")
        self.mdExposureTimeMode_Fast = PORISMode("ExposureTimeMode_Fast")
        self.mdCameraMode_Normal = PORISMode("CameraMode_Normal")
        self.mdCameraMode_Fast = PORISMode("CameraMode_Fast")
        self.vlHalf_field_mask_absent = PORISValue("Half_field_mask_absent")
        self.vlHalf_field_mask_present = PORISValue("Half_field_mask_present")
        self.mdHalf_field_maskMode_Normal = PORISMode("Half_field_maskMode_Normal")
        self.mdHalf_field_maskMode_Fast = PORISMode("Half_field_maskMode_Fast")
        self.mdInstrumentMode_Normal = PORISMode("InstrumentMode_Normal")
        self.mdInstrumentMode_Fast = PORISMode("InstrumentMode_Fast")
        self.mdInstrumentMode_Engineering = PORISMode("InstrumentMode_Engineering")
        self.mdCameraMode_Engineering = PORISMode("CameraMode_Engineering")
        self.addItem(self.sysInstrument)
        self.sysInstrument.ident = "n0"
        self.sysInstrument.setXMLName('Instrument')
        self.sysInstrument.description = ""
        self.addItem(self.sysCamera)
        self.sysCamera.ident = "n0::n0"
        self.sysCamera.setXMLName('Camera')
        self.sysCamera.description = ""
        self.sysInstrument.addSubsystem(self.sysCamera)
        self.addItem(self.prExposureTime)
        self.prExposureTime.ident = "n0::n0::n0"
        self.prExposureTime.setXMLName('ExposureTime')
        self.prExposureTime.description = ""
        self.sysCamera.addParam(self.prExposureTime)
        self.addItem(self.prHalf_field_mask)
        self.prHalf_field_mask.ident = "n0::n1"
        self.prHalf_field_mask.setXMLName('Half-field mask')
        self.prHalf_field_mask.description = ""
        self.sysInstrument.addParam(self.prHalf_field_mask)
        self.addItem(self.vlExposureTime_NormalRange)
        self.vlExposureTime_NormalRange.ident = "n0::n0::n0::n0"
        self.vlExposureTime_NormalRange.setXMLName('NormalRange')
        self.vlExposureTime_NormalRange.description = ""
        self.prExposureTime.addValue(self.vlExposureTime_NormalRange)
        self.addItem(self.mdExposureTimeMode_Normal)
        self.mdExposureTimeMode_Normal.ident = "n0::n0::n0::n1"
        self.mdExposureTimeMode_Normal.setXMLName('Normal')
        self.mdExposureTimeMode_Normal.description = ""
        self.prExposureTime.addMode(self.mdExposureTimeMode_Normal)
        self.addItem(self.mdExposureTimeMode_Fast)
        self.mdExposureTimeMode_Fast.ident = "n0::n0::n0::n2"
        self.mdExposureTimeMode_Fast.setXMLName('Fast')
        self.mdExposureTimeMode_Fast.description = ""
        self.prExposureTime.addMode(self.mdExposureTimeMode_Fast)
        self.addItem(self.mdCameraMode_Normal)
        self.mdCameraMode_Normal.ident = "n0::n0::n1"
        self.mdCameraMode_Normal.setXMLName('Normal')
        self.mdCameraMode_Normal.description = ""
        self.sysCamera.addMode(self.mdCameraMode_Normal)
        self.addItem(self.mdCameraMode_Fast)
        self.mdCameraMode_Fast.ident = "n0::n0::n2"
        self.mdCameraMode_Fast.setXMLName('Fast')
        self.mdCameraMode_Fast.description = ""
        self.sysCamera.addMode(self.mdCameraMode_Fast)
        self.addItem(self.vlHalf_field_mask_absent)
        self.vlHalf_field_mask_absent.ident = "n0::n1::n0"
        self.vlHalf_field_mask_absent.setXMLName('absent')
        self.vlHalf_field_mask_absent.description = ""
        self.prHalf_field_mask.addValue(self.vlHalf_field_mask_absent)
        self.addItem(self.vlHalf_field_mask_present)
        self.vlHalf_field_mask_present.ident = "n0::n1::n1"
        self.vlHalf_field_mask_present.setXMLName('present')
        self.vlHalf_field_mask_present.description = ""
        self.prHalf_field_mask.addValue(self.vlHalf_field_mask_present)
        self.addItem(self.mdHalf_field_maskMode_Normal)
        self.mdHalf_field_maskMode_Normal.ident = "n0::n1::n2"
        self.mdHalf_field_maskMode_Normal.setXMLName('Normal')
        self.mdHalf_field_maskMode_Normal.description = ""
        self.prHalf_field_mask.addMode(self.mdHalf_field_maskMode_Normal)
        self.addItem(self.mdHalf_field_maskMode_Fast)
        self.mdHalf_field_maskMode_Fast.ident = "n0::n1::n3"
        self.mdHalf_field_maskMode_Fast.setXMLName('Fast')
        self.mdHalf_field_maskMode_Fast.description = ""
        self.prHalf_field_mask.addMode(self.mdHalf_field_maskMode_Fast)
        self.addItem(self.mdInstrumentMode_Normal)
        self.mdInstrumentMode_Normal.ident = "n0::n2"
        self.mdInstrumentMode_Normal.setXMLName('Normal')
        self.mdInstrumentMode_Normal.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Normal)
        self.addItem(self.mdInstrumentMode_Fast)
        self.mdInstrumentMode_Fast.ident = "n0::n3"
        self.mdInstrumentMode_Fast.setXMLName('Fast')
        self.mdInstrumentMode_Fast.description = ""
        self.sysInstrument.addMode(self.mdInstrumentMode_Fast)
        self.addItem(self.mdInstrumentMode_Engineering)
        self.mdInstrumentMode_Engineering.ident = "ENG-1"
        self.mdInstrumentMode_Engineering.setXMLName('Engineering')
        self.mdInstrumentMode_Engineering.description = "Instrument_engineering_mode"
        self.sysInstrument.addMode(self.mdInstrumentMode_Engineering)
        self.addItem(self.mdCameraMode_Engineering)
        self.mdCameraMode_Engineering.ident = "ENG-2"
        self.mdCameraMode_Engineering.setXMLName('Engineering')
        self.mdCameraMode_Engineering.description = "Camera_engineering_mode"
        self.sysCamera.addMode(self.mdCameraMode_Engineering)
        # Marcamos CameraMode_Normal como elegible para InstrumentMode_Normal
        self.mdInstrumentMode_Normal.addSubMode(self.mdCameraMode_Normal)
        # Marcamos CameraMode_Fast como elegible para InstrumentMode_Fast
        self.mdInstrumentMode_Fast.addSubMode(self.mdCameraMode_Fast)
        # Marcamos CameraMode_Normal como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdCameraMode_Normal)
        # Marcamos CameraMode_Fast como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdCameraMode_Fast)
        # Marcamos CameraMode_Engineering como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdCameraMode_Engineering)
        # Marcamos ExposureTimeMode_Normal como elegible para CameraMode_Normal
        self.mdCameraMode_Normal.addSubMode(self.mdExposureTimeMode_Normal)
        # Marcamos ExposureTimeMode_Fast como elegible para CameraMode_Fast
        self.mdCameraMode_Fast.addSubMode(self.mdExposureTimeMode_Fast)
        # Marcamos ExposureTimeMode_Normal como elegible para CameraMode_Engineering
        self.mdCameraMode_Engineering.addSubMode(self.mdExposureTimeMode_Normal)
        # Marcamos ExposureTimeMode_Fast como elegible para CameraMode_Engineering
        self.mdCameraMode_Engineering.addSubMode(self.mdExposureTimeMode_Fast)
        # Marcamos ExposureTime_NormalRange como elegible para ExposureTimeMode_Normal
        self.mdExposureTimeMode_Normal.addValue(self.vlExposureTime_NormalRange)
        # Marcamos ExposureTime_NormalRange como elegible para ExposureTimeMode_Fast
        self.mdExposureTimeMode_Fast.addValue(self.vlExposureTime_NormalRange)
        # Marcamos Half_field_maskMode_Normal como elegible para InstrumentMode_Normal
        self.mdInstrumentMode_Normal.addSubMode(self.mdHalf_field_maskMode_Normal)
        # Marcamos Half_field_maskMode_Fast como elegible para InstrumentMode_Fast
        self.mdInstrumentMode_Fast.addSubMode(self.mdHalf_field_maskMode_Fast)
        # Marcamos Half_field_maskMode_Normal como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdHalf_field_maskMode_Normal)
        # Marcamos Half_field_maskMode_Fast como elegible para InstrumentMode_Engineering
        self.mdInstrumentMode_Engineering.addSubMode(self.mdHalf_field_maskMode_Fast)
        # Marcamos Half_field_mask_absent como elegible para Half_field_maskMode_Normal
        self.mdHalf_field_maskMode_Normal.addValue(self.vlHalf_field_mask_absent)
        # Marcamos Half_field_mask_present como elegible para Half_field_maskMode_Fast
        self.mdHalf_field_maskMode_Fast.addValue(self.vlHalf_field_mask_present)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## InstrumentMode 
    def get_InstrumentMode(self)-> PORISMode:
        return self.sysInstrument.getSelectedMode()

    def set_InstrumentMode(self, mode: PORISMode)-> PORISMode :
        return self.sysInstrument.selectMode(mode)


    ## CameraMode 
    def get_CameraMode(self)-> PORISMode:
        return self.sysCamera.getSelectedMode()

    def set_CameraMode(self, mode: PORISMode)-> PORISMode :
        return self.sysCamera.selectMode(mode)


    ## prParam ExposureTime 

    # ExposureTime
    def get_ExposureTime(self)-> PORISValue :
        return self.prExposureTime.getSelectedValue()

    def set_ExposureTime(self, value: PORISValue)-> PORISValue :
        return self.prExposureTime.setValue(value)


    ## ExposureTimeMode 
    def get_ExposureTimeMode(self)-> PORISMode:
        return self.prExposureTime.getSelectedMode()

    def set_ExposureTimeMode(self, mode: PORISMode)-> PORISMode :
        return self.prExposureTime.selectMode(mode)


    ## prParam Camera 

    # ExposureTimeDouble  
    def get_ExposureTimeDouble(self)-> float :
        v = self.prExposureTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExposureTimeDouble(self, data: float)-> float :
        return self.prExposureTime.getSelectedValue().setData(data)


    ## prParam Camera 

    # ExposureTimeDouble  
    def get_ExposureTimeDouble(self)-> float :
        v = self.prExposureTime.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ExposureTimeDouble(self, data: float)-> float :
        return self.prExposureTime.getSelectedValue().setData(data)


    ## prParam Half_field_mask 

    # Half_field_mask
    def get_Half_field_mask(self)-> PORISValue :
        return self.prHalf_field_mask.getSelectedValue()

    def set_Half_field_mask(self, value: PORISValue)-> PORISValue :
        return self.prHalf_field_mask.setValue(value)


    ## Half_field_maskMode 
    def get_Half_field_maskMode(self)-> PORISMode:
        return self.prHalf_field_mask.getSelectedMode()

    def set_Half_field_maskMode(self, mode: PORISMode)-> PORISMode :
        return self.prHalf_field_mask.selectMode(mode)

