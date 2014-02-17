Snaga2ical
==========

Simple script that exports [SNAGA-bins pickups](http://www.mojiodpadki.si/zemljevid) to ical format. It can be run as a webserver.


## How to configure

Visit http://www.mojiodpadki.si/zemljevid and find your location. The class has two parameters:
* ```url``` - inspect asynchrouniously made requests and copy requested url /mojiodpadki/getbins/lat/.../lng/..., for example, http://www.mojiodpadki.si/mojiodpadki/zemljevid/getbins/lat/46.05151/lng/14.50594019999994.
* ```addr``` - street name, for example, MALA ULICA 3


## How to use it

You can either call the class directly:
```python
snaga_bins = Snaga2ical(url, add)
print snaga_bins.to_ical()
```

Or you can run it as a web server:
```
$ python snaga2ical.py
```
which runs on http://localhost:5000 by default. If you have a public server, you can then add it as a feed your Google calendar or similar.







