import reexcel
import platdata

ff=reexcel.read_xls('白条开新_基础信息验证_DataModel_CDS_V2.17_20190716.xlsx','信息验证输入输出报文')
wenjian=ff.dict_xls()
systerm=platdata.getdata()
for i in range(len(wenjian)):
    for j in range(len(systerm)):
        if wenjian[i]['字段名称']==systerm[j]["paramName"]:
            if wenjian[i]['java类型'] ==systerm[j]['dataType']:
                pass
            else:
                print("excel中%s的java类型与系统中不一致" %wenjian[i]['字段名称'],wenjian[i]['java类型'] ,systerm[j]['dataType'])
            if wenjian[i]['长度'] ==systerm[j]['dataLength']:
                pass
            else:
                print("excel中%s的长度与系统中不一致" %wenjian[i]['字段名称'],wenjian[i]['长度'] ,systerm[j]['dataLength'])
            # 有的记录没有精度
            # if wenjian[i]['精度'] ==systerm[j]['dataPrecision']:
            #     pass
            # else:
            #     print("excel中%s的精度与系统中不一致" %wenjian[i]['字段名称'])
            if wenjian[i]['是否可空'] ==systerm[j]['nullStatus']:
                pass
            else:
                print("excel中%s的是否可空与系统中不一致" % wenjian[i]['字段名称'], wenjian[i]['是否可空'] ,systerm[j]['nullStatus'])
        else:
            j+=1



