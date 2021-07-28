#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
import cgi,pymysql,cgitb
cgitb.enable()

conn = pymysql.connect(host="localhost", user="root", password="", database="new")
cur = conn.cursor()


f=cgi.FieldStorage()
id=f.getvalue("id")

q="""delete from emp_table where id='%s'"""%(id)
cur.execute(q)
conn.commit()

print("""
    <script>
    alert("Data Deleted Successfully");
    location.href="viewemp_details.py";
    </script>
    """)

conn.close()

