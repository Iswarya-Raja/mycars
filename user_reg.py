#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb, os, smtplib
cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="new")
cur = conn.cursor()
print("""
<html>
<head>
<link href="styles/userreg.css" type="text/css" rel="stylesheet"/>
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
<style>
body
{
background-image:url("https://static.vecteezy.com/system/resources/previews/000/588/967/non_2x/abstract-geometric-style-smooth-background-blur-background-with-glass-vector-illustration.jpg");
background-repeat: no-repeat;
background-size:100% 2500px;
}
form{
margin-top:100px;
}
</style>

</head>  
<body>
<form id="user-form" action="#" method="post" autocomplete="off" enctype="multipart/form-data"><br>
<h1>USER REGISTRATION</h1> 
<div id="hr-line"></div>    
<h3>Name</h3>
    <input class="input-field" type="text" name="name" placeholder="Your Name" required>
<h3>DOB</h3>
<input class="input-field" type="date" name="dob" min="1900-01-01" max="2021-12-31" required>
<h3>Contact</h3>
<input class="input-field" type="text" name="contact" placeholder="Contact" maxlength="10"  pattern="[0-9]{10}" required>
<h3>Email</h3>
<input class="input-field" type="email" name="email" placeholder="abc@gmail.com" required>
<h3>Address</h3>
<textarea class="input-field" cols="30" rows="5" name="address" placeholder="D/No,Street Name.." required></textarea>
<h3>State</h3>
   <select class="input-field" name="state" required>
      <option default>select State</option>
      <option value="TamilNadu">TamilNadu</option>
      <option value="Telangana">Telangana</option>
      <option value="Kerala">Kerala</option>
      <option value="Maharashtra">Maharashtra</option>
      <option value="U.P">U.P</option>
      <option value="Rajashtan">Rajashtan</option>
    </select><br>
    <h3>City</h3>
    <input class="input-field" type="text" name="city" maxlength="25" placeholder="Your City" required>
    <h3>Pancard-Id:</h3>
    <input class="input-field" type="text" name="panno" placeholder="Pan-No" maxlength="10" required>
<h3>Purpose:</h3>
<p class="check-input"><input type="radio" name="purpose" value="Buy">Buy</p>
<p class="check-input"><input type="radio" name="purpose" value="Sale">Sale</p>
<center><h4>*If sale please provide the below details</h4></center>
<h3>Car-Model</h3>
<input class="input-field" type="text" name="carmodel" maxlength="20" placeholder="eg:swift">
<h3>Model-year</h3>
<input class="input-field" type="number" name="modelyear" maxlength="4" placeholder="eg:2010" min="1990" max="2021">
<h3>Car-Color</h3>
<input class="input-field" type="text" name="carcolor" maxlength="10" placeholder="eg:Red">
<h3>Price-Expected</h3>
<input class="input-field" type="text" name="price" maxlength="10" placeholder="eg:Rs.1Lk or 50,000">
<h3>Car-Image</h3>
<input class="profile-field" type="file" name="carimage">
<h3>Password</h3> 
<input class="input-field" type="password" name="pwd1" id="pwd1" placeholder="your Password" required>
<h3>Retype Password</h3>
<input class="input-field" type="password" name="pwd2" id="pwd2" placeholder="Retype Password" onchange="pwdcheck();" required>
<span id="display"></span>
<div id="hr-line"></div>
<div id="btn">    
<input class="btn-field" type="submit" name="sub" value="Register">
<input class="btn-field" type="button" value="cancel" onclick="location.href='user_login.py';">
  </div>      
</form>
</body>
</html>
""")
f=cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
        name=f.getvalue("name")
        dob = f.getvalue("dob")
        contact = f.getvalue("contact")
        email= f.getvalue("email")
        address= f.getvalue("address")
        state= f.getvalue("state")
        city = f.getvalue("city")
        panno= f.getvalue("panno")
        purpose= f.getvalue("purpose")
        carmodel= f.getvalue("carmodel")
        modelyear = f.getvalue("modelyear")
        carcolor= f.getvalue("carcolor")
        price = f.getvalue("price")
        password1 = f.getvalue("pwd1")
        password2 = f.getvalue("pwd2")
        profile = f['carimage']

        if profile.filename:
                fname = os.path.basename(profile.filename)
                fobj = open('files/' + fname, "wb")
                fobj.write(profile.file.read())

                q="""insert into user_table(name,dob,contact,email,address,city,state,panno,purpose,carmodel,modelyear,carcolor,priceexpected,carimage,password)
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name,dob,contact,email,address,city,state,panno,purpose,carmodel,modelyear,carcolor,price,fname,password2)
                cur.execute(q)
                conn.commit()

                print("""
                <script>
                alert("Registered successfully");
                </script>
                """)
                fromaddress = "iswaryatechvolt@gmail.com"
                password = "ishuraja2000"

                msg = """
                Your Registration Were Successfully Completed!
                --------Thankyou For Your Login--------
                            -keep in touch-
                """

                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo()
                server.starttls()

                server.login(fromaddress, password)

                server.sendmail(fromaddress, email, msg)
                server.quit()

                print("""
                <script>
                alert("Confirmation Mail sended to the provided Mail-id..Kindly check your mail");
                location.href="user_login.py";
                </script>
                """)

                conn.close()