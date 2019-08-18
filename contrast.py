import reexcel
import platdata

ff=reexcel.read_xls('白条开新_基础信息验证_DataModel_CDS_V2.17_20190716.xlsx','信息验证输入输出报文')
wenjian=ff.dict_xls()

systerm=platdata.getdata()
# 找到在excel中有，系统中没有到记录并输出
l1=[]
l2=[]
for i in range(len(wenjian)):
    l1.append(wenjian[i]['字段名称'])
for j in range(len(systerm)):
    l2.append(systerm[j]["paramName"])
c=[a for a in l1 if a not in l2]
if c !=[""]:
	print("系统中无%s记录"%c)
else:
	print("excel中数据全部在系统中有")
for i in range(len(wenjian)):
    for j in range(len(systerm)):
        if wenjian[i]['字段名称'] == systerm[j]["paramName"]:
            # 如果找到了开始对比Java类型
            if wenjian[i]['java类型'] ==systerm[j]['dataType']:
                pass
            else:
                print("%s的java类型不一致" %wenjian[i]['字段名称'],"excel:",wenjian[i]['java类型'] ,"系统:",systerm[j]['dataType'])
            # 对比长度
            if wenjian[i]['长度'] ==systerm[j]['dataLength']:
                pass
            else:
                print("%s的长度不一致" %wenjian[i]['字段名称'],"excel:",wenjian[i]['长度'] ,"系统:",systerm[j]['dataLength'])
            # 对比是否可空
            if wenjian[i]['是否可空'] ==systerm[j]['nullStatus']:
                pass
            else:
                print("%s的是否可空不一致" % wenjian[i]['字段名称'], "excel:",wenjian[i]['是否可空'] ,"系统:",systerm[j]['nullStatus'])
            # 对比精度
            try:
                # 有的记录没有精度
                if wenjian[i]['精度'] == systerm[j]['dataPrecision']:
                    pass

                else:
                    print("%s的精度不一致" % wenjian[i]['字段名称'], "excel:", wenjian[i]['精度'], "系统:",
                          systerm[j]['dataPrecision'])
            except:
                print("请查看excel中%s" % wenjian[i]['字段名称'], "是否填写精度，系统中无这个字段")
                # 将已经对比过的数据删除
            del systerm[j]
            break

        else:
            j+=1



