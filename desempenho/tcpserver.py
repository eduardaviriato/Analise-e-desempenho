import pygame
import time, sys
from pygame.locals import *
pygame.init()
from pygame.locals import *
pygame.init()
import socket
print "Servidor" 
HOST = ''
PORT = 3999

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Escutando a porta..."
s.bind((HOST,PORT))
s.listen(5)
print "Aceitando a conexao..."

tempoAtualMusica = time.time()
tempoinicio = time.time()

musica = 1

while 1:	
	
	if (tempoinicio+1.0) > tempoAtualMusica:
		tempoAtualMusica = time.time()
	else:
		musica += 1
		tempoinicio = time.time()
	
	if musica > 2:		
		musica=1
	
	conn,addr= s.accept()
	print 'endereco ip:', addr

	print "abrindo arquivo..."
	arq=open('music'+ str(musica) +'.mp3','rb')
	
	print "enviando music"+ str(musica)
	print tempoinicio+3.0, tempoinicio, tempoAtualMusica, "music"+str(musica)
	for i in arq:
			conn.send(i)

 
	print "saindo..."
	arq.close()
	conn.close()

		
	
'''
import socket
print "Servidor"
 
HOST = ''
PORT = 3999
 
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Escutando a porta..."
s.bind((HOST,PORT))
s.listen(5)
print "Aceitando a conexao..."
while 1:
		 
	conn,addr= s.accept()
	print 'endereco ip:', addr

	print "abrindo arquivo..."
	arq=open('music.ogg','rb')
	 
	print "enviado  arquivo"
	for i in arq:
		#print i
		conn.send(i)
 
	print "saindo..."
	arq.close()
	conn.close()
'''
