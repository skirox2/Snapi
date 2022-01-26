#########################################################################
#########################################################################
###########01010011 01001011 01001001 01010010 01001111 01011000#########
#########################################################################
#########################################################################

############bibli############
add_library('controlP5')
#############################

##########Onglets##########
from menu import *
from boutonp5 import *
from jeux import *
#########Space_invader######
#from controle import *
#from sprites import *
#from space_inavder import sp
###########################
###########################
############Globals########
import globals as gl
###########################

def setup():
    size(gl.x,gl.y)
    gl.cp5 = ControlP5(this)    
    gl.cp5.setBroadcast(False)  
    # desactive temporairement les evenements    
    # Creation des controles a placer ici    
    gl.cp5.setBroadcast(True)  
    # reactive les evenements
    gl.cp5.addButton("PacMan") \
        .setPosition(10, 10) \
        .setSize(200, 19) \
        .addListener(BP1)    
    gl.cp5.addButton("SpaceInvader") \
        .setPosition(10, 30) \
        .setSize(200, 19) \
        .addListener(BP2)
        
def BP1(evt):
    fill(gl.fondesnegro)
    rect (210,100,800,500)
    print("test")
def BP2(evt):
    fill(gl.fondesnegro)
    rect (1050,100,800,500)
    print("test")

def draw():
    pass
