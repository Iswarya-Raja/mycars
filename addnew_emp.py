#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb,os, smtplib
cgitb.enable()

conn=pymysql.connect(host="localhost", user="root", password="", database="new")
cur=conn.cursor()

q="""select max(id) from emp_table"""
cur.execute(q)
r=cur.fetchone()

if r[0]!=None:
  n=r[0]
else:
  n=0

if n<9:
  z="000"
elif n<99:
  z="00"
elif n<999:
  z="0"
else:
  z=""
eid="E"+z+str(n+1)
print("""
<head>
<link href="styles/empadd.css" type="text/css" rel="stylesheet"/>
</head>
<form id="add-employee-form" action="#" method="post" autocomplete="off" enctype="multipart/form-data" >
  <h1>ADD EMPLOYEE DETAILS</h1>
  <div id="hr-line"></div>
  <input type="hidden" id="eid" value="%s">
  <h3> Name</h3>
  <input class="input-field" type="text" name="name" placeholder="Your Name" required><br><br>
  <h3> DOB</h3>
  <input class="input-field" type="date" name="dob" min="1900-01-01" max="2021-12-31" required><br><br>
  <h3>Contact</h3>
  <input class="input-field" type="text" name="contact" placeholder="contact" maxlength="10" pattern="[0-9]{10}" required><br><br>
  <h3>Email ID</h3>
  <input class="input-field" type="email" name="email" placeholder="abc@gmail.com" required>
  <h3>Address</h3>
  <textarea class="input-field" cols="30" rows="5" name="address" placeholder="D.NO..City..State" required></textarea>
  <h3>Department</h3>
  <select class="input-field" name="department" id="dept" onchange="document.getElementById('drno').value=this.value+document.getElementById('eid').value;">
    <option default>Department</option>
    <option value="SAL">SALES</option>
    <option value="SER">SERVICE</option>
    <option value="ACC">ACCOUNTS</option>
    <option value="MNG">MANAGEMENT</option>
  </select><br><br>
  <h3>Emp-ID:</h3>
  <input class="input-field" type="text" name="empid" placeholder="Enter your Emp Id" id="drno" readonly>
  <h3>Year of Joining</h3>
  <input class="input-field" type="number" name="yoj" placeholder="yyyy" maxlength="4" min="1990" max="2021"  required><br><br>
  <h3>Salary</h3>
  <input class="input-field" type="text" name="salary" placeholder="Rs.." maxlength="10" required><br><br>
  <h3>Profile</h3>
  <input class="profile-field" type="file" name="profile" required>
  <div id="hr-line"></div>
  <div id="btn">
    <input class="btn-field" type="submit" name="sub" value="submit">
    <input class="btn-field" type="button" value="cancel" onclick="location.href='welcome.html';">
  </div>
</form>
"""%(eid))
f=cgi.FieldStorage()
sub=f.getvalue("sub")
if sub!=None:
    name = f.getvalue("name")
    dob = f.getvalue("dob")
    contact = f.getvalue("contact")
    email= f.getvalue("email")
    address= f.getvalue("address")
    department= f.getvalue("department")
    empid = f.getvalue("empid")
    yoj = f.getvalue("yoj")
    salary= f.getvalue("salary")
    profile = f['profile']


    if profile.filename:
        fname=os.path.basename(profile.filename)
        fobj=open('files/'+fname,"wb")
        fobj.write(profile.file.read())

        q="""insert into emp_table(name,dob,contact,email,address,department,empid,yoj,salary,profile)
        values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"""%(name,dob,contact,email,address,department,empid,yoj,salary,fname)
        cur.execute(q)
        conn.commit()

        print("""
        <script>
        alert("Data inserted successfully");
        </script>
        """)
        fromaddress = "iswaryatechvolt@gmail.com"
        password = "ishuraja2000"

        msg = """
        Your Employment Data has been registered to our database.
        Kindly note your Employee-Id:%s
        Is there any queries..feel free to contact to the below number.


        Thanks & Regards..
        Smart Cars 
        coimbatore.
        contact:98764-53832
        """ % (empid)

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()

        server.login(fromaddress, password)

        server.sendmail(fromaddress, email, msg)
        server.quit()

        print("""
        <script>
        alert("Mail sended successfully..");
        location.href="viewemp_details.py";
        </script>
        """)
        conn.close()

