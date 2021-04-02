from machine import Pin, PWM
import utime

buttonpower = Pin(10, Pin.OUT)
buttonpower.high()
button = Pin(11, Pin.IN, Pin.PULL_DOWN)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led = Pin(5, Pin.OUT)
speaker = PWM(Pin(21))

def ultra():
   trigger.low()
   utime.sleep_us(20)
   trigger.high()
   utime.sleep_us(10)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("The distance from object is ",distance,"cm")
   return distance
   
while True:
    utime.sleep(0.1)
    if button.value() == 1:
        button.value() == 0
        utime.sleep(0.1)
        led.high()
        utime.sleep(0.01)
        led.low()
        while True:
            
            if button.value() == 1:
                led.high()
                utime.sleep(0.01)
                led.low()
                utime.sleep(0.1)
                led.high()
                utime.sleep(0.01)
                led.low()
                break
            distance = ultra()
            if ultra() < 20:
                led.high()
                utime.sleep(0.01)
                led.low()
       
                speaker.duty_u16(3000)
                speaker.freq(1000)
                utime.sleep(0.1)
                speaker.deinit()
                utime.sleep(0.001)
                
     

