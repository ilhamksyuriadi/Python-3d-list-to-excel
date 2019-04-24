data = [[[[111],[112],[113],[114]],[[121],[122],[123],[124]],[[131],[132],[133],[134]],[[141],[142],[143],[144]]],[[[211],[212],[213],[214]],[[221],[222],[223],[224]],[[231],[232],[233],[234]],[[241],[242],[243],[244]]],[[[311],[312],[313],[314]],[[321],[322],[323],[324]],[[331],[332],[333],[334]],[[341],[342],[343],[344]]]]
import xlsxwriter

sheet_name = ['data 1', 'data 2','data 3']
workbook = xlsxwriter.Workbook('lists.xlsx')

for name in sheet_name:
    sheet = workbook.add_worksheet(name)
    idx = sheet_name.index(name)
    for j in range(len(data[idx])):
        for k in range(len(data[idx][j])):
            value = data[idx][j][k][0]
            sheet.write(j,k,value)
workbook.close()






















