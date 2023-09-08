personas = int(input('Kāds ir pasažieru skaits?')) #Var ievadīt adbildi "personas" (Tikai vesala skaitļa formā)
if personas <= 0: #Ja atbilde "personas" ir < 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties
elif personas > 4: #Ja atbilde "personas" ir > 4 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Nevar būt vairāk kā 4 pasažieri!')
  exit() #programma pārstāj darboties
elif personas <= 4:  #Ja atbilde "personas" ir <= 4 tad programa izdarīs nosacijumus zem šis funkcijas
  laiks = int(input('Kāds ir pūlksteņa laiks?')) #Var ievadīt adbildi "laiks" (Tikai vesala skaitļa formā)
if laiks > 24 or laiks < 0:  #Ja atbilde "laiks" ir > 24 VAI < 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties
elif laiks <= 6 or laiks >= 22: #Ja atbilde "laiks" ir <= 6 VAI >= 22 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Nakts trafiks.')
  cena = 0.67 # "cena" iedevu vērtību 0.67
  noligsana = input('Vai ir taksis stāvietā?(Jā/Nē)') #Var ievadīt adbildi "noligsana"
elif laiks > 6 or laiks < 22:  #Ja atbilde "laiks" ir > 6 VAI < 22 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Dienas trafiks.')
  cena = 0.57 # "cena" iedevu vērtību 0.57
  noligsana = input('Vai ir taksis stāvietā?(Jā/Nē)') #Var ievadīt adbildi "noligsana"
if noligsana == 'Jā':  #Ja atbilde "noligsana" ir "Jā" tad programa izdarīs nosacijumus zem šis funkcijas
  print('Jāmaksā tikai nolīgšanas maksa.')
  maksa = 1.25 # "maksa" iedevu vērtību 1.25
  gaida = int(input('Vai jāgaida?(min)')) #Var ievadīt adbildi "gaida" (Tikai vesala skaitļa formā)
elif noligsana == 'Nē':  #Ja atbilde "noligsana" ir "Nē" tad programa izdarīs nosacijumus zem šis funkcijas
  print('Jāmaksā nolīgšanas maksa un izsaukuma maksa.')
  maksa = 3.45 # "maksa" iedevu vērtību 3.45
  gaida = int(input('Vai jāgaida?(min)')) #Var ievadīt adbildi "gaida" (Tikai vesala skaitļa formā)
else:  #Ja atbildē "noligsana" adbildēs jebko citu tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties
if gaida < 0:  #Ja atbilde "gaida" ir < 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties
elif gaida >= 0:  #Ja atbilde "gaida" ir >= 0 tad programa izdarīs nosacijumus zem šis funkcijas
  gaidcena = round(gaida * 0.13, 2) # "gaida" vērtību sareizinu ar 0.13 un izmantoju round funkciju lai noapaļoju līdz diviem cipariem aiz komata
  km = int(input('Cik tālu jābrauc?(km)')) #Var ievadīt adbildi "km" (Tikai vesala skaitļa formā)
if km <= 0:  #Ja atbilde "km" ir <= 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties
elif km > 0:  #Ja atbilde "km" ir > 0 tad programa izdarīs nosacijumus zem šis funkcijas
  kmcena = round(km * cena, 2) # "km" vērtību sareizinu ar "cena" vērtību un izmantoju round funkciju lai noapaļoju līdz diviem cipariem aiz komata
  tip = input('Vai gribi iedot dzeramnaudu?(Jā/Nē)')  #Var ievadīt adbildi "tip"
if tip == 'Jā':  #Ja atbilde "tip" ir "Jā" tad programa izdarīs nosacijumus zem šis funkcijas
  tippay = float(input('Cik gribi piemaksāt?(0.00)')) #Var ievadīt adbildi "tippay" (vesala skaitļa formā vai ar komatiem)
elif tip == 'Nē':  #Ja atbilde "tip" ir "Nē" tad programa izdarīs nosacijumus zem šis funkcijas
  print('\n','\nČeks:','\nNolīgšana: ', maksa,'€', '\nGaidīšana: ', gaidcena,'€', '\nAtālums: ', kmcena,'€',) #izrakstu čeku kur izmantoju \n lai pārvietotu nākošu tekstu līniju zemāk
  print('Kopā: ', round(maksa+gaidcena+kmcena, 2),'€',) #saskaitu vērtības "maksa", "gaidcena" un "kmcena" kopā un izmantojot round funkciju noapaļoju līdz diviem cipariem aiz komata
  exit() #programma pārstāj darboties
if tippay > 0:  #Ja atbilde "tippay" ir > 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('\n','\nČeks:','\nNolīgšana: ', maksa,'€', '\nGaidīšana: ', gaidcena,'€', '\nAtālums: ', kmcena,'€', '\nPiemaksa: ', round(tippay, 2),'€') #izrakstu čeku kur izmantoju \n lai pārvietotu nākošu tekstu līniju zemāk un noapaļoju funkciju "tippay" līdz diviem cipariem aiz komata
  print('Kopā: ', round(maksa+gaidcena+kmcena+tippay, 2),'€',) #saskaitu vērtības "maksa", "gaidcena", "kmcena" un "tippay" kopā un izmantojot round funkciju noapaļoju līdz diviem cipariem aiz komata
  exit() #programma pārstāj darboties
elif tippay < 0:  #Ja atbilde "tippay" ir < 0 tad programa izdarīs nosacijumus zem šis funkcijas
  print('Ievadi pareizus datus!')
  exit() #programma pārstāj darboties