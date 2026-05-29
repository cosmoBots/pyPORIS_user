from PORIS import *

class osifiltPORIS(PORISDoc):
    def __init__(self, project_id):
        super().__init__(project_id)
        self.sysFilters = PORISSys("Filters")
        self.setRoot(self.sysFilters)
        self.prUFilters = PORISParam("UFilters")
        self.prOS = PORISParam("OS")
        self.prBroad = PORISParam("Broad")
        self.mdFiltersMode_OS = PORISMode("FiltersMode_OS")
        self.mdFiltersMode_UFilter = PORISMode("FiltersMode_UFilter")
        self.vlUFilters_U500_17 = PORISValue("UFilters_U500_17")
        self.vlUFilters_U517_17 = PORISValue("UFilters_U517_17")
        self.vlUFilters_U534_17 = PORISValue("UFilters_U534_17")
        self.vlUFilters_U551_17 = PORISValue("UFilters_U551_17")
        self.vlUFilters_U568_17 = PORISValue("UFilters_U568_17")
        self.vlUFilters_U585_17 = PORISValue("UFilters_U585_17")
        self.vlUFilters_U602_17 = PORISValue("UFilters_U602_17")
        self.vlUFilters_U619_17 = PORISValue("UFilters_U619_17")
        self.vlUFilters_U636_17 = PORISValue("UFilters_U636_17")
        self.vlUFilters_U653_17 = PORISValue("UFilters_U653_17")
        self.vlUFilters_U670_17 = PORISValue("UFilters_U670_17")
        self.vlUFilters_U687_17 = PORISValue("UFilters_U687_17")
        self.vlUFilters_U704_17 = PORISValue("UFilters_U704_17")
        self.vlUFilters_U721_17 = PORISValue("UFilters_U721_17")
        self.vlUFilters_U738_17 = PORISValue("UFilters_U738_17")
        self.vlUFilters_U755_17 = PORISValue("UFilters_U755_17")
        self.vlUFilters_U772_17 = PORISValue("UFilters_U772_17")
        self.vlUFilters_U789_17 = PORISValue("UFilters_U789_17")
        self.vlUFilters_U806_17 = PORISValue("UFilters_U806_17")
        self.vlUFilters_U823_17 = PORISValue("UFilters_U823_17")
        self.vlUFilters_U840_17 = PORISValue("UFilters_U840_17")
        self.vlUFilters_U857_17 = PORISValue("UFilters_U857_17")
        self.vlUFilters_U883_35 = PORISValue("UFilters_U883_35")
        self.vlUFilters_U913_25 = PORISValue("UFilters_U913_25")
        self.vlUFilters_U941_33 = PORISValue("UFilters_U941_33")
        self.mdUFiltersMode_U5xx = PORISMode("UFiltersMode_U5xx")
        self.mdUFiltersMode_U6xx = PORISMode("UFiltersMode_U6xx")
        self.mdUFiltersMode_U7xx = PORISMode("UFiltersMode_U7xx")
        self.mdUFiltersMode_U8xx = PORISMode("UFiltersMode_U8xx")
        self.mdUFiltersMode_U9xx = PORISMode("UFiltersMode_U9xx")
        self.vlOS_f504_16 = PORISValue("OS_f504_16")
        self.vlOS_f509_16 = PORISValue("OS_f509_16")
        self.vlOS_f514_16 = PORISValue("OS_f514_16")
        self.vlOS_f519_16 = PORISValue("OS_f519_16")
        self.vlOS_f525_17 = PORISValue("OS_f525_17")
        self.vlOS_f530_17 = PORISValue("OS_f530_17")
        self.vlOS_f536_17 = PORISValue("OS_f536_17")
        self.vlOS_f542_18 = PORISValue("OS_f542_18")
        self.vlOS_f548_18 = PORISValue("OS_f548_18")
        self.vlOS_f554_18 = PORISValue("OS_f554_18")
        self.vlOS_f561_19 = PORISValue("OS_f561_19")
        self.vlOS_f568_19 = PORISValue("OS_f568_19")
        self.vlOS_f575_19 = PORISValue("OS_f575_19")
        self.vlOS_f583_20 = PORISValue("OS_f583_20")
        self.vlOS_f591_21 = PORISValue("OS_f591_21")
        self.vlOS_f599_22 = PORISValue("OS_f599_22")
        self.mdOSMode_f5xx = PORISMode("OSMode_f5xx")
        self.vlOS_f477_14 = PORISValue("OS_f477_14")
        self.vlOS_f481_14 = PORISValue("OS_f481_14")
        self.mdOSMode_f4xx = PORISMode("OSMode_f4xx")
        self.vlOS_f486_14 = PORISValue("OS_f486_14")
        self.vlOS_f469_14 = PORISValue("OS_f469_14")
        self.vlOS_f461_13 = PORISValue("OS_f461_13")
        self.vlOS_f499_15 = PORISValue("OS_f499_15")
        self.vlOS_f454_13 = PORISValue("OS_f454_13")
        self.vlOS_f451_13 = PORISValue("OS_f451_13")
        self.vlOS_f495_15 = PORISValue("OS_f495_15")
        self.vlOS_f465_13 = PORISValue("OS_f465_13")
        self.vlOS_f490_15 = PORISValue("OS_f490_15")
        self.vlOS_f458_13 = PORISValue("OS_f458_13")
        self.vlOS_f473_14 = PORISValue("OS_f473_14")
        self.vlOS_f638_25 = PORISValue("OS_f638_25")
        self.vlOS_f680_43 = PORISValue("OS_f680_43")
        self.vlOS_f608_22 = PORISValue("OS_f608_22")
        self.vlOS_f627_24 = PORISValue("OS_f627_24")
        self.vlOS_f694_44 = PORISValue("OS_f694_44")
        self.vlOS_f617_23 = PORISValue("OS_f617_23")
        self.vlOS_f666_36 = PORISValue("OS_f666_36")
        self.vlOS_f649_25 = PORISValue("OS_f649_25")
        self.vlOS_f657_35 = PORISValue("OS_f657_35")
        self.mdOSMode_f6xx = PORISMode("OSMode_f6xx")
        self.vlOS_f661_27 = PORISValue("OS_f661_27")
        self.vlOS_f723_45 = PORISValue("OS_f723_45")
        self.mdOSMode_f7xx = PORISMode("OSMode_f7xx")
        self.vlOS_f770_50 = PORISValue("OS_f770_50")
        self.vlOS_f738_49 = PORISValue("OS_f738_49")
        self.vlOS_f709_45 = PORISValue("OS_f709_45")
        self.vlOS_f754_50 = PORISValue("OS_f754_50")
        self.vlOS_f785_48 = PORISValue("OS_f785_48")
        self.vlOS_f923_34 = PORISValue("OS_f923_34")
        self.mdOSMode_f9xx = PORISMode("OSMode_f9xx")
        self.vlOS_f932_34 = PORISValue("OS_f932_34")
        self.vlOS_f927_34 = PORISValue("OS_f927_34")
        self.vlOS_f902_44 = PORISValue("OS_f902_44")
        self.vlOS_f919_41 = PORISValue("OS_f919_41")
        self.vlOS_f910_40 = PORISValue("OS_f910_40")
        self.vlOS_f802_51 = PORISValue("OS_f802_51")
        self.vlOS_f878_59 = PORISValue("OS_f878_59")
        self.vlOS_f858_58 = PORISValue("OS_f858_58")
        self.vlOS_f893_50 = PORISValue("OS_f893_50")
        self.vlOS_f838_58 = PORISValue("OS_f838_58")
        self.vlOS_f819_52 = PORISValue("OS_f819_52")
        self.mdOSMode_f8xx = PORISMode("OSMode_f8xx")
        self.mdFiltersMode_NoFilter = PORISMode("FiltersMode_NoFilter")
        self.mdFiltersMode_GR = PORISMode("FiltersMode_GR")
        self.vlBroad_Sloan_u = PORISValue("Broad_Sloan_u")
        self.vlBroad_Sloan_g = PORISValue("Broad_Sloan_g")
        self.vlBroad_Sloan_r = PORISValue("Broad_Sloan_r")
        self.vlBroad_Sloan_i = PORISValue("Broad_Sloan_i")
        self.vlBroad_Sloan_z = PORISValue("Broad_Sloan_z")
        self.mdBroadMode_All = PORISMode("BroadMode_All")
        self.mdFiltersMode_Broad = PORISMode("FiltersMode_Broad")
        self.mdFiltersMode_OSCalc = PORISMode("FiltersMode_OSCalc")
        self.mdFiltersMode_Engineering = PORISMode("FiltersMode_Engineering")
        self.addItem(self.sysFilters)
        self.sysFilters.ident = "OSI-0137"
        self.sysFilters.setXMLName('Filters')
        self.sysFilters.description = ""
        self.addItem(self.prUFilters)
        self.prUFilters.ident = "OSI-0159"
        self.prUFilters.setXMLName('UFilters')
        self.prUFilters.description = ""
        self.sysFilters.addParam(self.prUFilters)
        self.addItem(self.prOS)
        self.prOS.ident = "OSI-0160"
        self.prOS.setXMLName('OS')
        self.prOS.description = ""
        self.sysFilters.addParam(self.prOS)
        self.addItem(self.prBroad)
        self.prBroad.ident = "OSI-0619"
        self.prBroad.setXMLName('Broad')
        self.prBroad.description = ""
        self.sysFilters.addParam(self.prBroad)
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
        self.addItem(self.vlUFilters_U500_17)
        self.vlUFilters_U500_17.ident = "OSI-0033"
        self.vlUFilters_U500_17.setXMLName('U500/17')
        self.vlUFilters_U500_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U500_17)
        self.addItem(self.vlUFilters_U517_17)
        self.vlUFilters_U517_17.ident = "OSI-0034"
        self.vlUFilters_U517_17.setXMLName('U517/17')
        self.vlUFilters_U517_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U517_17)
        self.addItem(self.vlUFilters_U534_17)
        self.vlUFilters_U534_17.ident = "OSI-0035"
        self.vlUFilters_U534_17.setXMLName('U534/17')
        self.vlUFilters_U534_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U534_17)
        self.addItem(self.vlUFilters_U551_17)
        self.vlUFilters_U551_17.ident = "OSI-0036"
        self.vlUFilters_U551_17.setXMLName('U551/17')
        self.vlUFilters_U551_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U551_17)
        self.addItem(self.vlUFilters_U568_17)
        self.vlUFilters_U568_17.ident = "OSI-0037"
        self.vlUFilters_U568_17.setXMLName('U568/17')
        self.vlUFilters_U568_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U568_17)
        self.addItem(self.vlUFilters_U585_17)
        self.vlUFilters_U585_17.ident = "OSI-0038"
        self.vlUFilters_U585_17.setXMLName('U585/17')
        self.vlUFilters_U585_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U585_17)
        self.addItem(self.vlUFilters_U602_17)
        self.vlUFilters_U602_17.ident = "OSI-0039"
        self.vlUFilters_U602_17.setXMLName('U602/17')
        self.vlUFilters_U602_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U602_17)
        self.addItem(self.vlUFilters_U619_17)
        self.vlUFilters_U619_17.ident = "OSI-0040"
        self.vlUFilters_U619_17.setXMLName('U619/17')
        self.vlUFilters_U619_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U619_17)
        self.addItem(self.vlUFilters_U636_17)
        self.vlUFilters_U636_17.ident = "OSI-0041"
        self.vlUFilters_U636_17.setXMLName('U636/17')
        self.vlUFilters_U636_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U636_17)
        self.addItem(self.vlUFilters_U653_17)
        self.vlUFilters_U653_17.ident = "OSI-0042"
        self.vlUFilters_U653_17.setXMLName('U653/17')
        self.vlUFilters_U653_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U653_17)
        self.addItem(self.vlUFilters_U670_17)
        self.vlUFilters_U670_17.ident = "OSI-0043"
        self.vlUFilters_U670_17.setXMLName('U670/17')
        self.vlUFilters_U670_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U670_17)
        self.addItem(self.vlUFilters_U687_17)
        self.vlUFilters_U687_17.ident = "OSI-0044"
        self.vlUFilters_U687_17.setXMLName('U687/17')
        self.vlUFilters_U687_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U687_17)
        self.addItem(self.vlUFilters_U704_17)
        self.vlUFilters_U704_17.ident = "OSI-0045"
        self.vlUFilters_U704_17.setXMLName('U704/17')
        self.vlUFilters_U704_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U704_17)
        self.addItem(self.vlUFilters_U721_17)
        self.vlUFilters_U721_17.ident = "OSI-0046"
        self.vlUFilters_U721_17.setXMLName('U721/17')
        self.vlUFilters_U721_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U721_17)
        self.addItem(self.vlUFilters_U738_17)
        self.vlUFilters_U738_17.ident = "OSI-0047"
        self.vlUFilters_U738_17.setXMLName('U738/17')
        self.vlUFilters_U738_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U738_17)
        self.addItem(self.vlUFilters_U755_17)
        self.vlUFilters_U755_17.ident = "OSI-0048"
        self.vlUFilters_U755_17.setXMLName('U755/17')
        self.vlUFilters_U755_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U755_17)
        self.addItem(self.vlUFilters_U772_17)
        self.vlUFilters_U772_17.ident = "OSI-0049"
        self.vlUFilters_U772_17.setXMLName('U772/17')
        self.vlUFilters_U772_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U772_17)
        self.addItem(self.vlUFilters_U789_17)
        self.vlUFilters_U789_17.ident = "OSI-0050"
        self.vlUFilters_U789_17.setXMLName('U789/17')
        self.vlUFilters_U789_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U789_17)
        self.addItem(self.vlUFilters_U806_17)
        self.vlUFilters_U806_17.ident = "OSI-0051"
        self.vlUFilters_U806_17.setXMLName('U806/17')
        self.vlUFilters_U806_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U806_17)
        self.addItem(self.vlUFilters_U823_17)
        self.vlUFilters_U823_17.ident = "OSI-0052"
        self.vlUFilters_U823_17.setXMLName('U823/17')
        self.vlUFilters_U823_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U823_17)
        self.addItem(self.vlUFilters_U840_17)
        self.vlUFilters_U840_17.ident = "OSI-0053"
        self.vlUFilters_U840_17.setXMLName('U840/17')
        self.vlUFilters_U840_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U840_17)
        self.addItem(self.vlUFilters_U857_17)
        self.vlUFilters_U857_17.ident = "OSI-0054"
        self.vlUFilters_U857_17.setXMLName('U857/17')
        self.vlUFilters_U857_17.description = ""
        self.prUFilters.addValue(self.vlUFilters_U857_17)
        self.addItem(self.vlUFilters_U883_35)
        self.vlUFilters_U883_35.ident = "OSI-0055"
        self.vlUFilters_U883_35.setXMLName('U883/35')
        self.vlUFilters_U883_35.description = ""
        self.prUFilters.addValue(self.vlUFilters_U883_35)
        self.addItem(self.vlUFilters_U913_25)
        self.vlUFilters_U913_25.ident = "OSI-0056"
        self.vlUFilters_U913_25.setXMLName('U913/25')
        self.vlUFilters_U913_25.description = ""
        self.prUFilters.addValue(self.vlUFilters_U913_25)
        self.addItem(self.vlUFilters_U941_33)
        self.vlUFilters_U941_33.ident = "OSI-0057"
        self.vlUFilters_U941_33.setXMLName('U941/33')
        self.vlUFilters_U941_33.description = ""
        self.prUFilters.addValue(self.vlUFilters_U941_33)
        self.addItem(self.mdUFiltersMode_U5xx)
        self.mdUFiltersMode_U5xx.ident = "OSI-0148"
        self.mdUFiltersMode_U5xx.setXMLName('U5xx')
        self.mdUFiltersMode_U5xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U5xx)
        self.addItem(self.mdUFiltersMode_U6xx)
        self.mdUFiltersMode_U6xx.ident = "OSI-0149"
        self.mdUFiltersMode_U6xx.setXMLName('U6xx')
        self.mdUFiltersMode_U6xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U6xx)
        self.addItem(self.mdUFiltersMode_U7xx)
        self.mdUFiltersMode_U7xx.ident = "OSI-0150"
        self.mdUFiltersMode_U7xx.setXMLName('U7xx')
        self.mdUFiltersMode_U7xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U7xx)
        self.addItem(self.mdUFiltersMode_U8xx)
        self.mdUFiltersMode_U8xx.ident = "OSI-0151"
        self.mdUFiltersMode_U8xx.setXMLName('U8xx')
        self.mdUFiltersMode_U8xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U8xx)
        self.addItem(self.mdUFiltersMode_U9xx)
        self.mdUFiltersMode_U9xx.ident = "OSI-0152"
        self.mdUFiltersMode_U9xx.setXMLName('U9xx')
        self.mdUFiltersMode_U9xx.description = ""
        self.prUFilters.addMode(self.mdUFiltersMode_U9xx)
        self.addItem(self.vlOS_f504_16)
        self.vlOS_f504_16.ident = "OSI-0071"
        self.vlOS_f504_16.setXMLName('f504/16')
        self.vlOS_f504_16.description = ""
        self.prOS.addValue(self.vlOS_f504_16)
        self.addItem(self.vlOS_f509_16)
        self.vlOS_f509_16.ident = "OSI-0072"
        self.vlOS_f509_16.setXMLName('f509/16')
        self.vlOS_f509_16.description = ""
        self.prOS.addValue(self.vlOS_f509_16)
        self.addItem(self.vlOS_f514_16)
        self.vlOS_f514_16.ident = "OSI-0073"
        self.vlOS_f514_16.setXMLName('f514/16')
        self.vlOS_f514_16.description = ""
        self.prOS.addValue(self.vlOS_f514_16)
        self.addItem(self.vlOS_f519_16)
        self.vlOS_f519_16.ident = "OSI-0074"
        self.vlOS_f519_16.setXMLName('f519/16')
        self.vlOS_f519_16.description = ""
        self.prOS.addValue(self.vlOS_f519_16)
        self.addItem(self.vlOS_f525_17)
        self.vlOS_f525_17.ident = "OSI-0075"
        self.vlOS_f525_17.setXMLName('f525/17')
        self.vlOS_f525_17.description = ""
        self.prOS.addValue(self.vlOS_f525_17)
        self.addItem(self.vlOS_f530_17)
        self.vlOS_f530_17.ident = "OSI-0076"
        self.vlOS_f530_17.setXMLName('f530/17')
        self.vlOS_f530_17.description = ""
        self.prOS.addValue(self.vlOS_f530_17)
        self.addItem(self.vlOS_f536_17)
        self.vlOS_f536_17.ident = "OSI-0077"
        self.vlOS_f536_17.setXMLName('f536/17')
        self.vlOS_f536_17.description = ""
        self.prOS.addValue(self.vlOS_f536_17)
        self.addItem(self.vlOS_f542_18)
        self.vlOS_f542_18.ident = "OSI-0078"
        self.vlOS_f542_18.setXMLName('f542/18')
        self.vlOS_f542_18.description = ""
        self.prOS.addValue(self.vlOS_f542_18)
        self.addItem(self.vlOS_f548_18)
        self.vlOS_f548_18.ident = "OSI-0079"
        self.vlOS_f548_18.setXMLName('f548/18')
        self.vlOS_f548_18.description = ""
        self.prOS.addValue(self.vlOS_f548_18)
        self.addItem(self.vlOS_f554_18)
        self.vlOS_f554_18.ident = "OSI-0080"
        self.vlOS_f554_18.setXMLName('f554/18')
        self.vlOS_f554_18.description = ""
        self.prOS.addValue(self.vlOS_f554_18)
        self.addItem(self.vlOS_f561_19)
        self.vlOS_f561_19.ident = "OSI-0081"
        self.vlOS_f561_19.setXMLName('f561/19')
        self.vlOS_f561_19.description = ""
        self.prOS.addValue(self.vlOS_f561_19)
        self.addItem(self.vlOS_f568_19)
        self.vlOS_f568_19.ident = "OSI-0082"
        self.vlOS_f568_19.setXMLName('f568/19')
        self.vlOS_f568_19.description = ""
        self.prOS.addValue(self.vlOS_f568_19)
        self.addItem(self.vlOS_f575_19)
        self.vlOS_f575_19.ident = "OSI-0083"
        self.vlOS_f575_19.setXMLName('f575/19')
        self.vlOS_f575_19.description = ""
        self.prOS.addValue(self.vlOS_f575_19)
        self.addItem(self.vlOS_f583_20)
        self.vlOS_f583_20.ident = "OSI-0084"
        self.vlOS_f583_20.setXMLName('f583/20')
        self.vlOS_f583_20.description = ""
        self.prOS.addValue(self.vlOS_f583_20)
        self.addItem(self.vlOS_f591_21)
        self.vlOS_f591_21.ident = "OSI-0085"
        self.vlOS_f591_21.setXMLName('f591/21')
        self.vlOS_f591_21.description = ""
        self.prOS.addValue(self.vlOS_f591_21)
        self.addItem(self.vlOS_f599_22)
        self.vlOS_f599_22.ident = "OSI-0086"
        self.vlOS_f599_22.setXMLName('f599/22')
        self.vlOS_f599_22.description = ""
        self.prOS.addValue(self.vlOS_f599_22)
        self.addItem(self.mdOSMode_f5xx)
        self.mdOSMode_f5xx.ident = "OSI-0153"
        self.mdOSMode_f5xx.setXMLName('f5xx')
        self.mdOSMode_f5xx.description = ""
        self.prOS.addMode(self.mdOSMode_f5xx)
        self.addItem(self.vlOS_f477_14)
        self.vlOS_f477_14.ident = "OSI-0065"
        self.vlOS_f477_14.setXMLName('f477/14')
        self.vlOS_f477_14.description = ""
        self.prOS.addValue(self.vlOS_f477_14)
        self.addItem(self.vlOS_f481_14)
        self.vlOS_f481_14.ident = "OSI-0066"
        self.vlOS_f481_14.setXMLName('f481/14')
        self.vlOS_f481_14.description = ""
        self.prOS.addValue(self.vlOS_f481_14)
        self.addItem(self.mdOSMode_f4xx)
        self.mdOSMode_f4xx.ident = "OSI-0154"
        self.mdOSMode_f4xx.setXMLName('f4xx')
        self.mdOSMode_f4xx.description = ""
        self.prOS.addMode(self.mdOSMode_f4xx)
        self.addItem(self.vlOS_f486_14)
        self.vlOS_f486_14.ident = "OSI-0067"
        self.vlOS_f486_14.setXMLName('f486/14')
        self.vlOS_f486_14.description = ""
        self.prOS.addValue(self.vlOS_f486_14)
        self.addItem(self.vlOS_f469_14)
        self.vlOS_f469_14.ident = "OSI-0063"
        self.vlOS_f469_14.setXMLName('f469/14')
        self.vlOS_f469_14.description = ""
        self.prOS.addValue(self.vlOS_f469_14)
        self.addItem(self.vlOS_f461_13)
        self.vlOS_f461_13.ident = "OSI-0061"
        self.vlOS_f461_13.setXMLName('f461/13')
        self.vlOS_f461_13.description = ""
        self.prOS.addValue(self.vlOS_f461_13)
        self.addItem(self.vlOS_f499_15)
        self.vlOS_f499_15.ident = "OSI-0070"
        self.vlOS_f499_15.setXMLName('f499/15')
        self.vlOS_f499_15.description = ""
        self.prOS.addValue(self.vlOS_f499_15)
        self.addItem(self.vlOS_f454_13)
        self.vlOS_f454_13.ident = "OSI-0059"
        self.vlOS_f454_13.setXMLName('f454/13')
        self.vlOS_f454_13.description = ""
        self.prOS.addValue(self.vlOS_f454_13)
        self.addItem(self.vlOS_f451_13)
        self.vlOS_f451_13.ident = "OSI-0058"
        self.vlOS_f451_13.setXMLName('f451/13')
        self.vlOS_f451_13.description = ""
        self.prOS.addValue(self.vlOS_f451_13)
        self.addItem(self.vlOS_f495_15)
        self.vlOS_f495_15.ident = "OSI-0069"
        self.vlOS_f495_15.setXMLName('f495/15')
        self.vlOS_f495_15.description = ""
        self.prOS.addValue(self.vlOS_f495_15)
        self.addItem(self.vlOS_f465_13)
        self.vlOS_f465_13.ident = "OSI-0062"
        self.vlOS_f465_13.setXMLName('f465/13')
        self.vlOS_f465_13.description = ""
        self.prOS.addValue(self.vlOS_f465_13)
        self.addItem(self.vlOS_f490_15)
        self.vlOS_f490_15.ident = "OSI-0068"
        self.vlOS_f490_15.setXMLName('f490/15')
        self.vlOS_f490_15.description = ""
        self.prOS.addValue(self.vlOS_f490_15)
        self.addItem(self.vlOS_f458_13)
        self.vlOS_f458_13.ident = "OSI-0060"
        self.vlOS_f458_13.setXMLName('f458/13')
        self.vlOS_f458_13.description = ""
        self.prOS.addValue(self.vlOS_f458_13)
        self.addItem(self.vlOS_f473_14)
        self.vlOS_f473_14.ident = "OSI-0064"
        self.vlOS_f473_14.setXMLName('f473/14')
        self.vlOS_f473_14.description = ""
        self.prOS.addValue(self.vlOS_f473_14)
        self.addItem(self.vlOS_f638_25)
        self.vlOS_f638_25.ident = "OSI-0090"
        self.vlOS_f638_25.setXMLName('f638/25')
        self.vlOS_f638_25.description = ""
        self.prOS.addValue(self.vlOS_f638_25)
        self.addItem(self.vlOS_f680_43)
        self.vlOS_f680_43.ident = "OSI-0095"
        self.vlOS_f680_43.setXMLName('f680/43')
        self.vlOS_f680_43.description = ""
        self.prOS.addValue(self.vlOS_f680_43)
        self.addItem(self.vlOS_f608_22)
        self.vlOS_f608_22.ident = "OSI-0087"
        self.vlOS_f608_22.setXMLName('f608/22')
        self.vlOS_f608_22.description = ""
        self.prOS.addValue(self.vlOS_f608_22)
        self.addItem(self.vlOS_f627_24)
        self.vlOS_f627_24.ident = "OSI-0089"
        self.vlOS_f627_24.setXMLName('f627/24')
        self.vlOS_f627_24.description = ""
        self.prOS.addValue(self.vlOS_f627_24)
        self.addItem(self.vlOS_f694_44)
        self.vlOS_f694_44.ident = "OSI-0096"
        self.vlOS_f694_44.setXMLName('f694/44')
        self.vlOS_f694_44.description = ""
        self.prOS.addValue(self.vlOS_f694_44)
        self.addItem(self.vlOS_f617_23)
        self.vlOS_f617_23.ident = "OSI-0088"
        self.vlOS_f617_23.setXMLName('f617/23')
        self.vlOS_f617_23.description = ""
        self.prOS.addValue(self.vlOS_f617_23)
        self.addItem(self.vlOS_f666_36)
        self.vlOS_f666_36.ident = "OSI-0094"
        self.vlOS_f666_36.setXMLName('f666/36')
        self.vlOS_f666_36.description = ""
        self.prOS.addValue(self.vlOS_f666_36)
        self.addItem(self.vlOS_f649_25)
        self.vlOS_f649_25.ident = "OSI-0091"
        self.vlOS_f649_25.setXMLName('f649/25')
        self.vlOS_f649_25.description = ""
        self.prOS.addValue(self.vlOS_f649_25)
        self.addItem(self.vlOS_f657_35)
        self.vlOS_f657_35.ident = "OSI-0093"
        self.vlOS_f657_35.setXMLName('f657/35')
        self.vlOS_f657_35.description = ""
        self.prOS.addValue(self.vlOS_f657_35)
        self.addItem(self.mdOSMode_f6xx)
        self.mdOSMode_f6xx.ident = "OSI-0155"
        self.mdOSMode_f6xx.setXMLName('f6xx')
        self.mdOSMode_f6xx.description = ""
        self.prOS.addMode(self.mdOSMode_f6xx)
        self.addItem(self.vlOS_f661_27)
        self.vlOS_f661_27.ident = "OSI-0092"
        self.vlOS_f661_27.setXMLName('f661/27')
        self.vlOS_f661_27.description = ""
        self.prOS.addValue(self.vlOS_f661_27)
        self.addItem(self.vlOS_f723_45)
        self.vlOS_f723_45.ident = "OSI-0098"
        self.vlOS_f723_45.setXMLName('f723/45')
        self.vlOS_f723_45.description = ""
        self.prOS.addValue(self.vlOS_f723_45)
        self.addItem(self.mdOSMode_f7xx)
        self.mdOSMode_f7xx.ident = "OSI-0156"
        self.mdOSMode_f7xx.setXMLName('f7xx')
        self.mdOSMode_f7xx.description = ""
        self.prOS.addMode(self.mdOSMode_f7xx)
        self.addItem(self.vlOS_f770_50)
        self.vlOS_f770_50.ident = "OSI-0101"
        self.vlOS_f770_50.setXMLName('f770/50')
        self.vlOS_f770_50.description = ""
        self.prOS.addValue(self.vlOS_f770_50)
        self.addItem(self.vlOS_f738_49)
        self.vlOS_f738_49.ident = "OSI-0099"
        self.vlOS_f738_49.setXMLName('f738/49')
        self.vlOS_f738_49.description = ""
        self.prOS.addValue(self.vlOS_f738_49)
        self.addItem(self.vlOS_f709_45)
        self.vlOS_f709_45.ident = "OSI-0097"
        self.vlOS_f709_45.setXMLName('f709/45')
        self.vlOS_f709_45.description = ""
        self.prOS.addValue(self.vlOS_f709_45)
        self.addItem(self.vlOS_f754_50)
        self.vlOS_f754_50.ident = "OSI-0100"
        self.vlOS_f754_50.setXMLName('f754/50')
        self.vlOS_f754_50.description = ""
        self.prOS.addValue(self.vlOS_f754_50)
        self.addItem(self.vlOS_f785_48)
        self.vlOS_f785_48.ident = "OSI-0102"
        self.vlOS_f785_48.setXMLName('f785/48')
        self.vlOS_f785_48.description = ""
        self.prOS.addValue(self.vlOS_f785_48)
        self.addItem(self.vlOS_f923_34)
        self.vlOS_f923_34.ident = "OSI-0112"
        self.vlOS_f923_34.setXMLName('f923/34')
        self.vlOS_f923_34.description = ""
        self.prOS.addValue(self.vlOS_f923_34)
        self.addItem(self.mdOSMode_f9xx)
        self.mdOSMode_f9xx.ident = "OSI-0157"
        self.mdOSMode_f9xx.setXMLName('f9xx')
        self.mdOSMode_f9xx.description = ""
        self.prOS.addMode(self.mdOSMode_f9xx)
        self.addItem(self.vlOS_f932_34)
        self.vlOS_f932_34.ident = "OSI-0114"
        self.vlOS_f932_34.setXMLName('f932/34')
        self.vlOS_f932_34.description = ""
        self.prOS.addValue(self.vlOS_f932_34)
        self.addItem(self.vlOS_f927_34)
        self.vlOS_f927_34.ident = "OSI-0113"
        self.vlOS_f927_34.setXMLName('f927/34')
        self.vlOS_f927_34.description = ""
        self.prOS.addValue(self.vlOS_f927_34)
        self.addItem(self.vlOS_f902_44)
        self.vlOS_f902_44.ident = "OSI-0109"
        self.vlOS_f902_44.setXMLName('f902/44')
        self.vlOS_f902_44.description = ""
        self.prOS.addValue(self.vlOS_f902_44)
        self.addItem(self.vlOS_f919_41)
        self.vlOS_f919_41.ident = "OSI-0111"
        self.vlOS_f919_41.setXMLName('f919/41')
        self.vlOS_f919_41.description = ""
        self.prOS.addValue(self.vlOS_f919_41)
        self.addItem(self.vlOS_f910_40)
        self.vlOS_f910_40.ident = "OSI-0110"
        self.vlOS_f910_40.setXMLName('f910/40')
        self.vlOS_f910_40.description = ""
        self.prOS.addValue(self.vlOS_f910_40)
        self.addItem(self.vlOS_f802_51)
        self.vlOS_f802_51.ident = "OSI-0103"
        self.vlOS_f802_51.setXMLName('f802/51')
        self.vlOS_f802_51.description = ""
        self.prOS.addValue(self.vlOS_f802_51)
        self.addItem(self.vlOS_f878_59)
        self.vlOS_f878_59.ident = "OSI-0107"
        self.vlOS_f878_59.setXMLName('f878/59')
        self.vlOS_f878_59.description = ""
        self.prOS.addValue(self.vlOS_f878_59)
        self.addItem(self.vlOS_f858_58)
        self.vlOS_f858_58.ident = "OSI-0106"
        self.vlOS_f858_58.setXMLName('f858/58')
        self.vlOS_f858_58.description = ""
        self.prOS.addValue(self.vlOS_f858_58)
        self.addItem(self.vlOS_f893_50)
        self.vlOS_f893_50.ident = "OSI-0108"
        self.vlOS_f893_50.setXMLName('f893/50')
        self.vlOS_f893_50.description = ""
        self.prOS.addValue(self.vlOS_f893_50)
        self.addItem(self.vlOS_f838_58)
        self.vlOS_f838_58.ident = "OSI-0105"
        self.vlOS_f838_58.setXMLName('f838/58')
        self.vlOS_f838_58.description = ""
        self.prOS.addValue(self.vlOS_f838_58)
        self.addItem(self.vlOS_f819_52)
        self.vlOS_f819_52.ident = "OSI-0104"
        self.vlOS_f819_52.setXMLName('f819/52')
        self.vlOS_f819_52.description = ""
        self.prOS.addValue(self.vlOS_f819_52)
        self.addItem(self.mdOSMode_f8xx)
        self.mdOSMode_f8xx.ident = "OSI-0158"
        self.mdOSMode_f8xx.setXMLName('f8xx')
        self.mdOSMode_f8xx.description = ""
        self.prOS.addMode(self.mdOSMode_f8xx)
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
        self.addItem(self.vlBroad_Sloan_u)
        self.vlBroad_Sloan_u.ident = "OSI-0028"
        self.vlBroad_Sloan_u.setXMLName('Sloan_u')
        self.vlBroad_Sloan_u.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_u)
        self.addItem(self.vlBroad_Sloan_g)
        self.vlBroad_Sloan_g.ident = "OSI-0029"
        self.vlBroad_Sloan_g.setXMLName('Sloan_g')
        self.vlBroad_Sloan_g.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_g)
        self.addItem(self.vlBroad_Sloan_r)
        self.vlBroad_Sloan_r.ident = "OSI-0030"
        self.vlBroad_Sloan_r.setXMLName('Sloan_r')
        self.vlBroad_Sloan_r.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_r)
        self.addItem(self.vlBroad_Sloan_i)
        self.vlBroad_Sloan_i.ident = "OSI-0031"
        self.vlBroad_Sloan_i.setXMLName('Sloan_i')
        self.vlBroad_Sloan_i.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_i)
        self.addItem(self.vlBroad_Sloan_z)
        self.vlBroad_Sloan_z.ident = "OSI-0032"
        self.vlBroad_Sloan_z.setXMLName('Sloan_z')
        self.vlBroad_Sloan_z.description = ""
        self.prBroad.addValue(self.vlBroad_Sloan_z)
        self.addItem(self.mdBroadMode_All)
        self.mdBroadMode_All.ident = "OSI-0618"
        self.mdBroadMode_All.setXMLName('All')
        self.mdBroadMode_All.description = ""
        self.prBroad.addMode(self.mdBroadMode_All)
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
        self.addItem(self.mdFiltersMode_Engineering)
        self.mdFiltersMode_Engineering.ident = "ENG-1"
        self.mdFiltersMode_Engineering.setXMLName('Engineering')
        self.mdFiltersMode_Engineering.description = "Filters engineering mode"
        self.sysFilters.addMode(self.mdFiltersMode_Engineering)
        # Marcamos UFiltersMode_U9xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U9xx)
        # Marcamos UFiltersMode_U8xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U8xx)
        # Marcamos UFiltersMode_U7xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U7xx)
        # Marcamos UFiltersMode_U6xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U6xx)
        # Marcamos UFiltersMode_U5xx como elegible para FiltersMode_UFilter
        self.mdFiltersMode_UFilter.addSubMode(self.mdUFiltersMode_U5xx)
        # Marcamos UFiltersMode_U5xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U5xx)
        # Marcamos UFiltersMode_U6xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U6xx)
        # Marcamos UFiltersMode_U7xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U7xx)
        # Marcamos UFiltersMode_U8xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U8xx)
        # Marcamos UFiltersMode_U9xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdUFiltersMode_U9xx)
        # Marcamos UFilters_U551_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U551_17)
        # Marcamos UFilters_U568_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U568_17)
        # Marcamos UFilters_U534_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U534_17)
        # Marcamos UFilters_U500_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U500_17)
        # Marcamos UFilters_U517_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U517_17)
        # Marcamos UFilters_U585_17 como elegible para UFiltersMode_U5xx
        self.mdUFiltersMode_U5xx.addValue(self.vlUFilters_U585_17)
        # Marcamos UFilters_U653_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U653_17)
        # Marcamos UFilters_U670_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U670_17)
        # Marcamos UFilters_U687_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U687_17)
        # Marcamos UFilters_U602_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U602_17)
        # Marcamos UFilters_U636_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U636_17)
        # Marcamos UFilters_U619_17 como elegible para UFiltersMode_U6xx
        self.mdUFiltersMode_U6xx.addValue(self.vlUFilters_U619_17)
        # Marcamos UFilters_U772_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U772_17)
        # Marcamos UFilters_U721_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U721_17)
        # Marcamos UFilters_U755_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U755_17)
        # Marcamos UFilters_U704_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U704_17)
        # Marcamos UFilters_U738_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U738_17)
        # Marcamos UFilters_U789_17 como elegible para UFiltersMode_U7xx
        self.mdUFiltersMode_U7xx.addValue(self.vlUFilters_U789_17)
        # Marcamos UFilters_U806_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U806_17)
        # Marcamos UFilters_U840_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U840_17)
        # Marcamos UFilters_U857_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U857_17)
        # Marcamos UFilters_U823_17 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U823_17)
        # Marcamos UFilters_U883_35 como elegible para UFiltersMode_U8xx
        self.mdUFiltersMode_U8xx.addValue(self.vlUFilters_U883_35)
        # Marcamos UFilters_U941_33 como elegible para UFiltersMode_U9xx
        self.mdUFiltersMode_U9xx.addValue(self.vlUFilters_U941_33)
        # Marcamos UFilters_U913_25 como elegible para UFiltersMode_U9xx
        self.mdUFiltersMode_U9xx.addValue(self.vlUFilters_U913_25)
        # Marcamos OSMode_f8xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f8xx)
        # Marcamos OSMode_f9xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f9xx)
        # Marcamos OSMode_f7xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f7xx)
        # Marcamos OSMode_f6xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f6xx)
        # Marcamos OSMode_f4xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f4xx)
        # Marcamos OSMode_f5xx como elegible para FiltersMode_OS
        self.mdFiltersMode_OS.addSubMode(self.mdOSMode_f5xx)
        # Marcamos OSMode_f5xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f5xx)
        # Marcamos OSMode_f4xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f4xx)
        # Marcamos OSMode_f6xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f6xx)
        # Marcamos OSMode_f7xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f7xx)
        # Marcamos OSMode_f9xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f9xx)
        # Marcamos OSMode_f8xx como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdOSMode_f8xx)
        # Marcamos OS_f504_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f504_16)
        # Marcamos OS_f509_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f509_16)
        # Marcamos OS_f514_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f514_16)
        # Marcamos OS_f519_16 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f519_16)
        # Marcamos OS_f525_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f525_17)
        # Marcamos OS_f530_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f530_17)
        # Marcamos OS_f536_17 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f536_17)
        # Marcamos OS_f542_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f542_18)
        # Marcamos OS_f548_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f548_18)
        # Marcamos OS_f554_18 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f554_18)
        # Marcamos OS_f561_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f561_19)
        # Marcamos OS_f568_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f568_19)
        # Marcamos OS_f575_19 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f575_19)
        # Marcamos OS_f583_20 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f583_20)
        # Marcamos OS_f591_21 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f591_21)
        # Marcamos OS_f599_22 como elegible para OSMode_f5xx
        self.mdOSMode_f5xx.addValue(self.vlOS_f599_22)
        # Marcamos OS_f451_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f451_13)
        # Marcamos OS_f477_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f477_14)
        # Marcamos OS_f454_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f454_13)
        # Marcamos OS_f481_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f481_14)
        # Marcamos OS_f458_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f458_13)
        # Marcamos OS_f486_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f486_14)
        # Marcamos OS_f461_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f461_13)
        # Marcamos OS_f490_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f490_15)
        # Marcamos OS_f495_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f495_15)
        # Marcamos OS_f465_13 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f465_13)
        # Marcamos OS_f499_15 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f499_15)
        # Marcamos OS_f469_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f469_14)
        # Marcamos OS_f473_14 como elegible para OSMode_f4xx
        self.mdOSMode_f4xx.addValue(self.vlOS_f473_14)
        # Marcamos OS_f608_22 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f608_22)
        # Marcamos OS_f617_23 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f617_23)
        # Marcamos OS_f627_24 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f627_24)
        # Marcamos OS_f638_25 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f638_25)
        # Marcamos OS_f649_25 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f649_25)
        # Marcamos OS_f657_35 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f657_35)
        # Marcamos OS_f661_27 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f661_27)
        # Marcamos OS_f666_36 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f666_36)
        # Marcamos OS_f680_43 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f680_43)
        # Marcamos OS_f694_44 como elegible para OSMode_f6xx
        self.mdOSMode_f6xx.addValue(self.vlOS_f694_44)
        # Marcamos OS_f709_45 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f709_45)
        # Marcamos OS_f754_50 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f754_50)
        # Marcamos OS_f770_50 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f770_50)
        # Marcamos OS_f723_45 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f723_45)
        # Marcamos OS_f738_49 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f738_49)
        # Marcamos OS_f785_48 como elegible para OSMode_f7xx
        self.mdOSMode_f7xx.addValue(self.vlOS_f785_48)
        # Marcamos OS_f902_44 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f902_44)
        # Marcamos OS_f910_40 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f910_40)
        # Marcamos OS_f919_41 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f919_41)
        # Marcamos OS_f923_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f923_34)
        # Marcamos OS_f927_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f927_34)
        # Marcamos OS_f932_34 como elegible para OSMode_f9xx
        self.mdOSMode_f9xx.addValue(self.vlOS_f932_34)
        # Marcamos OS_f802_51 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f802_51)
        # Marcamos OS_f819_52 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f819_52)
        # Marcamos OS_f838_58 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f838_58)
        # Marcamos OS_f858_58 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f858_58)
        # Marcamos OS_f878_59 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f878_59)
        # Marcamos OS_f893_50 como elegible para OSMode_f8xx
        self.mdOSMode_f8xx.addValue(self.vlOS_f893_50)
        # Marcamos BroadMode_All como elegible para FiltersMode_Broad
        self.mdFiltersMode_Broad.addSubMode(self.mdBroadMode_All)
        # Marcamos BroadMode_All como elegible para FiltersMode_Engineering
        self.mdFiltersMode_Engineering.addSubMode(self.mdBroadMode_All)
        # Marcamos Broad_Sloan_z como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_z)
        # Marcamos Broad_Sloan_u como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_u)
        # Marcamos Broad_Sloan_r como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_r)
        # Marcamos Broad_Sloan_g como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_g)
        # Marcamos Broad_Sloan_i como elegible para BroadMode_All
        self.mdBroadMode_All.addValue(self.vlBroad_Sloan_i)

    #----------------------------------------------------------------------
    #  Specific methods
    #----------------------------------------------------------------------


    ## FiltersMode 
    def get_FiltersMode(self)-> PORISMode:
        return self.sysFilters.getSelectedMode()

    def set_FiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.sysFilters.selectMode(mode)


    ## prParam UFilters 

    # UFilters
    def get_UFilters(self)-> PORISValue :
        return self.prUFilters.getSelectedValue()

    def set_UFilters(self, value: PORISValue)-> PORISValue :
        return self.prUFilters.setValue(value)


    ## UFiltersMode 
    def get_UFiltersMode(self)-> PORISMode:
        return self.prUFilters.getSelectedMode()

    def set_UFiltersMode(self, mode: PORISMode)-> PORISMode :
        return self.prUFilters.selectMode(mode)


    ## prParam OS 

    # OS
    def get_OS(self)-> PORISValue :
        return self.prOS.getSelectedValue()

    def set_OS(self, value: PORISValue)-> PORISValue :
        return self.prOS.setValue(value)


    ## OSMode 
    def get_OSMode(self)-> PORISMode:
        return self.prOS.getSelectedMode()

    def set_OSMode(self, mode: PORISMode)-> PORISMode :
        return self.prOS.selectMode(mode)


    ## prParam Broad 

    # Broad
    def get_Broad(self)-> PORISValue :
        return self.prBroad.getSelectedValue()

    def set_Broad(self, value: PORISValue)-> PORISValue :
        return self.prBroad.setValue(value)


    ## BroadMode 
    def get_BroadMode(self)-> PORISMode:
        return self.prBroad.getSelectedMode()

    def set_BroadMode(self, mode: PORISMode)-> PORISMode :
        return self.prBroad.selectMode(mode)

