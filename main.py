from browser import document, window, alert
import random 

def sketch(p): 
  #this p is needed. it will be the processing sketch itself.
  # to do things like background(0) instead do p.background(0)

    def setup():
        p.createCanvas(700, 410)
        p.background(255)
        p.rectMode(p.CENTER)

        # Wir haben nun einen weiteren Kreis auf den ersten gezeichnet.
        p.circle(250, 205, 20)
        p.circle(250, 205, 100)

    p.setup = setup
      
myp5 = window.p5.new(sketch)
