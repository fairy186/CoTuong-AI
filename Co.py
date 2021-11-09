import pygame
import random
pygame.init()
pygame.display.set_caption('Cờ tướng')
BLACK = (10,10,10)
WHITE = (200,200,200)
RED = (255,0,0)
BLUE = (0,0,255)
running = True
vien=50
o=100
X=o*11 + vien*3
Y=o*9 + vien*2
screen = pygame.display.set_mode((X,Y))
chessX = [0,1,2,3,4,5,6,7,8]
chessY = [0,1,2,3,4,5,6,7,8,9]
chess = []
D_Tuong = pygame.image.load('Co/D_Tuong.png')
D_Si = pygame.image.load('Co/D_Si.png')
D_Bo = pygame.image.load('Co/D_Bo.png')
D_Xe = pygame.image.load('Co/D_Xe.png')
D_Phao = pygame.image.load('Co/D_Phao.png')
D_Ngua = pygame.image.load('Co/D_Ngua.png')
D_Chot = pygame.image.load('Co/D_Chot.png')
X_Tuong = pygame.image.load('Co/X_Tuong.png')
X_Si = pygame.image.load('Co/X_Si.png')
X_Bo = pygame.image.load('Co/X_Bo.png')
X_Xe = pygame.image.load('Co/X_Xe.png')
X_Phao = pygame.image.load('Co/X_Phao.png')
X_Ngua = pygame.image.load('Co/X_Ngua.png')
X_Chot = pygame.image.load('Co/X_Chot.png')
status_Chon = False
vt_CoTheDi=[]
vt_CoTheAn=[]
vtCo_D = [[D_Tuong,[4,0]], [D_Si,[3,0],[5,0]], [D_Bo,[2,0],[6,0]], [D_Xe,[0,0],[8,0]], [D_Phao,[1,2],[7,2]], [D_Ngua,[1,0],[7,0]], [D_Chot,[0,3],[2,3],[4,3],[6,3],[8,3]]]
vtCo_X = [[X_Tuong,[4,9]], [X_Si,[3,9],[5,9]], [X_Bo,[2,9],[6,9]], [X_Xe,[0,9],[8,9]], [X_Phao,[1,7],[7,7]], [X_Ngua,[1,9],[7,9]], [X_Chot,[0,6],[2,6],[4,6],[6,6],[8,6]]]
	
#  khởi tạo bàn cờ
def F_KhoiTaoBanCo():
	global chess
	chess=[]
	for y in chessY:
		for x in chessX:
			chess.append([x,y,'',0])
	for x in vtCo_D:
		for y in x[1:]:
			chess[y[0]+y[1]*9] = [y[0],y[1],x[0],0]
	for x in vtCo_X:
		for y in x[1:]:
			chess[y[0]+y[1]*9] = [y[0],y[1],x[0],0]
# Debug
def check():
	chessDebug = chess.copy()
	for x in chessDebug:
		if(x[2]==D_Tuong):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Tuong',0]
		if(x[2]==D_Si):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Si',0]
		if(x[2]==D_Bo):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Bo',0]
		if(x[2]==D_Xe):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Xe',0]
		if(x[2]==D_Phao):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Phao',0]
		if(x[2]==D_Ngua):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Ngua',0]
		if(x[2]==D_Chot):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'D_Chot',0]
		if(x[2]==X_Tuong):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Tuong',0]
		if(x[2]==X_Si):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Si',0]
		if(x[2]==X_Bo):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Bo',0]
		if(x[2]==X_Xe):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Xe',0]
		if(x[2]==X_Phao):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Phao',0]
		if(x[2]==X_Ngua):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Ngua',0]
		if(x[2]==X_Chot):
			chessDebug[x[0]+x[1]*9] = [x[0],x[1],'X_Chot',0]
	for x in chessDebug:
		print(chessDebug.index(x),x[0],x[1],x[2])



#vẽ text
def drawText(x,y,t,c,s):
	s = round(s)
	font = pygame.font.Font('FreeSansBold.ttf', s)
	text = font.render(t, True, c)
	screen.blit(text,(x,y))

#Vị trí có thể đi

def kiemtra_Phe(quanco,phe):
	for x in phe:
		if(quanco==x[0]):
			return True
	return False
def kiemtra_co(x,y):
	try:
		if(chess[x+y*9][2]!=''):
			return True
		else:
			return False
	except:
		return False

