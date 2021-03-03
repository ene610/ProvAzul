#pip install mega.py

from mega import Mega

mega = Mega()

####inserisci email ####
email = ""

#### inserisci password####
password = ""

m = mega.login(email, password)
details = m.get_user()
print(details)

file = m.upload('C:\\Users\\Ene\\PycharmProjects\\Tesi_morelli\\ProvAzul\\scriptDario.txt')
