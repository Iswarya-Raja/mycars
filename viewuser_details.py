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
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
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
tr:nth-child(odd) {
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

</style>
</head>
<center>
<h2>USER DETAILS</h2>
   <table cellspacing="0" cellpadding="11" style="border-collapse:collapse;">
     <tr><th>S.No<th>NAME<th>DOB<th>CONTACT<th>E-MAIL<th>ADDRESS<th>CITY<th>STATE
     <th>PAN.NO<th>PURPOSE<th>CAR MODEL<th>MODEL YEAR<th>CAR COLOR<th>PRICE EXPECTED<th>CAR IMAGE<th>DELETE</th></tr>""")
for i in r:
    cnt+=1
    print("""
    <tr><td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>%s<td>
    <img src="cars/%s" height="50" width="50">
    <td><a href="delete_user.py?id=%s" onclick="return confirmfn();" style="color:black;font-size:24px;"><i class="fas fa-trash-alt"></i>
    </a>
    </td></tr>"""%(cnt,i[1],i[2],i[3],i[4],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15],i[0]))


print("""  
</table>
</center><br>
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
</script>
</body>
</html>
""")
