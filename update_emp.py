#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb,os
cgitb.enable()

conn=pymysql.connect(host="localhost", user="root", password="", database="new")
cur=conn.cursor()
f=cgi.FieldStorage()
id=f.getvalue("id")
q="""select * from emp_table where id='%s'"""%(id)
print("""
<head>
<link href="styles/empadd.css" type="text/css" rel="stylesheet"/>
</head>
<form id="add-employee-form" action="#" method="post" autocomplete="off" enctype="multipart/form-data">
  <h1>UPDATE EMPLOYEE DETAILS</h1>
  <div id="hr-line"></div>
  <h3>Name</h3>
  <input class="input-field" type="text" name="name" placeholder="Your Name" required>
  <h3>DOB</h3>
  <input class="input-field" type="date" name="dob" min="1980-01-01" max="2021-12-31" required><br><br>
  <h3>Contact</h3>
  <input class="input-field" type="text" name="contact" placeholder="contact" maxlength="10" pattern="[0-9]{10}" required><br><br>
  <h3>Email Id</h3>
  <input class="input-field" type="email" name="email" placeholder="abc@gmail.com" required><br><br>
  <h3>Address</h3>
  <textarea class="input-field" cols="30" rows="5" name="address" placeholder="D.NO..City..State" required></textarea><br><br>
  <h3>Department</h3>
  <select class="input-field" name="department" id="dept"><br><br>
    <option default>Department</option>
    <option value="SAL">SALES</option>
    <option value="SER">SERVICE</option>
    <option value="ACC">ACCOUNTS</option>
    <option value="MNG">MANAGEMENT</option>
  </select><br><br>
  <h3>Year of Joining:</h3>
  <input class="input-field" type="number" name="yoj" placeholder="yyyy" maxlength="4" min="1990" max="2021" required><br><br>
  <h3>Salary</h3>
  <input class="input-field" type="text" name="salary" placeholder="Rs.." maxlength="10" required><br><br>
  <h3>Profile</h3>
  <input class="profile-field" type="file" name="profile" required><br><br>
  <div id="hr-line"></div>
  <div id="btn">
    <input class="btn-field" type="submit" name="sub" value="submit">
    <input class="btn-field" type="button" value="cancel" onclick="location.href='viewemp_details.py';">
  </div>
</form>
""")
sub=f.getvalue("sub")
if sub!=None:
        name = f.getvalue("name")
        dob = f.getvalue("dob")
        contact = f.getvalue("contact")
        email = f.getvalue("email")
        address = f.getvalue("address")
        department = f.getvalue("department")
        yoj = f.getvalue("yoj")
        salary = f.getvalue("salary")
        profile = f['profile']

        if profile.filename:
            fname = os.path.basename(profile.filename)
            fobj = open('files/' + fname, "wb")
            fobj.write(profile.file.read())

            q="""update emp_table set name='%s',dob='%s',contact='%s',email='%s',address='%s',department='%s',yoj='%s',salary='%s',profile='%s'
            where id='%s'"""%(name,dob,contact,email,address,department,yoj,salary,fname,id)
            cur.execute(q)
            conn.commit()

            print("""
            <script>
            alert("Data updated successfully");
            location.href="viewemp_details.py";
            </script>
            """)
            conn.close()

















