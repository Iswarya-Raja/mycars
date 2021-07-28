#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

import pymysql
conn = pymysql.connect(host="localhost", user="root", password="", database="new")
cur = conn.cursor()

q="select * from user_table"
cur.execute(q)
r=cur.fetchall()
cnt=0
print("""
<html>
<head>
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
<style>
tr
{
text-align:center;
font-family:sans-serif;
font-weight:bold;
}
tr:nth-child(even) {
  background-color: skyblue;
  box-shadow: 0 0 8px skyblue;
}
#back
{
margin-left:50px;
padding:5px;
background-color:#fff;
box-shadow: 0 0 8px skyblue;
color:black;
}
tr:nth-child(odd) {
box-shadow: 0 0 8px skyblue;
}
</style>
</head>
<body>
<center>
<h2>CUSTOMER DETAILS</h2>
   <table cellspacing="0" cellpadding="11" style="border-collapse:collapse;">
     <tr><th>S.No<th>NAME<th>DOB<th>CONTACT<th>E-MAIL
     <th>PURPOSE<th>CAR MODEL<th>MODEL YEAR<th>CAR COLOR<th>PRICE EXPECTED<th>CAR IMAGE</th></tr>""")
for i in r:
    cnt+=1
    print("""
    <tr><td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>
    <img src="cars/%s" height="50" width="50">
    </td></tr>"""%(cnt,i[1],i[2],i[3],i[4],i[10],i[11],i[12],i[13],i[14],i[15]))


print("""  
</table>
</center><br><br>
<a href="admin_page.py" style="text-decoration:none" id="back">Back</a><br><br><br>
</body>
</html>
""")
