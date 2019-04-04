# PythonCanSteering
PyQt4 Kvaser Canlib Can Middleware for steering Elmo Motion Cello 10/100 driven BLDC drives with openpnp

# Canlib
Canlib is taken from the Kvaser Canlib SDK. It is used as a wrapper to their library.

Tested with Kvaser Leaf Light 2

# Communication
The Cello are commanded over CAN bus with the SimplIQ commands.
Middleware talks to openpnp through a network socket.
The middleware periodically polls the position of all axes, and TODO: sends it to the openpnp

# Homing
Homing is done each axis individually. ToDo: make the reading of information axis dependent and allow simultaneous homing of all axes.

How does homing work:

By pressing the Home button, the axis is driven to a defined mechanical stop, then the homing function is armed and the axis is travelling in the reverse direction, slowly it searches for the index pulse.
X1 and Y is getting home position 0, Z gets the home position 100000, X2 gets the home position -4000
C does not do the mechanical stop search, since it does not have one. It gets home position 0.
