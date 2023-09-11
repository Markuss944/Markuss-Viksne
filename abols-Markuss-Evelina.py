abolumasa, cukuracena, cukura_attieciba, extra, darbiba = float(input("Cik āboli tev ir? (kg) \n")), float(input("Cik ir cukura cena? (Euro/kg) \n")), float(input("Cik kg cukura vajag uz 1 kg ābolu? \n")), {}, 0
daudzums = abolumasa+(cukura_attieciba*abolumasa)
while darbiba != 2: 
    darbiba = int(input('Izvēlieties darbību:\n1 - pievienot sastāvdaļu\n2 - čeks\n'))
    if darbiba == 1: 
        extra[input("vards ")] = float(input("cena (Euro): ")),float(input("papildus sastāvdaļas daudzums (kg): "))
cukura_summa = round(cukuracena,2)*abolumasa*cukura_attieciba
print('\nJūsu čeks:',)
for key,list in extra.items():
    final = round(list[0]*list[1],2)
    print(key,'-',final,'EUR',)
    daudzums = daudzums+list[1]
print('Cukurs -',cukura_summa,'EUR','\nIevāriuma daudzums -',daudzums)
exit()