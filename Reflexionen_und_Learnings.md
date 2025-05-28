## Reflexion 1

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


## Schlussreflektion

Nach viel Schweiss und Tränen sind wir nun am Ende unserer Programmier-Reise. Dieser Leistungsnachweis hat uns, wohl oder übel, viel über Geduld und genaues Arbeiten beigebracht. Und obwohl nicht alles immer nach Plan gelaufen ist, sind wir glücklich und stolz auf unsere nun funktionierende App.

Der erste Streich spielte uns Chatgpt, der uns einen Datensatz mit nur vier sich wiederholenden Fragen ausspuckte. Das haben wir leider erst gemerkt, nachdem wir schon mit dem Quizcode begonnen hatten. Dies führte zu einem Quiz mit sich immer wiederholenden Fragen, da auch immer nur diese 4 Fragen gezogen werden konnten. Mit einem genaueren Prompt konnten wir dann einen brauchbaren Datensatz erstellen, woraufhin unser Quiz wieder besser funktioniert hat.

Ursprünglich hatten wir geplant, ein Bild einer "helfenden" Laborfachperson einzufügen, damit diese die Fragen stellen kann.
Nach unserem ersten Nutzertest wurde uns klar, dass diese Darstellung für einen kleinen Handybildschirm eher unübersichtlich und eng sein würde. Wir mussten das Design also etwas einfacher gestalten. Die App sah danach ziemlich leer aus, deswegen haben wir uns dazu entschieden, die App in den letzten Tagen noch etwas auszuschmücken.

Auch wurde uns ein Home Button empfohlen. Diesen hatten wir zuerst implementiert, im Verlauf der Entwicklung aber bemerkt, dass dieser eher überflüssig war. Der Verlauf der App ist ziemlich linear und die Startseite weist sehr wenige Funktionen auf, da sie mehr der Anleitung dient. Die spezifischeren Seitenwechsel-Buttons leiten den User direkt auf die richtige Seite. Damit die Lernenden immernoch die Möglichkeit haben, zwischen den Seiten hin und her zu springen, haben wir die Sidebar aktiviert gelassen.

In der ersten Reflexion haben wir erwähnt, dass wir die Bilder am Ende der V 3.0 einfügen würden, sofern dies zeitlich passt. Es hat dann doch etwas länger gedauert, das war es aber wert, da die Bilderfragen ein wichtiger Teil der App sind.

Leider war es uns nicht möglich den Weiter-Button im Quiz so anzupassen, dass man mit nur einem Klick zur nächsten Frage kommt. Beim Durchspielen ist uns auch aufgefallen, dass die Frage durch den Zurück-Button immer wieder neu lädt. Aufgrund dessen haben wir, obwohl wir das nach dem Nutzertest als gar nicht nötig empfanden, um Verwirrung vorzubeugen eine kurze Anleitung verfasst. Für den App Demo day haben wir als Backup ein Video mit einem ganzen Quizdurchlauf aufgenommen. Dieses haben wir auf die Startseite gestellt, so dass man es bei Bedarf anschauen kann.

Am meisten Mühe hat uns die Datenspeicherung bereitet. Es wurden pro Quizdurchlauf immer nur wenige Fragen gespeichert, aber nie alle, was sich natürlich dann schlecht auf die Statistik ausgewirkt hat. Vor allem als wir die 2 verschiedenen Modi eingeführt hatten, konnten wir lange keine saubere Datenspeicherung hinbekommen. --- Als dieses Problem aber gelöst war, konnten wir auch die Statistik etwas ausbauen. Da spezifisch eine separate Grafik für die einzelnen Modi geplant war und wir gut im Zeitplan waren, haben wir trotz Roadmap den Fokus zuerst auf die einzelnen Modi gesetzt und uns erst danach genauer mit der Statisitk auseinandergesetzt.

In der Roadmap haben wir die benötigte Zeit etwas knapp eingeschätzt. Mit mehr Erfahrung wäre die Planung sicher möglich gewesen, uns hat aber vor allem die Datenspeichergeschichte ziemlich viel Zeit gefressen. Zum Glück kam dieses Problem früh genug auf, so dass wir es trotz Überziehen des Zeitplanes früh genug lösen konnten.

In zukünftigen Versionen könnte man noch weitere Themengebiete des Faches Mikrobiologie hinzufügen, zum Beispiel Bakteriologie oder Virologie. Dafür müsste man noch eine Unterseite mit der Themenwahl erstellen. Mal schauen, vielleicht ist uns in den Ferien ja langweilig...

Im grossen und ganzen war es ein stressiges, aber auch cooles Projekt. Vor allem nach dem man alles nochmals reflektiert hat, kann man sich am Endergebnis umso mehr erfreuen.