def F_NuocDiHopLe(x,y):
	for i in vt_CoTheDi:
		if(x==i[0] and y==i[1]):
			return True
	return False

def cothedi(x,y,z,chess):
	vt_CoTheAn = []
	vt_CoTheDi = []
	if(kiemtra_Phe(z,vtCo_X)==True):
		ds_Co=vtCo_X
		phe=0
	else:
		phe=1
		ds_Co=vtCo_D
	#tướng
	if(z==ds_Co[0][0]):
		vt_CoTheDi.append([x+1,y])
		vt_CoTheDi.append([x,y+1])
		vt_CoTheDi.append([x-1,y])
		vt_CoTheDi.append([x,y-1])
		for i in vt_CoTheDi.copy():
			if(phe == 0):
				if( i[0]<3 or i[0]>5  or i[1]>9 or i[1]<7):
					vt_CoTheDi.remove(i)
			else:
				if( i[0]<3 or i[0]>5  or i[1]>2 or i[1]<0):
					vt_CoTheDi.remove(i)
		can = 0
		if phe == 0:
			for i in range(y-1,-1,-1):
				if chess[x+i*9][2]==D_Tuong:
					if can == 0:
						vt_CoTheDi.append([x,i])
					break
				if chess[x+i*9][2]!='':
					can = 1
		else:
			for i in range(y+1,10):
				if chess[x+i*9][2]==X_Tuong:
					if can == 0:
						vt_CoTheDi.append([x,i])
					break
				if chess[x+i*9][2]!='':
					can = 1
	#sĩ
	if(z==ds_Co[1][0]):
		vt_CoTheDi.append([x+1,y+1])
		vt_CoTheDi.append([x-1,y+1])
		vt_CoTheDi.append([x-1,y-1])
		vt_CoTheDi.append([x+1,y-1])
		if(phe==0):
			for i in vt_CoTheDi.copy():
				if( i[0]<3 or i[0]>5  or i[1]>9 or i[1]<7):
					vt_CoTheDi.remove(i)
		else:
			for i in vt_CoTheDi.copy():
				if( i[0]<3 or i[0]>5  or i[1]>2 or i[1]<0):
					vt_CoTheDi.remove(i)
	#bồ
	if(z==ds_Co[2][0]):
		if(kiemtra_co(x+1,y+1)!=True):
			vt_CoTheDi.append([x+2,y+2])
		if(kiemtra_co(x-1,y+1)!=True):
			vt_CoTheDi.append([x-2,y+2])
		if(kiemtra_co(x-1,y-1)!=True):
			vt_CoTheDi.append([x-2,y-2])
		if(kiemtra_co(x+1,y-1)!=True):
			vt_CoTheDi.append([x+2,y-2])
		if(phe==0):
			for i in vt_CoTheDi.copy():
				if(i[1]<4 or i[1]>9 or i[0]<0 or i[0]>8):
					vt_CoTheDi.remove(i)
		else:
			for i in vt_CoTheDi.copy():
				if(i[1]>5 or i[1]<0 or i[0]<0 or i[0]>8):
					vt_CoTheDi.remove(i)
	#xe
	if(z==ds_Co[3][0]):
		for i in range(x+1,9):
			if(i>8):
				break
			vt_CoTheDi.append([i,y])
			if(chess[i+y*9][2]!=''):
				break
		for i in range(x-1,-1,-1):
			if(i<0):
				break
			vt_CoTheDi.append([i,y])
			if(chess[i+y*9][2]!=''):
				break
		for i in range(y+1,10):
			if(i>9):
				break
			vt_CoTheDi.append([x,i])
			if(chess[x+i*9][2]!=''):
				break
		for i in range(y-1,-1,-1):
			if(i<0):
				break
			vt_CoTheDi.append([x,i])
			if(chess[x+i*9][2]!=''):
				break
	
	#ngựa
	if(z==ds_Co[5][0]):
		if(kiemtra_co(x+1,y)!=True):
			vt_CoTheDi.append([x+2,y+1])
			vt_CoTheDi.append([x+2,y-1])
		if(kiemtra_co(x-1,y)!=True):
			vt_CoTheDi.append([x-2,y+1])
			vt_CoTheDi.append([x-2,y-1])
		if(kiemtra_co(x,y+1)!=True):
			vt_CoTheDi.append([x+1,y+2])
			vt_CoTheDi.append([x-1,y+2])
		if(kiemtra_co(x,y-1)!=True):
			vt_CoTheDi.append([x+1,y-2])
			vt_CoTheDi.append([x-1,y-2])
		for i in vt_CoTheDi.copy():
			if( i[0]<0 or i[0]>8  or i[1]>9 or i[1]<0):
				vt_CoTheDi.remove(i)
	#chốt
	elif(z == ds_Co[6][0]):
		if(phe==0):
			if(y<5):
				if x-1>0:
					vt_CoTheDi.append([x-1,y])
				if x+1<9:
					vt_CoTheDi.append([x+1,y])
			if(y-1>=0):
				vt_CoTheDi.append([x,y-1])
		else:
			if(y>4):
				if x-1>0:
					vt_CoTheDi.append([x-1,y])
				if x+1<9:
					vt_CoTheDi.append([x+1,y])
			if(y+1<=9):
				vt_CoTheDi.append([x,y+1])
	#
	vt_CoTheAn.extend(vt_CoTheDi)
	#pháo
	if(z==ds_Co[4][0]):
		x1=0
		for i in range(x+1,9):
			if(i>8):
				break
			if(chess[i+y*9][2]!=''):
				x1=x1+1
				if(x1==2):
					vt_CoTheAn.append([i,y])
					vt_CoTheDi.append([i,y])
					break
			elif(x1==0):
				vt_CoTheDi.append([i,y])
			elif(x1==1):
				vt_CoTheAn.append([i,y])
		x1=0
		for i in range(x-1,-1,-1):
			if(i<0):
				break
			if(chess[i+y*9][2]!=''):
				x1=x1+1
				if(x1==2):
					vt_CoTheAn.append([i,y])
					vt_CoTheDi.append([i,y])
					break
			elif(x1==0):
				vt_CoTheDi.append([i,y])
			elif(x1==1):
				vt_CoTheAn.append([i,y])
		x1=0
		for i in range(y+1,10):
			if(i>9):
				break
			if(chess[x+i*9][2]!=''):
				x1=x1+1
				if(x1==2):
					vt_CoTheAn.append([x,i])
					vt_CoTheDi.append([x,i])
					break
			elif(x1==0):
				vt_CoTheDi.append([x,i])
			elif(x1==1):
				vt_CoTheAn.append([x,i])
		x1=0
		for i in range(y-1,-1,-1):
			if(i<0):
				break
			if(chess[x+i*9][2]!=''):
				x1=x1+1
				if(x1==2):
					vt_CoTheAn.append([x,i])
					vt_CoTheDi.append([x,i])
					break
			elif(x1==0):
				vt_CoTheDi.append([x,i])
			elif(x1==1):
				vt_CoTheAn.append([x,i])
	
	#lọc nước đi
	
	if(kiemtra_Phe(z,vtCo_X)==True):
		for i in vt_CoTheDi.copy():
			if(kiemtra_Phe(chess[i[0]+i[1]*9][2],vtCo_X)==True):
				vt_CoTheDi.remove(i)
	else:
		for i in vt_CoTheDi.copy():
			if(kiemtra_Phe(chess[i[0]+i[1]*9][2],vtCo_X)==False and chess[i[0]+i[1]*9][2]!=''):
				vt_CoTheDi.remove(i)
	return [vt_CoTheDi, vt_CoTheAn]


