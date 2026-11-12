# Task 02 – personalizace chatbota

Chatbot pro miliony uživatelů denně. Chci personalizaci, která pomůže, ale nezabije latenci, cenu ani soukromí.

## Data

Potřebuju `user_id`, základní profil (jazyk, timezone) a explicitní nastavení z UI – styl odpovědí, co nechce řešit atd. Tohle je nejspolehlivější.

Dál session: poslední zprávy, rozjetý úkol, jestli agent na něco čeká.

Dlouhodobě ne celý transcript do promptu, ale krátká shrnutí a konkrétní fakty se zdrojem a časem. Hodí se i signály z UI (thumbs, regenerace), ale jen jako slabý hint.

Odděleně souhlasy, retention a „nic si nepamatuj“. Raw log ≠ paměť pro model.

## Ukládání

Na requestu jen zápis zprávy + update session v Redis. Extrakce faktů, konflikty a embeddingy ať běží async ve frontě.

Postgres na profil/preference/audit, Redis na hot data, starší logy do cold storage. U paměti chci user_id, obsah, confidence, zdroj, čas a expiraci. Škálování per `user_id`.

## Generování odpovědi

Načtu session + malý profil, dohledám pár relevantních faktů k dotazu (jednotky, ne desítky) a složím prompt.

Personalizace ladí styl a prioritu, nevymýšlí fakta. Na hot path žádný další velký model, personalizační blok má strop na tokeny.

Nejistá nebo stará preference radši nepoužít. Uživatel musí mít reset. Citlivá témata defaultně neukládat.

## Měření

A/B: jen session vs. personalizace. Sledovat dokončení úkolu, thumbs, regenerace, latenci a cenu. Rollout jen když B pomůže a nerozbije zbytek.

Offline sada dialogů na spot-check. U nových userů je málo dat, výsledky dívat zvlášť.

## Soukromí

Mazání musí sáhnout na profil, paměti i embeddingy. Data jen kvůli personalizaci, s TTL a úklidem. Lepší slabší personalizace než špatně smazatelná data.
