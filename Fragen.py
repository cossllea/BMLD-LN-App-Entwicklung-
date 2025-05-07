import pandas as pd

# Beispiel-Quizfragen zu Parasitologie
data = [
    {
        "Frage": "Welcher Parasit verursacht Malaria?",
        "Optionen": ["Plasmodium falciparum", "Trypanosoma cruzi", "Giardia lamblia", "Ascaris lumbricoides"],
        "Richtige Antwort": "Plasmodium falciparum",
        "Erklärung": "Plasmodium falciparum ist der gefährlichste Erreger der Malaria tropica."
    },
    {
        "Frage": "Wie wird Toxoplasmose meist übertragen?",
        "Optionen": ["Durch Mückenstiche", "Durch Katzenkot", "Durch kontaminiertes Wasser", "Durch Zecken"],
        "Richtige Antwort": "Durch Katzenkot",
        "Erklärung": "Toxoplasma gondii wird häufig über Katzenkot oder rohes Fleisch übertragen."
    },
    {
        "Frage": "Was ist ein typisches Merkmal von Echinococcus granulosus?",
        "Optionen": ["Bildung von Zysten in Organen", "Blutige Durchfälle", "Chronischer Husten", "Nervenschäden"],
        "Richtige Antwort": "Bildung von Zysten in Organen",
        "Erklärung": "Echinococcus granulosus kann große Zysten in Leber und Lunge bilden."
    },
    {
        "Frage": "Wie infiziert sich der Mensch mit Schistosomen?",
        "Optionen": ["Durch Insektenstiche", "Durch Kontakt mit Süßwasser", "Durch den Verzehr von Fisch", "Durch Tröpfcheninfektion"],
        "Richtige Antwort": "Durch Kontakt mit Süßwasser",
        "Erklärung": "Larven der Schistosomen dringen beim Baden in kontaminiertem Süßwasser durch die Haut ein."
    },
    {
        "Frage": "Welcher Parasit verursacht Schlafkrankheit?",
        "Optionen": ["Leishmania donovani", "Trypanosoma brucei", "Entamoeba histolytica", "Plasmodium vivax"],
        "Richtige Antwort": "Trypanosoma brucei",
        "Erklärung": "Die Schlafkrankheit wird durch die Tsetsefliege übertragen und durch Trypanosoma brucei verursacht."
    }

    {
        "Frage": "Was sind Parasiten?",
        "Optionen": "Lebewesen, die Pflanzen befallen;Lebewesen, die nur im Wasser leben;Lebewesen, die sich auf oder in einem artfremden Wirt aufhalten und zu dessen Lasten leben;Lebewesen, die ausschließlich mutualistisch leben",
        "Richtige Antwort": "Lebewesen, die sich auf oder in einem artfremden Wirt aufhalten und zu dessen Lasten leben"
    },
    {
        "Frage": "Welche zwei Hauptarten von Parasiten gibt es?",
        "Optionen": "Bakterien und Viren;Protozoen und Metazoen;Pilze und Algen;Helminthen und Zecken",
        "Richtige Antwort": "Protozoen und Metazoen"
    },
    {
        "Frage": "Was gehört zu den Metazoen?",
        "Optionen": "Amoeben;Helminthen;Kinetoplastida;Bakterien",
        "Richtige Antwort": "Helminthen"
    },
     {
        "Frage": "Wie nennt man das Zusammenleben zweier Partner mit gegenseitigem Vorteil, aber auch unabhängig lebensfähig?",
        "Optionen": "Parasitismus;Kommensalismus;Mutualismus;Symbiose im engeren Sinne",
        "Richtige Antwort": "Mutualismus"
    },
    {
        "Frage": "Was ist Kommensalismus?",
        "Optionen": "Wenn beide Partner voneinander abhängig sind;Wenn der Wirt dem Parasiten schadet;Wenn der Wirt Nahrung bereitstellt, ohne selbst Schaden zu nehmen;Wenn zwei Parasiten denselben Wirt nutzen",
        "Richtige Antwort": "Wenn der Wirt Nahrung bereitstellt, ohne selbst Schaden zu nehmen"
    },
    {
        "Frage": "Was sind Ektoparasiten?",
        "Optionen": "Parasiten, die im Wirt leben;Parasiten, die sich in Pflanzen entwickeln;Parasiten, die auf der Oberfläche des Wirts leben;Virale Parasiten",
        "Richtige Antwort": "Parasiten, die auf der Oberfläche des Wirts leben"
    },
    {
        "Frage": "Wie nennt man Parasiten, die im Inneren des Wirtes leben?",
        "Optionen": "Exoparasiten;Endoparasiten;Kommensalen;Mutualisten",
        "Richtige Antwort": "Endoparasiten"
    },
    {
        "Frage": "Was ist ein Beispiel für Übertragung durch direkten Kontakt?",
        "Optionen": "Fliegeneier;Larvenaufnahme;Milben;Insektenlarven",
        "Richtige Antwort": "Milben"
    },
    {
        "Frage": "Was bedeutet perkutane Infektion?",
        "Optionen": "Aufnahme durch Trinken;Eindringen durch Haut;Übertragung durch Luft;Genetische Vererbung",
        "Richtige Antwort": "Eindringen durch Haut"
    },
    {
        "Frage": "Was ist vertikale Übertragung?",
        "Optionen": "Übertragung von Tier auf Mensch;Übertragung durch infizierte Nahrung;Übertragung vom Mutterorganismus auf Nachkommen;Übertragung durch Luftpartikel",
        "Richtige Antwort": "Übertragung vom Mutterorganismus auf Nachkommen"
    }
]

df = pd.DataFrame(parasite_quiz)
df.to_csv("parasitologie_grundbegriffe_quiz.csv", index=False)


# DataFrame erstellen
df = pd.DataFrame(data)
print(df.head())
