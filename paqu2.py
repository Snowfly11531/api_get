import requests
import json
import xlwt
import openpyxl
import pandas as pd
def export_excel(export,path,time,type):
   #将字典列表转换为DataFrame
   pf = pd.DataFrame(list(export))
   # columns_map = {
   #     'time': '时间',
   #     'val': '雨量值',
   #     'water_potential': '水势',
   #     'ID号': 'id',
   #     '站点名': 'name',
   #     '精度':'lng',
   #     '纬度':'lat',
   #     '类型':'type',
   #     '中文类型':'type_name',
   #     '隶属':'subjection',
   #     '地址':'address',
   #     '地区ID':'area_id',
   # }
   #pf.rename(columns=columns_map, inplace=True)
   #指定字段顺序
   #指定生成的Excel表格名称
   file_path = pd.ExcelWriter(path+'\\'+time+'_'+type+'.xlsx')
   #输出
   pf.to_excel(file_path,encoding = 'utf-8',index = False)
   #保存表格
   file_path.save()

html=requests.get("http://www.ynswj.cn/webapi/api/v1/rain?extra=area&itm=1&area_code=530000&no_data_visible=false&time=[2019-11-27T21:54:03,2019-11-28T21:54:03]")
infos=json.loads(html.text)["data"]
export_excel(infos,r"D:","2019-11-27","雨量")
