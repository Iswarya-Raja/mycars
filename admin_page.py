#!C:/Users/User/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type:text/html \r\n\r\n")
print("""
<html>
<head>
<link href="styles/adminpage.css" type="text/css" rel="stylesheet"/>
<link href="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" type="text/ico" rel="icon"/>
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.3/css/all.css" integrity="sha384-SZXxX4whJ79/gErwcOYf+zWLeJdY/qpuqC4cAa9rOGUstPomtqpuNWT9wdPEn2fk" crossorigin="anonymous">
</head>
<body>
<header>
<div id="logo-wrapper">
<div id="logo-background"></div>
<div id="logo"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjp6heWby8AqTEojE8-07S5C0iJMhB35fBvw&usqp=CAU" alt="logo"/></div>
</div>
<div id="company"><h1><span id="s">S</span>mart <span style="padding-left:15px;display:flex;align-items:center"><div id="s">C</div>ars</span></h1></div>
</header>
<section id="main-content">
<div id="sidebar">
<h2>MANAGE EMPLOYEE</h2>
<a href="addnew_emp.py"  target="page1"><i class="fas fa-user-plus">&emsp;</i>Add New Employee</a>
<a href="update_emp.py" target="page1"><i class="fas fa-user-edit">&emsp;</i>Update Employee Data</a>
<a href="viewemp_details.py" target="page1"><i class="fas fa-eye">&emsp;</i>View Employee</a>
<h2>MANAGE USER REGISTRATION</h2>
<a href="viewuser_details.py" target="page1"><i class="fas fa-eye">&emsp;</i>View User Details</a>
<a href="index.html"><i class="fas fa-arrow-circle-left">&emsp;</i>LOGOUT</a>
</div>
<iframe src="welcome.html" name="page1" id="formdisplay"></iframe>
</section>
<footer id="footer">
</footer> 
</body>
</html>
""")