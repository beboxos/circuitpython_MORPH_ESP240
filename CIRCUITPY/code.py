#REPL
# line x16
# column x36
# circuitpython demo file by BeBoX
# twitter : https://twitter.com/BeBoXoS
# proof of concept of circuitpython on MORPHESP240
# need to be improved but all is "working" with morph lib (to use instead of board)
# 
import morph #board replacement 
import busio
import terminalio
import displayio
#from adafruit_display_text import label
from adafruit_st7789 import ST7789
#import adafruit_st7789
import neopixel
import time
import wifi
import ipaddress
import adafruit_imageload
from adafruit_display_text import label
tft_sclk = morph.SCLK
tft_mosi = morph.MOSI
tft_res = morph.RES
#init neopixel on pin 16
pixels = neopixel.NeoPixel(morph.RGB, 1)
displayio.release_displays()
spi = busio.SPI( tft_sclk, tft_mosi)
tft_cs = morph.CS
tft_dc = morph.DC
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)
display = ST7789(display_bus, width=240, height=240, rowstart=80, rotation=180)
def clearScreen():
    for n in range(0,15):
        print("")

pixels[0] = (0, 10, 0)
print("-" * 36)
print("Adafruit CircuitPython 6.2.0 \r\non 2021-04-05\r\nMorphESP240 Wroom-I with ESP32S2")
print("")
print("")
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("-" * 36) # for REPL display
print("Available WiFi networks:")
print("-" * 36)
pixels[0] = (10, 10, 0)
for network in wifi.radio.start_scanning_networks():
    #print("%s\t\tRSSI: %d\tChannel: %d" % (str(network.ssid, "utf-8"),
    #        network.rssi, network.channel))
    print(str(network.ssid, "utf-8"))
wifi.radio.stop_scanning_networks()
print("-" * 36)
pixels[0] = (0, 10, 0)
try:
    wifi.radio.connect(secrets["ssid"], secrets["password"])
    print("Connected to %s!"%secrets["ssid"])
    print("My IP address is", wifi.radio.ipv4_address)
    print("-" * 36)
    ipv4 = ipaddress.ip_address("8.8.4.4")
    print("Ping google.com: %f ms" % (wifi.radio.ping(ipv4)*1000))
except:
    print("No Network connected")
print("-" * 36)
pixels[0] = (10, 10, 10)
time.sleep(3)
pixels[0] = (0, 0, 10)
clearScreen()
print("-" * 36)
print("IO16 = NEOPIXEL")
print("IO12 = TFT SCLK")
print("IO11 = TFT MOSI")
print("IO13 = TFT MISO")
print("IO9  = TFT RES")
print("IO10 = TFT CS")
print("IO14 = TFT DC")
print("IO41 = SDA")
print("IO40 = SCL")
print("IO18 = RX")
print("IO17 = TX")
print("-" * 36)
time.sleep(3)
image, palette = adafruit_imageload.load("images/m4bit.bmp")
tile_grid = displayio.TileGrid(image, pixel_shader=palette)
group = displayio.Group() #crée le groupe
group.append(tile_grid)   #applique image
text_group = displayio.Group(max_size=10, scale=2, x=50, y=150)
text_area = label.Label(terminalio.FONT, text="MorphESP240\r\nCircuitPython", color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling
group.append(text_group)
display.show(group)       #affiche le groupe
time.sleep(2)
#reset pour affichage REPL
displayio.release_displays()
display_bus = displayio.FourWire(
    spi, command=tft_dc, chip_select=tft_cs, reset=tft_res
)
display = ST7789(display_bus, width=240, height=240, rowstart=80, rotation=180)
clearScreen()
pixels[0] = (0, 10, 0)
print("-" * 36)
print("Welcome to Circuitpython 6.2")
print("on MorphESP240 ")
print("")
print("Material : ")
print("x1 ESP32-S2 WROVER-I")
print("x1 Neopixel on IO16")
print("x1 TFT 240x240 px SPI")
print("-" * 36)
pixels[0] = (0, 0, 0)