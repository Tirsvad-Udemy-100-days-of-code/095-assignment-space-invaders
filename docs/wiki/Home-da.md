[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Space Invaders

Det klassiske Space Invaders-skydespil til én spiller med Python turtle-grafik: flyt dit rumskib, skyd rumvæsnerne, før de når dig, og søg dækning bag barriererne.

![Linjen med point og liv over flåden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/095-assignment-space-invaders/raw/branch/main/docs/images/step-9-score-lives.png)

## Hvad er det?

Dag 95 i Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp*. Et sort vindue på 800 gange 600 med titlen "Space Invaders" åbner med et grønt rumskib nederst, fire barrierer over det og fem rækker rumvæsner øverst. <kbd>Left</kbd> og <kbd>Right</kbd> flytter skibet, og <kbd>Space</kbd> skyder én kugle ad gangen. Hvert sekund rykker rumvæsnerne tættere på, de vender og rykker ned ved kanten, og de bliver hurtigere, jo færre der er tilbage. De skyder igen; et træf koster et liv. Spillet er tabt, når et rumvæsen rører skibet, når dets række, eller livene er brugt, og vundet, når det sidste rumvæsen er skudt. Spillet er bygget i ni trin, én pull request pr. trin, og hvert trin har sin egen side med et skærmbillede og det, vi lærte.

## De ni trin

1. [Spilskærm](Step-1-Game-Screen-da)
2. [Rumskib](Step-2-Spaceship-da)
3. [Skydning](Step-3-Shooting-da)
4. [Rumvæsenflåde](Step-4-Alien-Fleet-da)
5. [Rumvæsnernes bevægelse](Step-5-Alien-Movement-da)
6. [Skyd rumvæsnerne](Step-6-Shooting-Aliens-da)
7. [Barrierer](Step-7-Barriers-da)
8. [Game over og sejr](Step-8-Game-Over-and-Win-da)
9. [Point og liv](Step-9-Score-and-Lives-da)

## Næste

- [Kom i gang](Getting-Started-da)
- [[('Hvordan greb jeg projektet an?', 'Jeg planlagde, før jeg kodede. Projektet blev delt i tre gateways: opsætning, selve spillet og dokumentationen. Spillet blev bygget i ni små trin, hvert på sin egen gren med sin egen pull request, tests, skærmbillede og gennemgangspost, så historikken viser, hvordan spillet voksede. Alt, der ikke kræver et vindue, som begrænsning, rumvæsnernes placering, kollisioner, tiden mellem bevægelser og spillets tilstand, kom i `rules.py`, så det kunne testes uden skærm.'), ('Hvad var svært?', 'At teste et spil med vindue. `turtle` kræver Tk og en skærm, så testene, der åbner et vindue, kan ikke køre på CI-serveren eller på mit skrivebord. Jeg løste det med et Docker-image, der kører spillet og testene på en virtuel skærm. Timing var også drilsk: et skærmbillede af en kugle i luften eller af en flåde, der har bevæget sig, kræver, at tastetryk og ventetid passer til billedløkken.'), ('Hvad var nemt?', 'Da reglerne var adskilt fra tegningen, blev logikken kort og nem at teste. At arve fra `Turtle` til skibet, kuglen, rumvæsnerne og barriereblokkene gav hver ting sin egen lille klasse, og konstanterne i `constants.py` gjorde det til en enkelt linje at justere spillet.'), ('Hvordan kan jeg forbedre mig til næste projekt?', 'Starte med skærmbillede- og testmiljøet, før den første linje spilkode, og skrive testen til en regel før reglen. Jeg ville også køre pipelinens scanningsregler lokalt på samme måde som serveren, så fundene kommer tidligere.'), ('Hvad var min største læring?', 'At holde et spils regler fri af skærmen er det, der gør et grafisk projekt testbart, og at en tidsstyret løkke (en bevægelse hvert sekund) er enklere og mere retfærdig end at tælle billeder.'), ('Hvad ville jeg gøre anderledes?', 'Jeg ville tegne rumvæsnerne og skibet som egne former i stedet for turtles indbyggede former, tilføje lyd og en highscore-liste og lade flåden skyde i mønstre. Jeg ville også tage skærmbillederne fra en optaget gennemspilning i stedet for enkelte tastetryk.')]](Reflection-da)
- [Projektdokumenter](Project-Documents-da)
