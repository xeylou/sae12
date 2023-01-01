import time, board, adafruit_dht

dht_device = adafruit_dht.DHT22(board.D4) # Charge le capteur sur le PIN GPIO 4

while True:
    try:
        temperature, humidity = dht_device.temperature, dht_device.humidity 
        # Recupere les donnees du capteur
        
        print("Temperature: " + str(temperature) + " C, Humidite: " + str(humidity) + "%", end="\r") 
        # Affiche les donnees sur la console
        
    except RuntimeError:                          # Prevention contre donnees du capteur corrompues 
        time.sleep(2.0)                             # Pause de 2 secondes
        continue                                     # Reprise de la boucle
        
    except Exception as error:                  # Precaution contre erreur grave extremement rare
        dht_device.exit()                          # Ferme proprement la liaison capteur-programme si erreur
        raise error                                  # Laisse l'erreur interrompre le programme
        
    time.sleep(2.0)                                 # Raffraichissement toutes les 2 secondes 