# game
ds_giatri_co=[[D_Tuong,100],[D_Si,2],[D_Bo,2],[D_Xe,10],[D_Phao,7],[D_Ngua,3],[D_Chot,1],[X_Tuong,100],[X_Si,2],[X_Bo,2],[X_Xe,10],[X_Phao,7],[X_Ngua,3],[X_Chot,1]]
def F_CoNgoaiSan():
	cobian_D=[2,2,2,2,2,5]
	cobian_X=[2,2,2,2,2,5]
	for i in chess.copy():
		for j in range(6):
			if(i[2]==vtCo_X[j+1][0]):
				cobian_X[j]=cobian_X[j]-1
			if(i[2]==vtCo_D[j+1][0]):
				cobian_D[j]=cobian_D[j]-1
	vt_D_n=[]
	vt_X_n=[]
	for x in range(1,6):
		for y in range(1,3):
			vt_X_n.append([vien*2+o*8.1+(x-1)*o/2+((o*2.8-35*5)/6 if o*2.8-35*6>=0 else 3), vien+o*3+(y-1)*o*3/4+((o*2.5-35*3)/4 if o*2.5-35*3>=0 else 0), ''])
			vt_D_n.append([vien*2+o*8.1+(x-1)*o/2+((o*2.8-35*5)/6 if o*2.8-35*6>=0 else 3), vien+o*6+(y-1)*o*3/4+((o*2.5-35*3)/4 if o*2.5-35*3>=0 else 0), ''])
	for x in range(1,6):
			vt_X_n.append([vien*2+o*8.1+(x-1)*o/2+((o*2.8-35*5)/6 if o*2.8-35*6>=0 else 3), vien+o*3+(3-1)*o*3/4+((o*2.5-35*3)/4 if o*2.5-35*3>=0 else 0), ''])
			vt_D_n.append([vien*2+o*8.1+(x-1)*o/2+((o*2.8-35*5)/6 if o*2.8-35*6>=0 else 3), vien+o*6+(3-1)*o*3/4+((o*2.5-35*3)/4 if o*2.5-35*3>=0 else 0), ''])
	# vẽ cờ ngoài sân
	for x in range(15):
		#xanh
		if(x<=1 and x<cobian_X[0]):
			vt_X_n[x][2]=X_Si
		if(x>1 and x<=3 and x<cobian_X[1]+2):
			vt_X_n[x][2]=X_Bo
		if(x>3 and x<=5 and x<cobian_X[2]+4):
			vt_X_n[x][2]=X_Xe
		if(x>5 and x<=7 and x<cobian_X[3]+6):
			vt_X_n[x][2]=X_Phao
		if(x>7 and x<=9 and x<cobian_X[4]+8):
			vt_X_n[x][2]=X_Ngua
		if(x>9 and x<=14 and x<cobian_X[5]+10):
			vt_X_n[x][2]=X_Chot
		# đỏ
		if(x<=1 and x<cobian_D[0]):
			vt_D_n[x][2]=D_Si
		if(x>1 and x<=3 and x<cobian_D[1]+2):
			vt_D_n[x][2]=D_Bo
		if(x>3 and x<=5 and x<cobian_D[2]+4):
			vt_D_n[x][2]=D_Xe
		if(x>5 and x<=7 and x<cobian_D[3]+6):
			vt_D_n[x][2]=D_Phao
		if(x>7 and x<=9 and x<cobian_D[4]+8):
			vt_D_n[x][2]=D_Ngua
		if(x>9 and x<cobian_D[5]+10):
			vt_D_n[x][2]=D_Chot
	for x in range(15):
		if(vt_X_n[x][2]!=''):
			i=vt_X_n[x]
			screen.blit(i[2], (i[0], i[1]))
		if(vt_D_n[x][2]!=''):
			i=vt_D_n[x]
			screen.blit(i[2], (i[0], i[1]))
