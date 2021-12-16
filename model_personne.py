import re
import operator


class ModelPersonne:
    def __init__(self, nom: str, prenom: str, ssn: str, cle, valeur_numerique):
        self.nom = nom
        self.prenom = prenom
        self.ssn = ssn
        self.cle = cle
        self.valeur_numerique = valeur_numerique

    def Encapsuler(self):
        print("Bonjour, je m'appelle  " + self.nom + self.prenom + ", mon numéro est:  " + str(self.ssn))

    def verife(self):
        self.cle == (97 - (int(self.valeur_numerique) % 97))
        print(self.cle)

    def has_valide_ssn(self):
        if re.search(
                "^[1-478][0-9]{2}(0[1-9]|1[0-2]|62|63)(2[ABab]|[0-9]{2})(00[1-9]|0[1-9][0-9]|[1-8][0-9]{2}|9[0-8][0-9]|990)(00[1-9]|0[1-9][0-9]|[1-9][0-9]{2})(0[1-9]|[1-8][0-9]|9[0-7])$",
                self.ssn) == None and operator.not_(self.valeur_numerique.verife()):
            return False
        else:
            return True


personne1 = ModelPersonne("Jean", "Marie", "299079933312527","27","2990799333125")
personne1.Encapsuler()
print(personne1.has_valide_ssn())
print(personne1.verife())
