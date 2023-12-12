# domasna zadaca 1

# domasna zadaca 2

# domasna zadaca 2+ : Da se isprintaat site atributi za zadaden objekt od employee_list.


# zadaca 1
# Da se napravat 2 instanci od klasata Company i 3 instanci od klasata Employee.

class Company:
    def __init__(
            self,
            name:str,
            adress:str
    ):
        self.name = name
        self.adress = adress

class Employee:
    def __init__(
            self,
            name:str,
            surname:str,
            phone:int
    ):
        self.name = name
        self.surname = surname
        self.phone = phone
        

# zadaca 2
# Da se napravi sporedba za prosecnite salary costs za sekoja kompanija.

# zadaca 3
# Da se napise metod days_off so koj employee ke ima pravo da bara denovi odmor.
# Pritoa imame annual leave, special circumstances leave, maternity leave, sick days leave.



# zadaca 4
# Da se napise metod promotion so koj employee ke moze da bide unapreden.

# zadaca 5
# Da se napravi klasa Produkt.
# Da se dodadat zadolzitelni atriibuti pri kreiranje na instanca od Produkt: naziv, seriski_broj, cena, tip
# i opcionalen atribut kolicina.

# zadaca 6
# Da se napravi klasa Prodavnica.
# Instancata od prodavnicata, mora da ima: ime, seriski_broj.
# Da se kreira metod dodaj_produkt, koj kje dodava produkti vo prodavnicata,
# so toa sto mora da se proveri dali e od tip Produkt.

# zadaca 7
# Da se kreira klasa Kupuvac.
# Sekoj Kupuvac mora da ima: ime, prezime, dostapni_paricni_sredstva.

# zadaca 8
# Da se kreiraat __str__ metodi za klasite.
# Da se kreira metod pecati_produkti na klasata Prodavnica koj sto kje gi printa site dostapni produkti.

# zadaca 9
#  Da se kreiraat 5 produkti.
# Da se kreiraat 2 prodavnici.
# Da se dodadat produkti vo prodavnicite.
# Da se kreiraat kupuvaci.
# Da se napravi scenario, kupuvacot da kupi produkt od prodavnica. Vo slucaj ako go nema produktot,
# da proba da go kupi produktot od drugata prodavnica.
# Pri kupuvanje na produkt od prodavnica, treba da se izbrise istoit od listata na produkti. Za ova da se koristi
# privaten metod __brisi_produkt.
# Da se vnimava na dostapnite sredstva na kupuvacot.
