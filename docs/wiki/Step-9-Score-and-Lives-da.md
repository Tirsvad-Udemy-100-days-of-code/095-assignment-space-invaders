[English](Step-9-Score-and-Lives) · **Dansk** · [Bahasa Malaysia](Step-9-Score-and-Lives-ms)

# Trin 9: Point og liv

![Linjen med point og liv over flåden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## Det vi byggede

En `Scoreboard` med point og tre liv. Rumvæsnerne skyder igen: hvert andet sekund skyder det nederste rumvæsen i en tilfældig kolonne en rød kugle, som en barriere stopper, og som skibet betaler for med et liv. En række rumvæsner er 50, 40, 30, 20 eller 10 point værd.

## Det vi lærte

- At holde point og liv i én lille klasse, der også skriver dem
- At genbruge `Bullet` til en kugle, der flyver nedad (et negativt skridt)
- At vælge en tilfældig skytte, hvor tilfældighedskilden gives udefra, så en test kan fastlægge den
- At finde det laveste element i hver kolonne med en ren funktion (`lowest_per_column`)

## Prøv det

Spil et helt spil og følg point og liv.

## Hvor koden er

`src/scoreboard.py`, `src/game.py`, `src/fleet.py`: `choose_shooter`

Forrige: [Game over og sejr](Step-8-Game-Over-and-Win-da) · Næste: [[('Hvordan greb jeg projektet an?', 'Jeg planlagde, før jeg kodede. Projektet blev delt i tre gateways: opsætning, selve spillet og dokumentationen. Spillet blev bygget i ni små trin, hvert på sin egen gren med sin egen pull request, tests, skærmbillede og gennemgangspost, så historikken viser, hvordan spillet voksede. Alt, der ikke kræver et vindue, som begrænsning, rumvæsnernes placering, kollisioner, tiden mellem bevægelser og spillets tilstand, kom i `rules.py`, så det kunne testes uden skærm.'), ('Hvad var svært?', 'At teste et spil med vindue. `turtle` kræver Tk og en skærm, så testene, der åbner et vindue, kan ikke køre på CI-serveren eller på mit skrivebord. Jeg løste det med et Docker-image, der kører spillet og testene på en virtuel skærm. Timing var også drilsk: et skærmbillede af en kugle i luften eller af en flåde, der har bevæget sig, kræver, at tastetryk og ventetid passer til billedløkken.'), ('Hvad var nemt?', 'Da reglerne var adskilt fra tegningen, blev logikken kort og nem at teste. At arve fra `Turtle` til skibet, kuglen, rumvæsnerne og barriereblokkene gav hver ting sin egen lille klasse, og konstanterne i `constants.py` gjorde det til en enkelt linje at justere spillet.'), ('Hvordan kan jeg forbedre mig til næste projekt?', 'Starte med skærmbillede- og testmiljøet, før den første linje spilkode, og skrive testen til en regel før reglen. Jeg ville også køre pipelinens scanningsregler lokalt på samme måde som serveren, så fundene kommer tidligere.'), ('Hvad var min største læring?', 'At holde et spils regler fri af skærmen er det, der gør et grafisk projekt testbart, og at en tidsstyret løkke (en bevægelse hvert sekund) er enklere og mere retfærdig end at tælle billeder.'), ('Hvad ville jeg gøre anderledes?', 'Jeg ville tegne rumvæsnerne og skibet som egne former i stedet for turtles indbyggede former, tilføje lyd og en highscore-liste og lade flåden skyde i mønstre. Jeg ville også tage skærmbillederne fra en optaget gennemspilning i stedet for enkelte tastetryk.')]](Reflection-da) · [Oversigt](Home-da)
