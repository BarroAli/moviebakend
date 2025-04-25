###exercice1 de POO
# %%
class calculator:
    def __init__(self, a, b):
        #vérification des types des deux valeurs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("les deux valeurs doivent être de type int ou float.")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def multiply(self):
        return self.a * self.b
    
    

#vérification des instances 3 et 5
# %%
calc = calculator(3, 5)
print("l'addition :", calc.add())
print("la multiplication :", calc.multiply())
# %%
