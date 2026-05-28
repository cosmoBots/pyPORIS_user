from PORIS import *

class mainaxisPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysMainAxis = PORISSys("MainAxis")
        self.setRoot(self.sysMainAxis)
        self.sysMainAxisSys = PORISSys("MainAxisSys")
        self.prYaw = PORISParam("Yaw")
        self.prPitch = PORISParam("Pitch")
        self.mdMainAxisMode_Disabled = PORISMode("MainAxisMode_Disabled")
        self.mdMainAxisMode_Operation = PORISMode("MainAxisMode_Operation")
        self.vlYaw_Y_HOME = PORISValue("Yaw_Y_HOME")
        self.vlYaw_Y_PARK = PORISValue("Yaw_Y_PARK")
        self.vlYaw_Y_TECH = PORISValue("Yaw_Y_TECH")
        self.vlYaw_Y_angle = PORISValueFloat("Yaw_Y_angle",-270.0,0.0,270.0)
        self.mdYawMode_Homing = PORISMode("YawMode_Homing")
        self.mdYawMode_Parking = PORISMode("YawMode_Parking")
        self.mdYawMode_Technical = PORISMode("YawMode_Technical")
        self.mdYawMode_Pointing = PORISMode("YawMode_Pointing")
        self.mdMainAxisSysMode_Homing = PORISMode("MainAxisSysMode_Homing")
        self.mdMainAxisSysMode_Parking = PORISMode("MainAxisSysMode_Parking")
        self.mdMainAxisSysMode_Technical = PORISMode("MainAxisSysMode_Technical")
        self.mdMainAxisSysMode_Pointing = PORISMode("MainAxisSysMode_Pointing")
        self.vlPitch_P_HOME = PORISValue("Pitch_P_HOME")
        self.vlPitch_P_PARK = PORISValue("Pitch_P_PARK")
        self.vlPitch_P_TECH = PORISValue("Pitch_P_TECH")
        self.vlPitch_P_angle = PORISValueFloat("Pitch_P_angle",-45.0,0.0,22.0)
        self.mdPitchMode_Homing = PORISMode("PitchMode_Homing")
        self.mdPitchMode_Parking = PORISMode("PitchMode_Parking")
        self.mdPitchMode_Technical = PORISMode("PitchMode_Technical")
        self.mdPitchMode_Pointing = PORISMode("PitchMode_Pointing")
        self.mdMainAxisMode_Technical = PORISMode("MainAxisMode_Technical")
        self.mdMainAxisMode_Engineering = PORISMode("MainAxisMode_Engineering")
        self.mdMainAxisSysMode_Engineering = PORISMode("MainAxisSysMode_Engineering")
        self.addItem(self.sysMainAxis)
        self.sysMainAxis.ident = "n0"
        self.sysMainAxis.setXMLName('MainAxis')
        self.sysMainAxis.description = ""
        self.addItem(self.sysMainAxisSys)
        self.sysMainAxisSys.ident = "n0::n2"
        self.sysMainAxisSys.setXMLName('MainAxisSys')
        self.sysMainAxisSys.description = ""
        self.sysMainAxis.addSubsystem(self.sysMainAxisSys)
        self.addItem(self.prYaw)
        self.prYaw.ident = "n0::n2::n0"
        self.prYaw.setXMLName('Yaw')
        self.prYaw.description = ""
        self.sysMainAxisSys.addParam(self.prYaw)
        self.addItem(self.prPitch)
        self.prPitch.ident = "n0::n2::n5"
        self.prPitch.setXMLName('Pitch')
        self.prPitch.description = ""
        self.sysMainAxisSys.addParam(self.prPitch)
        self.addItem(self.mdMainAxisMode_Disabled)
        self.mdMainAxisMode_Disabled.ident = "n0::n0"
        self.mdMainAxisMode_Disabled.setXMLName('Disabled')
        self.mdMainAxisMode_Disabled.description = ""
        self.sysMainAxis.addMode(self.mdMainAxisMode_Disabled)
        self.addItem(self.mdMainAxisMode_Operation)
        self.mdMainAxisMode_Operation.ident = "n0::n1"
        self.mdMainAxisMode_Operation.setXMLName('Operation')
        self.mdMainAxisMode_Operation.description = ""
        self.sysMainAxis.addMode(self.mdMainAxisMode_Operation)
        self.addItem(self.vlYaw_Y_HOME)
        self.vlYaw_Y_HOME.ident = "n0::n2::n0::n0"
        self.vlYaw_Y_HOME.setXMLName('Y_HOME')
        self.vlYaw_Y_HOME.description = ""
        self.prYaw.addValue(self.vlYaw_Y_HOME)
        self.addItem(self.vlYaw_Y_PARK)
        self.vlYaw_Y_PARK.ident = "n0::n2::n0::n1"
        self.vlYaw_Y_PARK.setXMLName('Y_PARK')
        self.vlYaw_Y_PARK.description = ""
        self.prYaw.addValue(self.vlYaw_Y_PARK)
        self.addItem(self.vlYaw_Y_TECH)
        self.vlYaw_Y_TECH.ident = "n0::n2::n0::n2"
        self.vlYaw_Y_TECH.setXMLName('Y_TECH')
        self.vlYaw_Y_TECH.description = ""
        self.prYaw.addValue(self.vlYaw_Y_TECH)
        self.addItem(self.vlYaw_Y_angle)
        self.vlYaw_Y_angle.ident = "n0::n2::n0::n3"
        self.vlYaw_Y_angle.setXMLName('Y_angle')
        self.vlYaw_Y_angle.description = ""
        self.prYaw.addValue(self.vlYaw_Y_angle)
        self.addItem(self.mdYawMode_Homing)
        self.mdYawMode_Homing.ident = "n0::n2::n0::n4"
        self.mdYawMode_Homing.setXMLName('Homing')
        self.mdYawMode_Homing.description = ""
        self.prYaw.addMode(self.mdYawMode_Homing)
        self.addItem(self.mdYawMode_Parking)
        self.mdYawMode_Parking.ident = "n0::n2::n0::n5"
        self.mdYawMode_Parking.setXMLName('Parking')
        self.mdYawMode_Parking.description = ""
        self.prYaw.addMode(self.mdYawMode_Parking)
        self.addItem(self.mdYawMode_Technical)
        self.mdYawMode_Technical.ident = "n0::n2::n0::n6"
        self.mdYawMode_Technical.setXMLName('Technical')
        self.mdYawMode_Technical.description = ""
        self.prYaw.addMode(self.mdYawMode_Technical)
        self.addItem(self.mdYawMode_Pointing)
        self.mdYawMode_Pointing.ident = "n0::n2::n0::n7"
        self.mdYawMode_Pointing.setXMLName('Pointing')
        self.mdYawMode_Pointing.description = ""
        self.prYaw.addMode(self.mdYawMode_Pointing)
        self.addItem(self.mdMainAxisSysMode_Homing)
        self.mdMainAxisSysMode_Homing.ident = "n0::n2::n1"
        self.mdMainAxisSysMode_Homing.setXMLName('Homing')
        self.mdMainAxisSysMode_Homing.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Homing)
        self.addItem(self.mdMainAxisSysMode_Parking)
        self.mdMainAxisSysMode_Parking.ident = "n0::n2::n2"
        self.mdMainAxisSysMode_Parking.setXMLName('Parking')
        self.mdMainAxisSysMode_Parking.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Parking)
        self.addItem(self.mdMainAxisSysMode_Technical)
        self.mdMainAxisSysMode_Technical.ident = "n0::n2::n3"
        self.mdMainAxisSysMode_Technical.setXMLName('Technical')
        self.mdMainAxisSysMode_Technical.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Technical)
        self.addItem(self.mdMainAxisSysMode_Pointing)
        self.mdMainAxisSysMode_Pointing.ident = "n0::n2::n4"
        self.mdMainAxisSysMode_Pointing.setXMLName('Pointing')
        self.mdMainAxisSysMode_Pointing.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Pointing)
        self.addItem(self.vlPitch_P_HOME)
        self.vlPitch_P_HOME.ident = "n0::n2::n5::n0"
        self.vlPitch_P_HOME.setXMLName('P_HOME')
        self.vlPitch_P_HOME.description = ""
        self.prPitch.addValue(self.vlPitch_P_HOME)
        self.addItem(self.vlPitch_P_PARK)
        self.vlPitch_P_PARK.ident = "n0::n2::n5::n1"
        self.vlPitch_P_PARK.setXMLName('P_PARK')
        self.vlPitch_P_PARK.description = ""
        self.prPitch.addValue(self.vlPitch_P_PARK)
        self.addItem(self.vlPitch_P_TECH)
        self.vlPitch_P_TECH.ident = "n0::n2::n5::n2"
        self.vlPitch_P_TECH.setXMLName('P_TECH')
        self.vlPitch_P_TECH.description = ""
        self.prPitch.addValue(self.vlPitch_P_TECH)
        self.addItem(self.vlPitch_P_angle)
        self.vlPitch_P_angle.ident = "n0::n2::n5::n3"
        self.vlPitch_P_angle.setXMLName('P_angle')
        self.vlPitch_P_angle.description = ""
        self.prPitch.addValue(self.vlPitch_P_angle)
        self.addItem(self.mdPitchMode_Homing)
        self.mdPitchMode_Homing.ident = "n0::n2::n5::n4"
        self.mdPitchMode_Homing.setXMLName('Homing')
        self.mdPitchMode_Homing.description = ""
        self.prPitch.addMode(self.mdPitchMode_Homing)
        self.addItem(self.mdPitchMode_Parking)
        self.mdPitchMode_Parking.ident = "n0::n2::n5::n5"
        self.mdPitchMode_Parking.setXMLName('Parking')
        self.mdPitchMode_Parking.description = ""
        self.prPitch.addMode(self.mdPitchMode_Parking)
        self.addItem(self.mdPitchMode_Technical)
        self.mdPitchMode_Technical.ident = "n0::n2::n5::n6"
        self.mdPitchMode_Technical.setXMLName('Technical')
        self.mdPitchMode_Technical.description = ""
        self.prPitch.addMode(self.mdPitchMode_Technical)
        self.addItem(self.mdPitchMode_Pointing)
        self.mdPitchMode_Pointing.ident = "n0::n2::n5::n7"
        self.mdPitchMode_Pointing.setXMLName('Pointing')
        self.mdPitchMode_Pointing.description = ""
        self.prPitch.addMode(self.mdPitchMode_Pointing)
        self.addItem(self.mdMainAxisMode_Technical)
        self.mdMainAxisMode_Technical.ident = "n0::n3"
        self.mdMainAxisMode_Technical.setXMLName('Technical')
        self.mdMainAxisMode_Technical.description = ""
        self.sysMainAxis.addMode(self.mdMainAxisMode_Technical)
        self.addItem(self.mdMainAxisMode_Engineering)
        self.mdMainAxisMode_Engineering.ident = "ENG-1"
        self.mdMainAxisMode_Engineering.setXMLName('Engineering')
        self.mdMainAxisMode_Engineering.description = "MainAxis engineering mode"
        self.sysMainAxis.addMode(self.mdMainAxisMode_Engineering)
        self.addItem(self.mdMainAxisSysMode_Engineering)
        self.mdMainAxisSysMode_Engineering.ident = "ENG-2"
        self.mdMainAxisSysMode_Engineering.setXMLName('Engineering')
        self.mdMainAxisSysMode_Engineering.description = "MainAxisSys engineering mode"
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Engineering)
        # Marcamos MainAxisSysMode_Homing como elegible para MainAxisMode_Operation
        self.mdMainAxisMode_Operation.addSubMode(self.mdMainAxisSysMode_Homing)
        # Marcamos MainAxisSysMode_Parking como elegible para MainAxisMode_Operation
        self.mdMainAxisMode_Operation.addSubMode(self.mdMainAxisSysMode_Parking)
        # Marcamos MainAxisSysMode_Pointing como elegible para MainAxisMode_Operation
        self.mdMainAxisMode_Operation.addSubMode(self.mdMainAxisSysMode_Pointing)
        # Marcamos MainAxisSysMode_Homing como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_Homing)
        # Marcamos MainAxisSysMode_Parking como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_Parking)
        # Marcamos MainAxisSysMode_Technical como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_Technical)
        # Marcamos MainAxisSysMode_Pointing como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_Pointing)
        # Marcamos MainAxisSysMode_Homing como elegible para MainAxisMode_Engineering
        self.mdMainAxisMode_Engineering.addSubMode(self.mdMainAxisSysMode_Homing)
        # Marcamos MainAxisSysMode_Parking como elegible para MainAxisMode_Engineering
        self.mdMainAxisMode_Engineering.addSubMode(self.mdMainAxisSysMode_Parking)
        # Marcamos MainAxisSysMode_Technical como elegible para MainAxisMode_Engineering
        self.mdMainAxisMode_Engineering.addSubMode(self.mdMainAxisSysMode_Technical)
        # Marcamos MainAxisSysMode_Pointing como elegible para MainAxisMode_Engineering
        self.mdMainAxisMode_Engineering.addSubMode(self.mdMainAxisSysMode_Pointing)
        # Marcamos MainAxisSysMode_Engineering como elegible para MainAxisMode_Engineering
        self.mdMainAxisMode_Engineering.addSubMode(self.mdMainAxisSysMode_Engineering)
        # Marcamos YawMode_Homing como elegible para MainAxisSysMode_Homing
        self.mdMainAxisSysMode_Homing.addSubMode(self.mdYawMode_Homing)
        # Marcamos YawMode_Parking como elegible para MainAxisSysMode_Parking
        self.mdMainAxisSysMode_Parking.addSubMode(self.mdYawMode_Parking)
        # Marcamos YawMode_Technical como elegible para MainAxisSysMode_Technical
        self.mdMainAxisSysMode_Technical.addSubMode(self.mdYawMode_Technical)
        # Marcamos YawMode_Pointing como elegible para MainAxisSysMode_Pointing
        self.mdMainAxisSysMode_Pointing.addSubMode(self.mdYawMode_Pointing)
        # Marcamos YawMode_Homing como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdYawMode_Homing)
        # Marcamos YawMode_Parking como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdYawMode_Parking)
        # Marcamos YawMode_Technical como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdYawMode_Technical)
        # Marcamos YawMode_Pointing como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdYawMode_Pointing)
        # Marcamos Yaw_Y_HOME como elegible para YawMode_Homing
        self.mdYawMode_Homing.addValue(self.vlYaw_Y_HOME)
        # Marcamos Yaw_Y_PARK como elegible para YawMode_Parking
        self.mdYawMode_Parking.addValue(self.vlYaw_Y_PARK)
        # Marcamos Yaw_Y_TECH como elegible para YawMode_Technical
        self.mdYawMode_Technical.addValue(self.vlYaw_Y_TECH)
        # Marcamos Yaw_Y_angle como elegible para YawMode_Pointing
        self.mdYawMode_Pointing.addValue(self.vlYaw_Y_angle)
        # Marcamos PitchMode_Homing como elegible para MainAxisSysMode_Homing
        self.mdMainAxisSysMode_Homing.addSubMode(self.mdPitchMode_Homing)
        # Marcamos PitchMode_Parking como elegible para MainAxisSysMode_Parking
        self.mdMainAxisSysMode_Parking.addSubMode(self.mdPitchMode_Parking)
        # Marcamos PitchMode_Technical como elegible para MainAxisSysMode_Technical
        self.mdMainAxisSysMode_Technical.addSubMode(self.mdPitchMode_Technical)
        # Marcamos PitchMode_Pointing como elegible para MainAxisSysMode_Pointing
        self.mdMainAxisSysMode_Pointing.addSubMode(self.mdPitchMode_Pointing)
        # Marcamos PitchMode_Homing como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdPitchMode_Homing)
        # Marcamos PitchMode_Parking como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdPitchMode_Parking)
        # Marcamos PitchMode_Technical como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdPitchMode_Technical)
        # Marcamos PitchMode_Pointing como elegible para MainAxisSysMode_Engineering
        self.mdMainAxisSysMode_Engineering.addSubMode(self.mdPitchMode_Pointing)
        # Marcamos Pitch_P_HOME como elegible para PitchMode_Homing
        self.mdPitchMode_Homing.addValue(self.vlPitch_P_HOME)
        # Marcamos Pitch_P_PARK como elegible para PitchMode_Parking
        self.mdPitchMode_Parking.addValue(self.vlPitch_P_PARK)
        # Marcamos Pitch_P_TECH como elegible para PitchMode_Technical
        self.mdPitchMode_Technical.addValue(self.vlPitch_P_TECH)
        # Marcamos Pitch_P_angle como elegible para PitchMode_Pointing
        self.mdPitchMode_Pointing.addValue(self.vlPitch_P_angle)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## MainAxisMode 
    def get_MainAxisMode(self)-> PORISMode:
        return self.sysMainAxis.getSelectedMode()

    def set_MainAxisMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMainAxis.selectMode(mode)


    ## MainAxisSysMode 
    def get_MainAxisSysMode(self)-> PORISMode:
        return self.sysMainAxisSys.getSelectedMode()

    def set_MainAxisSysMode(self, mode: PORISMode)-> PORISMode :
        return self.sysMainAxisSys.selectMode(mode)


    ## prParam Yaw 

    # Yaw
    def get_Yaw(self)-> PORISValue :
        return self.prYaw.getSelectedValue()

    def set_Yaw(self, value: PORISValue)-> PORISValue :
        return self.prYaw.setValue(value)


    ## YawMode 
    def get_YawMode(self)-> PORISMode:
        return self.prYaw.getSelectedMode()

    def set_YawMode(self, mode: PORISMode)-> PORISMode :
        return self.prYaw.selectMode(mode)


    ## prParam MainAxisSys 

    # YawDouble  
    def get_YawDouble(self)-> float :
        v = self.prYaw.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_YawDouble(self, data: float)-> float :
        return self.prYaw.getSelectedValue().setData(data)


    ## prParam Pitch 

    # Pitch
    def get_Pitch(self)-> PORISValue :
        return self.prPitch.getSelectedValue()

    def set_Pitch(self, value: PORISValue)-> PORISValue :
        return self.prPitch.setValue(value)


    ## PitchMode 
    def get_PitchMode(self)-> PORISMode:
        return self.prPitch.getSelectedMode()

    def set_PitchMode(self, mode: PORISMode)-> PORISMode :
        return self.prPitch.selectMode(mode)


    ## prParam MainAxisSys 

    # PitchDouble  
    def get_PitchDouble(self)-> float :
        v = self.prPitch.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_PitchDouble(self, data: float)-> float :
        return self.prPitch.getSelectedValue().setData(data)

