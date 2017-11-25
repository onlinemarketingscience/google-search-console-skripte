# Basis Python Skripte für das Anzapfen von Daten aus der Google Search Console

Die Google Search Console bietet eine Vielzahl an Daten, die durch Anwendung von Filtern zu wertvollen Informationen bei der Webanalyse werden können. Die Skripte sind im Kern nichts Weiteres als modifizierte API Requests, die als Python-Skript sehr simpel über den eigenen Computer gestartet werden können. 

# Wozu überhaupt die API nutzen?

1) Einrichten eines eigenen Data Warehouses
2) (Automatische) Speicherung über neunzig Tage hinweg
3) Spannende Kompositionsmöglichkeiten

# Skripte 

# gsc-statistics.py

Bsp: python gsc-statistics.py 'example.com' '2017-10-01' '2017-10-31' 

Dieses Skript speichert nach Ausführung eine csv-Datei im Verzeichnis, in dem sich das Skript befindet, mit dem Namen stats-YYYY-MM-DD.csv. Es enthält für die vier großen Sammel-KPIs (Klicks, Impressionen, CTR, Position) eine Übersicht der wichtigsten Kennzahlen der Statistik und eignen sich hervorragend für die Integration in ein SEO-Wochenreport, bspw. 

Das Skript gibt es seit dem 25. November 2017 und weißt noch viele Bugs auf, darunter die fehlende Modus-Angabe. Ich hoffe, dass ich zeitnahe die letzten Misszustände beheben kann. Stay tuned! 
