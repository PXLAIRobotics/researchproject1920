# DUCKIE CONTROL - STEP BY STEP GUIDE

*The duckie in our guide is called 'erna'. Replace this with your own duckiebot name.*

***

*This first step is only needed once, when you want to connect the duckie to your home network.*

0. **(ONCE)** Configure duckie to connect to your home network 
	* Prepare a mobile hotspot on your phone, name `duckienet`, password `quackquack`.
	* Plug in duckie USB cables & wait for LEDs to die out
	* `ping erna.local`	to check if duckie is online. If not, wait a bit longer
		> if this still doesn't work 15 minutes after the LEDs, try `ping erna`  or  `ping <IP_of_duckie>`
	* ssh into your duckie: `ssh duckie@erna.local` or `ssh duckie@<duckie_IP>`. The password of your duckie will be provided by the Sam entity
	* `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`
	* Add a new network to the list:
		```network={    
		id_str="network3"    ssid="<name of your network>"```
		`	psk="<password of your network>"
			key_mgmt=WPA-PSK
		}`
	* Save the file: `Ctrl + X`, then `Y`, then `Enter`
	* Reboot duckie: `sudo reboot` (will reboot after 1 minute)
	* Wait patiently for the duckie to be reborn. No LED feedback will be available this time.
	
***

1. Boot the duckie
	* (If not done already in previous step: ) Plug in USB cables & wait for LEDs to die out
      	* `ping erna.local`	to check if duckie is online. If not, wait a bit longer
		> if this still doesn't work 15 minutes after the LEDs, try `ping erna`  or  `ping <IP_of_duckie>`
	* In a browser, visit 	erna.local:9000		check the list of containers. There should be a container 'demo_joystick'. It should be running. This container enables the /erna/joy topic to steer the duckie easily with some code.
	    * If the container is not present, go to [this webpage](https://docs.duckietown.org/DT19/opmanual_duckiebot/out/rc_control.html) The first command that is mentioned, installs the container. However, the container should be pre-installed on all team duckiebots.
	    * If the container was not running, start it and wait a moment. Afterwards, click the container and select 'Unless stopped' in the checkbox besides 'Restart policies'.
2. Next up, we'll write some code to communicate with the duckie. We provided a very basic example in this git repo (demo.py)
	* Creates a ROS node
	* Creates a publisher
	* Publishes joy messages
	* It will publish a (vx=1, vy=0) message for 2 seconds and halt afterwards. This will causes the duckie to move forward for 2 seconds, then stop
3. Set up communication
    To be able to communicate properly when running this piece of code, we'll have to `export` some ROS environment variables: `ROS_MASTER_URI` and `ROS_IP`
	* `ROS_MASTER_URI`: The location/URI where the roscore is running. This should be `http://<IP of duckiebot>:11311`
	* `ROS_IP`: The IP address of the device that will send the messages (our computer's IP)
	* The script 'duckie_init.sh' sets these values automatically by pinging the duckie and retrieving the computers IP. Run `source duckie_init.sh erna` to run the script. (replacing 'erna' with your duckiebots name) Afterwards, check the scripts output for these 2 environment variables.
	* Remember that these environment variables have to be set again for each new terminal you open. (unless, you solve this in a different way)
4. Run code
    When the connection is set up, run the demo:	
    `python demo.py`
    The duckie should start moving. Hit Ctrl-C to quit the demo.
