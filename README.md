🐢 Turtlesim Joystick Controller

Questo progetto contiene un nodo ROS scritto in Python che permette di controllare la tartaruga di turtlesim utilizzando un joystick.
È pensato per esercitarsi con la pubblicazione di messaggi ROS, la gestione di input esterni e il controllo in tempo reale del simulatore turtlesim.

📦 Requisiti
- ROS (tested on ROS Noetic / ROS 1)
- Python 3
- turtlesim (sudo apt install ros-$ROS_DISTRO-turtlesim)
- joy package (sudo apt install ros-$ROS_DISTRO-joy)

⚙️ Installazione

Clona la repo all’interno del tuo workspace ROS:
cd ~/catkin_ws/src
git clone https://github.com/francescodeeluca/Turtle-Joy.git
cd ..
catkin_make
source devel/setup.bash

🕹️ Utilizzo

Avvia il master ROS:
roscore

In un nuovo terminale (CTRL+SHIFT+E/O), lancia il simulatore:
rosrun turtlesim turtlesim_node

In un altro terminale, avvia il nodo joy per leggere i comandi del joystick:
rosrun joy joy_node

Infine, esegui lo script di controllo:
rosrun <nome_pacchetto> turtle_joystick.py

🧠 Funzionamento

Il nodo:
1 - Sottoscrive al topic /joy per ricevere gli input del joystick.
2 - Traduce gli assi e i pulsanti del controller in comandi di velocità lineare e angolare.
3 - Pubblica i comandi sul topic /turtle1/cmd_vel per muovere la tartaruga.

🧩 Esempio di output

Quando muovi lo stick analogico, la tartaruga si sposta in tempo reale nella finestra di turtlesim:
[INFO] [1730816456.123]: Linear velocity: 1.0  Angular velocity: 0.5


🧑‍💻 Autore
Francesco De Luca
📧 franceescodeluca@gmail.com

📦 GitHub: @francescodeeluca