def F_BanCo():
	
	# vẽ cấm cung
	pygame.draw.rect(screen, (50,50,50), (vien+1+o*3, vien+1, o*2-1, o*2-1))
	pygame.draw.rect(screen, (50,50,50), (vien+1+o*3, vien+1+o*7, o*2-1, o*2-1))
	pygame.draw.line(screen, WHITE, (vien+o*3,vien+o*0), (vien+o*5,vien+o*2),2)
	pygame.draw.line(screen, WHITE, (vien+o*3,vien+o*2), (vien+o*5,vien+o*0),2)
	pygame.draw.line(screen, WHITE, (vien+o*3,vien+o*9), (vien+o*5,vien+o*7),2)
	pygame.draw.line(screen, WHITE, (vien+o*3,vien+o*7), (vien+o*5,vien+o*9),2)
	for x in range(10):
		#đường dọc
		if(x!=9):
			pygame.draw.line(screen, WHITE, (vien+o*x,vien+0), (vien+o*x,vien+o*9))
			drawText(vien+o*x-10,0-10,str(x),BLUE, 40)
		#đường ngang
		drawText(0+10,vien+o*x-30,str(x),BLUE, 40)
		pygame.draw.line(screen, WHITE, (vien+0,vien+o*x), (vien+o*8,vien+o*x))

	# vẽ menu
	pygame.draw.rect(screen, (0,255,0), (vien*2+o*8, vien, o*3, o*9) ,1)
	pygame.draw.rect(screen, (0,0,255), (vien*2+o*8.1, vien+o*3, o*2.8, o*2.5) ,1)
	pygame.draw.rect(screen, (255,0,0), (vien*2+o*8.1, vien+o*6, o*2.8, o*2.5) ,1)
	pygame.draw.rect(screen, (0,255,0), (vien*2+o*8.5, vien+o*1, o*2, o*1) ,1)
	
	# hover: button
	if(mouse_x>=vien*2+o*8.5 and mouse_x<=vien*2+o*10.5 and mouse_y>=vien+o*1 and mouse_y<=vien+o*2):
		pygame.draw.rect(screen, (0,255,0), (vien*2+o*8.5, vien+o*1, o*2, o*1))
	if win == 3:
		drawText(vien*2+o*8.5+o/4, vien+o*1+o/4,t,BLUE,o/2.5)
	else:
		drawText(vien*2+o*8.5+o/4, vien+o*1+o/4,t,BLUE,o/2.5)
	if tg!=-100:
		drawText(vien*2+o*9.5-o/5, vien+o*2.2, str(round(tg/60)), BLUE, o/2.5)
	# vẽ sông
	pygame.draw.rect(screen, (0,150,255), (vien+1, vien+o*4+1, o*8-1, o-1))
