def perimetro():
print("il seguente programma calcola il perimetro di una figura geometrica")
print("""
- Quadrato: >> 1
-Triangolo equilaterale >> 2
- rombo >> 3
""")
 print ('inserire la scelta:')
 scelta == int (input(">>> "))
 if scelta= 1:
 	print ("hai selezionato il perimetro del Quadrato")
 	lato= float(input('Inserisce il valore del lato del quadrato?))
 	print("il perimetro del Quadrato, avente lato", lato, "è:", lato *4)
 elif scelta= 2:
 	print("hai selezionato il triangolo")
 	base= float(input('inserice il valore della base'))
 	print("il perimetro del triangolo equilaterale è", base *3)
 elif scelta = 3:
 	print("hai selezionato la circonferanza del rombo")
 	r= float(input('inserisci il valore del lato'))
 	print("il perimetro del rombo di lato", r,"è", r *4)
 else:
  	print ("inserire una scelta valida")
  	
  perimetro();
