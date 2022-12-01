import time, board, adafruit_dht

dht_device = adafruit_dht.DHT22(board.D4) # Charge le capteur sur le PIN GPIO 4.

while True:
    try:
        temperature, humidity = dht_device.temperature, dht_device.humidity # Récupère les données du capteur.
        print("Température: " + str(temperature) + " °C, Humidité: " + str(humidity) + "%", end="\r") # Affiche ces données dans la console.
    except RuntimeError: # Il arrive que les données du capteur arrivent dans le Raspberry en étant corrompues, on ignore donc cette erreur.
        time.sleep(2.0) # Pause de 2 secondes.
        continue # On continue la boucle.
    except Exception as error: # Cette erreur est considérée comme grave, elle n'est pas censée arriver mais on sait jamais.
        dht_device.exit() # Ferme proprement la liaison entre le capteur et le programme.
        raise error # Laisse l'erreur interrompre le programme.
    time.sleep(2.0) # Pause de 2 secondes.