from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
import sys

rng = 200000

def change_freq(value):
    global p
    p.terminate()
    p.wait()
    p = play(value / 10)

def play(value):
    return subprocess.Popen(["play", "-r", "192000", "-n", "synth", "sine", str(value)])

if __name__ == "__main__":
    app=QApplication(sys.argv)
    slider=QSlider(Qt.Horizontal)
    slider.setRange(1, rng)
    p = play(120)
    QObject.connect(slider,SIGNAL("valueChanged(int)"), change_freq)
    slider.show()
    #Start the evnt loop
    app.exec_()
    p.terminate()
    p.wait()
