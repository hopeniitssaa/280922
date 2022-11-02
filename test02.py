from datetime import date
iaurt=['iaurt', date(2022,11,2), date(2022,11,9), 26]
smantana=['smantana', date(2022,11,1), date(2022,11,7), 32]
salam=['salam', date(2022,9,17), date(2022,10,11), 105]
paine=['paine', date(2022,11,2), date(2022,11,3), 8]
inghetata=['inghetata', date(2022,7,13), date(2022,12,23), 17]
ciocolata=['ciocolata', date(2022,6,18), date(2023,4,10), 41]
hrisca=['hrisca', date(2021,3,11), date(2022,7,11), 33]
azi=date(2022,11,2)
def termenval(t): 
    return (t[2]-t[1])
print("Termenul de valabilitate este ", termenval(iaurt).days, "zile")
print("Termenul de valabilitate este ", termenval(smantana).days, "zile")
print("Termenul de valabilitate este ", termenval(salam).days, "zile")
print("Termenul de valabilitate este ", termenval(paine).days, "zile")
print("Termenul de valabilitate este ", termenval(inghetata).days, "zile")
print("Termenul de valabilitate este ", termenval(ciocolata).days, "zile")
print("Termenul de valabilitate este ", termenval(hrisca).days, "zile")

pex=[]
red=[]
if azi>date(iaurt[2]):
    pex.append(iaurt[0])
if azi>date(smantana[2]):
    pex.append(smantana[0])
if azi>date(salam[2]):
    pex.append(salam[0])
if azi>date(paine[2]):
    pex.append(paine[0])
if azi>date(ciocolata[2]):
    pex.append(ciocolata[0])
if azi>date(hrisca[2]):
    pex.append(hrisca[0])
print("Lisa produselor expirate:",pex,"cu pretul 0 lei")

if (date(iaurt[2])-azi)<(0,25*termenval(iaurt).days):
    red.append(iaurt[0])
if (date(smantana[2])-azi)<(0,25*termenval(smantana).days):
    red.append(smantana[0])
if (date(salam[2])-azi)<(0,25*termenval(salam).days):
    red.append(salam[0])
if (date(paine[2])-azi)<(0,25*termenval(paine).days):
    red.append(paine[0])
if (date(inghetata[2])-azi)<(0,5*termenval(inghetata).days):
    red.append(inghetata[0])
if (date(ciocolata[2])-azi)<(0,25*termenval(ciocolata).days):
    red.append(ciocolata[0])
if (date(hrisca[2])-azi)<(0,25*termenval(hrisca).days):
    red.append(hrisca[0])
print('Prodse cu 50% reducere ',red) 

