#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb, smtplib
cgitb.enable()
f=cgi.FieldStorage()
id=f.getvalue("id")
otp=f.getvalue("otp")
submit=f.getvalue("submit")
if submit!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="new")
    cur = conn.cursor()
    q ="""select * from user_table where otp='%s'"""%(otp)
    cur.execute(q)
    r = cur.fetchone()
    if r != None:
        print("""
        <script>
        alert("OTP verified");
        location.href="new_password.py";
        </script>
        """)
    else:
        print("""
        <script>
        alert("OTP Not matched..Please get new OTP");
        location.href="forget_password.html";
        </script>
        """)
    otp = " "
    q = """update user_table set otp='%s'""" % (otp)
    cur.execute(q)
    conn.commit()
    conn.close()