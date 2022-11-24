import time, board, adafruit_dht

dht_device = adafruit_dht.DHT22(board.D4) # Charge le capteur sur le PIN GPIO 4

while True:
    try:
        temperature, humidity = dht_device.temperature, dht_device.humidity 
        # Recupere les donnees du capteur
        print("Temperature: " + str(temperature) + " C, Humidite: " + str(humidity) + "%", end="\r") 
        # Affiche ces donnees dans la console
    except RuntimeError: 
    # Il arrive que les donnees du capteur arrivent dans le Raspberry en etant corrompues, on ignore donc cette erreur
        time.sleep(2.0) # Pause de 2 secondes
        continue # On continue la boucle
    except Exception as error: 
    # Cette erreur est consideree comme grave, elle n'est pas censee arriver mais protection par precaution
        dht_device.exit() # Ferme proprement la liaison capteur-programme si erreur
        raise error # Laisse l'erreur interrompre le programme
    time.sleep(2.0) # Raffraichissement toutes les 2 secondes 
