from django import forms
from .models import list, Work_Volume, Slab_Level, Site, WV_Main,WV_Daily_Report_Details

class Listform (forms.ModelForm):
    class Meta:
        model = list
        fields= ["item", "completed"]


class WorkVolumeform (forms.ModelForm):
    class Meta:
        model = Work_Volume
        fields= ["Tx_Name", "Is_Active"]


class SlabLevelForm (forms.ModelForm):
    class Meta:
        model = Slab_Level
        fields= ["TX_Slab_Level_Name", "Is_Active"]


class SiteForm (forms.ModelForm):
    class Meta:
        model = Site
        fields= ["TX_Site_Name", "Is_Active"]


class WVMainForm (forms.ModelForm):
    class Meta:
        model = WV_Main
        fields= ["CD_Site", "TX_Site_Supervisor", "TX_Site_In_charge_Design", "TX_Site_In_charge_QS", "TX_Site_Manager"
            ,"TX_Construction_Manager", "Is_Active"]


class WVDailyReportDetailsForm (forms.ModelForm):
    class Meta:
        model = WV_Daily_Report_Details
        fields= ["ID_WV_Main","TX_Panel_No","TX_Zone","CD_Slab_Level","CD_Work","TX_Man_Power_Work","TX_Sur_Joint"
            ,"PU_Kg","PU_PKR","Volume_L","Volume_W","Volume_H","Volume","AREA","Progress","Cement","Rebar_Qty"
            ,"Rebar_Length","Rebar_Size","Is_Active"]
