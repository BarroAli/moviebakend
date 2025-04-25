############## class #############


class chien:
    pass

##################### objet(instance) ###
# %%
mon_chien = chien()
type(mon_chien)


########## attributs #############

# %%
class chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race
# %%
mon_chien = chien("Pipo","Labrador")
print(mon_chien.nom)
print(mon_chien.race)


########## méthodes ###############

# %%
class chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

    def aboyer(self):
        print(f"{self.nom} aboie !")
# %%
rex = chien("Rex", "Berger allemand")
print(rex.aboyer())

