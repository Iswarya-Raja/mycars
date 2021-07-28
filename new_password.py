#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")

print("""
<html>
<head>
<title>new password</title>
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
<script>
    function pwdcheck()
    {
        var pwd1, pwd2;
        pwd1=document.getElementById('pwd1');
        pwd2=document.getElementById('pwd2');
        if (pwd1.value!=pwd2.value)
        {
        document.getElementById('display').innerHTML="check your password";
        pwd2.value="";
        pwd2.focus();
        }

    }
</script> 
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
<link href="./styles/newpwd.css" type="text/css" rel="stylesheet"/>
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
<body>
<center>
<form action="#" method="post" id="admin-login">
<h2>SET NEW PASSWORD</h2>
<div id="admin-body">
<i class="far fa-user admin-icons"></i>
<input class="input-part" type="email" name="email" placeholder="Enter your Mail-id" required><br><br>
<i class="fas fa-unlock-alt admin-icons"></i>
<input class="input-part" type="password" name="pwd1" id="pwd1" placeholder="Enter your New Password" required><br><br>
<i class="fas fa-unlock-alt admin-icons"></i>
<input class="input-part" type="password" name="pwd2" id="pwd2" placeholder="Retype New Password" onchange="pwdcheck();" required><span id="display"></span><br><br>
<i class="fas fa-sign-in-alt admin-icons"></i>
<input class="input-part" id="login" type="submit" name="sub" onclick="location.href='user_log.py'">
</div>
<input id="cancel" type="button" type="button" value="cancel" onclick="location.href='forget_password.html';"><br><br><br>
</form>
</center>
</body>
</html>
""")
import cgi, pymysql, cgitb, smtplib
cgitb.enable()

f=cgi.FieldStorage()
email=f.getvalue("email")
pwd1=f.getvalue("pwd1")
pwd2=f.getvalue("pwd2")
sub=f.getvalue("sub")

if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="new")
    cur = conn.cursor()

    q="""update user_table set password='%s' where email='%s'"""%(pwd2,email)
    cur.execute(q)
    conn.commit()

    print("""
        <script>
        alert("Password Updated Successfully");
        location.href="user_login.py";
        </script>
        """)
    conn.close()
