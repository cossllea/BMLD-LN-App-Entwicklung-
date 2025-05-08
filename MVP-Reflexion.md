### Konnte das MVP (V1.0) wie geplant umgesetzt werden?

-	Wir konnten einen ersten Datensatz mit Chatgpt generieren
-	Diesen haben wir auf Switchdrive hochgeladen und mit unserer App verbunden
-	Viele Informationen, die auf unserer Startseite stehen, waren schon vorhanden, wir konnten sie also grösstenteils so belassen
-	Wir haben wie geplant eine Unterseite mit einer Tabelle mit den ersten 10 Fragen des Datensatzes erstellt

### Bezüglich MVP (V2.0)

-	Wir haben eine neue Unterseite für das Quiz erstellt und einen Code für 10 randomisierte Fragen geschrieben
-	Nach der Generierung und Bearbeitung eines neuen Datensatzes hat der Code funktioniert
-	Die Fragen werden korrigiert, am Ende wird angezeigt wie viele Fragen man richtig / falsch beantwortet hat. Bei den falsch gelösten Fragen wird die richtige Antwort angezeigt


### Was konnte nicht umgesetzt werden und warum?

-	In der 2. Woche haben wir dann leider festgestellt, dass unser Datensatz immer wieder die gleichen Fragen enthielt und die Umlaute nicht richtig in der App angezeigt wurden.
-	Die Tabellenspalte, in der die richtige Antwort hinterlegt war, zeigte nur den richtigen Buchstaben der jeweiligen Spalte an, was zu einer Fehlermeldung beim Korrigieren führte.
-	Aufgrund dessen haben wir einen neuen Datensatz erstellt. Dieser enthält tatsächlich unterschiedliche Fragen und die richtige Antwort ist  ausgeschrieben, dass die Fehlerkontrolle reibungslos abläuft.


### Müssen wir die Roadmap anpassen und falls ja, wie?

Wir mussten aufgrund der gegebenen Kritik unsere Roadmap überarbeiten. Unsere Ziele waren zu hochgesteckt und wir müssen einige grundlegende Funktionen vorziehen, bevor wir unsere App ausschmücken.
Unsere ersten 2 Versionen sehen neu geplant so aus:

#### V 1.0 Dataframe (6.5-7.5h)
- Dataframe mit ChatGPT generieren aus Vorlesungsunterlagen über Parasitologie (1h) 
- Dataframe auf SwitchDrive laden und mit VsCodes & Streamlit verbinden  (4h) 
- Startbildschirm mit Infos (30 min) 
- Tabelle mit den ersten 10 Fragen des Dataframe erstellen (1-2h) 

#### V 2.0  + kleines Quiz mit 10 Fragen (5-6h) 
- 10 randomisierte Single Choice fragen mit je 4 Antwortmöglichkeiten, werden beim Klick auf den Quizbutton generiert (2-3h) 
- Anzahl richtig beantwortete Fragen werden angezeigt (1h) 
- Wenn zeitlich möglich -> welche Fragen richtig/falsch waren (2h)

Wir haben auch herausgefunden, dass wir die Bilder, die wir in unsere Fragen einfügen möchten als URL hinterlegen müssen. Da wir das noch nie gemacht haben wird es etwas länger brauchen. Wenn es zeitlich passt, gehört dieser Schritt noch zu V 3.0. 

### V 3.0 + User Login & Datenspeicherung auf SwitchDrive (5-6h)
- Login/SignUp implementieren (1-2h) 
- Ordner auf Switchdrive erstellen damit Userspezifische Daten gespeichert werden können (1h) 
- Switchdrive und App verknüpfen (2h) 
- Wenn zeitlich möglich -> Bider als URL hinterlegen (1h)


### Welche Unterstützung brauchen wir, um unsere Ziele zu erreichen?

Bis jetzt haben wir noch keine spezifischen Fragen, es werden aber sicher noch welche aufkommen:)
