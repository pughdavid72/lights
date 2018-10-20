#basic traffic light demo that runs throigh red green amber, then amber flashes for a bit.

from gpiozero import LED
from time import sleep

red = LED(25)
yellow = LED(8)
green = LED(7)

green.on()
yellow.off()
red.off()

while True:
  sleep(10)
  green.off()
  yellow.on()
  sleep(1)
  amber.off()
  red.on()
  sleep(10)
  yellow.on()
  sleep(1)
  green.on()
  red.off()
  yellow.off()
  sleep(5)
  green.off()
  yellow.blink()
  sleep(5)
  yellow.off()
  green.on()
