# gw-flat-distribution
Bei diesem Python Script handelt es sich die Umsetzung einer Optimierungsfunktion, um die optimale Verteilung von 
Wohnungen nach den von den Haushalten geäußerten Präferenzen. [(Pareto-Optimierung)](https://de.wikipedia.org/wiki/Pareto-Optimierung)

Aktuell handelt es sich nur um ein Konzept und das Python Script ist noch zu schreiben.

## mögliche Kriterien:
* Gebäude
* Etage
  * 2 Ausprägungen: lieber höher gelegen ***oder*** lieber tiefer gelegen
* Nähe zu bestimmten Haushalten
* Wohnungsgröße eher kleiner
  * nicht alle Wohnungen gleich in einer Klasse (z.B. 1,5 ZiWg)
  * Es soll nur die Option geben eine „eher kleine Wohnung aus finanziellen Gründen“ auswählen zu können
* Idee: Haustiere kommen zusammen in einen Bereich des Grünen Weilers
  * Konkrete Auswahlmöglichkeiten:
    * Gerne in der Nähe von Tieren
      * Haustierwunsch
    * Eher weit weg von Tieren
      * Allergie

## Allgemeines
* Zufriedenheit eines Haushalts ist auf Werte zwischen 0 und 1 zu normieren
* Wohnungsdistanz-Berechnung zwischen den Wohnungen
  * Referenz sollte die Haustür der Wohnung sein
  * zwei Ansätze denkbar:
    * Laufwege: Distanzangabe auf Basis der Laufwege (inkl. Weg zur Treppe und zu anderen Gebäuden etc.)
      * Voraussichtlich initial aufwendig, da das nicht berechnet werden kann und die Distanzen händisch angegeben 
      werden müssen
    * Luftlinie: Distanz auf Basis geometrischen Distanz der Haustüren
  * Grundsätzlich ist die Distanz nach Laufwegen zu präferieren, da eher Realität entsprechend
    * Problemfall: bei Haustier-Allergikern, die über einer Haustierwohnung wohnen, wäre der Laufweg lang, aber die 
    Tierhaare könnten dennoch einfach eine Etage hochfliegen &rarr; evtl. Nebenbedingung mit Mindestdistanz bei 
    Allergikern?
  * Variablen zur Distanzbewertung:
    * **MinDistanz**: 10 m
    * **MaxDistanz**: 100 m
    * **MinHaustierAversionsDistanz**: 50 m
    * **MaxHaustierAversionsDistanz**: 150 m
    * **MinAllergikerDistanz**: 75 m
      * Sollte ausreichend hoch sein, damit auch Wohnung ausgeschlossen werden, die direkt über den Haustierwohnungen liegen
* Haustiere
  * Hier sind 4 Optionen zur Auswahl zu stellen:
    * Ich habe einen Hund oder eine Katze (wie bei meiner Bewerbung angegeben)
    * Ich möchte gerne in der Nähe von Haushalten mit Hunden oder Katzen wohnen
    * Ich möchte Distanz zu Haushalten mit Hunden oder Katzen haben
    * Ich bin allergisch gegen Hund oder Katze
* Gewichtungsnormierung
  * Die Gewichtung je Kriterium sollte im Fragebogen von 0 bis 10 auswählbar sein
  * Für die Zielfunktion sollte die Zahl dann auf einen Wert zwischen 0 und 1 normiert werden

## Zielfunktion
Jedes Kriterium kann einzeln optimiert werden. Die einzelnen Optimierungsfunktionen sehen folgendermaßen aus:
1. Gebäude
   * Wunsch erfüllt = 1; Wunsch nicht erfüllt = 0
2. Etage
   * Je nach Wunsch (höher/tiefer). 
     * lieber höher : "tats. Etage" - 1 / (max<sub>(Etage)</sub> - 1) 
       * z.B. 2/3 = 0,66 &rarr; gut
     * lieber tiefer : (("tats. Etage" - 1 / (max<sub>(Etage)</sub> - 1)) - 1) * (-1) 
       * z.B. (2/3 - 1) * (-1) = 0,33 &rarr; schlecht
3. Nähe zu bestimmten Haushalten
   * ein Haushalt
     * Distanz < **MinDistanz** = 1
     * Distanz > **MaxDistanz** = 0
     * Dazwischen fließend
   * etwas komplizierter, wenn mehrere andere Haushalte angegeben wurden, da die Zufriedenheit 1 nicht übersteigen darf.
   Die Nähe zu einem der Haushalte ist als besonders wichtig anzusehen. Jeder weitere Haushalt bekommt dann weniger Gewicht
     * Vorschlag: Maximal 2 Haushalte angebbar. Dann:
       * Distanz < **MinDistanz** = 0,75 für den näher gelegenen Haushalt
       * Distanz < **MinDistanz** = 0,25 für den entfernter gelegenen Haushalt
       * Distanz > **MaxDistanz** = 0 je Haushalt
4. Lieber kleinere Wohnung &rarr; weniger Kosten
   * Wenn kleinste Wohnung im Vergleich zu Wohnungsgruppe (z.B. 1,5 ZiWg) = 1
   * Wenn größte Wohnung = 0
5. Haustiere
   * Wenn Haustierhaushalt oder Nähe dazu gewünscht
     * Distanz zu anderem Haustierhaushalt < **MinDistanz** = 1
     * Distanz zu anderem Haustierhaushalt > **MaxDistanz** = 0
   * Wenn Distanz gewünscht
     * Distanz zu anderem Haustierhaushalt < **MinHaustierAversionsDistanz** = 0
     * Distanz zu anderem Haustierhaushalt > **MaxHaustierAversionsDistanz** = 1

Für eine Optimierungsfunktion müssen alle Funktionen zusammengebracht werden.
Dazu können wie beim Scoring die Einzelfunktionen einfach aufsummiert werden.
* Je Funktion ist jedoch noch eine Gewichtung zu ergänzen, da nicht jeder Haushalt die Kriterien gleichgewichten wird.
* Man könnte auch zusätzlich eine Gewichtung der Belegungskommission ergänzen, falls sich dafür ein Argument aus den 
Belegungskriterien ergeben sollte
* Eine Optimierung erfolgt auf paarweises Tauschen von Haushalten und einem erneuten Prüfen der Zielfunktion auf eine 
Verbesserung.
* Die initiale Verteilung sollte möglichst zufällig sein.
  * Um ein globales und nicht nur ein lokales Optimum zu finden, sollte die Optimierung mehrmals mit unterschiedlichen 
  Startverteilungen durchlaufen werden

## Nebenbedingungen
* kein Haushalt darf komplett schlecht darstehen &rarr; Zufriedenheit bei einem einzelnen Haushalt darf nicht < 0.1 sein
  * Im Gegensatz zur Optimierungsfunktion muss hierfür die Gewichtung normiert werden. Sonst kann die Bedingung bei Haushalten, denen alles egal ist (Gewichtung überall = 0) nicht erfüllt werden 
* Bei Allergien ist ein Mindestabstand zu Tieren einzuhalten &rarr; Distanz zu Tierwohnungen > **MinAllergikerDistanz** 
  * Hier könnte beim Wunsch auf Distanz auch eine minimale Distanz als Nebenbedingung ergänzen

