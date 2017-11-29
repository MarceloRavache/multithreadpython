import sys

print (sys.argv[0])
print (sys.argv[0])
print (sys.argv[0])

arq1 = open("mt1","r")
arq2 = open("mt1","r")
arq3 = open("mt1rp","w+")

tamanho1 = int(arq1.readline())

tamanho2 = int(arq2.readline())

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
 
import threading

class minhaThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
	self.tm = tamanho1/2
    def run(self):
	self.incre = self.threadID * self.tm
	self.inicio = 0 + self.incre
	self.fim = self.tm + self.incre
    	for i in range(self.inicio,self.fim):
			for j in range(0,tamanho1):
				acumulador = 0.0
				for k in range(0,tamanho1):
					acumulador = acumulador + (matriz1[i][k]*matriz2[k][j])
				matriz3[i][j] = acumulador
 
threads = []
for i in range(0,2):
	thread1 = minhaThread(i)
 	thread1.start()
	threads.append(thread1)
for t in threads:
    t.join()

arq3.write("%d\n"%tamanho1)

for i in range(0,tamanho1):
	for j in range(1,tamanho1):
		if j<(tamanho1-1):
			arq3.write("%.1f:"%matriz3[i][j])
		else:
			arq3.write("%.1f\n"%matriz3[i][j])

 
print "Saindo da main"

arq1.close()
arq2.close()
arq3.close()
