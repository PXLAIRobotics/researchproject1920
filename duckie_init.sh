if [ -z "$1" ]
    then
        echo "No duckiebot given..."
        echo "Usage: source ./duckie_init.sh <duckiebot_name> (<ROS_MASTER_PORT:11311>)"
        return
fi

duckiebot_ip="$(getent hosts $1.local | cut -d ' ' -f 1)"
port=11311
if [ -z "$2" ]
  then
    port=11311
  else
    port=$2
fi
export ROS_MASTER_URI=http://$duckiebot_ip:$port
echo "ROS_MASTER_URI >>> $duckiebot_ip:$port"

ip="$(hostname -I | cut -d ' ' -f 1)"
export ROS_IP=$ip
echo "ROS_IP >>> $ip"

export | grep ROS
