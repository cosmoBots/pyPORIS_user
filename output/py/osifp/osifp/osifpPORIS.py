from PORIS import *

class osifpPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysFPE = PORISSys("FPE")
        self.setRoot(self.sysFPE)
        self.prFocalPlaneElement = PORISParam("FocalPlaneElement")
        self.mdFocalPlaneElementMode_Disabled = PORISMode("FocalPlaneElementMode_Disabled")
        self.vlFocalPlaneElement_LS0_4 = PORISValue("FocalPlaneElement_LS0_4")
        self.vlFocalPlaneElement_LS0_6 = PORISValue("FocalPlaneElement_LS0_6")
        self.vlFocalPlaneElement_LS0_8 = PORISValue("FocalPlaneElement_LS0_8")
        self.vlFocalPlaneElement_LS1_0 = PORISValue("FocalPlaneElement_LS1_0")
        self.vlFocalPlaneElement_LS1_2 = PORISValue("FocalPlaneElement_LS1_2")
        self.vlFocalPlaneElement_LS1_5 = PORISValue("FocalPlaneElement_LS1_5")
        self.vlFocalPlaneElement_LS1_8 = PORISValue("FocalPlaneElement_LS1_8")
        self.vlFocalPlaneElement_LS2_5 = PORISValue("FocalPlaneElement_LS2_5")
        self.vlFocalPlaneElement_LS3_0 = PORISValue("FocalPlaneElement_LS3_0")
        self.vlFocalPlaneElement_LS5_0 = PORISValue("FocalPlaneElement_LS5_0")
        self.vlFocalPlaneElement_LS10_0 = PORISValue("FocalPlaneElement_LS10_0")
        self.vlFocalPlaneElement_LS12_0 = PORISValue("FocalPlaneElement_LS12_0")
        self.vlFocalPlaneElement_LS40_0 = PORISValue("FocalPlaneElement_LS40_0")
        self.mdFocalPlaneElementMode_MOS = PORISMode("FocalPlaneElementMode_MOS")
        self.mdFocalPlaneElementMode_FastPhotometry = PORISMode("FocalPlaneElementMode_FastPhotometry")
        self.mdFocalPlaneElementMode_FrameTransfer = PORISMode("FocalPlaneElementMode_FrameTransfer")
        self.mdFocalPlaneElementMode_LS = PORISMode("FocalPlaneElementMode_LS")
        self.vlFocalPlaneElement_FrameTransferMask = PORISValue("FocalPlaneElement_FrameTransferMask")
        self.vlFocalPlaneElement_FastPhotometryMask = PORISValue("FocalPlaneElement_FastPhotometryMask")
        self.vlFocalPlaneElement_MOSmask = PORISValue("FocalPlaneElement_MOSmask")
        self.vlFocalPlaneElement_NoFPE = PORISValue("FocalPlaneElement_NoFPE")
        self.mdFPEMode_NoFPE = PORISMode("FPEMode_NoFPE")
        self.mdFPEMode_MOSmask = PORISMode("FPEMode_MOSmask")
        self.mdFPEMode_FastPhotometryMask = PORISMode("FPEMode_FastPhotometryMask")
        self.mdFPEMode_FrameTransferMask = PORISMode("FPEMode_FrameTransferMask")
        self.mdFPEMode_LSMask = PORISMode("FPEMode_LSMask")
        self.mdFPEMode_Engineering = PORISMode("FPEMode_Engineering")
        self.addItem(self.sysFPE)
        self.sysFPE.ident = "FP-0006"
        self.sysFPE.setXMLName('FPE')
        self.sysFPE.description = ""
        self.addItem(self.prFocalPlaneElement)
        self.prFocalPlaneElement.ident = "OSI-0138"
        self.prFocalPlaneElement.setXMLName('FocalPlaneElement')
        self.prFocalPlaneElement.description = ""
        self.sysFPE.addParam(self.prFocalPlaneElement)
        self.addItem(self.mdFocalPlaneElementMode_Disabled)
        self.mdFocalPlaneElementMode_Disabled.ident = "FP-0001"
        self.mdFocalPlaneElementMode_Disabled.setXMLName('Disabled')
        self.mdFocalPlaneElementMode_Disabled.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_Disabled)
        self.addItem(self.vlFocalPlaneElement_LS0_4)
        self.vlFocalPlaneElement_LS0_4.ident = "OSI-0117"
        self.vlFocalPlaneElement_LS0_4.setXMLName('LS0.4')
        self.vlFocalPlaneElement_LS0_4.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_4)
        self.addItem(self.vlFocalPlaneElement_LS0_6)
        self.vlFocalPlaneElement_LS0_6.ident = "OSI-0118"
        self.vlFocalPlaneElement_LS0_6.setXMLName('LS0.6')
        self.vlFocalPlaneElement_LS0_6.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_6)
        self.addItem(self.vlFocalPlaneElement_LS0_8)
        self.vlFocalPlaneElement_LS0_8.ident = "OSI-0119"
        self.vlFocalPlaneElement_LS0_8.setXMLName('LS0.8')
        self.vlFocalPlaneElement_LS0_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS0_8)
        self.addItem(self.vlFocalPlaneElement_LS1_0)
        self.vlFocalPlaneElement_LS1_0.ident = "OSI-0120"
        self.vlFocalPlaneElement_LS1_0.setXMLName('LS1.0')
        self.vlFocalPlaneElement_LS1_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_0)
        self.addItem(self.vlFocalPlaneElement_LS1_2)
        self.vlFocalPlaneElement_LS1_2.ident = "OSI-0121"
        self.vlFocalPlaneElement_LS1_2.setXMLName('LS1.2')
        self.vlFocalPlaneElement_LS1_2.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_2)
        self.addItem(self.vlFocalPlaneElement_LS1_5)
        self.vlFocalPlaneElement_LS1_5.ident = "OSI-0122"
        self.vlFocalPlaneElement_LS1_5.setXMLName('LS1.5')
        self.vlFocalPlaneElement_LS1_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_5)
        self.addItem(self.vlFocalPlaneElement_LS1_8)
        self.vlFocalPlaneElement_LS1_8.ident = "OSI-0123"
        self.vlFocalPlaneElement_LS1_8.setXMLName('LS1.8')
        self.vlFocalPlaneElement_LS1_8.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS1_8)
        self.addItem(self.vlFocalPlaneElement_LS2_5)
        self.vlFocalPlaneElement_LS2_5.ident = "OSI-0124"
        self.vlFocalPlaneElement_LS2_5.setXMLName('LS2.5')
        self.vlFocalPlaneElement_LS2_5.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS2_5)
        self.addItem(self.vlFocalPlaneElement_LS3_0)
        self.vlFocalPlaneElement_LS3_0.ident = "OSI-0125"
        self.vlFocalPlaneElement_LS3_0.setXMLName('LS3.0')
        self.vlFocalPlaneElement_LS3_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS3_0)
        self.addItem(self.vlFocalPlaneElement_LS5_0)
        self.vlFocalPlaneElement_LS5_0.ident = "OSI-0126"
        self.vlFocalPlaneElement_LS5_0.setXMLName('LS5.0')
        self.vlFocalPlaneElement_LS5_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS5_0)
        self.addItem(self.vlFocalPlaneElement_LS10_0)
        self.vlFocalPlaneElement_LS10_0.ident = "OSI-0127"
        self.vlFocalPlaneElement_LS10_0.setXMLName('LS10.0')
        self.vlFocalPlaneElement_LS10_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS10_0)
        self.addItem(self.vlFocalPlaneElement_LS12_0)
        self.vlFocalPlaneElement_LS12_0.ident = "OSI-0128"
        self.vlFocalPlaneElement_LS12_0.setXMLName('LS12.0')
        self.vlFocalPlaneElement_LS12_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS12_0)
        self.addItem(self.vlFocalPlaneElement_LS40_0)
        self.vlFocalPlaneElement_LS40_0.ident = "OSI-0129"
        self.vlFocalPlaneElement_LS40_0.setXMLName('LS40.0')
        self.vlFocalPlaneElement_LS40_0.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_LS40_0)
        self.addItem(self.mdFocalPlaneElementMode_MOS)
        self.mdFocalPlaneElementMode_MOS.ident = "FP-0002"
        self.mdFocalPlaneElementMode_MOS.setXMLName('MOS')
        self.mdFocalPlaneElementMode_MOS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_MOS)
        self.addItem(self.mdFocalPlaneElementMode_FastPhotometry)
        self.mdFocalPlaneElementMode_FastPhotometry.ident = "FP-0003"
        self.mdFocalPlaneElementMode_FastPhotometry.setXMLName('FastPhotometry')
        self.mdFocalPlaneElementMode_FastPhotometry.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FastPhotometry)
        self.addItem(self.mdFocalPlaneElementMode_FrameTransfer)
        self.mdFocalPlaneElementMode_FrameTransfer.ident = "FP-0004"
        self.mdFocalPlaneElementMode_FrameTransfer.setXMLName('FrameTransfer')
        self.mdFocalPlaneElementMode_FrameTransfer.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_FrameTransfer)
        self.addItem(self.mdFocalPlaneElementMode_LS)
        self.mdFocalPlaneElementMode_LS.ident = "FP-0005"
        self.mdFocalPlaneElementMode_LS.setXMLName('LS')
        self.mdFocalPlaneElementMode_LS.description = ""
        self.prFocalPlaneElement.addMode(self.mdFocalPlaneElementMode_LS)
        self.addItem(self.vlFocalPlaneElement_FrameTransferMask)
        self.vlFocalPlaneElement_FrameTransferMask.ident = "OSI-0586"
        self.vlFocalPlaneElement_FrameTransferMask.setXMLName('FrameTransferMask')
        self.vlFocalPlaneElement_FrameTransferMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FrameTransferMask)
        self.addItem(self.vlFocalPlaneElement_FastPhotometryMask)
        self.vlFocalPlaneElement_FastPhotometryMask.ident = "OSI-0585"
        self.vlFocalPlaneElement_FastPhotometryMask.setXMLName('FastPhotometryMask')
        self.vlFocalPlaneElement_FastPhotometryMask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_FastPhotometryMask)
        self.addItem(self.vlFocalPlaneElement_MOSmask)
        self.vlFocalPlaneElement_MOSmask.ident = "OSI-0584"
        self.vlFocalPlaneElement_MOSmask.setXMLName('MOSmask')
        self.vlFocalPlaneElement_MOSmask.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_MOSmask)
        self.addItem(self.vlFocalPlaneElement_NoFPE)
        self.vlFocalPlaneElement_NoFPE.ident = "OSI-0583"
        self.vlFocalPlaneElement_NoFPE.setXMLName('NoFPE')
        self.vlFocalPlaneElement_NoFPE.description = ""
        self.prFocalPlaneElement.addValue(self.vlFocalPlaneElement_NoFPE)
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
        self.addItem(self.mdFPEMode_Engineering)
        self.mdFPEMode_Engineering.ident = "ENG-1"
        self.mdFPEMode_Engineering.setXMLName('Engineering')
        self.mdFPEMode_Engineering.description = "FPE engineering mode"
        self.sysFPE.addMode(self.mdFPEMode_Engineering)
        # Marcamos FocalPlaneElementMode_Disabled como elegible para FPEMode_NoFPE
        self.mdFPEMode_NoFPE.addSubMode(self.mdFocalPlaneElementMode_Disabled)
        # Marcamos FocalPlaneElementMode_MOS como elegible para FPEMode_MOSmask
        self.mdFPEMode_MOSmask.addSubMode(self.mdFocalPlaneElementMode_MOS)
        # Marcamos FocalPlaneElementMode_FastPhotometry como elegible para FPEMode_FastPhotometryMask
        self.mdFPEMode_FastPhotometryMask.addSubMode(self.mdFocalPlaneElementMode_FastPhotometry)
        # Marcamos FocalPlaneElementMode_FrameTransfer como elegible para FPEMode_FrameTransferMask
        self.mdFPEMode_FrameTransferMask.addSubMode(self.mdFocalPlaneElementMode_FrameTransfer)
        # Marcamos FocalPlaneElementMode_LS como elegible para FPEMode_LSMask
        self.mdFPEMode_LSMask.addSubMode(self.mdFocalPlaneElementMode_LS)
        # Marcamos FocalPlaneElementMode_Disabled como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_Disabled)
        # Marcamos FocalPlaneElementMode_MOS como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_MOS)
        # Marcamos FocalPlaneElementMode_FastPhotometry como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_FastPhotometry)
        # Marcamos FocalPlaneElementMode_FrameTransfer como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_FrameTransfer)
        # Marcamos FocalPlaneElementMode_LS como elegible para FPEMode_Engineering
        self.mdFPEMode_Engineering.addSubMode(self.mdFocalPlaneElementMode_LS)
        # Marcamos FocalPlaneElement_NoFPE como elegible para FocalPlaneElementMode_Disabled
        self.mdFocalPlaneElementMode_Disabled.addValue(self.vlFocalPlaneElement_NoFPE)
        # Marcamos FocalPlaneElement_MOSmask como elegible para FocalPlaneElementMode_MOS
        self.mdFocalPlaneElementMode_MOS.addValue(self.vlFocalPlaneElement_MOSmask)
        # Marcamos FocalPlaneElement_FastPhotometryMask como elegible para FocalPlaneElementMode_FastPhotometry
        self.mdFocalPlaneElementMode_FastPhotometry.addValue(self.vlFocalPlaneElement_FastPhotometryMask)
        # Marcamos FocalPlaneElement_FrameTransferMask como elegible para FocalPlaneElementMode_FrameTransfer
        self.mdFocalPlaneElementMode_FrameTransfer.addValue(self.vlFocalPlaneElement_FrameTransferMask)
        # Marcamos FocalPlaneElement_LS1_5 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_5)
        # Marcamos FocalPlaneElement_LS1_8 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_8)
        # Marcamos FocalPlaneElement_LS1_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_0)
        # Marcamos FocalPlaneElement_LS5_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS5_0)
        # Marcamos FocalPlaneElement_LS40_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS40_0)
        # Marcamos FocalPlaneElement_LS0_8 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_8)
        # Marcamos FocalPlaneElement_LS1_2 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS1_2)
        # Marcamos FocalPlaneElement_LS12_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS12_0)
        # Marcamos FocalPlaneElement_LS0_4 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_4)
        # Marcamos FocalPlaneElement_LS2_5 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS2_5)
        # Marcamos FocalPlaneElement_LS3_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS3_0)
        # Marcamos FocalPlaneElement_LS10_0 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS10_0)
        # Marcamos FocalPlaneElement_LS0_6 como elegible para FocalPlaneElementMode_LS
        self.mdFocalPlaneElementMode_LS.addValue(self.vlFocalPlaneElement_LS0_6)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## FPEMode 
    def get_FPEMode(self)-> PORISMode:
        return self.sysFPE.getSelectedMode()

    def set_FPEMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFPE.selectMode(mode)


    ## prParam FocalPlaneElement 

    # FocalPlaneElement
    def get_FocalPlaneElement(self)-> PORISValue :
        return self.prFocalPlaneElement.getSelectedValue()

    def set_FocalPlaneElement(self, value: PORISValue)-> PORISValue :
        return self.prFocalPlaneElement.setValue(value)


    ## FocalPlaneElementMode 
    def get_FocalPlaneElementMode(self)-> PORISMode:
        return self.prFocalPlaneElement.getSelectedMode()

    def set_FocalPlaneElementMode(self, mode: PORISMode)-> PORISMode :
        return self.prFocalPlaneElement.selectMode(mode)