def F_GiaTriQuanCo(x):
	for i in ds_giatri_co:
		if x==i[0]:
			return i[1]
	return 0
def F_n(xm,ym,z):
	na=[]
	for i in chess.copy():
		if i[2]!='' and kiemtra_Phe(i[2],phe_NguoiChoi)==True:
			if [xm,ym] in cothedi(i[0],i[1],i[2],chess)[1]:
				return F_GiaTriQuanCo(z)
	return 0
def F_DuDoanNuocDi(chess):
	max_e = -100000
	for i in chess.copy():
		if(kiemtra_Phe(i[2],phe_NguoiChoi)==True):
			nd = cothedi(i[0],i[1],i[2],chess)[0]
			for j in nd:
				m=0
				n=0
				vtc=i[0]+i[1]*9
				vt=j[0]+j[1]*9
				m = m + F_GiaTriQuanCo(chess[vt][2])
				n = n + F_n(j[0],j[1],i[2])
				e = m-n
				if e > max_e:
					max_e=e
	return max_e

def F_NuocDiTotNhat(x,y,z,do_sau):
	nd = cothedi(x,y,z,chess)[0]
	m_e = [-100000]
	if nd ==[]:
		return 0
	for j in nd:
		m=0
		n=0
		vt=j[0]+j[1]*9
		m = m + F_GiaTriQuanCo(chess[vt][2])
		n = n + F_n(j[0],j[1],z)
		e=m-n
		if m_e[0]!=-1000000 and e<m_e[0]-2:
			continue
		if e > m_e[0]:
			m_e=[e,x,y,j[0],j[1]]
	if(do_sau!=0):
		return m_e[0] + F_NuocDiTotNhat(m_e[3],m_e[4],z,do_sau-1)/100
	else:
		return m_e[0]
win = 3
def F_CheckWin():
	global win
	win = 0
	for i in chess:
		if(i[2]==X_Tuong):
			win = win +1
		if(i[2]==D_Tuong):
			win = win + 2
