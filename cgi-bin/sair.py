#!/usr/bin/python3

import MySQLdb
import cgi, cgitb

form = cgi.FieldStorage()

codigo = form.getvalue("codigod")
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Retirar carro</title>")
print ("</head>")
print ("<style>")
print ("body {")
print ("background-color: SteelBlue")
print ("}")
print (".flex-box {")
print ("  display: flex;")
print ("  align-items: center;")
print ("  justify-content: center;")
print ("}")

print (".content-box {")
print ("  background-color: white;")
print ("  color:#191970;")
print ("  text-align: center;")
print ("  width: 400px;")
print ("}")
print ("</style>")
print ("<body>")
print ("<div class='flex-box'>")
print ("<div class='content-box'>")
print ("<p>")

print ("<body>")

con = MySQLdb.connect(host='localhost', user='mayara', password='Mayara123.', database='estacionamento')
cursor = con.cursor()

cursor.execute('SELECT * FROM clientes')
rsu= cursor.fetchall()

var = 0
for l in rsu:
    cod = str(l[5])
    if (codigo == cod):
        var = 1
        cursor.execute('DELETE FROM clientes where codigo = "%s"'% codigo)
        con.commit()
        print ("<h1><center>")
        print ("Cod&iacute;go correto. Sua retirada foi liberada!")
        print ("</center></h1>")

if (var == 0):
   print ("<h1><center>")
   print ("Cod&iacute;go incorreto. Tente novamente.")
   print ("</center></h1>")
print ("<input style='background-color: SteelBlue; border-color:#191970; color:black' type='button' value='Voltar a tela inicial' onClick="+"document.location='https://3.82.124.239/telaini.html'>")
print ("</p>")
print ("</div>")
print ("</div>")
print ("</body>")
