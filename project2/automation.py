def importar_texto():
	texto = open("/Users/julianestebanquintana/Desktop/project2/text.txt")
	contenido = texto.readlines()
	texto.close()
	return contenido

#def fragmentar_texto(texto):


documento = importar_texto()
#print type(documento)
file = open("/Users/julianestebanquintana/Desktop/project2/newfile.py", "w")

#file.write(documento)
file.writelines(documento)

file.close()

#for line in documento:
#	print line

#documento = importar_texto()
#lista = fragmentar_texto(documento)
#print lista
