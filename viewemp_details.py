#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb
cgitb.enable()
conn=pymysql.connect(host="localhost", user="root", password="", database="new")
cur=conn.cursor()
q="""select * from emp_table"""
cur.execute(q)
r=cur.fetchall()
cnt=0
print("""
<html>
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
</head>
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
margin-left:30px;
padding:5px;
background-color:#fff;
box-shadow: 0 0 8px skyblue;
color:black;
}
tr:nth-child(odd) {
box-shadow: 0 0 8px skyblue;
}
</style>
<body>
<center><h3>EMPLOYEE DETAILS</h3>
<table cellspacing="0" cellpadding="12"  style="border-collapse:collapse;">
<tr><th>PROFILE<th>EMP-ID<th>NAME<th>DOB<th>CONTACT<th>E-MAIL<th>ADDRESS<th>DEPARTMENT<th>YOJ<th>SALARY<th>UPDATE<th>DELETE</th></tr>""")
for i in r:
    cnt+=1
    print("""
      <tr><td><img src="files/%s" height="50" width="50" style="border-radius:50px;"><td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td><a href="update_emp.py?id=%s" style="color:black;font-size:24px;"><i class="fas fa-user-edit"></i></a>
      <td><a href="delete_emp.py?id=%s" onclick="return confirmfn();" style="color:black;font-size:24px;"><i class="fas fa-trash-alt"></i></a></td></tr>"""%(i[10],i[7],i[1],i[2],i[3],i[4],i[5],i[6],i[8],i[9],i[0],i[0]))
print("""</table>
</center><br><br>
<a href="welcome.html" style="text-decoration:none" id="back">Back</a>
<script>
    function confirmfn()
    {
        if(confirm("Do you Want to Delete?"))
        {
             return true;
        }
        return false;
    }
</script><br><br><br><br><br><br>      
</body>
</html>
""")