t = 'Bắt đầu'
phe_NguoiChoi = vtCo_X
tg = -100
while running:
	screen.fill(BLACK)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	F_BanCo()
	F_CoNgoaiSan()
	#Cập nhật trạng thái
	vt_CoTheAn=[]
	for x in chess:
		# vẽ lựa chọn
		if(x[3]!=0):
			pygame.draw.circle(screen, BLUE, (x[0]*o+vien, x[1]*o+vien), 28, 1)
			pygame.draw.circle(screen, WHITE, (x[0]*o+vien, x[1]*o+vien), 27, 1)
			pygame.draw.circle(screen, BLUE, (x[0]*o+vien, x[1]*o+vien), 26, 1)
			pygame.draw.circle(screen, WHITE, (x[0]*o+vien, x[1]*o+vien), 25, 1)
			pygame.draw.circle(screen, BLUE, (x[0]*o+vien, x[1]*o+vien), 24, 1)
		# vẽ cờ
		if(x[2]!=''):
			if kiemtra_Phe(x[2],vtCo_X):
				vt_CoTheAn.extend(cothedi(x[0],x[1],x[2],chess)[1])
			screen.blit(x[2], (x[0]*o+vien-21, x[1]*o+vien-21))
		#
	# vẽ các vị trí có thể đi khi 1 quân cờ được chọn
	for x in vt_CoTheDi:
		pygame.draw.circle(screen, (255,0,0), (x[0]*o+vien, x[1]*o+vien), 10)
	# for x in vt_CoTheAn:
	# 	pygame.draw.circle(screen, (0,255,0), (x[0]*o+vien, x[1]*o+vien), 21,3)
	# Các sự kiện
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mx=round((mouse_x-vien)/o)
				my=round((mouse_y-vien)/o)
				if(mouse_x>=vien*2+o*8.5 and mouse_x<=vien*2+o*10.5 and mouse_y>=vien+o*1 and mouse_y<=vien+o*2):
					F_KhoiTaoBanCo()
					tg=120*60
					win = 3
					t = 'Chơi lại'
					break
				vt=mx+my*9
				if (mx<=8 and my<=9 and t== 'Chơi lại'):
					if(win==3):
						if(status_Chon==False):
							if (chess[vt][2]!='' and kiemtra_Phe(chess[vt][2],phe_NguoiChoi)):
								chess[vt][3]=1
								status_Chon=True
								vt_CoTheDi=cothedi(chess[vt][0],chess[vt][1],chess[vt][2],chess)[0]
								luachon_cu = vt
						else:
								# Người chơi
							if(F_NuocDiHopLe(mx,my)):
								chess[vt][2]=chess[luachon_cu][2]
								chess[luachon_cu][2]=''
								chess[luachon_cu][3]=0
								F_CheckWin()
								if win != 3:
									break
								#AI
								max_e = [-100000]
								for i in chess.copy():
									if kiemtra_Phe(i[2],phe_NguoiChoi)==False and i[2]!='':
										nd = cothedi(i[0],i[1],i[2],chess)[0]
										for j in nd:
											# print(i[0],i[1],j[0],j[1])
											m=0
											n=0
											vtc=i[0]+i[1]*9
											vt=j[0]+j[1]*9
											chess1 = []
											for k in range(len(chess.copy())):
												chess1.append(chess[k].copy())
											chess1[vtc][2]=''
											chess1[vt][2]=i[2]
											m = m + F_GiaTriQuanCo(chess[vt][2])
											if m ==100:
												m=m+1000000
											n = n + F_n(j[0],j[1],i[2])
											# print(m,n)
											m1 = F_DuDoanNuocDi(chess)
											m2 = F_DuDoanNuocDi(chess1)
											# print(m1,m2)
											m = m + (m1-m2)
											e = m-n + F_NuocDiTotNhat(j[0],j[1],i[2],3)/100
											if max_e[0]!=-1000000 and e<max_e[0]-2:
												continue
											# print(m,n,e)
											# print("-------------")
											if e > max_e[0]:
												max_e=[e,i[0],i[1],j[0],j[1]]
								print(max_e)
								# check()
								vt1=max_e[1]+max_e[2]*9
								vt2=max_e[3]+max_e[4]*9
								chess[vt2][2]=chess[vt1][2]
								chess[vt1][2]=''
								#
								F_CheckWin()
								tg = 120*60
							else:
								chess[luachon_cu][3]=0
							vt_CoTheDi =[]
							del luachon_cu
							status_Chon = False
							vt_CoTheDi = []
	if tg>0:
		tg=tg-1
	if round(tg/60)==0:
		win =2
	if(win == 1):
		pygame.draw.rect(screen, (50,50,50), (vien+o*2.5, vien+o*3.75, o*3, o*1.5))
		pygame.draw.rect(screen, (0,255,0), (vien+o*2.5, vien+o*3.75, o*3, o*1.5),2)
		drawText(vien+o*3.4,vien+o*4.2,'Thắng', BlUE, o/2.5)
	if(win == 2):
		pygame.draw.rect(screen, (50,50,50), (vien+o*2.5, vien+o*3.75, o*3, o*1.5))
		pygame.draw.rect(screen, (0,255,0), (vien+o*2.5, vien+o*3.75, o*3, o*1.5),2)
		drawText(vien+o*3.5,vien+o*4.2,'Thua', BLUE, o/2.5)
	pygame.display.flip()
pygame.quit()