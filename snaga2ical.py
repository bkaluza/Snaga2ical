# -*- coding: utf-8 -*-
#
# Snaga2ical
# 
# Simple script that exports SNAGA-bins pickups (http://www.mojiodpadki.si/zemljevid) 
# to ical format. 
#
# Author: Bostjan Kaluza
# Date: Feb 17, 2014
#

import urllib, json
from datetime import datetime
from datetime import timedelta
import locale

from flask import Flask, Response


locale.setlocale(locale.LC_TIME, "sl_SI.utf-8")


class Snaga2ical(object):

    bin_type = {
        "mko": "Mesani odpadki",
        "bio": "BIO odpadki",
        "emb": "Embalaza",
        "pap": "Papir"
    }

    def __init__(self, url, addr):
        self.url = url
        self.addr = addr


    def to_ical(self):

        ical = ""

        response = urllib.urlopen(self.url);
        data = json.loads(response.read())
        for d in data["data"]:
            if "addr" in d.keys() and d["addr"] == self.addr:
                bt = d["type"]
                takeouts = (d["takeouts"].replace("<br /><br />", "")).split("<br />")
                #print bin_type[bt], takeouts
                for t in takeouts:
                    #print t
                    t_date = datetime.strptime(t, "%a, %d. %b %Y")
                    t_date_after = t_date + timedelta(days=1)
                    # print bin_type[bt], t_date.strftime("%Y%m%d"), t_date_after.strftime("%Y%m%d")
                    ical += "BEGIN:VEVENT\r\nDTSTART;VALUE=DATE:%s\r\nDTEND;VALUE=DATE:%s\r\nSUMMARY:%s\r\nEND:VEVENT\r\n"%(
                        t_date.strftime("%Y%m%d"), t_date_after.strftime("%Y%m%d"), self.bin_type[bt]
                        )
        ical = "BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//Coeus//snaga2ical//EN\r\n%sEND:VCALENDAR"%ical

        return ical




URL = "http://www.mojiodpadki.si/mojiodpadki/zemljevid/getbins/lat/46.05151/lng/14.50594019999994"
ADDR = "MALA ULICA 3"


app = Flask(__name__)
snaga_bins = Snaga2ical(URL, ADDR)


@app.route('/')
def get_calendar():

    ical = snaga_bins.to_ical()

    return Response(ical,
                    mimetype="text/calendar",
                    headers={"Content-Disposition": "attachment;filename=snaga.ical"})

    
if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0")
