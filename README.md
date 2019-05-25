# PythonCanSteering
PyQt4 Kvaser Canlib Can Middleware for steering Elmo Motion Cello 10/100 driven BLDC drives with openpnp

# Canlib
Canlib is taken from the Kvaser Canlib SDK. It is used as a wrapper to their library.

Tested with Kvaser Leaf Light 2

# Communication

The Cello are commanded over CAN bus with the SimplIQ commands.

Middleware talks to openpnp through a network socket.

The middleware periodically polls the position of all axes, and sends it to the openpnp

Middleware sends all M commands higher than 800 to the Smoothieboard.

# Homing

Homing is done simultaneously on all axes at the same time, after calling init().

How does homing work:

By pressing the Home button, the axis is driven with a defined jogSpeed to a mechanical stop, then the homing function is armed and the axis is travelling in the reverse direction with searchSpeed, slowly it searches for the index pulse.

X1 and Y is getting home position 0, Z gets the home position 100000, X2 gets the home position -4000, when it sees the index pulse.

C does not do the mechanical stop search, since that axis does not have one. It gets home position 744, so the nose of my tips is looking to the left.

# X axes
Since my machine has 2 X axes, where one of them is on the arm, and one of them is moving the desktop table, an algorithm had to be written to decide how to consistently and for openpnp transparently reach the specific points on the table. The goal is to extend the X travel possibilities.

It is currently set so that the table moves to 7500, 0 or -4600, depending on the overall sum X that needs to be reached.
