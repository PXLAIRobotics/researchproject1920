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
- roscore (**TODO**)
- rosinterface (**TODO**)
- demo_joystick of custom (**TODO**)

In principe moeten er geen Docker containers toegevoegd over aangepast worden voor het uitvoeren van de minimale vereisten van dit project. VOor extra's kan dit eventueel nodig zijn, doe dit in samenspraak met Sam&Sam.

Om via ROS te communiceren met de duckiebot, moeten de `ROS_MASTER_URI` en `ROS_IP` exports op de juiste waarde gezet worden. `ROS_MASTER_URI` moet als waarde het IP van de duckiebot krijgen, `ROS_IP` moet als waarde het IP van de laptop krijgen.
(**TODO** double check of dit alle requirements zijn)

#### Quick/Quack checks

Als alle ROS parameters juist zijn ingesteld, kan je bv. via een `rostopic list` command kijken of de beschikbare ROS topics ook die van de duckiebot bevatten (bv. joy/... **TODO**)

Er kunnen ook default containers gebruikt worden om bv. [via keyboard de duckiebot te besturen](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/rc_control.html). Hiervoor heb je wel `dts` (duckietown-shell) nodig. Omdat jullie dit in principe niet nodig hebben voor jullie minimale requirements, verwijzen we hiervoor naar de [Duckietown documentatie](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/laptop_setup.html).
**Let op:** deze documentatie kan soms verwarrend zijn, vraag eerst even raad aan het onderwijsteam voor je hier aan begint.
