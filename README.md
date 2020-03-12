# Research Project '19-'20
## PXL Digital | AI & Robotics

#### Deze README wordt, samen met de andere bestanden in de repo, regelmatig aangevuld.

## IP Camera

### AI Hub setup
We gebruiken een DLink IP camera (dcs-4602ev). Deze kan aangesproken worden via ROS als je volgende stappen onderneemt:
- Clone de [RODIPCa](https://github.com/PXLRoboticsLab/RODIPCa) github repo
- Verbind met het netwerk ```AI Hub Devices``` (wachtwoord wordt via Slack gecommuniceerd)
- Start ```roscore```
- Run het RODIPCa script ```connect.py``` met de gewenste parameters (adres en login camera wordt via Slack gecommuniceerd)

Nadien zou met bv. ```rostopic list``` een nieuwe topic zichtbaar moeten zijn (eventueel met de gespecifieerde naam) waarop je kan subscriben om de camerabeelden binnen te halen.

### Remote setup: rosbag
Om remote al wat werk te kunnen doen richting communicatie met de IP camera, proberen we zo snel mogelijk een `rosbag` te voorzien. Dit kan je zien als een soort recording van één of meerdere ROS topics en de berichten die er over verstuurd worden. Deze kan je opnieuw afspelen en zo dus 'simuleren'. Op die manier kan je dan in je applicatie naar de opgenomen data luisteren alsof dat het *live* beeld is. Dit kan je dan reeds in je applicatie proberen te tonen, zodat jullie nadien enkel de koppeling eventueel wat moeten aanpassen.
We geven jullie hieronder de info die jullie normaal nodig hebben, maar een andere tutorial kunnen jullie [hier](http://wiki.ros.org/rosbag/Tutorials/Recording%20and%20playing%20back%20data) vinden.

De rosbag kan je afspelen door in een terminal naar de folder te navigeren waar het rosbag bestand is opgeslagen. Daarna kan je met `rosbag play <naam van het rosbag bestand>` de opgenomen topics weer laten afspelen. Omdat het fragment maar 1 seconde duurt, kan je dit best laten loopen. Dit doe je door de `-l` flag toe te voegen.

`rosbag play -l 2020-03-12-20-20-05.bag`

Let er op dat `roscore` ook moet opstaan voordat je dit doet. Na het opstarten van de recording, kan je normaal gezien de opgenomen topic zien. Na `rostopic list` zou je dus het volgende moeten zien:

`sam@sam:~$ rostopic list
/clock
/duckiecam/compressed
/rosout
/rosout_agg`

De topic `/duckiecam/compressed` is dezelfde die jullie zullen opvragen aan de 'live' camera, dus hiermee kunnen jullie voorlopig aan de slag om dit te integreren in de applicatie en computer vision algoritmen uit te proberen.

## Duckumentation
*duckiebot-naam* moet overal vervangen worden met de naame van de bot die jullie team probeert aan te spreken. Hier kan ook het statische IP voor gebruikt worden in plaats van de naam.

De duckiebots zijn onderdeel van het [Duckietown](https://www.duckietown.org/) pakket (niet te verwarren met [Ducktown](https://nl.wikipedia.org/wiki/Ducktown)), dat ontwikkeld werd aan MIT. 
Duckiebots werken met een Raspberry Pi, waarop Docker draait. Hierin worden enkele container gedeployed die het mogelijk maken om rechtstreeks met de duckiebot te communiceren via ROS.
Om een overzicht van de actieve containers op een duckiebot te krijgen, kan je naar http://*duckiebot-naam*(.local):9000 gaan om de Portainer interface te openen in de browser. (Ook deze Portainer interface wordt gehost door een container die [op de duckiebot](https://jfk.men/app/uploads/2019/10/Inception-film.png) draait.)

De belangrijkste andere containers zijn:
- roscore
- rosinterface
- demo_joystick : stelt enkele ROS topics open om de duckiebot aan te sturen
Deze containers worden normaal gezien automatisch opgestart.

In principe moeten er verder geen Docker containers toegevoegd of aangepast worden voor het uitvoeren van de minimale vereisten van dit project. Voor extra's kan dit eventueel nodig zijn, doe dit in samenspraak met Sam&Sam.

Zorg er in eerste instantie voor dat je met je laptop op hetzelfde netwerk verbonden bent als de duckie. Anders kunnen de devices elkaar niet vinden en dus ook niet communiceren. Standaard verbinden de duckiebots met het `AI Hub Devices_5Ghz` netwerk op de AI Hub. Zorg dus dat jij dat ook doet als je wil communiceren met de bot. Het wachtwoord voor dit netwerk werd reeds via Slack gecommuniceerd.
Als tweede optie hebben we er voor gezorgd dat de duckies proberen te verbinden met een mobiele hotspot `duckienet` en het wachtwoord `quackquack`. Dit kan je gebruiken om thuis de duckiebots te integreren in jullie project.

Om een duckiebot op te starten, voorzie je deze van een opgeladen batterij en steek je de 2 USB kabeltjes er in. De duckiebot zal dan automatisch opstarten. Zo lang de LED's branden, is het opstart-proces nog bezig. Dit kan enkele minuten duren. Het kan soms nog even duren na het doven van de LED's, voor de duckiebot responsief is. Wanneer de LED's uit gaan, probeer je daarom best eerst te pingen naar de duckiebot, om te kijken of hij al responsief is. Pas daarna kan je met de bot communiceren.

```ping duckiebot-naam.local```

Om via ROS te communiceren met de duckiebot, moeten de `ROS_MASTER_URI` en `ROS_IP` exports op de juiste waarde gezet worden. `ROS_MASTER_URI` moet als waarde het IP van de duckiebot krijgen, `ROS_IP` moet als waarde het IP van de laptop krijgen.
Het IP van de duckiebot kan je vinden met ```ping duckiebot-naam.local```, je eigen IP met bv. ```ip a```.
We hebben ook een scriptje geschreven om deze initialisatie automatisch te doen, dit wordt binnenkort op deze git repo geplaatst.

### Richtlijnen voor gebruik van duckiebots

0. **Draag zorg voor het materiaal!** We vertrouwen jullie de duckiebots toe, zodat jullie ze mee naar huis kunnen nemen om remote te kunnen werken aan het project. Toon dat dit vertrouwen terecht is!
1. Batterij van duckiebots **niet** opladen terwijl de duckiebot zelf aan staat. Steeds ontkoppelen en dan opladen.
2. **NOOIT** op tafels testen, zet je duckiebot steeds op de grond. Door netwerkvertraging of een bug kan de bot onverwachte bewegingen maken en van de tafel vallen. 
3. **BE PATIENT** - *Eenden zijn rustige beestjes en zullen zich niet haasten als je boos wordt op hen.*
4. Don't be **TOO** patient - *Wanneer de LED's van de duckiebot al 10 minuten uit zijn na opstarten en de duckiebot is nog niet responsief (ping) : best eens proberen om hem opnieuw [uit en aan](https://www.cipher-it.co.uk/wp-content/uploads/2017/11/ITCrow.jpg) te zetten.*
5. Spreek Sam en Sam gerust aan wanneer er problemen blijken te zijn met de duckiebots. Steeds eerst checken voor je zelf configuratie begint aan te passen.

### Quick/Quack checks

Als alle ROS parameters juist zijn ingesteld, kan je bv. via een `rostopic list` command kijken of de beschikbare ROS topics ook die van de duckiebot bevatten (bv. ```/duckiebot-naam/joy```)

Er kunnen ook default containers gebruikt worden om bv. [via keyboard de duckiebot te besturen](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/rc_control.html). Hiervoor heb je wel `dts` (duckietown-shell) nodig. Omdat jullie dit in principe niet nodig hebben voor jullie minimale requirements, verwijzen we hiervoor naar de [Duckietown documentatie](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/laptop_setup.html).
**Let op:** deze documentatie kan soms verwarrend zijn, vraag eerst even raad aan het onderwijsteam voor je hier aan begint.
