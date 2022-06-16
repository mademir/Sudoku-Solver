import os
import pygame
from time import sleep

NUM= {pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9}
lc=(150,150,0)#line color
blc=(255,30,30)#hardborder color
nocolor=(0,250,0)#color of the numbers
n,nx=[9,50]

def remove(x,fro):
    for i in x:
        if i in fro:
            fro.remove(i)
    return fro

def flip():
    pygame.display.flip()
    
pygame.init()
pygame.display.set_caption(u'Sudoku Solver (by Backtracking)')
scr=pygame.display.set_mode((n*nx, n*nx))
font = pygame.font.Font('freesansbold.ttf', 32)

scr.fill((0,34,64)) #background

def line(spos,epos,color=False):
    if not color:
        pygame.draw.line(scr,pygame.Color(lc[0],lc[1],lc[2]), spos, epos)
    else:
        pygame.draw.line(scr,pygame.Color(color[0],color[1],color[2]), spos, epos)
def draw_board(n=9,nx=50):
    scr.fill((0,34,64))
    for i in range(n):
        line((nx*(i+1),0),(nx*(i+1),n*nx))
        line((0,nx*(i+1)),(n*nx,nx*(i+1)))
    line((nx*3,0),(nx*3,nx*n),blc)
    line((nx*6,0),(nx*6,nx*n),blc)
    line((0,nx*3),(nx*n,nx*3),blc)
    line((0,nx*6),(nx*n,nx*6),blc)

def flipb():
    draw_board()
    y,z=0,0
    for m in b:
        for n in m:
            if b[y][z]==0:
                rsc=""
            else:
                rsc=str(b[y][z])
            scr.blit(font.render(rsc, True,nocolor),((nx*z)+16,(nx*y)+13))########################################################################
            z+=1
        z=0
        y+=1
    drawOrg()
    flip()

b =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]

ORG_B=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]
]

def refresh():
    global SLOT
    SLOT=[b[0],
    b[1],
    b[2],
    b[3],
    b[4],
    b[5],
    b[6],
    b[7],
    b[8],#row
    [b[0][0],b[1][0],b[2][0],b[3][0],b[4][0],b[5][0],b[6][0],b[7][0],b[8][0]],
    [b[0][1],b[1][1],b[2][1],b[3][1],b[4][1],b[5][1],b[6][1],b[7][1],b[8][1]],
    [b[0][2],b[1][2],b[2][2],b[3][2],b[4][2],b[5][2],b[6][2],b[7][2],b[8][2]],
    [b[0][3],b[1][3],b[2][3],b[3][3],b[4][3],b[5][3],b[6][3],b[7][3],b[8][3]],
    [b[0][4],b[1][4],b[2][4],b[3][4],b[4][4],b[5][4],b[6][4],b[7][4],b[8][4]],
    [b[0][5],b[1][5],b[2][5],b[3][5],b[4][5],b[5][5],b[6][5],b[7][5],b[8][5]],
    [b[0][6],b[1][6],b[2][6],b[3][6],b[4][6],b[5][6],b[6][6],b[7][6],b[8][6]],
    [b[0][7],b[1][7],b[2][7],b[3][7],b[4][7],b[5][7],b[6][7],b[7][7],b[8][7]],
    [b[0][8],b[1][8],b[2][8],b[3][8],b[4][8],b[5][8],b[6][8],b[7][8],b[8][8]],#column
    [b[0][0],b[0][1],b[0][2],b[1][0],b[1][1],b[1][2],b[2][0],b[2][1],b[2][2]],
    [b[3][0],b[3][1],b[3][2],b[4][0],b[4][1],b[4][2],b[5][0],b[5][1],b[5][2]],
    [b[6][0],b[6][1],b[6][2],b[7][0],b[7][1],b[7][2],b[8][0],b[8][1],b[8][2]],
    [b[0][3],b[0][4],b[0][5],b[1][3],b[1][4],b[1][5],b[2][3],b[2][4],b[2][5]],
    [b[3][3],b[3][4],b[3][5],b[4][3],b[4][4],b[4][5],b[5][3],b[5][4],b[5][5]],
    [b[6][3],b[6][4],b[6][5],b[7][3],b[7][4],b[7][5],b[8][3],b[8][4],b[8][5]],
    [b[0][6],b[0][7],b[0][8],b[1][6],b[1][7],b[1][8],b[2][6],b[2][7],b[2][8]],
    [b[3][6],b[3][7],b[3][8],b[4][6],b[4][7],b[4][8],b[5][6],b[5][7],b[5][8]],
    [b[6][6],b[6][7],b[6][8],b[7][6],b[7][7],b[7][8],b[8][6],b[8][7],b[8][8]]]#box
