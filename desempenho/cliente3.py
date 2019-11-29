import pygame,time
from pygame.locals import *
pygame.init()
import socket
 
print "Cliente"

print " :) Radio UFC, a sua radio favorita ><"
 
HOST='192.168.1.9' #coloca o host do servidor 
PORT=3999


	 
while True:	 
	if pygame.mixer.music.get_busy() == 0:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
		#print "conectando com servidor..."
		s.connect((HOST,PORT))
		
			
		#print "recebendo Fluxo ..."
		arq = open('musica.mp3','wb')
		
		while True:
		 
			dados=s.recv(1024)
			if not dados:
				#print 'recebido'
				break
			arq.write(dados)

		arq.close()
		pygame.mixer.music.load('musica.mp3')
		pygame.mixer.music.play()
		#pygame.event.wait()
		
		s.close()
print "fim"

