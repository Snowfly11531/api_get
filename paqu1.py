import requests
import xmltodict
from OperateExcel import OperateExcel as OE
import xlwt
import openpyxl
from openpyxl import Workbook,load_workbook
import pandas as pd
# def export_excel(export,path,time,type):
#    #将字典列表转换为DataFrame
#    pf = pd.DataFrame(list(export))
#    #指定字段顺序
#    #指定生成的Excel表格名称
#    file_path = pd.ExcelWriter(path+'\\'+time+'_'+type+'.xlsx')
#    #输出
#    pf.to_excel(file_path,encoding = 'utf-8',index = False)
#    #保存表格
#    file_path.save()
def export_excel(infoList,path,time,type):
    oe=OE()
    oe.OpenOrCreateExcelWorkBookByPathAndName(path,time+"_"+type)
    oe.setOrCreateActiveSheetByname("实时雨量")
    oe.insertDirtList(infoList)
    oe.insertDataColByID(1,[])
    oe.save()

def get_info(time,path):
    headers_sw={
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "455",
        "Content-Type": "text/xml; charset=utf-8",
        "Host": "218.1.102.107:702",
        "Origin": "http://218.1.102.107:8100",
        "Referer": "http://218.1.102.107:8100/indexWater.swf/[[DYNAMIC]]/3",
        "SOAPAction": "http://tempuri.org/GetDtTableXY",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "X-Requested-With": "ShockwaveFlash/32.0.0.293",
    }
    headers_jy={
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "477",
        "Content-Type": "text/xml; charset=utf-8",
        "Host": "218.1.102.107:702",
        "Origin": "http://218.1.102.107:8100",
        "Referer": "http://218.1.102.107:8100/indexWater.swf/[[DYNAMIC]]/3",
        "SOAPAction": "http://tempuri.org/GetDtYQ",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        "X-Requested-With": "ShockwaveFlash/32.0.0.293",
    }
    data_sw='<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' \
            '<SOAP-ENV:Body>' \
            '<tns:GetDtTableXY xmlns:tns="http://tempuri.org/">' \
            '<tns:a>2</tns:a>' \
            '<tns:b>%s</tns:b>' \
            '<tns:c></tns:c>' \
            '<tns:d></tns:d>' \
            '<tns:e></tns:e>' \
            '<tns:f></tns:f>' \
            '</tns:GetDtTableXY>' \
            '</SOAP-ENV:Body>' \
            '</SOAP-ENV:Envelope>'%(time)
    data_jy='<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">' \
            '<SOAP-ENV:Body>' \
            '<tns:GetDtYQ  xmlns:tns="http://tempuri.org/">' \
            '<tns:a>%s</tns:a>' \
            '<tns:b>%s</tns:b>' \
            '<tns:c></tns:c>' \
            '<tns:d></tns:d>' \
            '<tns:e></tns:e>' \
            '<tns:f></tns:f>' \
            '<tns:g>1</tns:g>'\
            '</tns:GetDtYQ>' \
            '</SOAP-ENV:Body>' \
            '</SOAP-ENV:Envelope>'%(time,time)
    html=requests.post("http://218.1.102.107:702/Orcl_Idbs3.asmx",headers=headers_sw,data=data_sw)
    info_dict=xmltodict.parse(html.text)
    tables=info_dict["soap:Envelope"]["soap:Body"]["GetDtTableXYResponse"]["GetDtTableXYResult"]["diffgr:diffgram"]["DocumentElement"]["Table"]
    infos=[]
    for table in tables:
        info={}
        info.update({"站名":table["STNM"] if table["STNM"]!=None else ''})
        info.update({"ID号":table["STCD"] if table["STCD"]!=None else ''})
        info.update({"经度":table["LGTD"] if table["LGTD"]!=None else ''})
        info.update({"纬度":table["LTTD"] if table["LTTD"]!=None else ''})
        info.update({"数据来源":table["FRGRD"] if table["FRGRD"]!=None else ''})
        info.update({"区域归属":table["BSNM"] if table["BSNM"]!=None else ''})
        info.update({"类型":table["STTP"] if table["STTP"]!=None else ''})
        info.update({"时间":table["LASTTM"] if table["LASTTM"]!=None else ''})
        info.update({"水位":table["Z"] if table["Z"]!=None else ''})
        info.update({"警戒水位":table["WRZ"] if table["WRZ"]!=None else ''})
        infos.append(info)
        print(info)
    export_excel(infos,path,time,"水位")
    html1 = requests.post("http://218.1.102.107:702/Orcl_Idbs3.asmx", headers=headers_jy, data=data_jy)
    info_dict = xmltodict.parse(html1.text)
    #print(html1.text)
    #print(info_dict["soap:Envelope"]["soap:Body"])
    tables = info_dict["soap:Envelope"]["soap:Body"]["GetDtYQResponse"]["GetDtYQResult"]["diffgr:diffgram"]["DocumentElement"]["Table"]
    print(tables)
    infos=[]
    for table in tables:
        info={}
        info.update({"站名":table["STNM"] if table["STNM"]!=None else ''})
        info.update({"ID号":table["STCD"] if table["STCD"]!=None else ''})
        info.update({"经度":table["LGTD"] if table["LGTD"]!=None else ''})
        info.update({"纬度":table["LTTD"] if table["LTTD"]!=None else ''})
        info.update({"区域归属":table["BSNM"] if table["BSNM"]!=None else ''})
        info.update({"流域":table["HNNM"] if table["HNNM"]!=None else ''})
        info.update({"类型":table["STTP"] if table["STTP"]!=None else ''})
        info.update({"累计雨量":table["DRP"] if table["DRP"]!=None else ''})
        infos.append(info)
        print(info)
    export_excel(infos, path, time, "雨量")
get_info("2019-11-30","D:\\liangliang_data")