#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
print("""
<head>
<link href="./styles/adminlogin.css" type="text/css" rel="stylesheet"/>
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
<style>
body
{
background-image:url("https://static.vecteezy.com/system/resources/previews/000/588/967/non_2x/abstract-geometric-style-smooth-background-blur-background-with-glass-vector-illustration.jpg");
background-repeat: no-repeat;
background-size:100% auto;
}
form{
margin-top:100px;
}
</style>

</head>
<center>

<form id="admin-login" action="#" method="post" autocomplete="off">
<h2>EMPLOYEE LOGIN</h2>
<div id="admin-body">
<i class="far fa-user admin-icons"></i>
<input  class="input-part" type="email" name="email" placeholder="Email-id"  autocomplete="off" required><br><br>
<i class="fas fa-unlock-alt admin-icons"></i>
<input class="input-part" type="password" name="empid" placeholder="Emp-Id"  required><br><br>
<i class="fas fa-sign-in-alt admin-icons"></i>
<input class="input-part" id="login" type="submit" name="sub" value="Login">
</div>
<input id="cancel" type="button" value="Cancel" onclick="location.href='index.html';">
</form>
</center>
""")
import cgi,pymysql,cgitb
cgitb.enable()
f=cgi.FieldStorage()
email=f.getvalue("email")
empid=f.getvalue("empid")
sub=f.getvalue("sub")
#print(f)
if sub!=None:
  conn = pymysql.connect(host="localhost", user="root", password="", database="new")
  cur = conn.cursor()

  q="""select * from emp_table Where email='%s' and empid='%s'"""%(email,empid)
  cur.execute(q)

  r=cur.fetchone()
  if r !=None:
    print("""
    <script>
    alert("Logged in Successfully");
    location.href='emp_profile.py?id=%s';
    </script>
    """%(r[0]))
  else:
    print("""
    <script>
    alert("Invalid Email-Id or Password");
    location.href='emp_login.py';
    </script>
    """)
  conn.close()




