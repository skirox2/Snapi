# Gestion joueur
player=None
playerx=300

# gestion de cooldown
base=0
baseshoot=0
comparaison=0
comparaisonshoot=0

# gestion du tir
shoot=False
bullety=700
bulletx=0

def sprite(sprite):
    if sprite=="player":
        if var.playerx<=45:
            var.playerx=45
        if var.playerx>=555:
            var.playerx=555
        image(var.player,var.playerx-40,700,80,100)