refresh()

class tile:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.inslots=[self.x,9+self.y,18+3*(self.y//3)+self.x//3]
        self.tried=[]

    def findopts(self):
        allop=list(range(1,10))
        for i in range(1,10):
            for k in [SLOT[self.x],SLOT[9+self.y],SLOT[18+3*(self.y//3)+self.x//3]]:
                if i in k:
                    if not (i in allop):continue
                    allop.remove(i)
        self.opts=allop
        return allop

tiles=list(range(9))
for i in range(9):tiles[i] = [tile(i,k) for k in range(9)]

def check(x,y):
    for m in tiles[x][y].inslots:
        l=SLOT[m]
        for k in range(1,10):
            if len([index for index, value in enumerate(l) if value == k])>1:
                return False
    return True


def drawOrg():
    y,z=0,0
    for m in b:
        for n in m:
            if ORG_B[y][z]==0:
                rsc=""
            else:
                rsc=str(ORG_B[y][z])
            scr.blit(font.render(rsc, True,(200,100,0)),((nx*z)+16,(nx*y)+13))#########################################################################
            z+=1
        z=0
        y+=1


flipb()
flip()

active=False
last=[]
bx=0
by=0
dnm=0

solved=False

while 1:
    for event in pygame.event.get():
        if bool(active) & (event.type == pygame.KEYDOWN):
##            if event.key in NUM:
##                if event.key < 58:
##                    no=event.key-48
##                else:
##                    no=event.key-(pygame.K_KP1-1)
##                if b[y][x]==0:
##                    b[y][x]=no
##                    refresh()
##                    flipb()
            if event.key==pygame.K_ESCAPE: raise
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            x=x//50
            y=y//50
            active=[x,y]

        if event.type == pygame.QUIT:
            pygame.quit()
            os._exit(1)
    full=True
    for i in range(9):
            if 0 in b[i]:full=False
    if not full:
        if b[bx][by]!=0:#if tile filled, iterate
            by+=1
            if by==9:
                by=0
                bx+=1
        else:#if tile is empty
            if tiles[bx][by].findopts() != []:
                print("tried",tiles[bx][by].tried,"allopts",tiles[bx][by].findopts())
                dnmlist=remove(tiles[bx][by].tried,tiles[bx][by].findopts())
                if dnmlist != []:
                    dnm=dnmlist[0]
                    print("dnm",dnm,"pos",bx,by,"opts",tiles[bx][by].findopts())
                    b[bx][by]=dnm
                    tiles[bx][by].tried.append(b[bx][by])
                    refresh()
                    last.append((bx,by))
                    flipb()
                    if not check(bx,by):#if value makes it false
                        b[bx][by]=0
                        refresh()
                        flipb()
                else:#if no possible options
                    tiles[bx][by].tried.clear()
                    bx,by=list(last[-1])
                    last.pop()
                    b[bx][by]=0
                    refresh()
                    flipb()
            else:#if no possible options
                bx,by=list(last[-1])
                last.pop()
                b[bx][by]=0
                refresh()
                flipb()
