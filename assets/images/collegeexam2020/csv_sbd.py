import os, html

#open the text file pushed out by crawlsbd
f = open("sobaodanh.txt","r", encoding="UTF-8")
a = (f.read())
#remove all the uneceesary thing
a = a.replace("\n","").replace("\r","")
a = a.replace('!DOCTYPE html><html><head>    <meta charset="utf-8" />    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Show - Sở Giáo dục và Đào tạo TP HCM</title>    <link href="/Content/css?v=Xso9L40tE7BMv39QjIwZA-y7XWNRBA0m2c4mZornwBo1" rel="stylesheet"/>    <script src="/bundles/modernizr?v=wBEWDufH_8Md-Pbioxomt90vm6tJN2Pyy9u9zHtWsPo1"></script>    <script src="/bundles/jquery?v=FVs3ACwOLIVInrAl5sdzR2jrCDmVOWFbZMY6g6Q0ulE1"></script>    <script src="/bundles/bootstrap?v=2Fz3B0iizV2NnnamQFrx-NbYJNTFeBJ2GM05SilbtQU1"></script>    <script src="/bundles/jqueryui"></script>    <link href="/bundles/fonts" rel="stylesheet"/>   </head><body>    <nav class="navbar navbar-inverse">        <div class="container-fluid">            <div class="navbar-header">                <img style="float:left" src="/Images/Logo_so.png" width="85" /><div> <label style="margin-top: 12px; color: #eeeeee ; font-size: x-large">TRA CỨU ĐIỂM</label>   		<label style="color: #eeeeee ; font-size: medium ">KỲ THI TỐT NGHIỆP TRUNG HỌC PHỔ THÔNG 2020</label>                              </div>                           </div>                   </div>    </nav>           <div class="container body-content" style="margin-top:50px">            <table style="margin-top:50px; border: 1px solid; width:100%">        <tr>            <td style="border: 1px solid ; font-weight: bold ">                ','')
a = a.replace('            </td>            <td style="border: 1px solid ; font-weight: bold">                ',',')
a = a.replace('            </td>                   </tr>        <tr>            <td style="border: 1px solid">                ','\n')
a = a.replace('            </td>            <td style="border: 1px solid">                ',',')
a = a.replace('               </td>        </tr>    </table><br />        <br />          </div>         </body></html><Họ và Tên,Ngày sinh,Điểm thi',"")
a = a.replace('<Họ và Tên',"fullname")
a = a.replace('Ngày sinh',"dob")
#make it readable
a = html.unescape(a)

#create a new file and write a in
nf = open("sobaodanhnew.txt","w",encoding="UTF-8")
nf.write(a)
nf.close()

nf = open('sobaodanhnew.txt',"r",encoding="UTF-8")
b = nf.readlines()
c = list()

# loop through the lines of the text file, turn it into a csv
monhoc = ['Toán:', 'Ngữ văn:', 'Vật lí:', 'Hóa học:', 'Sinh học:', 'Lịch sử:', 'Địa lí:', 'GDCD:', 'KHTN:', 'KHXH:', 'Tiếng Anh:', 'Tiếng Pháp:', 'Tiếng Trung:', 'Tiếng Nhật:', 'Tiếng Đức:','Tiếng Nga:']
c.append(b[0].rstrip("Điểm thi\n") + "Toán,Văn,Lý,Hoá,Sinh,Sử,Địa,GDCD,KHTN,KHXH,TA,TP,TT,TN,TD,TNga\n")
for i in b[1:]:
    diem = str()
    d = i.rsplit(sep=",")
    for x in monhoc:
        if x in i:
            diem = diem + ',' + str(i.split(x)[1].strip()[0:4])
        else:
            diem = diem + ',' + str(-1)
    diem = diem + '\n'
    c.append(d[0]+","+d[1]+ diem)


nf = open('sobaodanh.csv','w',encoding='UTF-8')
for i in c:
    nf.write(i)
nf.close()