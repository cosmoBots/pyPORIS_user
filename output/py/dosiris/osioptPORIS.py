from PORIS import *

class osioptPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysPreOptics = PORISSys("PreOptics")
        self.setRoot(self.sysPreOptics)
        self.sysFilters = PORISSys("Filters")
        self.prGrisms = PORISParam("Grisms")
        self.sysRedTF = PORISSys("RedTF")
        self.prRedFWHM = PORISParam("RedFWHM")
        self.prRedLamda = PORISParam("RedLamda")
        self.sysBlueTF = PORISSys("BlueTF")
        self.prBlueFWHM = PORISParam("BlueFWHM")
        self.prBlueLamda = PORISParam("BlueLamda")
        self.przzero = PORISParam("zzero")
        self.mdPreOpticsMode_NoDispersion = PORISMode("PreOpticsMode_NoDispersion")
        self.mdFiltersMode_OS = PORISMode("FiltersMode_OS")
        self.mdFiltersMode_UFilter = PORISMode("FiltersMode_UFilter")
        self.mdFiltersMode_NoFilter = PORISMode("FiltersMode_NoFilter")
        self.mdFiltersMode_GR = PORISMode("FiltersMode_GR")
        self.mdFiltersMode_Broad = PORISMode("FiltersMode_Broad")
        self.mdFiltersMode_OSCalc = PORISMode("FiltersMode_OSCalc")
        self.mdPreOpticsMode_RTF = PORISMode("PreOpticsMode_RTF")
        self.mdPreOpticsMode_GrismR = PORISMode("PreOpticsMode_GrismR")
        self.mdPreOpticsMode_BTF = PORISMode("PreOpticsMode_BTF")
        self.vlGrisms_R300B = PORISValue("Grisms_R300B")
        self.vlGrisms_R300R = PORISValue("Grisms_R300R")
        self.vlGrisms_R500B = PORISValue("Grisms_R500B")
        self.vlGrisms_R500R = PORISValue("Grisms_R500R")
        self.vlGrisms_R1000B = PORISValue("Grisms_R1000B")
        self.vlGrisms_R1000R = PORISValue("Grisms_R1000R")
        self.vlGrisms_R2000B = PORISValue("Grisms_R2000B")
        self.vlGrisms_R2500U = PORISValue("Grisms_R2500U")
        self.vlGrisms_R2500V = PORISValue("Grisms_R2500V")
        self.vlGrisms_R2500R = PORISValue("Grisms_R2500R")
        self.vlGrisms_R2500I = PORISValue("Grisms_R2500I")
        self.mdGrismsMode_GrismsB = PORISMode("GrismsMode_GrismsB")
        self.mdGrismsMode_GrismsR = PORISMode("GrismsMode_GrismsR")
        self.mdPreOpticsMode_GrismB = PORISMode("PreOpticsMode_GrismB")
        self.mdPreOpticsMode_GrismBMOS = PORISMode("PreOpticsMode_GrismBMOS")
        self.vlRedFWHM_Range2_0 = PORISValueFloat("RedFWHM_Range2_0",1.2,1.6,2.0)
        self.mdRedFWHMMode_l2_0 = PORISMode("RedFWHMMode_l2_0")
        self.mdRedFWHMMode_l1_5 = PORISMode("RedFWHMMode_l1_5")
        self.mdRedFWHMMode_l1_4 = PORISMode("RedFWHMMode_l1_4")
        self.mdRedFWHMMode_l1_3 = PORISMode("RedFWHMMode_l1_3")
        self.mdRedFWHMMode_l1_2 = PORISMode("RedFWHMMode_l1_2")
        self.mdRedFWHMMode_l1_2b = PORISMode("RedFWHMMode_l1_2b")
        self.vlRedFWHM_Range1_5 = PORISValueFloat("RedFWHM_Range1_5",1.0,1.25,1.5)
        self.vlRedFWHM_Range1_4 = PORISValueFloat("RedFWHM_Range1_4",0.9,1.2,1.4)
        self.vlRedFWHM_Range1_3 = PORISValueFloat("RedFWHM_Range1_3",0.8,1.1,1.3)
        self.vlRedFWHM_Range1_2 = PORISValueFloat("RedFWHM_Range1_2",0.85,1.0,1.2)
        self.vlRedFWHM_Range1_2b = PORISValueFloat("RedFWHM_Range1_2b",0.9,1.0,1.2)
        self.mdRedTFMode_l651_799 = PORISMode("RedTFMode_l651_799")
        self.mdRedTFMode_l800_819 = PORISMode("RedTFMode_l800_819")
        self.mdRedTFMode_l820_839 = PORISMode("RedTFMode_l820_839")
        self.mdRedTFMode_l840_879 = PORISMode("RedTFMode_l840_879")
        self.mdRedTFMode_l880_909 = PORISMode("RedTFMode_l880_909")
        self.mdRedTFMode_l910_934 = PORISMode("RedTFMode_l910_934")
        self.vlRedLamda_Range651 = PORISValueFloat("RedLamda_Range651",651.0,700.0,799.9)
        self.mdRedLamdaMode_l651_799 = PORISMode("RedLamdaMode_l651_799")
        self.mdRedLamdaMode_l800_819 = PORISMode("RedLamdaMode_l800_819")
        self.mdRedLamdaMode_l820_839 = PORISMode("RedLamdaMode_l820_839")
        self.mdRedLamdaMode_l840_879 = PORISMode("RedLamdaMode_l840_879")
        self.mdRedLamdaMode_l880_909 = PORISMode("RedLamdaMode_l880_909")
        self.mdRedLamdaMode_l910_934 = PORISMode("RedLamdaMode_l910_934")
        self.vlRedLamda_Range800 = PORISValueFloat("RedLamda_Range800",800.0,810.0,819.9)
        self.vlRedLamda_Range820 = PORISValueFloat("RedLamda_Range820",820.0,830.0,839.9)
        self.vlRedLamda_Range840 = PORISValueFloat("RedLamda_Range840",840.0,860.0,879.9)
        self.vlRedLamda_Range880 = PORISValueFloat("RedLamda_Range880",880.0,895.0,909.9)
        self.vlRedLamda_Range910 = PORISValueFloat("RedLamda_Range910",910.0,920.0,934.5)
        self.vlBlueFWHM_0_8 = PORISValue("BlueFWHM_0_8")
        self.mdBlueFWHMMode_l0_8 = PORISMode("BlueFWHMMode_l0_8")
        self.mdBlueFWHMMode_l0_85 = PORISMode("BlueFWHMMode_l0_85")
        self.mdBlueFWHMMode_l0_50 = PORISMode("BlueFWHMMode_l0_50")
        self.mdBlueFWHMMode_l0_45 = PORISMode("BlueFWHMMode_l0_45")
        self.vlBlueFWHM_0_85 = PORISValue("BlueFWHM_0_85")
        self.vlBlueFWHM_0_50 = PORISValue("BlueFWHM_0_50")
        self.vlBlueFWHM_0_45 = PORISValue("BlueFWHM_0_45")
        self.vlBlueFWHM_0_70 = PORISValue("BlueFWHM_0_70")
        self.mdBlueFWHMMode_l0_70 = PORISMode("BlueFWHMMode_l0_70")
        self.mdBlueFWHMMode_l0_90 = PORISMode("BlueFWHMMode_l0_90")
        self.mdBlueFWHMMode_l1_10 = PORISMode("BlueFWHMMode_l1_10")
        self.vlBlueFWHM_0_90 = PORISValue("BlueFWHM_0_90")
        self.vlBlueFWHM_1_10 = PORISValue("BlueFWHM_1_10")
        self.mdBlueTFMode_l448_463 = PORISMode("BlueTFMode_l448_463")
        self.mdBlueTFMode_l464_480 = PORISMode("BlueTFMode_l464_480")
        self.mdBlueTFMode_l481_502 = PORISMode("BlueTFMode_l481_502")
        self.mdBlueTFMode_l503_521 = PORISMode("BlueTFMode_l503_521")
        self.mdBlueTFMode_l522_542 = PORISMode("BlueTFMode_l522_542")
        self.mdBlueTFMode_l543_583 = PORISMode("BlueTFMode_l543_583")
        self.vlBlueLamda_Range448 = PORISValueFloat("BlueLamda_Range448",448.0,454.0,463.9)
        self.mdBlueLamdaMode_l448_463 = PORISMode("BlueLamdaMode_l448_463")
        self.mdBlueLamdaMode_l464_480 = PORISMode("BlueLamdaMode_l464_480")
        self.mdBlueLamdaMode_l481_502 = PORISMode("BlueLamdaMode_l481_502")
        self.mdBlueLamdaMode_l503_521 = PORISMode("BlueLamdaMode_l503_521")
        self.mdBlueLamdaMode_l522_542 = PORISMode("BlueLamdaMode_l522_542")
        self.mdBlueLamdaMode_l543_583 = PORISMode("BlueLamdaMode_l543_583")
        self.vlBlueLamda_Range464 = PORISValueFloat("BlueLamda_Range464",464.0,472.0,480.9)
        self.vlBlueLamda_Range481 = PORISValueFloat("BlueLamda_Range481",481.0,492.0,502.9)
        self.vlBlueLamda_Range503 = PORISValueFloat("BlueLamda_Range503",503.0,514.0,521.9)
        self.vlBlueLamda_Range522 = PORISValueFloat("BlueLamda_Range522",522.0,536.0,542.9)
        self.vlBlueLamda_Range543 = PORISValueFloat("BlueLamda_Range543",543.0,565.0,583.9)
        self.mdBlueLamdaMode_l584_609 = PORISMode("BlueLamdaMode_l584_609")
        self.mdBlueLamdaMode_l610_637 = PORISMode("BlueLamdaMode_l610_637")
        self.mdBlueLamdaMode_l638_671 = PORISMode("BlueLamdaMode_l638_671")
        self.vlBlueLamda_Range584 = PORISValueFloat("BlueLamda_Range584",584.0,602.0,609.9)
        self.vlBlueLamda_Range610 = PORISValueFloat("BlueLamda_Range610",610.0,622.0,637.9)
        self.vlBlueLamda_Range638 = PORISValueFloat("BlueLamda_Range638",638.0,654.0,671.0)
        self.mdBlueTFMode_l584_609 = PORISMode("BlueTFMode_l584_609")
        self.mdBlueTFMode_l610_637 = PORISMode("BlueTFMode_l610_637")
        self.mdBlueTFMode_l638_671 = PORISMode("BlueTFMode_l638_671")
        self.mdPreOpticsMode_RTFCalib = PORISMode("PreOpticsMode_RTFCalib")
        self.mdPreOpticsMode_BTFCalib = PORISMode("PreOpticsMode_BTFCalib")
        self.vlzzero_NormalRange = PORISValueFloat("zzero_NormalRange",25000.0,29000.0,45000.0)
        self.mdzzeroMode_Normal = PORISMode("zzeroMode_Normal")
        self.mdPreOpticsMode_Engineering = PORISMode("PreOpticsMode_Engineering")
        self.mdRedTFMode_Engineering = PORISMode("RedTFMode_Engineering")
        self.mdBlueTFMode_Engineering = PORISMode("BlueTFMode_Engineering")
        self.addItem(self.sysPreOptics)
        self.sysPreOptics.ident = "OSI-0136"
        self.sysPreOptics.setXMLName('PreOptics')
        self.sysPreOptics.description = ""
        self.addItem(self.sysFilters)
        self.sysFilters.ident = "OSI-0137"
        self.sysFilters.setXMLName('Filters')
        self.sysFilters.description = ""
        self.sysPreOptics.addSubsystem(self.sysFilters)
        self.addItem(self.prGrisms)
        self.prGrisms.ident = "OSI-0475"
        self.prGrisms.setXMLName('Grisms')
        self.prGrisms.description = ""
        self.sysPreOptics.addParam(self.prGrisms)
        self.addItem(self.sysRedTF)
        self.sysRedTF.ident = "OSI-0575"
        self.sysRedTF.setXMLName('RedTF')
        self.sysRedTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysRedTF)
        self.addItem(self.prRedFWHM)
        self.prRedFWHM.ident = "OSI-0576"
        self.prRedFWHM.setXMLName('RedFWHM')
        self.prRedFWHM.description = ""
        self.sysRedTF.addParam(self.prRedFWHM)
        self.addItem(self.prRedLamda)
        self.prRedLamda.ident = "OSI-0577"
        self.prRedLamda.setXMLName('RedLamda')
        self.prRedLamda.description = ""
        self.sysRedTF.addParam(self.prRedLamda)
        self.addItem(self.sysBlueTF)
        self.sysBlueTF.ident = "OSI-0578"
        self.sysBlueTF.setXMLName('BlueTF')
        self.sysBlueTF.description = ""
        self.sysPreOptics.addSubsystem(self.sysBlueTF)
        self.addItem(self.prBlueFWHM)
        self.prBlueFWHM.ident = "OSI-0579"
        self.prBlueFWHM.setXMLName('BlueFWHM')
        self.prBlueFWHM.description = ""
        self.sysBlueTF.addParam(self.prBlueFWHM)
        self.addItem(self.prBlueLamda)
        self.prBlueLamda.ident = "OSI-0580"
        self.prBlueLamda.setXMLName('BlueLamda')
        self.prBlueLamda.description = ""
        self.sysBlueTF.addParam(self.prBlueLamda)
        self.addItem(self.przzero)
        self.przzero.ident = "OP-0109"
        self.przzero.setXMLName('zzero')
        self.przzero.description = ""
        self.sysPreOptics.addParam(self.przzero)
        self.addItem(self.mdPreOpticsMode_NoDispersion)
        self.mdPreOpticsMode_NoDispersion.ident = "OSI-0014"
        self.mdPreOpticsMode_NoDispersion.setXMLName('NoDispersion')
        self.mdPreOpticsMode_NoDispersion.description = ""
        self.sysPreOptics.addMode(self.mdPreOpticsMode_NoDispersion)
        self.addItem(self.mdFiltersMode_OS)
        self.mdFiltersMode_OS.ident = "OSI-0143"
        self.mdFiltersMode_OS.setXMLName('OS')
        self.mdFiltersMode_OS.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OS)
        self.addItem(self.mdFiltersMode_UFilter)
        self.mdFiltersMode_UFilter.ident = "OSI-0145"
        self.mdFiltersMode_UFilter.setXMLName('UFilter')
        self.mdFiltersMode_UFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_UFilter)
        self.addItem(self.mdFiltersMode_NoFilter)
        self.mdFiltersMode_NoFilter.ident = "OSI-0389"
        self.mdFiltersMode_NoFilter.setXMLName('NoFilter')
        self.mdFiltersMode_NoFilter.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_NoFilter)
        self.addItem(self.mdFiltersMode_GR)
        self.mdFiltersMode_GR.ident = "OSI-0390"
        self.mdFiltersMode_GR.setXMLName('GR')
        self.mdFiltersMode_GR.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_GR)
        self.addItem(self.mdFiltersMode_Broad)
        self.mdFiltersMode_Broad.ident = "OSI-0144"
        self.mdFiltersMode_Broad.setXMLName('Broad')
        self.mdFiltersMode_Broad.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_Broad)
        self.addItem(self.mdFiltersMode_OSCalc)
        self.mdFiltersMode_OSCalc.ident = "FILT-0018"
        self.mdFiltersMode_OSCalc.setXMLName('OSCalc')
        self.mdFiltersMode_OSCalc.description = ""
        self.sysFilters.addMode(self.mdFiltersMode_OSCalc)
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
        self.addItem(self.vlGrisms_R300B)
        self.vlGrisms_R300B.ident = "OSI-0017"
        self.vlGrisms_R300B.setXMLName('R300B')
        self.vlGrisms_R300B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300B)
        self.addItem(self.vlGrisms_R300R)
        self.vlGrisms_R300R.ident = "OSI-0018"
        self.vlGrisms_R300R.setXMLName('R300R')
        self.vlGrisms_R300R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R300R)
        self.addItem(self.vlGrisms_R500B)
        self.vlGrisms_R500B.ident = "OSI-0019"
        self.vlGrisms_R500B.setXMLName('R500B')
        self.vlGrisms_R500B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500B)
        self.addItem(self.vlGrisms_R500R)
        self.vlGrisms_R500R.ident = "OSI-0020"
        self.vlGrisms_R500R.setXMLName('R500R')
        self.vlGrisms_R500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R500R)
        self.addItem(self.vlGrisms_R1000B)
        self.vlGrisms_R1000B.ident = "OSI-0021"
        self.vlGrisms_R1000B.setXMLName('R1000B')
        self.vlGrisms_R1000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000B)
        self.addItem(self.vlGrisms_R1000R)
        self.vlGrisms_R1000R.ident = "OSI-0022"
        self.vlGrisms_R1000R.setXMLName('R1000R')
        self.vlGrisms_R1000R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R1000R)
        self.addItem(self.vlGrisms_R2000B)
        self.vlGrisms_R2000B.ident = "OSI-0023"
        self.vlGrisms_R2000B.setXMLName('R2000B')
        self.vlGrisms_R2000B.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2000B)
        self.addItem(self.vlGrisms_R2500U)
        self.vlGrisms_R2500U.ident = "OSI-0024"
        self.vlGrisms_R2500U.setXMLName('R2500U')
        self.vlGrisms_R2500U.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500U)
        self.addItem(self.vlGrisms_R2500V)
        self.vlGrisms_R2500V.ident = "OSI-0025"
        self.vlGrisms_R2500V.setXMLName('R2500V')
        self.vlGrisms_R2500V.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500V)
        self.addItem(self.vlGrisms_R2500R)
        self.vlGrisms_R2500R.ident = "OSI-0026"
        self.vlGrisms_R2500R.setXMLName('R2500R')
        self.vlGrisms_R2500R.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500R)
        self.addItem(self.vlGrisms_R2500I)
        self.vlGrisms_R2500I.ident = "OSI-0027"
        self.vlGrisms_R2500I.setXMLName('R2500I')
        self.vlGrisms_R2500I.description = ""
        self.prGrisms.addValue(self.vlGrisms_R2500I)
        self.addItem(self.mdGrismsMode_GrismsB)
        self.mdGrismsMode_GrismsB.ident = "OSI-0140"
        self.mdGrismsMode_GrismsB.setXMLName('GrismsB')
        self.mdGrismsMode_GrismsB.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsB)
        self.addItem(self.mdGrismsMode_GrismsR)
        self.mdGrismsMode_GrismsR.ident = "OSI-0393"
        self.mdGrismsMode_GrismsR.setXMLName('GrismsR')
        self.mdGrismsMode_GrismsR.description = ""
        self.prGrisms.addMode(self.mdGrismsMode_GrismsR)
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
        self.addItem(self.vlRedFWHM_Range2_0)
        self.vlRedFWHM_Range2_0.ident = "OSI-0502"
        self.vlRedFWHM_Range2_0.setXMLName('Range2.0')
        self.vlRedFWHM_Range2_0.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range2_0)
        self.addItem(self.mdRedFWHMMode_l2_0)
        self.mdRedFWHMMode_l2_0.ident = "OSI-0503"
        self.mdRedFWHMMode_l2_0.setXMLName('l2.0')
        self.mdRedFWHMMode_l2_0.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l2_0)
        self.addItem(self.mdRedFWHMMode_l1_5)
        self.mdRedFWHMMode_l1_5.ident = "OSI-0504"
        self.mdRedFWHMMode_l1_5.setXMLName('l1.5')
        self.mdRedFWHMMode_l1_5.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_5)
        self.addItem(self.mdRedFWHMMode_l1_4)
        self.mdRedFWHMMode_l1_4.ident = "OSI-0505"
        self.mdRedFWHMMode_l1_4.setXMLName('l1.4')
        self.mdRedFWHMMode_l1_4.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_4)
        self.addItem(self.mdRedFWHMMode_l1_3)
        self.mdRedFWHMMode_l1_3.ident = "OSI-0506"
        self.mdRedFWHMMode_l1_3.setXMLName('l1.3')
        self.mdRedFWHMMode_l1_3.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_3)
        self.addItem(self.mdRedFWHMMode_l1_2)
        self.mdRedFWHMMode_l1_2.ident = "OSI-0507"
        self.mdRedFWHMMode_l1_2.setXMLName('l1.2')
        self.mdRedFWHMMode_l1_2.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2)
        self.addItem(self.mdRedFWHMMode_l1_2b)
        self.mdRedFWHMMode_l1_2b.ident = "OSI-0508"
        self.mdRedFWHMMode_l1_2b.setXMLName('l1.2b')
        self.mdRedFWHMMode_l1_2b.description = ""
        self.prRedFWHM.addMode(self.mdRedFWHMMode_l1_2b)
        self.addItem(self.vlRedFWHM_Range1_5)
        self.vlRedFWHM_Range1_5.ident = "OSI-0509"
        self.vlRedFWHM_Range1_5.setXMLName('Range1.5')
        self.vlRedFWHM_Range1_5.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_5)
        self.addItem(self.vlRedFWHM_Range1_4)
        self.vlRedFWHM_Range1_4.ident = "OSI-0510"
        self.vlRedFWHM_Range1_4.setXMLName('Range1.4')
        self.vlRedFWHM_Range1_4.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_4)
        self.addItem(self.vlRedFWHM_Range1_3)
        self.vlRedFWHM_Range1_3.ident = "OSI-0511"
        self.vlRedFWHM_Range1_3.setXMLName('Range1.3')
        self.vlRedFWHM_Range1_3.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_3)
        self.addItem(self.vlRedFWHM_Range1_2)
        self.vlRedFWHM_Range1_2.ident = "OSI-0512"
        self.vlRedFWHM_Range1_2.setXMLName('Range1.2')
        self.vlRedFWHM_Range1_2.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2)
        self.addItem(self.vlRedFWHM_Range1_2b)
        self.vlRedFWHM_Range1_2b.ident = "OSI-0513"
        self.vlRedFWHM_Range1_2b.setXMLName('Range1.2b')
        self.vlRedFWHM_Range1_2b.description = ""
        self.prRedFWHM.addValue(self.vlRedFWHM_Range1_2b)
        self.addItem(self.mdRedTFMode_l651_799)
        self.mdRedTFMode_l651_799.ident = "OSI-0514"
        self.mdRedTFMode_l651_799.setXMLName('l651_799')
        self.mdRedTFMode_l651_799.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l651_799)
        self.addItem(self.mdRedTFMode_l800_819)
        self.mdRedTFMode_l800_819.ident = "OSI-0515"
        self.mdRedTFMode_l800_819.setXMLName('l800_819')
        self.mdRedTFMode_l800_819.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l800_819)
        self.addItem(self.mdRedTFMode_l820_839)
        self.mdRedTFMode_l820_839.ident = "OSI-0516"
        self.mdRedTFMode_l820_839.setXMLName('l820_839')
        self.mdRedTFMode_l820_839.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l820_839)
        self.addItem(self.mdRedTFMode_l840_879)
        self.mdRedTFMode_l840_879.ident = "OSI-0517"
        self.mdRedTFMode_l840_879.setXMLName('l840_879')
        self.mdRedTFMode_l840_879.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l840_879)
        self.addItem(self.mdRedTFMode_l880_909)
        self.mdRedTFMode_l880_909.ident = "OSI-0518"
        self.mdRedTFMode_l880_909.setXMLName('l880_909')
        self.mdRedTFMode_l880_909.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l880_909)
        self.addItem(self.mdRedTFMode_l910_934)
        self.mdRedTFMode_l910_934.ident = "OSI-0519"
        self.mdRedTFMode_l910_934.setXMLName('l910_934')
        self.mdRedTFMode_l910_934.description = ""
        self.sysRedTF.addMode(self.mdRedTFMode_l910_934)
        self.addItem(self.vlRedLamda_Range651)
        self.vlRedLamda_Range651.ident = "OSI-0520"
        self.vlRedLamda_Range651.setXMLName('Range651')
        self.vlRedLamda_Range651.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range651)
        self.addItem(self.mdRedLamdaMode_l651_799)
        self.mdRedLamdaMode_l651_799.ident = "OSI-0521"
        self.mdRedLamdaMode_l651_799.setXMLName('l651_799')
        self.mdRedLamdaMode_l651_799.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l651_799)
        self.addItem(self.mdRedLamdaMode_l800_819)
        self.mdRedLamdaMode_l800_819.ident = "OSI-0522"
        self.mdRedLamdaMode_l800_819.setXMLName('l800_819')
        self.mdRedLamdaMode_l800_819.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l800_819)
        self.addItem(self.mdRedLamdaMode_l820_839)
        self.mdRedLamdaMode_l820_839.ident = "OSI-0523"
        self.mdRedLamdaMode_l820_839.setXMLName('l820_839')
        self.mdRedLamdaMode_l820_839.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l820_839)
        self.addItem(self.mdRedLamdaMode_l840_879)
        self.mdRedLamdaMode_l840_879.ident = "OSI-0524"
        self.mdRedLamdaMode_l840_879.setXMLName('l840_879')
        self.mdRedLamdaMode_l840_879.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l840_879)
        self.addItem(self.mdRedLamdaMode_l880_909)
        self.mdRedLamdaMode_l880_909.ident = "OSI-0525"
        self.mdRedLamdaMode_l880_909.setXMLName('l880_909')
        self.mdRedLamdaMode_l880_909.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l880_909)
        self.addItem(self.mdRedLamdaMode_l910_934)
        self.mdRedLamdaMode_l910_934.ident = "OSI-0526"
        self.mdRedLamdaMode_l910_934.setXMLName('l910_934')
        self.mdRedLamdaMode_l910_934.description = ""
        self.prRedLamda.addMode(self.mdRedLamdaMode_l910_934)
        self.addItem(self.vlRedLamda_Range800)
        self.vlRedLamda_Range800.ident = "OSI-0527"
        self.vlRedLamda_Range800.setXMLName('Range800')
        self.vlRedLamda_Range800.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range800)
        self.addItem(self.vlRedLamda_Range820)
        self.vlRedLamda_Range820.ident = "OSI-0528"
        self.vlRedLamda_Range820.setXMLName('Range820')
        self.vlRedLamda_Range820.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range820)
        self.addItem(self.vlRedLamda_Range840)
        self.vlRedLamda_Range840.ident = "OSI-0529"
        self.vlRedLamda_Range840.setXMLName('Range840')
        self.vlRedLamda_Range840.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range840)
        self.addItem(self.vlRedLamda_Range880)
        self.vlRedLamda_Range880.ident = "OSI-0530"
        self.vlRedLamda_Range880.setXMLName('Range880')
        self.vlRedLamda_Range880.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range880)
        self.addItem(self.vlRedLamda_Range910)
        self.vlRedLamda_Range910.ident = "OSI-0531"
        self.vlRedLamda_Range910.setXMLName('Range910')
        self.vlRedLamda_Range910.description = ""
        self.prRedLamda.addValue(self.vlRedLamda_Range910)
        self.addItem(self.vlBlueFWHM_0_8)
        self.vlBlueFWHM_0_8.ident = "OSI-0532"
        self.vlBlueFWHM_0_8.setXMLName('0.8')
        self.vlBlueFWHM_0_8.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_8)
        self.addItem(self.mdBlueFWHMMode_l0_8)
        self.mdBlueFWHMMode_l0_8.ident = "OSI-0533"
        self.mdBlueFWHMMode_l0_8.setXMLName('l0.8')
        self.mdBlueFWHMMode_l0_8.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_8)
        self.addItem(self.mdBlueFWHMMode_l0_85)
        self.mdBlueFWHMMode_l0_85.ident = "OSI-0534"
        self.mdBlueFWHMMode_l0_85.setXMLName('l0.85')
        self.mdBlueFWHMMode_l0_85.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_85)
        self.addItem(self.mdBlueFWHMMode_l0_50)
        self.mdBlueFWHMMode_l0_50.ident = "OSI-0536"
        self.mdBlueFWHMMode_l0_50.setXMLName('l0.50')
        self.mdBlueFWHMMode_l0_50.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_50)
        self.addItem(self.mdBlueFWHMMode_l0_45)
        self.mdBlueFWHMMode_l0_45.ident = "OSI-0537"
        self.mdBlueFWHMMode_l0_45.setXMLName('l0.45')
        self.mdBlueFWHMMode_l0_45.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_45)
        self.addItem(self.vlBlueFWHM_0_85)
        self.vlBlueFWHM_0_85.ident = "OSI-0539"
        self.vlBlueFWHM_0_85.setXMLName('0.85')
        self.vlBlueFWHM_0_85.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_85)
        self.addItem(self.vlBlueFWHM_0_50)
        self.vlBlueFWHM_0_50.ident = "OSI-0540"
        self.vlBlueFWHM_0_50.setXMLName('0.50')
        self.vlBlueFWHM_0_50.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_50)
        self.addItem(self.vlBlueFWHM_0_45)
        self.vlBlueFWHM_0_45.ident = "OSI-0541"
        self.vlBlueFWHM_0_45.setXMLName('0.45')
        self.vlBlueFWHM_0_45.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_45)
        self.addItem(self.vlBlueFWHM_0_70)
        self.vlBlueFWHM_0_70.ident = "OSI-0542"
        self.vlBlueFWHM_0_70.setXMLName('0.70')
        self.vlBlueFWHM_0_70.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_70)
        self.addItem(self.mdBlueFWHMMode_l0_70)
        self.mdBlueFWHMMode_l0_70.ident = "OSI-0543"
        self.mdBlueFWHMMode_l0_70.setXMLName('l0.70')
        self.mdBlueFWHMMode_l0_70.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_70)
        self.addItem(self.mdBlueFWHMMode_l0_90)
        self.mdBlueFWHMMode_l0_90.ident = "OSI-0544"
        self.mdBlueFWHMMode_l0_90.setXMLName('l0.90')
        self.mdBlueFWHMMode_l0_90.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l0_90)
        self.addItem(self.mdBlueFWHMMode_l1_10)
        self.mdBlueFWHMMode_l1_10.ident = "OSI-0545"
        self.mdBlueFWHMMode_l1_10.setXMLName('l1.10')
        self.mdBlueFWHMMode_l1_10.description = ""
        self.prBlueFWHM.addMode(self.mdBlueFWHMMode_l1_10)
        self.addItem(self.vlBlueFWHM_0_90)
        self.vlBlueFWHM_0_90.ident = "OSI-0546"
        self.vlBlueFWHM_0_90.setXMLName('0.90')
        self.vlBlueFWHM_0_90.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_0_90)
        self.addItem(self.vlBlueFWHM_1_10)
        self.vlBlueFWHM_1_10.ident = "OSI-0547"
        self.vlBlueFWHM_1_10.setXMLName('1.10')
        self.vlBlueFWHM_1_10.description = ""
        self.prBlueFWHM.addValue(self.vlBlueFWHM_1_10)
        self.addItem(self.mdBlueTFMode_l448_463)
        self.mdBlueTFMode_l448_463.ident = "OSI-0548"
        self.mdBlueTFMode_l448_463.setXMLName('l448_463')
        self.mdBlueTFMode_l448_463.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l448_463)
        self.addItem(self.mdBlueTFMode_l464_480)
        self.mdBlueTFMode_l464_480.ident = "OSI-0549"
        self.mdBlueTFMode_l464_480.setXMLName('l464_480')
        self.mdBlueTFMode_l464_480.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l464_480)
        self.addItem(self.mdBlueTFMode_l481_502)
        self.mdBlueTFMode_l481_502.ident = "OSI-0550"
        self.mdBlueTFMode_l481_502.setXMLName('l481_502')
        self.mdBlueTFMode_l481_502.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l481_502)
        self.addItem(self.mdBlueTFMode_l503_521)
        self.mdBlueTFMode_l503_521.ident = "OSI-0551"
        self.mdBlueTFMode_l503_521.setXMLName('l503_521')
        self.mdBlueTFMode_l503_521.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l503_521)
        self.addItem(self.mdBlueTFMode_l522_542)
        self.mdBlueTFMode_l522_542.ident = "OSI-0552"
        self.mdBlueTFMode_l522_542.setXMLName('l522_542')
        self.mdBlueTFMode_l522_542.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l522_542)
        self.addItem(self.mdBlueTFMode_l543_583)
        self.mdBlueTFMode_l543_583.ident = "OSI-0553"
        self.mdBlueTFMode_l543_583.setXMLName('l543_583')
        self.mdBlueTFMode_l543_583.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l543_583)
        self.addItem(self.vlBlueLamda_Range448)
        self.vlBlueLamda_Range448.ident = "OSI-0554"
        self.vlBlueLamda_Range448.setXMLName('Range448')
        self.vlBlueLamda_Range448.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range448)
        self.addItem(self.mdBlueLamdaMode_l448_463)
        self.mdBlueLamdaMode_l448_463.ident = "OSI-0555"
        self.mdBlueLamdaMode_l448_463.setXMLName('l448_463')
        self.mdBlueLamdaMode_l448_463.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l448_463)
        self.addItem(self.mdBlueLamdaMode_l464_480)
        self.mdBlueLamdaMode_l464_480.ident = "OSI-0556"
        self.mdBlueLamdaMode_l464_480.setXMLName('l464_480')
        self.mdBlueLamdaMode_l464_480.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l464_480)
        self.addItem(self.mdBlueLamdaMode_l481_502)
        self.mdBlueLamdaMode_l481_502.ident = "OSI-0557"
        self.mdBlueLamdaMode_l481_502.setXMLName('l481_502')
        self.mdBlueLamdaMode_l481_502.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l481_502)
        self.addItem(self.mdBlueLamdaMode_l503_521)
        self.mdBlueLamdaMode_l503_521.ident = "OSI-0558"
        self.mdBlueLamdaMode_l503_521.setXMLName('l503_521')
        self.mdBlueLamdaMode_l503_521.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l503_521)
        self.addItem(self.mdBlueLamdaMode_l522_542)
        self.mdBlueLamdaMode_l522_542.ident = "OSI-0559"
        self.mdBlueLamdaMode_l522_542.setXMLName('l522_542')
        self.mdBlueLamdaMode_l522_542.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l522_542)
        self.addItem(self.mdBlueLamdaMode_l543_583)
        self.mdBlueLamdaMode_l543_583.ident = "OSI-0560"
        self.mdBlueLamdaMode_l543_583.setXMLName('l543_583')
        self.mdBlueLamdaMode_l543_583.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l543_583)
        self.addItem(self.vlBlueLamda_Range464)
        self.vlBlueLamda_Range464.ident = "OSI-0561"
        self.vlBlueLamda_Range464.setXMLName('Range464')
        self.vlBlueLamda_Range464.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range464)
        self.addItem(self.vlBlueLamda_Range481)
        self.vlBlueLamda_Range481.ident = "OSI-0562"
        self.vlBlueLamda_Range481.setXMLName('Range481')
        self.vlBlueLamda_Range481.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range481)
        self.addItem(self.vlBlueLamda_Range503)
        self.vlBlueLamda_Range503.ident = "OSI-0563"
        self.vlBlueLamda_Range503.setXMLName('Range503')
        self.vlBlueLamda_Range503.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range503)
        self.addItem(self.vlBlueLamda_Range522)
        self.vlBlueLamda_Range522.ident = "OSI-0564"
        self.vlBlueLamda_Range522.setXMLName('Range522')
        self.vlBlueLamda_Range522.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range522)
        self.addItem(self.vlBlueLamda_Range543)
        self.vlBlueLamda_Range543.ident = "OSI-0565"
        self.vlBlueLamda_Range543.setXMLName('Range543')
        self.vlBlueLamda_Range543.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range543)
        self.addItem(self.mdBlueLamdaMode_l584_609)
        self.mdBlueLamdaMode_l584_609.ident = "OSI-0566"
        self.mdBlueLamdaMode_l584_609.setXMLName('l584_609')
        self.mdBlueLamdaMode_l584_609.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l584_609)
        self.addItem(self.mdBlueLamdaMode_l610_637)
        self.mdBlueLamdaMode_l610_637.ident = "OSI-0567"
        self.mdBlueLamdaMode_l610_637.setXMLName('l610_637')
        self.mdBlueLamdaMode_l610_637.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l610_637)
        self.addItem(self.mdBlueLamdaMode_l638_671)
        self.mdBlueLamdaMode_l638_671.ident = "OSI-0568"
        self.mdBlueLamdaMode_l638_671.setXMLName('l638_671')
        self.mdBlueLamdaMode_l638_671.description = ""
        self.prBlueLamda.addMode(self.mdBlueLamdaMode_l638_671)
        self.addItem(self.vlBlueLamda_Range584)
        self.vlBlueLamda_Range584.ident = "OSI-0569"
        self.vlBlueLamda_Range584.setXMLName('Range584')
        self.vlBlueLamda_Range584.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range584)
        self.addItem(self.vlBlueLamda_Range610)
        self.vlBlueLamda_Range610.ident = "OSI-0570"
        self.vlBlueLamda_Range610.setXMLName('Range610')
        self.vlBlueLamda_Range610.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range610)
        self.addItem(self.vlBlueLamda_Range638)
        self.vlBlueLamda_Range638.ident = "OSI-0571"
        self.vlBlueLamda_Range638.setXMLName('Range638')
        self.vlBlueLamda_Range638.description = ""
        self.prBlueLamda.addValue(self.vlBlueLamda_Range638)
        self.addItem(self.mdBlueTFMode_l584_609)
        self.mdBlueTFMode_l584_609.ident = "OSI-0572"
        self.mdBlueTFMode_l584_609.setXMLName('l584_609')
        self.mdBlueTFMode_l584_609.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l584_609)
        self.addItem(self.mdBlueTFMode_l610_637)
        self.mdBlueTFMode_l610_637.ident = "OSI-0573"
        self.mdBlueTFMode_l610_637.setXMLName('l610_637')
        self.mdBlueTFMode_l610_637.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l610_637)
        self.addItem(self.mdBlueTFMode_l638_671)
        self.mdBlueTFMode_l638_671.ident = "OSI-0574"
        self.mdBlueTFMode_l638_671.setXMLName('l638_671')
        self.mdBlueTFMode_l638_671.description = ""
        self.sysBlueTF.addMode(self.mdBlueTFMode_l638_671)
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
        self.addItem(self.vlzzero_NormalRange)
        self.vlzzero_NormalRange.ident = "OP-0107"
        self.vlzzero_NormalRange.setXMLName('NormalRange')
        self.vlzzero_NormalRange.description = ""
        self.przzero.addValue(self.vlzzero_NormalRange)
        self.addItem(self.mdzzeroMode_Normal)
        self.mdzzeroMode_Normal.ident = "OP-0108"
        self.mdzzeroMode_Normal.setXMLName('Normal')
        self.mdzzeroMode_Normal.description = ""
        self.przzero.addMode(self.mdzzeroMode_Normal)
        self.addItem(self.mdPreOpticsMode_Engineering)
        self.mdPreOpticsMode_Engineering.ident = "ENG-1"
        self.mdPreOpticsMode_Engineering.setXMLName('Engineering')
        self.mdPreOpticsMode_Engineering.description = "PreOptics_engineering_mode"
        self.sysPreOptics.addMode(self.mdPreOpticsMode_Engineering)
        self.addItem(self.mdRedTFMode_Engineering)
        self.mdRedTFMode_Engineering.ident = "ENG-2"
        self.mdRedTFMode_Engineering.setXMLName('Engineering')
        self.mdRedTFMode_Engineering.description = "RedTF_engineering_mode"
        self.sysRedTF.addMode(self.mdRedTFMode_Engineering)
        self.addItem(self.mdBlueTFMode_Engineering)
        self.mdBlueTFMode_Engineering.ident = "ENG-3"
        self.mdBlueTFMode_Engineering.setXMLName('Engineering')
        self.mdBlueTFMode_Engineering.description = "BlueTF_engineering_mode"
        self.sysBlueTF.addMode(self.mdBlueTFMode_Engineering)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_NoDispersion
        self.mdPreOpticsMode_NoDispersion.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos FiltersMode_GR como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_GR)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_GrismB
        self.mdPreOpticsMode_GrismB.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_OS como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_OS)
        # Marcamos FiltersMode_UFilter como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_UFilter)
        # Marcamos FiltersMode_NoFilter como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_NoFilter)
        # Marcamos FiltersMode_GR como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_GR)
        # Marcamos FiltersMode_Broad como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_Broad)
        # Marcamos FiltersMode_OSCalc como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdFiltersMode_OSCalc)
        # Marcamos GrismsMode_GrismsR como elegible para PreOpticsMode_GrismR
        self.mdPreOpticsMode_GrismR.addSubMode(self.mdGrismsMode_GrismsR)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_GrismB
        self.mdPreOpticsMode_GrismB.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_GrismBMOS
        self.mdPreOpticsMode_GrismBMOS.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsB como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdGrismsMode_GrismsB)
        # Marcamos GrismsMode_GrismsR como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdGrismsMode_GrismsR)
        # Marcamos Grisms_R1000B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R1000B)
        # Marcamos Grisms_R300B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R300B)
        # Marcamos Grisms_R2500U como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2500U)
        # Marcamos Grisms_R500B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R500B)
        # Marcamos Grisms_R2000B como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2000B)
        # Marcamos Grisms_R2500V como elegible para GrismsMode_GrismsB
        self.mdGrismsMode_GrismsB.addValue(self.vlGrisms_R2500V)
        # Marcamos Grisms_R300R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R300R)
        # Marcamos Grisms_R2500R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R2500R)
        # Marcamos Grisms_R1000R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R1000R)
        # Marcamos Grisms_R2500I como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R2500I)
        # Marcamos Grisms_R500R como elegible para GrismsMode_GrismsR
        self.mdGrismsMode_GrismsR.addValue(self.vlGrisms_R500R)
        # Marcamos RedTFMode_l651_799 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l651_799)
        # Marcamos RedTFMode_l800_819 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l800_819)
        # Marcamos RedTFMode_l820_839 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l820_839)
        # Marcamos RedTFMode_l840_879 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l840_879)
        # Marcamos RedTFMode_l880_909 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l880_909)
        # Marcamos RedTFMode_l910_934 como elegible para PreOpticsMode_RTF
        self.mdPreOpticsMode_RTF.addSubMode(self.mdRedTFMode_l910_934)
        # Marcamos RedTFMode_l651_799 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l651_799)
        # Marcamos RedTFMode_l800_819 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l800_819)
        # Marcamos RedTFMode_l820_839 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l820_839)
        # Marcamos RedTFMode_l840_879 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l840_879)
        # Marcamos RedTFMode_l880_909 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l880_909)
        # Marcamos RedTFMode_l910_934 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_l910_934)
        # Marcamos RedTFMode_Engineering como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdRedTFMode_Engineering)
        # Marcamos RedFWHMMode_l2_0 como elegible para RedTFMode_l651_799
        self.mdRedTFMode_l651_799.addSubMode(self.mdRedFWHMMode_l2_0)
        # Marcamos RedFWHMMode_l1_5 como elegible para RedTFMode_l800_819
        self.mdRedTFMode_l800_819.addSubMode(self.mdRedFWHMMode_l1_5)
        # Marcamos RedFWHMMode_l1_4 como elegible para RedTFMode_l820_839
        self.mdRedTFMode_l820_839.addSubMode(self.mdRedFWHMMode_l1_4)
        # Marcamos RedFWHMMode_l1_3 como elegible para RedTFMode_l840_879
        self.mdRedTFMode_l840_879.addSubMode(self.mdRedFWHMMode_l1_3)
        # Marcamos RedFWHMMode_l1_2 como elegible para RedTFMode_l880_909
        self.mdRedTFMode_l880_909.addSubMode(self.mdRedFWHMMode_l1_2)
        # Marcamos RedFWHMMode_l1_2b como elegible para RedTFMode_l910_934
        self.mdRedTFMode_l910_934.addSubMode(self.mdRedFWHMMode_l1_2b)
        # Marcamos RedFWHMMode_l2_0 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l2_0)
        # Marcamos RedFWHMMode_l1_5 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_5)
        # Marcamos RedFWHMMode_l1_4 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_4)
        # Marcamos RedFWHMMode_l1_3 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_3)
        # Marcamos RedFWHMMode_l1_2 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_2)
        # Marcamos RedFWHMMode_l1_2b como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedFWHMMode_l1_2b)
        # Marcamos RedFWHM_Range2_0 como elegible para RedFWHMMode_l2_0
        self.mdRedFWHMMode_l2_0.addValue(self.vlRedFWHM_Range2_0)
        # Marcamos RedFWHM_Range1_5 como elegible para RedFWHMMode_l1_5
        self.mdRedFWHMMode_l1_5.addValue(self.vlRedFWHM_Range1_5)
        # Marcamos RedFWHM_Range1_4 como elegible para RedFWHMMode_l1_4
        self.mdRedFWHMMode_l1_4.addValue(self.vlRedFWHM_Range1_4)
        # Marcamos RedFWHM_Range1_3 como elegible para RedFWHMMode_l1_3
        self.mdRedFWHMMode_l1_3.addValue(self.vlRedFWHM_Range1_3)
        # Marcamos RedFWHM_Range1_2 como elegible para RedFWHMMode_l1_2
        self.mdRedFWHMMode_l1_2.addValue(self.vlRedFWHM_Range1_2)
        # Marcamos RedFWHM_Range1_2b como elegible para RedFWHMMode_l1_2b
        self.mdRedFWHMMode_l1_2b.addValue(self.vlRedFWHM_Range1_2b)
        # Marcamos RedLamdaMode_l651_799 como elegible para RedTFMode_l651_799
        self.mdRedTFMode_l651_799.addSubMode(self.mdRedLamdaMode_l651_799)
        # Marcamos RedLamdaMode_l800_819 como elegible para RedTFMode_l800_819
        self.mdRedTFMode_l800_819.addSubMode(self.mdRedLamdaMode_l800_819)
        # Marcamos RedLamdaMode_l820_839 como elegible para RedTFMode_l820_839
        self.mdRedTFMode_l820_839.addSubMode(self.mdRedLamdaMode_l820_839)
        # Marcamos RedLamdaMode_l840_879 como elegible para RedTFMode_l840_879
        self.mdRedTFMode_l840_879.addSubMode(self.mdRedLamdaMode_l840_879)
        # Marcamos RedLamdaMode_l880_909 como elegible para RedTFMode_l880_909
        self.mdRedTFMode_l880_909.addSubMode(self.mdRedLamdaMode_l880_909)
        # Marcamos RedLamdaMode_l910_934 como elegible para RedTFMode_l910_934
        self.mdRedTFMode_l910_934.addSubMode(self.mdRedLamdaMode_l910_934)
        # Marcamos RedLamdaMode_l651_799 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l651_799)
        # Marcamos RedLamdaMode_l800_819 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l800_819)
        # Marcamos RedLamdaMode_l820_839 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l820_839)
        # Marcamos RedLamdaMode_l840_879 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l840_879)
        # Marcamos RedLamdaMode_l880_909 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l880_909)
        # Marcamos RedLamdaMode_l910_934 como elegible para RedTFMode_Engineering
        self.mdRedTFMode_Engineering.addSubMode(self.mdRedLamdaMode_l910_934)
        # Marcamos RedLamda_Range651 como elegible para RedLamdaMode_l651_799
        self.mdRedLamdaMode_l651_799.addValue(self.vlRedLamda_Range651)
        # Marcamos RedLamda_Range800 como elegible para RedLamdaMode_l800_819
        self.mdRedLamdaMode_l800_819.addValue(self.vlRedLamda_Range800)
        # Marcamos RedLamda_Range820 como elegible para RedLamdaMode_l820_839
        self.mdRedLamdaMode_l820_839.addValue(self.vlRedLamda_Range820)
        # Marcamos RedLamda_Range840 como elegible para RedLamdaMode_l840_879
        self.mdRedLamdaMode_l840_879.addValue(self.vlRedLamda_Range840)
        # Marcamos RedLamda_Range880 como elegible para RedLamdaMode_l880_909
        self.mdRedLamdaMode_l880_909.addValue(self.vlRedLamda_Range880)
        # Marcamos RedLamda_Range910 como elegible para RedLamdaMode_l910_934
        self.mdRedLamdaMode_l910_934.addValue(self.vlRedLamda_Range910)
        # Marcamos BlueTFMode_l448_463 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l448_463)
        # Marcamos BlueTFMode_l464_480 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l464_480)
        # Marcamos BlueTFMode_l481_502 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l481_502)
        # Marcamos BlueTFMode_l503_521 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l503_521)
        # Marcamos BlueTFMode_l522_542 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l522_542)
        # Marcamos BlueTFMode_l543_583 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l543_583)
        # Marcamos BlueTFMode_l584_609 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l584_609)
        # Marcamos BlueTFMode_l610_637 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l610_637)
        # Marcamos BlueTFMode_l638_671 como elegible para PreOpticsMode_BTF
        self.mdPreOpticsMode_BTF.addSubMode(self.mdBlueTFMode_l638_671)
        # Marcamos BlueTFMode_l448_463 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l448_463)
        # Marcamos BlueTFMode_l464_480 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l464_480)
        # Marcamos BlueTFMode_l481_502 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l481_502)
        # Marcamos BlueTFMode_l503_521 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l503_521)
        # Marcamos BlueTFMode_l522_542 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l522_542)
        # Marcamos BlueTFMode_l543_583 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l543_583)
        # Marcamos BlueTFMode_l584_609 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l584_609)
        # Marcamos BlueTFMode_l610_637 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l610_637)
        # Marcamos BlueTFMode_l638_671 como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_l638_671)
        # Marcamos BlueTFMode_Engineering como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdBlueTFMode_Engineering)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_l448_463
        self.mdBlueTFMode_l448_463.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_85 como elegible para BlueTFMode_l464_480
        self.mdBlueTFMode_l464_480.addSubMode(self.mdBlueFWHMMode_l0_85)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_l481_502
        self.mdBlueTFMode_l481_502.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_l503_521
        self.mdBlueTFMode_l503_521.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_45 como elegible para BlueTFMode_l522_542
        self.mdBlueTFMode_l522_542.addSubMode(self.mdBlueFWHMMode_l0_45)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_l543_583
        self.mdBlueTFMode_l543_583.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_70 como elegible para BlueTFMode_l584_609
        self.mdBlueTFMode_l584_609.addSubMode(self.mdBlueFWHMMode_l0_70)
        # Marcamos BlueFWHMMode_l0_90 como elegible para BlueTFMode_l610_637
        self.mdBlueTFMode_l610_637.addSubMode(self.mdBlueFWHMMode_l0_90)
        # Marcamos BlueFWHMMode_l1_10 como elegible para BlueTFMode_l638_671
        self.mdBlueTFMode_l638_671.addSubMode(self.mdBlueFWHMMode_l1_10)
        # Marcamos BlueFWHMMode_l0_8 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_8)
        # Marcamos BlueFWHMMode_l0_85 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_85)
        # Marcamos BlueFWHMMode_l0_50 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_50)
        # Marcamos BlueFWHMMode_l0_45 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_45)
        # Marcamos BlueFWHMMode_l0_70 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_70)
        # Marcamos BlueFWHMMode_l0_90 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l0_90)
        # Marcamos BlueFWHMMode_l1_10 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueFWHMMode_l1_10)
        # Marcamos BlueFWHM_0_8 como elegible para BlueFWHMMode_l0_8
        self.mdBlueFWHMMode_l0_8.addValue(self.vlBlueFWHM_0_8)
        # Marcamos BlueFWHM_0_85 como elegible para BlueFWHMMode_l0_85
        self.mdBlueFWHMMode_l0_85.addValue(self.vlBlueFWHM_0_85)
        # Marcamos BlueFWHM_0_50 como elegible para BlueFWHMMode_l0_50
        self.mdBlueFWHMMode_l0_50.addValue(self.vlBlueFWHM_0_50)
        # Marcamos BlueFWHM_0_45 como elegible para BlueFWHMMode_l0_45
        self.mdBlueFWHMMode_l0_45.addValue(self.vlBlueFWHM_0_45)
        # Marcamos BlueFWHM_0_70 como elegible para BlueFWHMMode_l0_70
        self.mdBlueFWHMMode_l0_70.addValue(self.vlBlueFWHM_0_70)
        # Marcamos BlueFWHM_0_90 como elegible para BlueFWHMMode_l0_90
        self.mdBlueFWHMMode_l0_90.addValue(self.vlBlueFWHM_0_90)
        # Marcamos BlueFWHM_1_10 como elegible para BlueFWHMMode_l1_10
        self.mdBlueFWHMMode_l1_10.addValue(self.vlBlueFWHM_1_10)
        # Marcamos BlueLamdaMode_l448_463 como elegible para BlueTFMode_l448_463
        self.mdBlueTFMode_l448_463.addSubMode(self.mdBlueLamdaMode_l448_463)
        # Marcamos BlueLamdaMode_l464_480 como elegible para BlueTFMode_l464_480
        self.mdBlueTFMode_l464_480.addSubMode(self.mdBlueLamdaMode_l464_480)
        # Marcamos BlueLamdaMode_l481_502 como elegible para BlueTFMode_l481_502
        self.mdBlueTFMode_l481_502.addSubMode(self.mdBlueLamdaMode_l481_502)
        # Marcamos BlueLamdaMode_l503_521 como elegible para BlueTFMode_l503_521
        self.mdBlueTFMode_l503_521.addSubMode(self.mdBlueLamdaMode_l503_521)
        # Marcamos BlueLamdaMode_l522_542 como elegible para BlueTFMode_l522_542
        self.mdBlueTFMode_l522_542.addSubMode(self.mdBlueLamdaMode_l522_542)
        # Marcamos BlueLamdaMode_l543_583 como elegible para BlueTFMode_l543_583
        self.mdBlueTFMode_l543_583.addSubMode(self.mdBlueLamdaMode_l543_583)
        # Marcamos BlueLamdaMode_l584_609 como elegible para BlueTFMode_l584_609
        self.mdBlueTFMode_l584_609.addSubMode(self.mdBlueLamdaMode_l584_609)
        # Marcamos BlueLamdaMode_l610_637 como elegible para BlueTFMode_l610_637
        self.mdBlueTFMode_l610_637.addSubMode(self.mdBlueLamdaMode_l610_637)
        # Marcamos BlueLamdaMode_l638_671 como elegible para BlueTFMode_l638_671
        self.mdBlueTFMode_l638_671.addSubMode(self.mdBlueLamdaMode_l638_671)
        # Marcamos BlueLamdaMode_l448_463 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l448_463)
        # Marcamos BlueLamdaMode_l464_480 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l464_480)
        # Marcamos BlueLamdaMode_l481_502 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l481_502)
        # Marcamos BlueLamdaMode_l503_521 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l503_521)
        # Marcamos BlueLamdaMode_l522_542 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l522_542)
        # Marcamos BlueLamdaMode_l543_583 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l543_583)
        # Marcamos BlueLamdaMode_l584_609 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l584_609)
        # Marcamos BlueLamdaMode_l610_637 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l610_637)
        # Marcamos BlueLamdaMode_l638_671 como elegible para BlueTFMode_Engineering
        self.mdBlueTFMode_Engineering.addSubMode(self.mdBlueLamdaMode_l638_671)
        # Marcamos BlueLamda_Range448 como elegible para BlueLamdaMode_l448_463
        self.mdBlueLamdaMode_l448_463.addValue(self.vlBlueLamda_Range448)
        # Marcamos BlueLamda_Range464 como elegible para BlueLamdaMode_l464_480
        self.mdBlueLamdaMode_l464_480.addValue(self.vlBlueLamda_Range464)
        # Marcamos BlueLamda_Range481 como elegible para BlueLamdaMode_l481_502
        self.mdBlueLamdaMode_l481_502.addValue(self.vlBlueLamda_Range481)
        # Marcamos BlueLamda_Range503 como elegible para BlueLamdaMode_l503_521
        self.mdBlueLamdaMode_l503_521.addValue(self.vlBlueLamda_Range503)
        # Marcamos BlueLamda_Range522 como elegible para BlueLamdaMode_l522_542
        self.mdBlueLamdaMode_l522_542.addValue(self.vlBlueLamda_Range522)
        # Marcamos BlueLamda_Range543 como elegible para BlueLamdaMode_l543_583
        self.mdBlueLamdaMode_l543_583.addValue(self.vlBlueLamda_Range543)
        # Marcamos BlueLamda_Range584 como elegible para BlueLamdaMode_l584_609
        self.mdBlueLamdaMode_l584_609.addValue(self.vlBlueLamda_Range584)
        # Marcamos BlueLamda_Range610 como elegible para BlueLamdaMode_l610_637
        self.mdBlueLamdaMode_l610_637.addValue(self.vlBlueLamda_Range610)
        # Marcamos BlueLamda_Range638 como elegible para BlueLamdaMode_l638_671
        self.mdBlueLamdaMode_l638_671.addValue(self.vlBlueLamda_Range638)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_RTFCalib
        self.mdPreOpticsMode_RTFCalib.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_BTFCalib
        self.mdPreOpticsMode_BTFCalib.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzeroMode_Normal como elegible para PreOpticsMode_Engineering
        self.mdPreOpticsMode_Engineering.addSubMode(self.mdzzeroMode_Normal)
        # Marcamos zzero_NormalRange como elegible para zzeroMode_Normal
        self.mdzzeroMode_Normal.addValue(self.vlzzero_NormalRange)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## PreOpticsMode 
    def get_PreOpticsMode(self)-> PORISMode:
        return self.sysPreOptics.getSelectedMode()

    def set_PreOpticsMode(self, mode: PORISMode)-> PORISMode :
        return self.sysPreOptics.selectMode(mode)


    ## FiltersMode 
    def get_FiltersMode(self)-> PORISMode:
        return self.sysFilters.getSelectedMode()

    def set_FiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFilters.selectMode(mode)


    ## prParam Grisms 

    # Grisms
    def get_Grisms(self)-> PORISValue :
        return self.prGrisms.getSelectedValue()

    def set_Grisms(self, value: PORISValue)-> PORISValue :
        return self.prGrisms.setValue(value)


    ## GrismsMode 
    def get_GrismsMode(self)-> PORISMode:
        return self.prGrisms.getSelectedMode()

    def set_GrismsMode(self, mode: PORISMode)-> PORISMode :
        return self.prGrisms.selectMode(mode)


    ## RedTFMode 
    def get_RedTFMode(self)-> PORISMode:
        return self.sysRedTF.getSelectedMode()

    def set_RedTFMode(self, mode: PORISMode)-> PORISMode :
        return self.sysRedTF.selectMode(mode)


    ## prParam RedFWHM 

    # RedFWHM
    def get_RedFWHM(self)-> PORISValue :
        return self.prRedFWHM.getSelectedValue()

    def set_RedFWHM(self, value: PORISValue)-> PORISValue :
        return self.prRedFWHM.setValue(value)


    ## RedFWHMMode 
    def get_RedFWHMMode(self)-> PORISMode:
        return self.prRedFWHM.getSelectedMode()

    def set_RedFWHMMode(self, mode: PORISMode)-> PORISMode :
        return self.prRedFWHM.selectMode(mode)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedFWHMDouble  
    def get_RedFWHMDouble(self)-> float :
        v = self.prRedFWHM.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedFWHMDouble(self, data: float)-> float :
        return self.prRedFWHM.getSelectedValue().setData(data)


    ## prParam RedLamda 

    # RedLamda
    def get_RedLamda(self)-> PORISValue :
        return self.prRedLamda.getSelectedValue()

    def set_RedLamda(self, value: PORISValue)-> PORISValue :
        return self.prRedLamda.setValue(value)


    ## RedLamdaMode 
    def get_RedLamdaMode(self)-> PORISMode:
        return self.prRedLamda.getSelectedMode()

    def set_RedLamdaMode(self, mode: PORISMode)-> PORISMode :
        return self.prRedLamda.selectMode(mode)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## prParam RedTF 

    # RedLamdaDouble  
    def get_RedLamdaDouble(self)-> float :
        v = self.prRedLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_RedLamdaDouble(self, data: float)-> float :
        return self.prRedLamda.getSelectedValue().setData(data)


    ## BlueTFMode 
    def get_BlueTFMode(self)-> PORISMode:
        return self.sysBlueTF.getSelectedMode()

    def set_BlueTFMode(self, mode: PORISMode)-> PORISMode :
        return self.sysBlueTF.selectMode(mode)


    ## prParam BlueFWHM 

    # BlueFWHM
    def get_BlueFWHM(self)-> PORISValue :
        return self.prBlueFWHM.getSelectedValue()

    def set_BlueFWHM(self, value: PORISValue)-> PORISValue :
        return self.prBlueFWHM.setValue(value)


    ## BlueFWHMMode 
    def get_BlueFWHMMode(self)-> PORISMode:
        return self.prBlueFWHM.getSelectedMode()

    def set_BlueFWHMMode(self, mode: PORISMode)-> PORISMode :
        return self.prBlueFWHM.selectMode(mode)


    ## prParam BlueLamda 

    # BlueLamda
    def get_BlueLamda(self)-> PORISValue :
        return self.prBlueLamda.getSelectedValue()

    def set_BlueLamda(self, value: PORISValue)-> PORISValue :
        return self.prBlueLamda.setValue(value)


    ## BlueLamdaMode 
    def get_BlueLamdaMode(self)-> PORISMode:
        return self.prBlueLamda.getSelectedMode()

    def set_BlueLamdaMode(self, mode: PORISMode)-> PORISMode :
        return self.prBlueLamda.selectMode(mode)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam BlueTF 

    # BlueLamdaDouble  
    def get_BlueLamdaDouble(self)-> float :
        v = self.prBlueLamda.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_BlueLamdaDouble(self, data: float)-> float :
        return self.prBlueLamda.getSelectedValue().setData(data)


    ## prParam zzero 

    # zzero
    def get_zzero(self)-> PORISValue :
        return self.przzero.getSelectedValue()

    def set_zzero(self, value: PORISValue)-> PORISValue :
        return self.przzero.setValue(value)


    ## zzeroMode 
    def get_zzeroMode(self)-> PORISMode:
        return self.przzero.getSelectedMode()

    def set_zzeroMode(self, mode: PORISMode)-> PORISMode :
        return self.przzero.selectMode(mode)


    ## prParam PreOptics 

    # zzeroDouble  
    def get_zzeroDouble(self)-> float :
        v = self.przzero.getSelectedValue()
        v.__class__ = PORISValueFloat
        return v.getData()

    def set_zzeroDouble(self, data: float)-> float :
        return self.przzero.getSelectedValue().setData(data)

