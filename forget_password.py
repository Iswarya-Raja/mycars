#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi, pymysql, cgitb, smtplib
cgitb.enable()
import random as r
f=cgi.FieldStorage()
email=f.getvalue("email")
sub=f.getvalue("sub")
otp = str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9)) + str(r.randint(0, 9))
#print(otp)

if sub!=None:
    conn = pymysql.connect(host="localhost", user="root", password="", database="new")
    cur = conn.cursor()

    q="""update user_table set otp='%s' where email='%s'"""%(otp, email)
    cur.execute(q)
    conn.commit()



    fromaddress = "iswaryatechvolt@gmail.com"
    password = "ishuraja2000"

    msg = """
    Kindly note your OTP:%s
    """%(str(otp))

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromaddress, password)

    server.sendmail(fromaddress, email, msg)
    server.quit()

    print("""
    <script>
    alert("OTP Sended to your Mail Given");
    location.href="otp.html";
    </script>
    """)

    conn.close()

