REM python.exe -m pip install --upgrade pip
REM pip install esptool
REM git clone https://github.com/espressif/esptool.git
cd .\esptool-master\
pip install -e .
cd ..
echo "EDIT THIS FILE FOR CORRECT COM PORT NUMBER"
esptool.py --chip esp32s2 --port COM17 erase_flash
esptool.py --chip esp32s2 --port COM17 --baud 921600 write_flash -z 0x0000 adafruit-circuitpython-espressif_saola_1_wroom-fr-6.2.0.bin




