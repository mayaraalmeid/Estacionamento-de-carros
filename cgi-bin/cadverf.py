#!/usr/bin/python3

import MySQLdb
import cgi, cgitb
import random

form = cgi.FieldStorage()

placa = form.getvalue("placa")
modelo = form.getvalue("modelo")
cor = form.getvalue("cor")
imagem = form.getvalue("imagem")
print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>estacionamento</title>")
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

codigo = (random.randrange(1000,999999999))
cursor.execute('SELECT * FROM clientes')
rsu= cursor.fetchall()

for l in rsu:
    cod = str(l[5])
    if (codigo == cod):
        print ("Tente novamente")

cursor.execute('INSERT INTO clientes (placa, modelo,cor, codigo) VALUES (%s, %s, %s, %s)', (placa, modelo, cor, codigo))
con.commit()

print ("<h1><center>")
print ("Estacionamento liberado! Pode entrar e estacionar seu ve&iacute;culo.")
print ("</center></h1>")
print ("<br>")
print ("<center>O seu cod&iacute;go est&aacute; logo abaixo, ele ser&aacute; necess&aacute;rio para retirar seu carro.<br>")

cursor.execute('SELECT * FROM clientes where placa= "%s"'% placa)
codigo= cursor.fetchall()
for i in codigo:
    plac= i[1]
    mod= i[2]
    co= i[3]
    codi= i[5]
print ("<br>")
print ("Codigo:",codi)
print ("<br>")
print ("<br>")
print ("Informa&ccedil;&otilde;es do carro:")
print ("<br>")
print ("Placa - ", plac)
print ("<br>")
print ("Modelo - ", mod)
print ("<br>")
print ("Cor - ", co)
print ("<br>")
print ("<br>")
print ("<form>")
print ("<input style='background-color: SteelBlue; border-color:#191970; color:black' type='button' value='Imprimir' onClick='window.print()'/>")
print ("<input style='background-color: SteelBlue; border-color:#191970; color:black' type='button' value='Voltar a tela inicial' onClick="+"document.location='https://3.82.124.239/telaini.html'>")

print ("</form>")
print ("</p>")
print ("</div>")
print ("</div>")
print ("</body>")
