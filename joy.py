#!/usr/bin/env python3

# Autore: De Luca Francesco
# Descrizione: Nodo ROS per controllare una tartaruga in turtlesim usando un joystick.
# Funziona con un joystick collegato al computer.
# Riceve i dati del joystick dal topic /joy e pubblica i comandi di velocità sul topic /cmd_vel.
# La velocità lineare è controllata dall'asse verticale dello stick sinistro,
# La velocità angolare è controllata dall'asse orizzontale dello stick sinistro.
# La velocità massima è limitata a 2.0 unità per la linearità e 2.0 unità per l'angolarità.
# Il nodo è implementato in Python utilizzando rospy.


# 1. il joystick invia messaggi di tipo Joy sul topic /joy
# 2. il subscriber riceve i messaggi e chiama la funzione di callback
# 3. la funzione di callback converte i messaggi Joy in messaggi Twist
# 4. il publisher invia i messaggi Twist sul topic /cmd_vel
# 5. il robot (tartaruga) si muove in base ai messaggi ricevuti su /cmd_vel


import rospy #importa la libreria rospy per ROS in Python
from sensor_msgs.msg import Joy #importa il messaggio Joy per i dati del joystick
from geometry_msgs.msg import Twist #importa il messaggio Twist per i comandi di velocità

#funzione di callback, ogni volta che arriva un messaggio sul topic /joy viene chiamata dal subscriber
def joy_callback(joy_msg): #riceve il messaggio di tipo Joy
    twist_msg = Twist() # crea un nuovo messaggio di tipo Twist
    twist_msg.linear.x = joy_msg.axes[1] * 2.0  # asse verticale stick
    twist_msg.angular.z = joy_msg.axes[0] * 2.0 # asse orizzontale stick
    publisher.publish(twist_msg) #pubblica il messaggio Twist sul topic /cmd_vel

    rospy.loginfo(f"Published Twist: linear.x={twist_msg.linear.x}, angular.z={twist_msg.angular.z}") #log delle velocità pubblicate

if __name__ == '__main__': #punto di ingresso del programma
    rospy.init_node('joy_to_twist') #nome nodo

    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) #publisher per inviare messaggi di tipo Twist su cmd_vel
    rospy.Subscriber('/joy', Joy, joy_callback) # subscriber per ricevere messaggi di tipo Joy da /joy

    rospy.loginfo("Joystick Teleop Node Started") #log di avvio
    rospy.spin()  # mantiene il nodo in esecuzione
    
    