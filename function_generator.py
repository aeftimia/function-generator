from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
import sys

def change_freq(value):
    global p
    p.terminate()
    p.wait()
    p = play(value)

def play(value):
    print "%dHz" % value
    return subprocess.Popen(["play", "-r", "192000", "-n", "synth", "sine", str(value)])

if __name__ == "__main__":
    app=QApplication(sys.argv)
    slider=QSlider(Qt.Horizontal)
    slider.setRange(20, 2000)
    p = play(100)
    QObject.connect(slider,SIGNAL("valueChanged(int)"), change_freq)
    slider.show()
    #Start the evnt loop
    app.exec_()
    p.terminate()
    p.wait()
