# Research Project 19-20
## PXL Digital | AI & Robotics

### Disclaimer: Deze README is een work in progress

### Camera
We gebruiken een DLink IP camera (dcs-4602ev). Deze kan aangesproken worden via ROS als je volgende stappen onderneemt:
- Clone de [RODIPCa](https://github.com/PXLRoboticsLab/RODIPCa) github repo
- Verbind met het netwerk ```AI Hub Devices``` (wachtwoord wordt via Slack gecommuniceerd)
- Start ```roscore```
- Run het RODIPCa script ```connect.py``` met de gewenste parameters (adres en login camera wordt via Slack gecommuniceerd)

Nadien zou met bv. ```rostopic list``` een nieuwe topic zichtbaar moeten zijn (eventueel met de gespecifieerde naam) waarop je kan subscriben om de camerabeelden binnen te halen.

### Duckumentation
De duckiebots zijn onderdeel van het [Duckietown](https://www.duckietown.org/) pakket (niet te verwarren met [Ducktown](https://nl.wikipedia.org/wiki/Ducktown)), dat ontwikkeld werd aan MIT. 
Duckiebots werken met een Raspberry Pi, waarop Docker draait. Hierin worden enkele container gedeployed die het mogelijk maken om rechtstreeks met de duckiebot te communiceren via ROS.
Om een overzicht van de actieve containers op een duckiebot te krijgen, kan je naar http://*duckiebot-naam*.local:9000 gaan om de Portainer interface te openen in de browser. (Ook deze Portainer interface wordt gehost door een container die [op de duckiebot](https://jfk.men/app/uploads/2019/10/Inception-film.png) draait.)

De belangrijkste andere containers zijn:
- roscore (automatisch opgestart **TODO**)
- rosinterface (automatisch opgestart **TODO**)
- demo_joystick (opstarten via Portainer interface **TODO**)

In principe moeten er verder geen Docker containers toegevoegd of aangepast worden voor het uitvoeren van de minimale vereisten van dit project. Voor extra's kan dit eventueel nodig zijn, doe dit in samenspraak met Sam&Sam.

Om een duckiebot op te starten, voorzie je deze van een opgeladen batterij en steek je de 2 USB kabeltjes er in. De duckiebot zal dan automatisch opstarten. Zo lang de LED's branden, is het opstart-proces nog bezig. Dit kan enkele minuten duren. Het kan soms nog even duren na het doven van de LED's, voor de duckiebot responsief is. Wanneer de LED's uit gaan, probeer je daarom best eerst te pingen naar de duckiebot, om te kijken of hij al responsief is. Pas daarna kan je met de bot communiceren.

```ping duckiebot-naam.local```

Om via ROS te communiceren met de duckiebot, moeten de `ROS_MASTER_URI` en `ROS_IP` exports op de juiste waarde gezet worden. `ROS_MASTER_URI` moet als waarde het IP van de duckiebot krijgen, `ROS_IP` moet als waarde het IP van de laptop krijgen.
Het IP van de duckiebot kan je vinden met ```ping duckiebot-naam.local```, je eigen IP met bv. ```ip a```.
We hebben ook een scriptje geschreven om deze initialisatie automatisch te doen, dit wordt binnenkort op deze git repo geplaatst.

#### Richtlijnen gebruik duckiebots

1. Batterij van duckiebots niet opladen wanneer ze gebruikt worden om een duckiebot te voeden.
2. Niet op tafels testen, duckiebots steeds op grond zetten. Door lag of bug kan de bot onverwachts bewegen en van de tafel vallen.
3. **BE PATIENT** - *Overall, duckies are extremely chill and will not hurry up if you get angry.*
4. ...

#### Quick/Quack checks

Als alle ROS parameters juist zijn ingesteld, kan je bv. via een `rostopic list` command kijken of de beschikbare ROS topics ook die van de duckiebot bevatten (bv. ```/duckiebot-naam/joy```)

Er kunnen ook default containers gebruikt worden om bv. [via keyboard de duckiebot te besturen](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/rc_control.html). Hiervoor heb je wel `dts` (duckietown-shell) nodig. Omdat jullie dit in principe niet nodig hebben voor jullie minimale requirements, verwijzen we hiervoor naar de [Duckietown documentatie](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/laptop_setup.html).
**Let op:** deze documentatie kan soms verwarrend zijn, vraag eerst even raad aan het onderwijsteam voor je hier aan begint.
