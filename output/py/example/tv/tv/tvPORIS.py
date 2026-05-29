from PORIS import *

class tvPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysTV = PORISSys("TV")
        self.setRoot(self.sysTV)
        self.sysEntrada = PORISSys("Entrada")
        self.prAudio = PORISParam("Audio")
        self.sysAntena = PORISSys("Antena")
        self.prCanal = PORISParam("Canal")
        self.prBanda = PORISParam("Banda")
        self.mdTVMode_Antena = PORISMode("TVMode_Antena")
        self.mdTVMode_AV = PORISMode("TVMode_AV")
        self.mdEntradaMode_HDMI1 = PORISMode("EntradaMode_HDMI1")
        self.mdEntradaMode_HDMI2 = PORISMode("EntradaMode_HDMI2")
        self.mdEntradaMode_AUX = PORISMode("EntradaMode_AUX")
        self.mdEntradaMode_VGA = PORISMode("EntradaMode_VGA")
        self.vlAudio_Jack = PORISValue("Audio_Jack")
        self.vlAudio_RCA = PORISValue("Audio_RCA")
        self.mdAudioMode_Mode = PORISMode("AudioMode_Mode")
        self.vlCanal_Rango_Analogico = PORISValueFloat("Canal_Rango_Analogico",1.0,1.0,16.0)
        self.mdCanalMode_Digital = PORISMode("CanalMode_Digital")
        self.mdCanalMode_Analogico = PORISMode("CanalMode_Analogico")
        self.vlCanal_Rango_Digital = PORISValueFloat("Canal_Rango_Digital",1.0,1.0,999.0)
        self.vlBanda_UHF = PORISValue("Banda_UHF")
        self.vlBanda_VHF = PORISValue("Banda_VHF")
        self.mdBandaMode_Analogico = PORISMode("BandaMode_Analogico")
        self.mdAntenaMode_Digital = PORISMode("AntenaMode_Digital")
        self.mdAntenaMode_Analogico = PORISMode("AntenaMode_Analogico")
        self.cmdTV_Apply = PORISCmd("TV_Apply")
        self.mdTVMode_Engineering = PORISMode("TVMode_Engineering")
        self.mdEntradaMode_Engineering = PORISMode("EntradaMode_Engineering")
        self.mdAntenaMode_Engineering = PORISMode("AntenaMode_Engineering")
        self.addItem(self.sysTV)
        self.sysTV.ident = "n0"
        self.sysTV.setXMLName('TV')
        self.sysTV.description = ""
        self.addItem(self.sysEntrada)
        self.sysEntrada.ident = "n0::n2"
        self.sysEntrada.setXMLName('Entrada')
        self.sysEntrada.description = ""
        self.sysTV.addSubsystem(self.sysEntrada)
        self.addItem(self.prAudio)
        self.prAudio.ident = "n0::n2::n4"
        self.prAudio.setXMLName('Audio')
        self.prAudio.description = ""
        self.sysEntrada.addParam(self.prAudio)
        self.addItem(self.sysAntena)
        self.sysAntena.ident = "n0::n3"
        self.sysAntena.setXMLName('Antena')
        self.sysAntena.description = ""
        self.sysTV.addSubsystem(self.sysAntena)
        self.addItem(self.prCanal)
        self.prCanal.ident = "n0::n3::n0"
        self.prCanal.setXMLName('Canal')
        self.prCanal.description = ""
        self.sysAntena.addParam(self.prCanal)
        self.addItem(self.prBanda)
        self.prBanda.ident = "n0::n3::n1"
        self.prBanda.setXMLName('Banda')
        self.prBanda.description = ""
        self.sysAntena.addParam(self.prBanda)
        self.addItem(self.mdTVMode_Antena)
        self.mdTVMode_Antena.ident = "n0::n0"
        self.mdTVMode_Antena.setXMLName('Antena')
        self.mdTVMode_Antena.description = ""
        self.sysTV.addMode(self.mdTVMode_Antena)
        self.addItem(self.mdTVMode_AV)
        self.mdTVMode_AV.ident = "n0::n1"
        self.mdTVMode_AV.setXMLName('AV')
        self.mdTVMode_AV.description = ""
        self.sysTV.addMode(self.mdTVMode_AV)
        self.addItem(self.mdEntradaMode_HDMI1)
        self.mdEntradaMode_HDMI1.ident = "n0::n2::n0"
        self.mdEntradaMode_HDMI1.setXMLName('HDMI1')
        self.mdEntradaMode_HDMI1.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_HDMI1)
        self.addItem(self.mdEntradaMode_HDMI2)
        self.mdEntradaMode_HDMI2.ident = "n0::n2::n1"
        self.mdEntradaMode_HDMI2.setXMLName('HDMI2')
        self.mdEntradaMode_HDMI2.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_HDMI2)
        self.addItem(self.mdEntradaMode_AUX)
        self.mdEntradaMode_AUX.ident = "n0::n2::n2"
        self.mdEntradaMode_AUX.setXMLName('AUX')
        self.mdEntradaMode_AUX.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_AUX)
        self.addItem(self.mdEntradaMode_VGA)
        self.mdEntradaMode_VGA.ident = "n0::n2::n3"
        self.mdEntradaMode_VGA.setXMLName('VGA')
        self.mdEntradaMode_VGA.description = ""
        self.sysEntrada.addMode(self.mdEntradaMode_VGA)
        self.addItem(self.vlAudio_Jack)
        self.vlAudio_Jack.ident = "n0::n2::n4::n0"
        self.vlAudio_Jack.setXMLName('Jack')
        self.vlAudio_Jack.description = ""
        self.prAudio.addValue(self.vlAudio_Jack)
        self.addItem(self.vlAudio_RCA)
        self.vlAudio_RCA.ident = "n0::n2::n4::n1"
        self.vlAudio_RCA.setXMLName('RCA')
        self.vlAudio_RCA.description = ""
        self.prAudio.addValue(self.vlAudio_RCA)
        self.addItem(self.mdAudioMode_Mode)
        self.mdAudioMode_Mode.ident = "n0::n2::n4::n2"
        self.mdAudioMode_Mode.setXMLName('Mode')
        self.mdAudioMode_Mode.description = ""
        self.prAudio.addMode(self.mdAudioMode_Mode)
        self.addItem(self.vlCanal_Rango_Analogico)
        self.vlCanal_Rango_Analogico.ident = "n0::n3::n0::n0"
        self.vlCanal_Rango_Analogico.setXMLName('Rango_Analogico')
        self.vlCanal_Rango_Analogico.description = ""
        self.prCanal.addValue(self.vlCanal_Rango_Analogico)
        self.addItem(self.mdCanalMode_Digital)
        self.mdCanalMode_Digital.ident = "n0::n3::n0::n1"
        self.mdCanalMode_Digital.setXMLName('Digital')
        self.mdCanalMode_Digital.description = ""
        self.prCanal.addMode(self.mdCanalMode_Digital)
        self.addItem(self.mdCanalMode_Analogico)
        self.mdCanalMode_Analogico.ident = "n0::n3::n0::n2"
        self.mdCanalMode_Analogico.setXMLName('Analogico')
        self.mdCanalMode_Analogico.description = ""
        self.prCanal.addMode(self.mdCanalMode_Analogico)
        self.addItem(self.vlCanal_Rango_Digital)
        self.vlCanal_Rango_Digital.ident = "n0::n3::n0::n3"
        self.vlCanal_Rango_Digital.setXMLName('Rango_Digital')
        self.vlCanal_Rango_Digital.description = ""
        self.prCanal.addValue(self.vlCanal_Rango_Digital)
        self.addItem(self.vlBanda_UHF)
        self.vlBanda_UHF.ident = "n0::n3::n1::n0"
        self.vlBanda_UHF.setXMLName('UHF')
        self.vlBanda_UHF.description = ""
        self.prBanda.addValue(self.vlBanda_UHF)
        self.addItem(self.vlBanda_VHF)
        self.vlBanda_VHF.ident = "n0::n3::n1::n1"
        self.vlBanda_VHF.setXMLName('VHF')
        self.vlBanda_VHF.description = ""
        self.prBanda.addValue(self.vlBanda_VHF)
        self.addItem(self.mdBandaMode_Analogico)
        self.mdBandaMode_Analogico.ident = "n0::n3::n1::n2"
        self.mdBandaMode_Analogico.setXMLName('Analógico')
        self.mdBandaMode_Analogico.description = ""
        self.prBanda.addMode(self.mdBandaMode_Analogico)
        self.addItem(self.mdAntenaMode_Digital)
        self.mdAntenaMode_Digital.ident = "n0::n3::n2"
        self.mdAntenaMode_Digital.setXMLName('Digital')
        self.mdAntenaMode_Digital.description = ""
        self.sysAntena.addMode(self.mdAntenaMode_Digital)
        self.addItem(self.mdAntenaMode_Analogico)
        self.mdAntenaMode_Analogico.ident = "n0::n3::n3"
        self.mdAntenaMode_Analogico.setXMLName('Analogico')
        self.mdAntenaMode_Analogico.description = ""
        self.sysAntena.addMode(self.mdAntenaMode_Analogico)
        self.addItem(self.cmdTV_Apply)
        self.cmdTV_Apply.setActionName("Apply")
        self.cmdTV_Apply.setHandlerName("execTV_Apply")
        self.cmdTV_Apply.setTracePath("sysTV.Apply")
        self.cmdTV_Apply.ident = "n0::n4"
        self.cmdTV_Apply.setXMLName('Apply')
        self.cmdTV_Apply.description = ""
        self.sysTV.addCommand(self.cmdTV_Apply)
        self.addItem(self.mdTVMode_Engineering)
        self.mdTVMode_Engineering.ident = "ENG-1"
        self.mdTVMode_Engineering.setXMLName('Engineering')
        self.mdTVMode_Engineering.description = "TV_engineering_mode"
        self.sysTV.addMode(self.mdTVMode_Engineering)
        self.addItem(self.mdEntradaMode_Engineering)
        self.mdEntradaMode_Engineering.ident = "ENG-2"
        self.mdEntradaMode_Engineering.setXMLName('Engineering')
        self.mdEntradaMode_Engineering.description = "Entrada_engineering_mode"
        self.sysEntrada.addMode(self.mdEntradaMode_Engineering)
        self.addItem(self.mdAntenaMode_Engineering)
        self.mdAntenaMode_Engineering.ident = "ENG-3"
        self.mdAntenaMode_Engineering.setXMLName('Engineering')
        self.mdAntenaMode_Engineering.description = "Antena_engineering_mode"
        self.sysAntena.addMode(self.mdAntenaMode_Engineering)
        # Marcamos EntradaMode_HDMI1 como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_HDMI1)
        # Marcamos EntradaMode_HDMI2 como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_HDMI2)
        # Marcamos EntradaMode_AUX como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_AUX)
        # Marcamos EntradaMode_VGA como elegible para TVMode_AV
        self.mdTVMode_AV.addSubMode(self.mdEntradaMode_VGA)
        # Marcamos EntradaMode_HDMI1 como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_HDMI1)
        # Marcamos EntradaMode_HDMI2 como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_HDMI2)
        # Marcamos EntradaMode_AUX como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_AUX)
        # Marcamos EntradaMode_VGA como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_VGA)
        # Marcamos EntradaMode_Engineering como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdEntradaMode_Engineering)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_AUX
        self.mdEntradaMode_AUX.addSubMode(self.mdAudioMode_Mode)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_VGA
        self.mdEntradaMode_VGA.addSubMode(self.mdAudioMode_Mode)
        # Marcamos AudioMode_Mode como elegible para EntradaMode_Engineering
        self.mdEntradaMode_Engineering.addSubMode(self.mdAudioMode_Mode)
        # Marcamos Audio_Jack como elegible para AudioMode_Mode
        self.mdAudioMode_Mode.addValue(self.vlAudio_Jack)
        # Marcamos Audio_RCA como elegible para AudioMode_Mode
        self.mdAudioMode_Mode.addValue(self.vlAudio_RCA)
        # Marcamos AntenaMode_Analogico como elegible para TVMode_Antena
        self.mdTVMode_Antena.addSubMode(self.mdAntenaMode_Analogico)
        # Marcamos AntenaMode_Digital como elegible para TVMode_Antena
        self.mdTVMode_Antena.addSubMode(self.mdAntenaMode_Digital)
        # Marcamos AntenaMode_Digital como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Digital)
        # Marcamos AntenaMode_Analogico como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Analogico)
        # Marcamos AntenaMode_Engineering como elegible para TVMode_Engineering
        self.mdTVMode_Engineering.addSubMode(self.mdAntenaMode_Engineering)
        # Marcamos CanalMode_Digital como elegible para AntenaMode_Digital
        self.mdAntenaMode_Digital.addSubMode(self.mdCanalMode_Digital)
        # Marcamos CanalMode_Analogico como elegible para AntenaMode_Analogico
        self.mdAntenaMode_Analogico.addSubMode(self.mdCanalMode_Analogico)
        # Marcamos CanalMode_Digital como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdCanalMode_Digital)
        # Marcamos CanalMode_Analogico como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdCanalMode_Analogico)
        # Marcamos Canal_Rango_Digital como elegible para CanalMode_Digital
        self.mdCanalMode_Digital.addValue(self.vlCanal_Rango_Digital)
        # Marcamos Canal_Rango_Analogico como elegible para CanalMode_Analogico
        self.mdCanalMode_Analogico.addValue(self.vlCanal_Rango_Analogico)
        # Marcamos BandaMode_Analogico como elegible para AntenaMode_Analogico
        self.mdAntenaMode_Analogico.addSubMode(self.mdBandaMode_Analogico)
        # Marcamos BandaMode_Analogico como elegible para AntenaMode_Engineering
        self.mdAntenaMode_Engineering.addSubMode(self.mdBandaMode_Analogico)
        # Marcamos Banda_UHF como elegible para BandaMode_Analogico
        self.mdBandaMode_Analogico.addValue(self.vlBanda_UHF)
        # Marcamos Banda_VHF como elegible para BandaMode_Analogico
        self.mdBandaMode_Analogico.addValue(self.vlBanda_VHF)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## TVMode 
    def get_TVMode(self)-> PORISMode:
        return self.sysTV.getSelectedMode()

    def set_TVMode(self, mode: PORISMode)-> PORISMode :
        return self.sysTV.selectMode(mode)


    ## EntradaMode 
    def get_EntradaMode(self)-> PORISMode:
        return self.sysEntrada.getSelectedMode()

    def set_EntradaMode(self, mode: PORISMode)-> PORISMode :
        return self.sysEntrada.selectMode(mode)


    ## prParam Audio 

    # Audio
    def get_Audio(self)-> PORISValue :
        return self.prAudio.getSelectedValue()

    def set_Audio(self, value: PORISValue)-> PORISValue :
        return self.prAudio.setValue(value)


    ## AudioMode 
    def get_AudioMode(self)-> PORISMode:
        return self.prAudio.getSelectedMode()

    def set_AudioMode(self, mode: PORISMode)-> PORISMode :
        return self.prAudio.selectMode(mode)


    ## AntenaMode 
    def get_AntenaMode(self)-> PORISMode:
        return self.sysAntena.getSelectedMode()

    def set_AntenaMode(self, mode: PORISMode)-> PORISMode :
        return self.sysAntena.selectMode(mode)


    ## prParam Canal 

    # Canal
    def get_Canal(self)-> PORISValue :
        return self.prCanal.getSelectedValue()

    def set_Canal(self, value: PORISValue)-> PORISValue :
        return self.prCanal.setValue(value)


    ## CanalMode 
    def get_CanalMode(self)-> PORISMode:
        return self.prCanal.getSelectedMode()

    def set_CanalMode(self, mode: PORISMode)-> PORISMode :
        return self.prCanal.selectMode(mode)


    ## prParam Antena 

    # CanalDouble  
    def get_CanalDouble(self)-> float :
        v = self.prCanal.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CanalDouble(self, data: float)-> float :
        return self.prCanal.getSelectedValue().setData(data)


    ## prParam Antena 

    # CanalDouble  
    def get_CanalDouble(self)-> float :
        v = self.prCanal.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_CanalDouble(self, data: float)-> float :
        return self.prCanal.getSelectedValue().setData(data)


    ## prParam Banda 

    # Banda
    def get_Banda(self)-> PORISValue :
        return self.prBanda.getSelectedValue()

    def set_Banda(self, value: PORISValue)-> PORISValue :
        return self.prBanda.setValue(value)


    ## BandaMode 
    def get_BandaMode(self)-> PORISMode:
        return self.prBanda.getSelectedMode()

    def set_BandaMode(self, mode: PORISMode)-> PORISMode :
        return self.prBanda.selectMode(mode)


    ## Action trigger TV_Apply ##
    def execTV_Apply(self, *args, **kwargs) -> bool:
        return self.cmdTV_Apply.defaultExecute(*args, **kwargs)

