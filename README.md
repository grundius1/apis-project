# apis-project


![Lol](inputs/LOL.jpg)


## Objetivos
el bjetivo de este proyecto es aprender a conectarse a una api, saber controlar el argparse para poder seleccionar algunos datos unicos y poder saber los comportamientos de los jugadores para con esos campeones.

## Librerias
	1- pandas
	2- sys
	3- argparse
	4- re
	5- random
	6- json
	7- os
	8- dotenv
	9- requests
	10- matplotlib
	
## usabilidad
usage: main.py [-h] [-n NAME [NAME ...]] [-t TYPE] [-s STYLE [STYLE ...]] [-l [HEALTH]]
               [-p PLOT]

#csv y apis
	csv- kaggle link: https://www.kaggle.com/gyejr95/league-of-legendslol-champion-and-item-2020
	api- https://developer.riotgames.com/


## Notas
debido a la configuracion de la API y a las pocas request que te permite hacer por segundo,no se han configurado loops para las paginas de summoners, ya que eso puede dar problemas por cancelacion de las request.
