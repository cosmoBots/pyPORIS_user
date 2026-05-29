from PORIS import *

class controlboxPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysControlBox = PORISSys("ControlBox")
        self.setRoot(self.sysControlBox)
        self.prOutputMux = PORISParam("OutputMux")
        self.sysControlLoop = PORISSys("ControlLoop")
        self.prKd = PORISParam("Kd")
        self.prKi = PORISParam("Ki")
        self.prKp = PORISParam("Kp")
        self.sysSubtractor = PORISSys("Subtractor")
        self.prRate = PORISParam("Rate")
        self.prSetPoint = PORISParam("SetPoint")
        self.mdOutputMuxMode_AllNothing = PORISMode("OutputMuxMode_AllNothing")
        self.mdOutputMuxMode_PID = PORISMode("OutputMuxMode_PID")
        self.mdOutputMuxMode_Abrupt = PORISMode("OutputMuxMode_Abrupt")
        self.mdOutputMuxMode_Keep = PORISMode("OutputMuxMode_Keep")
        self.mdOutputMuxMode_Sweet = PORISMode("OutputMuxMode_Sweet")
        self.vlOutputMux_CtrlLoopOutput = PORISValue("OutputMux_CtrlLoopOutput")
        self.vlOutputMux_CurrentOutput = PORISValue("OutputMux_CurrentOutput")
        self.vlOutputMux_0 = PORISValue("OutputMux_0")
        self.vlOutputMux_SubtractOutput = PORISValue("OutputMux_SubtractOutput")
        self.vlOutputMux_AllNothing = PORISValue("OutputMux_AllNothing")
        self.mdControlBoxMode_PI = PORISMode("ControlBoxMode_PI")
        self.mdControlBoxMode_P = PORISMode("ControlBoxMode_P")
        self.mdControlBoxMode_PID = PORISMode("ControlBoxMode_PID")
        self.mdControlBoxMode_Abrupt = PORISMode("ControlBoxMode_Abrupt")
        self.mdControlBoxMode_Keep = PORISMode("ControlBoxMode_Keep")
        self.mdControlBoxMode_Sweet = PORISMode("ControlBoxMode_Sweet")
        self.mdControlLoopMode_P = PORISMode("ControlLoopMode_P")
        self.vlKd_Range = PORISValueFloat("Kd_Range",0.0,0.01,0.5)
        self.mdKdMode_Normal = PORISMode("KdMode_Normal")
        self.vlKd_0 = PORISValue("Kd_0")
        self.mdKdMode_Disabled = PORISMode("KdMode_Disabled")
        self.vlKi_Range = PORISValueFloat("Ki_Range",0.0,0.01,0.5)
        self.mdKiMode_Normal = PORISMode("KiMode_Normal")
        self.vlKi_0 = PORISValue("Ki_0")
        self.mdKiMode_Disabled = PORISMode("KiMode_Disabled")
        self.vlKp_Range = PORISValueFloat("Kp_Range",0.0,0.01,0.5)
        self.mdKpMode_Normal = PORISMode("KpMode_Normal")
        self.mdControlLoopMode_PI = PORISMode("ControlLoopMode_PI")
        self.mdControlLoopMode_PID = PORISMode("ControlLoopMode_PID")
        self.vlRate_Range = PORISValueFloat("Rate_Range",0.0,0.01,0.5)
        self.mdRateMode_Active = PORISMode("RateMode_Active")
        self.mdSubtractorMode_Active = PORISMode("SubtractorMode_Active")
        self.mdControlBoxMode_AllNothing = PORISMode("ControlBoxMode_AllNothing")
        self.vlSetPoint_Range = PORISValueFloat("SetPoint_Range",0.0,0.01,0.5)
        self.mdSetPointMode_Normal = PORISMode("SetPointMode_Normal")
        self.mdControlBoxMode_Engineering = PORISMode("ControlBoxMode_Engineering")
        self.mdControlLoopMode_Engineering = PORISMode("ControlLoopMode_Engineering")
        self.mdSubtractorMode_Engineering = PORISMode("SubtractorMode_Engineering")
        self.addItem(self.sysControlBox)
        self.sysControlBox.ident = "n0"
        self.sysControlBox.setXMLName('ControlBox')
        self.sysControlBox.description = ""
        self.addItem(self.prOutputMux)
        self.prOutputMux.ident = "n0::n0"
        self.prOutputMux.setXMLName('OutputMux')
        self.prOutputMux.description = ""
        self.sysControlBox.addParam(self.prOutputMux)
        self.addItem(self.sysControlLoop)
        self.sysControlLoop.ident = "n0::n7"
        self.sysControlLoop.setXMLName('ControlLoop')
        self.sysControlLoop.description = ""
        self.sysControlBox.addSubsystem(self.sysControlLoop)
        self.addItem(self.prKd)
        self.prKd.ident = "n0::n7::n1"
        self.prKd.setXMLName('Kd')
        self.prKd.description = ""
        self.sysControlLoop.addParam(self.prKd)
        self.addItem(self.prKi)
        self.prKi.ident = "n0::n7::n2"
        self.prKi.setXMLName('Ki')
        self.prKi.description = ""
        self.sysControlLoop.addParam(self.prKi)
        self.addItem(self.prKp)
        self.prKp.ident = "n0::n7::n3"
        self.prKp.setXMLName('Kp')
        self.prKp.description = ""
        self.sysControlLoop.addParam(self.prKp)
        self.addItem(self.sysSubtractor)
        self.sysSubtractor.ident = "n0::n8"
        self.sysSubtractor.setXMLName('Subtractor')
        self.sysSubtractor.description = ""
        self.sysControlBox.addSubsystem(self.sysSubtractor)
        self.addItem(self.prRate)
        self.prRate.ident = "n0::n8::n0"
        self.prRate.setXMLName('Rate')
        self.prRate.description = ""
        self.sysSubtractor.addParam(self.prRate)
        self.addItem(self.prSetPoint)
        self.prSetPoint.ident = "n0::n10"
        self.prSetPoint.setXMLName('SetPoint')
        self.prSetPoint.description = ""
        self.sysControlBox.addParam(self.prSetPoint)
        self.addItem(self.mdOutputMuxMode_AllNothing)
        self.mdOutputMuxMode_AllNothing.ident = "n0::n0::n0"
        self.mdOutputMuxMode_AllNothing.setXMLName('AllNothing')
        self.mdOutputMuxMode_AllNothing.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_AllNothing)
        self.addItem(self.mdOutputMuxMode_PID)
        self.mdOutputMuxMode_PID.ident = "n0::n0::n1"
        self.mdOutputMuxMode_PID.setXMLName('PID')
        self.mdOutputMuxMode_PID.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_PID)
        self.addItem(self.mdOutputMuxMode_Abrupt)
        self.mdOutputMuxMode_Abrupt.ident = "n0::n0::n2"
        self.mdOutputMuxMode_Abrupt.setXMLName('Abrupt')
        self.mdOutputMuxMode_Abrupt.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Abrupt)
        self.addItem(self.mdOutputMuxMode_Keep)
        self.mdOutputMuxMode_Keep.ident = "n0::n0::n3"
        self.mdOutputMuxMode_Keep.setXMLName('Keep')
        self.mdOutputMuxMode_Keep.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Keep)
        self.addItem(self.mdOutputMuxMode_Sweet)
        self.mdOutputMuxMode_Sweet.ident = "n0::n0::n4"
        self.mdOutputMuxMode_Sweet.setXMLName('Sweet')
        self.mdOutputMuxMode_Sweet.description = ""
        self.prOutputMux.addMode(self.mdOutputMuxMode_Sweet)
        self.addItem(self.vlOutputMux_CtrlLoopOutput)
        self.vlOutputMux_CtrlLoopOutput.ident = "n0::n0::n5"
        self.vlOutputMux_CtrlLoopOutput.setXMLName('CtrlLoopOutput')
        self.vlOutputMux_CtrlLoopOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_CtrlLoopOutput)
        self.addItem(self.vlOutputMux_CurrentOutput)
        self.vlOutputMux_CurrentOutput.ident = "n0::n0::n6"
        self.vlOutputMux_CurrentOutput.setXMLName('CurrentOutput')
        self.vlOutputMux_CurrentOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_CurrentOutput)
        self.addItem(self.vlOutputMux_0)
        self.vlOutputMux_0.ident = "n0::n0::n7"
        self.vlOutputMux_0.setXMLName('0')
        self.vlOutputMux_0.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_0)
        self.addItem(self.vlOutputMux_SubtractOutput)
        self.vlOutputMux_SubtractOutput.ident = "n0::n0::n8"
        self.vlOutputMux_SubtractOutput.setXMLName('SubtractOutput')
        self.vlOutputMux_SubtractOutput.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_SubtractOutput)
        self.addItem(self.vlOutputMux_AllNothing)
        self.vlOutputMux_AllNothing.ident = "n0::n0::n9"
        self.vlOutputMux_AllNothing.setXMLName('AllNothing')
        self.vlOutputMux_AllNothing.description = ""
        self.prOutputMux.addValue(self.vlOutputMux_AllNothing)
        self.addItem(self.mdControlBoxMode_PI)
        self.mdControlBoxMode_PI.ident = "n0::n1"
        self.mdControlBoxMode_PI.setXMLName('PI')
        self.mdControlBoxMode_PI.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_PI)
        self.addItem(self.mdControlBoxMode_P)
        self.mdControlBoxMode_P.ident = "n0::n2"
        self.mdControlBoxMode_P.setXMLName('P')
        self.mdControlBoxMode_P.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_P)
        self.addItem(self.mdControlBoxMode_PID)
        self.mdControlBoxMode_PID.ident = "n0::n3"
        self.mdControlBoxMode_PID.setXMLName('PID')
        self.mdControlBoxMode_PID.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_PID)
        self.addItem(self.mdControlBoxMode_Abrupt)
        self.mdControlBoxMode_Abrupt.ident = "n0::n4"
        self.mdControlBoxMode_Abrupt.setXMLName('Abrupt')
        self.mdControlBoxMode_Abrupt.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Abrupt)
        self.addItem(self.mdControlBoxMode_Keep)
        self.mdControlBoxMode_Keep.ident = "n0::n5"
        self.mdControlBoxMode_Keep.setXMLName('Keep')
        self.mdControlBoxMode_Keep.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Keep)
        self.addItem(self.mdControlBoxMode_Sweet)
        self.mdControlBoxMode_Sweet.ident = "n0::n6"
        self.mdControlBoxMode_Sweet.setXMLName('Sweet')
        self.mdControlBoxMode_Sweet.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_Sweet)
        self.addItem(self.mdControlLoopMode_P)
        self.mdControlLoopMode_P.ident = "n0::n7::n0"
        self.mdControlLoopMode_P.setXMLName('P')
        self.mdControlLoopMode_P.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_P)
        self.addItem(self.vlKd_Range)
        self.vlKd_Range.ident = "n0::n7::n1::n0"
        self.vlKd_Range.setXMLName('Range')
        self.vlKd_Range.description = ""
        self.prKd.addValue(self.vlKd_Range)
        self.addItem(self.mdKdMode_Normal)
        self.mdKdMode_Normal.ident = "n0::n7::n1::n1"
        self.mdKdMode_Normal.setXMLName('Normal')
        self.mdKdMode_Normal.description = ""
        self.prKd.addMode(self.mdKdMode_Normal)
        self.addItem(self.vlKd_0)
        self.vlKd_0.ident = "n0::n7::n1::n2"
        self.vlKd_0.setXMLName('0')
        self.vlKd_0.description = ""
        self.prKd.addValue(self.vlKd_0)
        self.addItem(self.mdKdMode_Disabled)
        self.mdKdMode_Disabled.ident = "n0::n7::n1::n3"
        self.mdKdMode_Disabled.setXMLName('Disabled')
        self.mdKdMode_Disabled.description = ""
        self.prKd.addMode(self.mdKdMode_Disabled)
        self.addItem(self.vlKi_Range)
        self.vlKi_Range.ident = "n0::n7::n2::n0"
        self.vlKi_Range.setXMLName('Range')
        self.vlKi_Range.description = ""
        self.prKi.addValue(self.vlKi_Range)
        self.addItem(self.mdKiMode_Normal)
        self.mdKiMode_Normal.ident = "n0::n7::n2::n1"
        self.mdKiMode_Normal.setXMLName('Normal')
        self.mdKiMode_Normal.description = ""
        self.prKi.addMode(self.mdKiMode_Normal)
        self.addItem(self.vlKi_0)
        self.vlKi_0.ident = "n0::n7::n2::n2"
        self.vlKi_0.setXMLName('0')
        self.vlKi_0.description = ""
        self.prKi.addValue(self.vlKi_0)
        self.addItem(self.mdKiMode_Disabled)
        self.mdKiMode_Disabled.ident = "n0::n7::n2::n3"
        self.mdKiMode_Disabled.setXMLName('Disabled')
        self.mdKiMode_Disabled.description = ""
        self.prKi.addMode(self.mdKiMode_Disabled)
        self.addItem(self.vlKp_Range)
        self.vlKp_Range.ident = "n0::n7::n3::n0"
        self.vlKp_Range.setXMLName('Range')
        self.vlKp_Range.description = ""
        self.prKp.addValue(self.vlKp_Range)
        self.addItem(self.mdKpMode_Normal)
        self.mdKpMode_Normal.ident = "n0::n7::n3::n1"
        self.mdKpMode_Normal.setXMLName('Normal')
        self.mdKpMode_Normal.description = ""
        self.prKp.addMode(self.mdKpMode_Normal)
        self.addItem(self.mdControlLoopMode_PI)
        self.mdControlLoopMode_PI.ident = "n0::n7::n4"
        self.mdControlLoopMode_PI.setXMLName('PI')
        self.mdControlLoopMode_PI.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_PI)
        self.addItem(self.mdControlLoopMode_PID)
        self.mdControlLoopMode_PID.ident = "n0::n7::n5"
        self.mdControlLoopMode_PID.setXMLName('PID')
        self.mdControlLoopMode_PID.description = ""
        self.sysControlLoop.addMode(self.mdControlLoopMode_PID)
        self.addItem(self.vlRate_Range)
        self.vlRate_Range.ident = "n0::n8::n0::n0"
        self.vlRate_Range.setXMLName('Range')
        self.vlRate_Range.description = ""
        self.prRate.addValue(self.vlRate_Range)
        self.addItem(self.mdRateMode_Active)
        self.mdRateMode_Active.ident = "n0::n8::n0::n1"
        self.mdRateMode_Active.setXMLName('Active')
        self.mdRateMode_Active.description = ""
        self.prRate.addMode(self.mdRateMode_Active)
        self.addItem(self.mdSubtractorMode_Active)
        self.mdSubtractorMode_Active.ident = "n0::n8::n1"
        self.mdSubtractorMode_Active.setXMLName('Active')
        self.mdSubtractorMode_Active.description = ""
        self.sysSubtractor.addMode(self.mdSubtractorMode_Active)
        self.addItem(self.mdControlBoxMode_AllNothing)
        self.mdControlBoxMode_AllNothing.ident = "n0::n9"
        self.mdControlBoxMode_AllNothing.setXMLName('AllNothing')
        self.mdControlBoxMode_AllNothing.description = ""
        self.sysControlBox.addMode(self.mdControlBoxMode_AllNothing)
        self.addItem(self.vlSetPoint_Range)
        self.vlSetPoint_Range.ident = "n0::n10::n0"
        self.vlSetPoint_Range.setXMLName('Range')
        self.vlSetPoint_Range.description = ""
        self.prSetPoint.addValue(self.vlSetPoint_Range)
        self.addItem(self.mdSetPointMode_Normal)
        self.mdSetPointMode_Normal.ident = "n0::n10::n1"
        self.mdSetPointMode_Normal.setXMLName('Normal')
        self.mdSetPointMode_Normal.description = ""
        self.prSetPoint.addMode(self.mdSetPointMode_Normal)
        self.addItem(self.mdControlBoxMode_Engineering)
        self.mdControlBoxMode_Engineering.ident = "ENG-1"
        self.mdControlBoxMode_Engineering.setXMLName('Engineering')
        self.mdControlBoxMode_Engineering.description = "ControlBox_engineering_mode"
        self.sysControlBox.addMode(self.mdControlBoxMode_Engineering)
        self.addItem(self.mdControlLoopMode_Engineering)
        self.mdControlLoopMode_Engineering.ident = "ENG-2"
        self.mdControlLoopMode_Engineering.setXMLName('Engineering')
        self.mdControlLoopMode_Engineering.description = "ControlLoop_engineering_mode"
        self.sysControlLoop.addMode(self.mdControlLoopMode_Engineering)
        self.addItem(self.mdSubtractorMode_Engineering)
        self.mdSubtractorMode_Engineering.ident = "ENG-3"
        self.mdSubtractorMode_Engineering.setXMLName('Engineering')
        self.mdSubtractorMode_Engineering.description = "Subtractor_engineering_mode"
        self.sysSubtractor.addMode(self.mdSubtractorMode_Engineering)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_Abrupt como elegible para ControlBoxMode_Abrupt
        self.mdControlBoxMode_Abrupt.addSubMode(self.mdOutputMuxMode_Abrupt)
        # Marcamos OutputMuxMode_Keep como elegible para ControlBoxMode_Keep
        self.mdControlBoxMode_Keep.addSubMode(self.mdOutputMuxMode_Keep)
        # Marcamos OutputMuxMode_Sweet como elegible para ControlBoxMode_Sweet
        self.mdControlBoxMode_Sweet.addSubMode(self.mdOutputMuxMode_Sweet)
        # Marcamos OutputMuxMode_AllNothing como elegible para ControlBoxMode_AllNothing
        self.mdControlBoxMode_AllNothing.addSubMode(self.mdOutputMuxMode_AllNothing)
        # Marcamos OutputMuxMode_AllNothing como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_AllNothing)
        # Marcamos OutputMuxMode_PID como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_PID)
        # Marcamos OutputMuxMode_Abrupt como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Abrupt)
        # Marcamos OutputMuxMode_Keep como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Keep)
        # Marcamos OutputMuxMode_Sweet como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdOutputMuxMode_Sweet)
        # Marcamos OutputMux_AllNothing como elegible para OutputMuxMode_AllNothing
        self.mdOutputMuxMode_AllNothing.addValue(self.vlOutputMux_AllNothing)
        # Marcamos OutputMux_CtrlLoopOutput como elegible para OutputMuxMode_PID
        self.mdOutputMuxMode_PID.addValue(self.vlOutputMux_CtrlLoopOutput)
        # Marcamos OutputMux_0 como elegible para OutputMuxMode_Abrupt
        self.mdOutputMuxMode_Abrupt.addValue(self.vlOutputMux_0)
        # Marcamos OutputMux_CurrentOutput como elegible para OutputMuxMode_Keep
        self.mdOutputMuxMode_Keep.addValue(self.vlOutputMux_CurrentOutput)
        # Marcamos OutputMux_SubtractOutput como elegible para OutputMuxMode_Sweet
        self.mdOutputMuxMode_Sweet.addValue(self.vlOutputMux_SubtractOutput)
        # Marcamos ControlLoopMode_PI como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdControlLoopMode_PI)
        # Marcamos ControlLoopMode_P como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdControlLoopMode_P)
        # Marcamos ControlLoopMode_PID como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdControlLoopMode_PID)
        # Marcamos ControlLoopMode_P como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_P)
        # Marcamos ControlLoopMode_PI como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_PI)
        # Marcamos ControlLoopMode_PID como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_PID)
        # Marcamos ControlLoopMode_Engineering como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdControlLoopMode_Engineering)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKdMode_Disabled)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKdMode_Disabled)
        # Marcamos KdMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKdMode_Normal)
        # Marcamos KdMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKdMode_Normal)
        # Marcamos KdMode_Disabled como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKdMode_Disabled)
        # Marcamos Kd_Range como elegible para KdMode_Normal
        self.mdKdMode_Normal.addValue(self.vlKd_Range)
        # Marcamos Kd_0 como elegible para KdMode_Disabled
        self.mdKdMode_Disabled.addValue(self.vlKd_0)
        # Marcamos KiMode_Disabled como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKiMode_Disabled)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKiMode_Normal)
        # Marcamos KiMode_Disabled como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKiMode_Disabled)
        # Marcamos Ki_Range como elegible para KiMode_Normal
        self.mdKiMode_Normal.addValue(self.vlKi_Range)
        # Marcamos Ki_0 como elegible para KiMode_Disabled
        self.mdKiMode_Disabled.addValue(self.vlKi_0)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_P
        self.mdControlLoopMode_P.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_PI
        self.mdControlLoopMode_PI.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_PID
        self.mdControlLoopMode_PID.addSubMode(self.mdKpMode_Normal)
        # Marcamos KpMode_Normal como elegible para ControlLoopMode_Engineering
        self.mdControlLoopMode_Engineering.addSubMode(self.mdKpMode_Normal)
        # Marcamos Kp_Range como elegible para KpMode_Normal
        self.mdKpMode_Normal.addValue(self.vlKp_Range)
        # Marcamos SubtractorMode_Active como elegible para ControlBoxMode_Sweet
        self.mdControlBoxMode_Sweet.addSubMode(self.mdSubtractorMode_Active)
        # Marcamos SubtractorMode_Active como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSubtractorMode_Active)
        # Marcamos SubtractorMode_Engineering como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSubtractorMode_Engineering)
        # Marcamos RateMode_Active como elegible para SubtractorMode_Active
        self.mdSubtractorMode_Active.addSubMode(self.mdRateMode_Active)
        # Marcamos RateMode_Active como elegible para SubtractorMode_Engineering
        self.mdSubtractorMode_Engineering.addSubMode(self.mdRateMode_Active)
        # Marcamos Rate_Range como elegible para RateMode_Active
        self.mdRateMode_Active.addValue(self.vlRate_Range)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_PI
        self.mdControlBoxMode_PI.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_P
        self.mdControlBoxMode_P.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_PID
        self.mdControlBoxMode_PID.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_AllNothing
        self.mdControlBoxMode_AllNothing.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPointMode_Normal como elegible para ControlBoxMode_Engineering
        self.mdControlBoxMode_Engineering.addSubMode(self.mdSetPointMode_Normal)
        # Marcamos SetPoint_Range como elegible para SetPointMode_Normal
        self.mdSetPointMode_Normal.addValue(self.vlSetPoint_Range)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## ControlBoxMode 
    def get_ControlBoxMode(self)-> PORISMode:
        return self.sysControlBox.getSelectedMode()

    def set_ControlBoxMode(self, mode: PORISMode)-> PORISMode :
        return self.sysControlBox.selectMode(mode)


    ## prParam OutputMux 

    # OutputMux
    def get_OutputMux(self)-> PORISValue :
        return self.prOutputMux.getSelectedValue()

    def set_OutputMux(self, value: PORISValue)-> PORISValue :
        return self.prOutputMux.setValue(value)


    ## OutputMuxMode 
    def get_OutputMuxMode(self)-> PORISMode:
        return self.prOutputMux.getSelectedMode()

    def set_OutputMuxMode(self, mode: PORISMode)-> PORISMode :
        return self.prOutputMux.selectMode(mode)


    ## ControlLoopMode 
    def get_ControlLoopMode(self)-> PORISMode:
        return self.sysControlLoop.getSelectedMode()

    def set_ControlLoopMode(self, mode: PORISMode)-> PORISMode :
        return self.sysControlLoop.selectMode(mode)


    ## prParam Kd 

    # Kd
    def get_Kd(self)-> PORISValue :
        return self.prKd.getSelectedValue()

    def set_Kd(self, value: PORISValue)-> PORISValue :
        return self.prKd.setValue(value)


    ## KdMode 
    def get_KdMode(self)-> PORISMode:
        return self.prKd.getSelectedMode()

    def set_KdMode(self, mode: PORISMode)-> PORISMode :
        return self.prKd.selectMode(mode)


    ## prParam ControlLoop 

    # KdDouble  
    def get_KdDouble(self)-> float :
        v = self.prKd.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KdDouble(self, data: float)-> float :
        return self.prKd.getSelectedValue().setData(data)


    ## prParam Ki 

    # Ki
    def get_Ki(self)-> PORISValue :
        return self.prKi.getSelectedValue()

    def set_Ki(self, value: PORISValue)-> PORISValue :
        return self.prKi.setValue(value)


    ## KiMode 
    def get_KiMode(self)-> PORISMode:
        return self.prKi.getSelectedMode()

    def set_KiMode(self, mode: PORISMode)-> PORISMode :
        return self.prKi.selectMode(mode)


    ## prParam ControlLoop 

    # KiDouble  
    def get_KiDouble(self)-> float :
        v = self.prKi.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KiDouble(self, data: float)-> float :
        return self.prKi.getSelectedValue().setData(data)


    ## prParam Kp 

    # Kp
    def get_Kp(self)-> PORISValue :
        return self.prKp.getSelectedValue()

    def set_Kp(self, value: PORISValue)-> PORISValue :
        return self.prKp.setValue(value)


    ## KpMode 
    def get_KpMode(self)-> PORISMode:
        return self.prKp.getSelectedMode()

    def set_KpMode(self, mode: PORISMode)-> PORISMode :
        return self.prKp.selectMode(mode)


    ## prParam ControlLoop 

    # KpDouble  
    def get_KpDouble(self)-> float :
        v = self.prKp.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_KpDouble(self, data: float)-> float :
        return self.prKp.getSelectedValue().setData(data)


    ## SubtractorMode 
    def get_SubtractorMode(self)-> PORISMode:
        return self.sysSubtractor.getSelectedMode()

    def set_SubtractorMode(self, mode: PORISMode)-> PORISMode :
        return self.sysSubtractor.selectMode(mode)


    ## prParam Rate 

    # Rate
    def get_Rate(self)-> PORISValue :
        return self.prRate.getSelectedValue()

    def set_Rate(self, value: PORISValue)-> PORISValue :
        return self.prRate.setValue(value)


    ## RateMode 
    def get_RateMode(self)-> PORISMode:
        return self.prRate.getSelectedMode()

    def set_RateMode(self, mode: PORISMode)-> PORISMode :
        return self.prRate.selectMode(mode)


    ## prParam Subtractor 

    # RateDouble  
    def get_RateDouble(self)-> float :
        v = self.prRate.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RateDouble(self, data: float)-> float :
        return self.prRate.getSelectedValue().setData(data)


    ## prParam SetPoint 

    # SetPoint
    def get_SetPoint(self)-> PORISValue :
        return self.prSetPoint.getSelectedValue()

    def set_SetPoint(self, value: PORISValue)-> PORISValue :
        return self.prSetPoint.setValue(value)


    ## SetPointMode 
    def get_SetPointMode(self)-> PORISMode:
        return self.prSetPoint.getSelectedMode()

    def set_SetPointMode(self, mode: PORISMode)-> PORISMode :
        return self.prSetPoint.selectMode(mode)


    ## prParam ControlBox 

    # SetPointDouble  
    def get_SetPointDouble(self)-> float :
        v = self.prSetPoint.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_SetPointDouble(self, data: float)-> float :
        return self.prSetPoint.getSelectedValue().setData(data)

