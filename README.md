
RFID-RC522 Modul:

Das RC522 RFID Modul wie folgt mit dem Raspberry verbinden:

| Name | Pin # | Pin name   |
|------|-------|------------|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

(INFO: zum RFID Tool gehören die folgenden Bibliotheken: Read.py und MFRC522.py sowie MFRC522.pyc)


LED wie folgt verbinden:

| Name  | Pin # | Pin name   |
|-------|-------|------------|
| GND   | 14    | GND        |
| Plus  | 11    | GPIO 0     |

Wichtig: Bitte bei der Schaltung der LED einen 220OHM Wiederstand verwenden.


2x16 LCD I2C Display wie folgt verbinden:

| Name | Pin # | Pin name   |
|------|-------|------------|
| GND  |  6    | GND        |
| VCC  |  2    | 5.0 VDC    |
| SDA  |  3    | SDA        |
| SCL  |  5    | SCL        |

(INFO: zum 2x16 LCD I2C Tool gehören die folgenden Bibliotheken: i2c_lib.py, i2c_lib.pyc sowie lcddriver.py und lcdriver.pyc)



Danach die Entsprechenden Dateien heruterlagen und die Read.py im Terminal mit sudo python Read.py ausführen.
WICHTI!: Ihr müsst nach dem Ausführen der Read.py zuerst euren Chip an den Leser halten, im Terminal wird euch dann die Entsprechende UID angezeigt aber die Schaltung der LED wird noch nicht funktionieren.
Diese UID von eurem Chip müsst Ihr im Anschluss in der Read.py an der entsprechenden Stelle eintagen (= in der Read.py in Zeile 54), damit euer Chip auch die Freigabe bekommt die Schaltung auszuführen.
Speichert die Read.py erneut ab und führt diese noch einmal aus, jetzt sollte die LED geschaltet werden.
