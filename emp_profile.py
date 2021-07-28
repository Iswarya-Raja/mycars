#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb
cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="new")
cur = conn.cursor()
f = cgi.FieldStorage()
id = f.getvalue("id")
q = """select * from emp_table where id ='%s'"""%(id)
cur.execute(q)
r = cur.fetchone()
#print(r)
print("""
<head>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap">
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
<style>
tr:nth-child(even) {
  background-color: skyblue;
  box-shadow: 0 0 8px skyblue;
}
tr{
height:70px;
text-align:center;
font-family: "Montserrat", sans-serif;
font-size: 20px;
font-weight: bolder;
}
a{
margin-left:380px;
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
<center>
<table cellspacing="0" cellpadding="12"  width="600px;" style="border-collapse:collapse;">
<tr><th><img src="files/%s" height="130px" width="150px" style="border-radius:5px;"></th></tr>
<tr><td>Name: %s</td></tr>
<tr><td>DOB: %s</td></tr>
<tr><td>Contact: %s</td></tr>
<tr><td>Address: %s</td></tr>
<tr><td>Department: %s</td></tr>
<tr><td>Emp-ID: %s</td></tr>
<tr><td>YOJ: %s</td></tr>
</table>
</center><br><br>
<a href="task.py" style="text-decoration:none;font-size:12pt;font-weight:bold">Customer Details</a>
<a href="index.html" style="text-decoration:none;font-size:12pt;font-weight:bold">Logout</a><br><br>

"""%(r[10],r[1],r[2],r[3],r[4],r[5],r[6],r[7]))
conn.close()