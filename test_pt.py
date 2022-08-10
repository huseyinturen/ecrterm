# -*- coding: utf-8 -*-
"""
    Example script to demonstrate a payment process.
"""
from ecrterm import packets
from ecrterm.packets import *
from ecrterm.transmission.transport_serial import *
from ecrterm import ecr,common
import time

from ecrterm.packets.base_packets import ReadCard

if __name__ == '__main__':
    def printer(lines_of_text):
        for line in lines_of_text:
            print(line)
    e = ecr.ECR(device='/dev/ttymxc2')
    e.transmit(packets.LogOff())
    # reenable logging:
    e.transport.slog = ecr.ecr_log
    
    print(e.detect_pt())
    if e.detect_pt():
         e.register(0x8E)
         print(f"Read Card===================>\n\n\n\n")
         e.transmit(packets.ReadCard(timeout = 15))
       
         if e.payment(50):
             printer(e.last_printout())
             e.wait_for_status()
             e.show_text(lines=['Auf Wiedersehen!', ' ', 'Zahlung erfolgt'], beeps=0)
         else:
             e.wait_for_status()
             e.show_text(lines=['Auf Wiedersehen!', ' ', 'Vorgang abgebrochen'], beeps=1)
#        e.register(0xBA)
#        e.payment(10)
#        print(e.status())
        #status = 0x9c
        
#        e.transmit(packets.ReadCard())
"""        if status:
            print("Status code of PT is %s" % status)
            # laut doku sollte 0x9c bedeuten, ein tagesabschluss erfolgt
            # bis jetzt unklar ob er es von selbst ausführt.

            if status == 0x9c:
                print("End Of Day")
                e.end_of_day()
                # last_printout() would work too:
                printer(e.daylog)
            else:
                print("Unknown Status Code: %s" % status)
                # status == 0xDC for ReadCard (06 C0) -> Karte drin. 0x9c karte draussen.
"""

