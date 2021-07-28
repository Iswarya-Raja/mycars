#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

print("""
<head>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
<link href="./styles/userlogin.css" type="text/css" rel="stylesheet"/>
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
<form action="#" method="post" autocomlete="off" id="admin-login">
<h2>USER LOGIN</h2>
<div id="admin-body">
<i class="far fa-user admin-icons"></i>
<input class="input-part" type="email" name="email" placeholder="email-id" required><br><br>
<i class="fas fa-unlock-alt admin-icons"></i>
<input class="input-part" type="password" name="password" placeholder="password" required >
<p class="forget-pwd" ><span class="click-text"> Click Here</span><a href="forget_password.html" style="color:orange;text-decoration:none">  Forget Password</a></p> 
<i class="fas fa-sign-in-alt admin-icons"></i>
<input class="input-part" id="login" type="submit" name="sub" value="Login">
</div>
<input id="cancel" type="button" type="button" value="Cancel" onclick="location.href='index.html';"><br>
<p class="new-text">New user <a href='user_reg.py';" style="color:orange;text-decoration:none"> Register Here</a></p>
</form>
</center>
""")
import cgi,pymysql,cgitb

f=cgi.FieldStorage()
email=f.getvalue("email")
password=f.getvalue("password")
sub=f.getvalue("sub")

if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="new")
    cur = conn.cursor()


    q="""select * from user_table where email='%s' and password='%s'"""%(email,password)
    cur.execute(q)
    r=cur.fetchone()
    if r != None:
        print("""<script>
        alert("Logged in Successfully");
        location.href='car_details.html';
        </script>""")
    else:
        print("""
           <script>
           alert("Invalid username or password");
           location.href="user_login.py";
           </script>
           """)
    conn.close()

