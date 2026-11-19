from PORIS import *

class mainaxisPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysMainAxis = PORISSys("MainAxis")
        self.setRoot(self.sysMainAxis)
        self.sysMainAxisSys = PORISSys("MainAxisSys")
        self.prAzimuth = PORISParam("Azimuth")
        self.prElevation = PORISParam("Elevation")
        self.mdMainAxisMode_Operation = PORISMode("MainAxisMode_Operation")
        self.vlAzimuth_Y_HOME = PORISValue("Azimuth_Y_HOME")
        self.vlAzimuth_Y_PARK = PORISValue("Azimuth_Y_PARK")
        self.vlAzimuth_Y_MAINT = PORISValue("Azimuth_Y_MAINT")
        self.vlAzimuth_Y_angle = PORISValueFloat("Azimuth_Y_angle",-270.0,0.0,270.0)
        self.mdAzimuthMode_Homing = PORISMode("AzimuthMode_Homing")
        self.mdAzimuthMode_Parking = PORISMode("AzimuthMode_Parking")
        self.mdAzimuthMode_Maintenance = PORISMode("AzimuthMode_Maintenance")
        self.mdAzimuthMode_Pointing = PORISMode("AzimuthMode_Pointing")
        self.mdAzimuthMode_PointingTech = PORISMode("AzimuthMode_PointingTech")
        self.vlAzimuth_Y_angle_unbound = PORISValueFloat("Azimuth_Y_angle_unbound",-300.0,0.0,300.0)
        self.mdMainAxisSysMode_Homing = PORISMode("MainAxisSysMode_Homing")
        self.mdMainAxisSysMode_Parking = PORISMode("MainAxisSysMode_Parking")
        self.mdMainAxisSysMode_Maintenance = PORISMode("MainAxisSysMode_Maintenance")
        self.mdMainAxisSysMode_Pointing = PORISMode("MainAxisSysMode_Pointing")
        self.vlElevation_P_HOME = PORISValue("Elevation_P_HOME")
        self.vlElevation_P_PARK = PORISValue("Elevation_P_PARK")
        self.vlElevation_P_MAINT = PORISValue("Elevation_P_MAINT")
        self.vlElevation_P_angle = PORISValueFloat("Elevation_P_angle",0.0,0.0,90.0)
        self.mdElevationMode_Homing = PORISMode("ElevationMode_Homing")
        self.mdElevationMode_Parking = PORISMode("ElevationMode_Parking")
        self.mdElevationMode_Maintenance = PORISMode("ElevationMode_Maintenance")
        self.mdElevationMode_Pointing = PORISMode("ElevationMode_Pointing")
        self.mdElevationMode_PointingTech = PORISMode("ElevationMode_PointingTech")
        self.vlElevation_P_angle_unbound = PORISValueFloat("Elevation_P_angle_unbound",-18.0,0.0,90.0)
        self.mdMainAxisSysMode_PointingTech = PORISMode("MainAxisSysMode_PointingTech")
        self.cmdMainAxisSys_command = PORISCmd("MainAxisSys_command")
        self.mdMainAxisMode_Technical = PORISMode("MainAxisMode_Technical")
        self.addItem(self.sysMainAxis)
        self.sysMainAxis.ident = "n0"
        self.sysMainAxis.setXMLName('MainAxis')
        self.sysMainAxis.description = ""
        self.addItem(self.sysMainAxisSys)
        self.sysMainAxisSys.ident = "n0::n1"
        self.sysMainAxisSys.setXMLName('MainAxisSys')
        self.sysMainAxisSys.description = ""
        self.sysMainAxis.addSubsystem(self.sysMainAxisSys)
        self.addItem(self.prAzimuth)
        self.prAzimuth.ident = "n0::n1::n0"
        self.prAzimuth.setXMLName('Azimuth')
        self.prAzimuth.description = ""
        self.sysMainAxisSys.addParam(self.prAzimuth)
        self.addItem(self.prElevation)
        self.prElevation.ident = "n0::n1::n5"
        self.prElevation.setXMLName('Elevation')
        self.prElevation.description = ""
        self.sysMainAxisSys.addParam(self.prElevation)
        self.addItem(self.mdMainAxisMode_Operation)
        self.mdMainAxisMode_Operation.ident = "n0::n0"
        self.mdMainAxisMode_Operation.setXMLName('Operation')
        self.mdMainAxisMode_Operation.description = ""
        self.sysMainAxis.addMode(self.mdMainAxisMode_Operation)
        self.addItem(self.vlAzimuth_Y_HOME)
        self.vlAzimuth_Y_HOME.ident = "n0::n1::n0::n0"
        self.vlAzimuth_Y_HOME.setXMLName('Y_HOME')
        self.vlAzimuth_Y_HOME.description = ""
        self.prAzimuth.addValue(self.vlAzimuth_Y_HOME)
        self.addItem(self.vlAzimuth_Y_PARK)
        self.vlAzimuth_Y_PARK.ident = "n0::n1::n0::n1"
        self.vlAzimuth_Y_PARK.setXMLName('Y_PARK')
        self.vlAzimuth_Y_PARK.description = ""
        self.prAzimuth.addValue(self.vlAzimuth_Y_PARK)
        self.addItem(self.vlAzimuth_Y_MAINT)
        self.vlAzimuth_Y_MAINT.ident = "n0::n1::n0::n2"
        self.vlAzimuth_Y_MAINT.setXMLName('Y_MAINT')
        self.vlAzimuth_Y_MAINT.description = ""
        self.prAzimuth.addValue(self.vlAzimuth_Y_MAINT)
        self.addItem(self.vlAzimuth_Y_angle)
        self.vlAzimuth_Y_angle.ident = "n0::n1::n0::n3"
        self.vlAzimuth_Y_angle.setXMLName('Y_angle')
        self.vlAzimuth_Y_angle.description = ""
        self.prAzimuth.addValue(self.vlAzimuth_Y_angle)
        self.addItem(self.mdAzimuthMode_Homing)
        self.mdAzimuthMode_Homing.ident = "n0::n1::n0::n4"
        self.mdAzimuthMode_Homing.setXMLName('Homing')
        self.mdAzimuthMode_Homing.description = ""
        self.prAzimuth.addMode(self.mdAzimuthMode_Homing)
        self.addItem(self.mdAzimuthMode_Parking)
        self.mdAzimuthMode_Parking.ident = "n0::n1::n0::n5"
        self.mdAzimuthMode_Parking.setXMLName('Parking')
        self.mdAzimuthMode_Parking.description = ""
        self.prAzimuth.addMode(self.mdAzimuthMode_Parking)
        self.addItem(self.mdAzimuthMode_Maintenance)
        self.mdAzimuthMode_Maintenance.ident = "n0::n1::n0::n6"
        self.mdAzimuthMode_Maintenance.setXMLName('Maintenance')
        self.mdAzimuthMode_Maintenance.description = ""
        self.prAzimuth.addMode(self.mdAzimuthMode_Maintenance)
        self.addItem(self.mdAzimuthMode_Pointing)
        self.mdAzimuthMode_Pointing.ident = "n0::n1::n0::n7"
        self.mdAzimuthMode_Pointing.setXMLName('Pointing')
        self.mdAzimuthMode_Pointing.description = ""
        self.prAzimuth.addMode(self.mdAzimuthMode_Pointing)
        self.addItem(self.mdAzimuthMode_PointingTech)
        self.mdAzimuthMode_PointingTech.ident = "n0::n1::n0::n8"
        self.mdAzimuthMode_PointingTech.setXMLName('PointingTech')
        self.mdAzimuthMode_PointingTech.description = ""
        self.prAzimuth.addMode(self.mdAzimuthMode_PointingTech)
        self.addItem(self.vlAzimuth_Y_angle_unbound)
        self.vlAzimuth_Y_angle_unbound.ident = "n0::n1::n0::n9"
        self.vlAzimuth_Y_angle_unbound.setXMLName('Y_angle_unbound')
        self.vlAzimuth_Y_angle_unbound.description = ""
        self.prAzimuth.addValue(self.vlAzimuth_Y_angle_unbound)
        self.addItem(self.mdMainAxisSysMode_Homing)
        self.mdMainAxisSysMode_Homing.ident = "n0::n1::n1"
        self.mdMainAxisSysMode_Homing.setXMLName('Homing')
        self.mdMainAxisSysMode_Homing.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Homing)
        self.addItem(self.mdMainAxisSysMode_Parking)
        self.mdMainAxisSysMode_Parking.ident = "n0::n1::n2"
        self.mdMainAxisSysMode_Parking.setXMLName('Parking')
        self.mdMainAxisSysMode_Parking.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Parking)
        self.addItem(self.mdMainAxisSysMode_Maintenance)
        self.mdMainAxisSysMode_Maintenance.ident = "n0::n1::n3"
        self.mdMainAxisSysMode_Maintenance.setXMLName('Maintenance')
        self.mdMainAxisSysMode_Maintenance.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Maintenance)
        self.addItem(self.mdMainAxisSysMode_Pointing)
        self.mdMainAxisSysMode_Pointing.ident = "n0::n1::n4"
        self.mdMainAxisSysMode_Pointing.setXMLName('Pointing')
        self.mdMainAxisSysMode_Pointing.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_Pointing)
        self.addItem(self.vlElevation_P_HOME)
        self.vlElevation_P_HOME.ident = "n0::n1::n5::n0"
        self.vlElevation_P_HOME.setXMLName('P_HOME')
        self.vlElevation_P_HOME.description = ""
        self.prElevation.addValue(self.vlElevation_P_HOME)
        self.addItem(self.vlElevation_P_PARK)
        self.vlElevation_P_PARK.ident = "n0::n1::n5::n1"
        self.vlElevation_P_PARK.setXMLName('P_PARK')
        self.vlElevation_P_PARK.description = ""
        self.prElevation.addValue(self.vlElevation_P_PARK)
        self.addItem(self.vlElevation_P_MAINT)
        self.vlElevation_P_MAINT.ident = "n0::n1::n5::n2"
        self.vlElevation_P_MAINT.setXMLName('P_MAINT')
        self.vlElevation_P_MAINT.description = ""
        self.prElevation.addValue(self.vlElevation_P_MAINT)
        self.addItem(self.vlElevation_P_angle)
        self.vlElevation_P_angle.ident = "n0::n1::n5::n3"
        self.vlElevation_P_angle.setXMLName('P_angle')
        self.vlElevation_P_angle.description = ""
        self.prElevation.addValue(self.vlElevation_P_angle)
        self.addItem(self.mdElevationMode_Homing)
        self.mdElevationMode_Homing.ident = "n0::n1::n5::n4"
        self.mdElevationMode_Homing.setXMLName('Homing')
        self.mdElevationMode_Homing.description = ""
        self.prElevation.addMode(self.mdElevationMode_Homing)
        self.addItem(self.mdElevationMode_Parking)
        self.mdElevationMode_Parking.ident = "n0::n1::n5::n5"
        self.mdElevationMode_Parking.setXMLName('Parking')
        self.mdElevationMode_Parking.description = ""
        self.prElevation.addMode(self.mdElevationMode_Parking)
        self.addItem(self.mdElevationMode_Maintenance)
        self.mdElevationMode_Maintenance.ident = "n0::n1::n5::n6"
        self.mdElevationMode_Maintenance.setXMLName('Maintenance')
        self.mdElevationMode_Maintenance.description = ""
        self.prElevation.addMode(self.mdElevationMode_Maintenance)
        self.addItem(self.mdElevationMode_Pointing)
        self.mdElevationMode_Pointing.ident = "n0::n1::n5::n7"
        self.mdElevationMode_Pointing.setXMLName('Pointing')
        self.mdElevationMode_Pointing.description = ""
        self.prElevation.addMode(self.mdElevationMode_Pointing)
        self.addItem(self.mdElevationMode_PointingTech)
        self.mdElevationMode_PointingTech.ident = "n0::n1::n5::n8"
        self.mdElevationMode_PointingTech.setXMLName('PointingTech')
        self.mdElevationMode_PointingTech.description = ""
        self.prElevation.addMode(self.mdElevationMode_PointingTech)
        self.addItem(self.vlElevation_P_angle_unbound)
        self.vlElevation_P_angle_unbound.ident = "n0::n1::n5::n9"
        self.vlElevation_P_angle_unbound.setXMLName('P_angle_unbound')
        self.vlElevation_P_angle_unbound.description = ""
        self.prElevation.addValue(self.vlElevation_P_angle_unbound)
        self.addItem(self.mdMainAxisSysMode_PointingTech)
        self.mdMainAxisSysMode_PointingTech.ident = "n0::n1::n6"
        self.mdMainAxisSysMode_PointingTech.setXMLName('PointingTech')
        self.mdMainAxisSysMode_PointingTech.description = ""
        self.sysMainAxisSys.addMode(self.mdMainAxisSysMode_PointingTech)
        self.addItem(self.cmdMainAxisSys_command)
        self.cmdMainAxisSys_command.setActionName("command")
        self.cmdMainAxisSys_command.setHandlerName("execMainAxisSys_command")
        self.cmdMainAxisSys_command.setTracePath("sysMainAxisSys.command")
        self.cmdMainAxisSys_command.ident = "n0::n1::n7"
        self.cmdMainAxisSys_command.setXMLName('command')
        self.cmdMainAxisSys_command.description = ""
        self.sysMainAxisSys.addCommand(self.cmdMainAxisSys_command)
        self.addItem(self.mdMainAxisMode_Technical)
        self.mdMainAxisMode_Technical.ident = "n0::n2"
        self.mdMainAxisMode_Technical.setXMLName('Technical')
        self.mdMainAxisMode_Technical.description = ""
        self.sysMainAxis.addMode(self.mdMainAxisMode_Technical)
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
        # Marcamos MainAxisSysMode_Maintenance como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_Maintenance)
        # Marcamos MainAxisSysMode_PointingTech como elegible para MainAxisMode_Technical
        self.mdMainAxisMode_Technical.addSubMode(self.mdMainAxisSysMode_PointingTech)
        # Marcamos AzimuthMode_Homing como elegible para MainAxisSysMode_Homing
        self.mdMainAxisSysMode_Homing.addSubMode(self.mdAzimuthMode_Homing)
        # Marcamos AzimuthMode_Parking como elegible para MainAxisSysMode_Parking
        self.mdMainAxisSysMode_Parking.addSubMode(self.mdAzimuthMode_Parking)
        # Marcamos AzimuthMode_Maintenance como elegible para MainAxisSysMode_Maintenance
        self.mdMainAxisSysMode_Maintenance.addSubMode(self.mdAzimuthMode_Maintenance)
        # Marcamos AzimuthMode_Pointing como elegible para MainAxisSysMode_Pointing
        self.mdMainAxisSysMode_Pointing.addSubMode(self.mdAzimuthMode_Pointing)
        # Marcamos AzimuthMode_PointingTech como elegible para MainAxisSysMode_PointingTech
        self.mdMainAxisSysMode_PointingTech.addSubMode(self.mdAzimuthMode_PointingTech)
        # Marcamos Azimuth_Y_HOME como elegible para AzimuthMode_Homing
        self.mdAzimuthMode_Homing.addValue(self.vlAzimuth_Y_HOME)
        # Marcamos Azimuth_Y_PARK como elegible para AzimuthMode_Parking
        self.mdAzimuthMode_Parking.addValue(self.vlAzimuth_Y_PARK)
        # Marcamos Azimuth_Y_MAINT como elegible para AzimuthMode_Maintenance
        self.mdAzimuthMode_Maintenance.addValue(self.vlAzimuth_Y_MAINT)
        # Marcamos Azimuth_Y_angle como elegible para AzimuthMode_Pointing
        self.mdAzimuthMode_Pointing.addValue(self.vlAzimuth_Y_angle)
        # Marcamos Azimuth_Y_angle_unbound como elegible para AzimuthMode_PointingTech
        self.mdAzimuthMode_PointingTech.addValue(self.vlAzimuth_Y_angle_unbound)
        # Marcamos ElevationMode_Homing como elegible para MainAxisSysMode_Homing
        self.mdMainAxisSysMode_Homing.addSubMode(self.mdElevationMode_Homing)
        # Marcamos ElevationMode_Parking como elegible para MainAxisSysMode_Parking
        self.mdMainAxisSysMode_Parking.addSubMode(self.mdElevationMode_Parking)
        # Marcamos ElevationMode_Maintenance como elegible para MainAxisSysMode_Maintenance
        self.mdMainAxisSysMode_Maintenance.addSubMode(self.mdElevationMode_Maintenance)
        # Marcamos ElevationMode_Pointing como elegible para MainAxisSysMode_Pointing
        self.mdMainAxisSysMode_Pointing.addSubMode(self.mdElevationMode_Pointing)
        # Marcamos ElevationMode_PointingTech como elegible para MainAxisSysMode_PointingTech
        self.mdMainAxisSysMode_PointingTech.addSubMode(self.mdElevationMode_PointingTech)
        # Marcamos Elevation_P_HOME como elegible para ElevationMode_Homing
        self.mdElevationMode_Homing.addValue(self.vlElevation_P_HOME)
        # Marcamos Elevation_P_PARK como elegible para ElevationMode_Parking
        self.mdElevationMode_Parking.addValue(self.vlElevation_P_PARK)
        # Marcamos Elevation_P_MAINT como elegible para ElevationMode_Maintenance
        self.mdElevationMode_Maintenance.addValue(self.vlElevation_P_MAINT)
        # Marcamos Elevation_P_angle como elegible para ElevationMode_Pointing
        self.mdElevationMode_Pointing.addValue(self.vlElevation_P_angle)
        # Marcamos Elevation_P_angle_unbound como elegible para ElevationMode_PointingTech
        self.mdElevationMode_PointingTech.addValue(self.vlElevation_P_angle_unbound)

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


    ## prParam Azimuth 

    # Azimuth
    def get_Azimuth(self)-> PORISValue :
        return self.prAzimuth.getSelectedValue()

    def set_Azimuth(self, value: PORISValue)-> PORISValue :
        return self.prAzimuth.setValue(value)


    ## AzimuthMode 
    def get_AzimuthMode(self)-> PORISMode:
        return self.prAzimuth.getSelectedMode()

    def set_AzimuthMode(self, mode: PORISMode)-> PORISMode :
        return self.prAzimuth.selectMode(mode)


    ## prParam MainAxisSys 

    # AzimuthDouble  
    def get_AzimuthDouble(self)-> float :
        v = self.prAzimuth.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_AzimuthDouble(self, data: float)-> float :
        return self.prAzimuth.getSelectedValue().setData(data)


    ## prParam MainAxisSys 

    # AzimuthDouble  
    def get_AzimuthDouble(self)-> float :
        v = self.prAzimuth.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_AzimuthDouble(self, data: float)-> float :
        return self.prAzimuth.getSelectedValue().setData(data)


    ## prParam Elevation 

    # Elevation
    def get_Elevation(self)-> PORISValue :
        return self.prElevation.getSelectedValue()

    def set_Elevation(self, value: PORISValue)-> PORISValue :
        return self.prElevation.setValue(value)


    ## ElevationMode 
    def get_ElevationMode(self)-> PORISMode:
        return self.prElevation.getSelectedMode()

    def set_ElevationMode(self, mode: PORISMode)-> PORISMode :
        return self.prElevation.selectMode(mode)


    ## prParam MainAxisSys 

    # ElevationDouble  
    def get_ElevationDouble(self)-> float :
        v = self.prElevation.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ElevationDouble(self, data: float)-> float :
        return self.prElevation.getSelectedValue().setData(data)


    ## prParam MainAxisSys 

    # ElevationDouble  
    def get_ElevationDouble(self)-> float :
        v = self.prElevation.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_ElevationDouble(self, data: float)-> float :
        return self.prElevation.getSelectedValue().setData(data)


    ## Action trigger MainAxisSys_command ##
    def execMainAxisSys_command(self, *args, **kwargs) -> bool:
        return self.cmdMainAxisSys_command.defaultExecute(*args, **kwargs)

