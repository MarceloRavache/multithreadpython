

arq1 = open("mt100","r")
arq2 = open("mt100","r")
arq3 = open("mt100rp","w+")

buffer = arq1.readline()
tamanho1 = int(buffer)
buffer = arq2.readline()
tamanho2 = int(buffer)


print tamanho1

matriz1 = []
for i in range(tamanho1):
	matriz1.append([0]*tamanho1)

matriz2 = []
for i in range(tamanho2):
	matriz2.append([0]*tamanho2)


text1 = arq1.readlines()
text2 = arq2.readlines()

t=0

for i in text1:
	aux = i.split(':')
	for j in range(0,tamanho1):
		matriz1[t][j]=float(aux[j])
	t+=1
for i in range(0,tamanho1):
	for j in range(0,tamanho1):
		if matriz1[i][j] != 1.0:
			print("\n matriz[%d][%d] = %f" %(i,j,matriz1[i][j]))


t=0

for i in text2:
	aux = i.split(':')
	for j in range(0,tamanho1):
		matriz2[t][j]=float(aux[j])
	t+=1
for i in range(0,tamanho1):
	for j in range(0,tamanho1):
		if matriz2[i][j] != 1.0:
			print("\n matriz[%d][%d] = %f" %(i,j,matriz2[i][j]))

matriz3 = []
for i in range(tamanho1):
	matriz3.append([0]*tamanho1)

acumulador = 0.0

for i in range(0,tamanho1):
	for j in range(0,tamanho1):
		acumulador = 0.0
		for k in range(0,tamanho1):
			acumulador = acumulador + (matriz1[i][k]*matriz2[k][j])
		matriz3[i][j] = acumulador

arq3.write("%d\n"%tamanho1)

for i in range(0,tamanho1):
	for j in range(1,tamanho1):
		if j<(tamanho1-1):
			arq3.write("%.1f:"%matriz3[i][j])

		else:
			arq3.write("%.1f\n"%matriz3[i][j])
	

arq1.close()
arq2.close()
arq3.close()
