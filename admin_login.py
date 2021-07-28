#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
print("""
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
<link href="./styles/adminlogin.css" type="text/css" rel="stylesheet"/>
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
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
<form  action="#" method="post" autocomplete="off" id="admin-login">
<h2>ADMIN LOGIN</h2>
<div id="admin-body">
<i class="far fa-user admin-icons"></i>
<input class="input-part" type="text" name="username" placeholder="Username" required autocomplete="off"><br><br>
<i class="fas fa-unlock-alt admin-icons"></i>
<input class="input-part" type="password" name="password" placeholder="Password" required><br><br>
<i class="fas fa-sign-in-alt admin-icons"></i>
<input class="input-part" id="login" type="submit" name="sub" value="LOGIN"><br><br>
</div>
<input id="cancel" type="button" value="Cancel" onclick="location.href='index.html';">
</form>
</center>
""")
import cgi,pymysql,cgitb
cgitb.enable()
f=cgi.FieldStorage()
name=f.getvalue("username")
password=f.getvalue("password")
sub=f.getvalue("sub")
#print(f)
if sub !=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="new")
    cur = conn.cursor()

    q="""select * from admin_table Where username='%s' and password='%s'"""%(name,password)
    cur.execute(q)

    r=cur.fetchone()
    if r !=None:
      print("""
      <script>
      alert("Logged in Successfully");
      location.href='admin_page.py';
      </script>
      """)
    else:
      print("""
      <script>
      alert("Invalid Admin_Id or Password");
      location.href='admin_login.py';
      </script>
      """)
    conn.close()

