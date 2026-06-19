# Personal Website — Branch `personal-site`

Sito portfolio personale costruito con [Astro 6](https://astro.build/). Il principio fondamentale è la **separazione totale tra contenuto e codice**: tutto il materiale editabile vive in `input/` e in `public/portfolio/img/`, senza mai toccare `src/`.

---

## Struttura della repo

```
Personal-website/
├── raw/                    ← FILE SORGENTE (PDF, DOCX, TXT, MD grezzi)
│   ├── projects/           ← sorgenti dei case study
│   ├── work/               ← sorgenti delle esperienze lavorative
│   ├── education/          ← sorgenti della formazione
│   └── portfolio/          ← sorgenti dei side project
│
├── input/                  ← CONTENUTO GENERATO (output di convert.py)
│   ├── about.md            ← unico file scritto a mano (dati personali)
│   ├── work/
│   ├── education/
│   ├── projects/
│   ├── portfolio/
│   └── assets/             ← file binari (CV in PDF, avatar)
│
├── public/
│   ├── assets/             ← file serviti staticamente (dani.png, cv.pdf…)
│   └── portfolio/img/      ← IMMAGINI dei case study
│
├── scripts/
│   ├── convert.py          ← pipeline di conversione raw → input/
│   └── requirements.txt    ← dipendenze Python
│
├── wiki/                   ← log di conversione + documentazione
│   ├── README.md
│   ├── content-guide.md
│   ├── naming-conventions.md
│   ├── projects/           ← un file per ogni case study convertito
│   ├── work/
│   ├── education/
│   └── portfolio/
│
└── src/                    ← codice Astro (non modificare per aggiornare contenuti)
```

---

## Come funziona il flusso dei contenuti

```
raw/projects/01-po-river.pdf
         │
         ▼
  scripts/convert.py  (Claude API)
         │
         ├──►  input/projects/01-po-river.md   ──►  Astro  ──►  /work/case-study-1-po-river/
         └──►  wiki/projects/01-po-river.md    (log di conversione)
```

I file in `raw/` sono i sorgenti originali (tesi, report, appunti). Lo script `convert.py` li legge, li invia a Claude API con un prompt specifico per sezione, e scrive in `input/` il Markdown strutturato con frontmatter corretto. Astro poi costruisce il sito da `input/`.

`input/about.md` è l'unico file scritto manualmente, non ha un equivalente in `raw/`.

---

## Regole di nomenclatura

### Regola generale

Tutti i file usano **lowercase kebab-case** e, dove l'ordine conta, un **prefisso numerico a due cifre**:

```
NN-nome-descrittivo.md
```

- `NN` = numero progressivo con zero iniziale (`01`, `02`, `03`…)
- Il numero determina l'ordine di visualizzazione sul sito (01 = primo)
- Nessuno spazio, nessuna maiuscola nei nomi file

---

## Directory `input/` — dove caricare i file di testo

### `input/about.md` — unico file, dati personali

Fonte di verità per nome, bio, contatti, certificazioni, lingue. Viene usato da homepage, pagina About e pagina Contatti.

```yaml
---
name: "Nome Cognome"
tagline: "Titolo professionale breve"
avatar: "/assets/foto.png"       # percorso relativo a public/
location: "Città, Paese"
email: "email@esempio.com"
linkedin: "https://linkedin.com/in/handle"
github: "https://github.com/handle"
certifications:
  - "Nome certificato (Ente)"
languages:
  - "Italiano (madrelingua)"
  - "Inglese (C1)"
---

Bio in testo libero. Questo paragrafo appare nella pagina About.
```

---

### `input/work/NN-azienda.md` — esperienze lavorative

Un file per ogni ruolo. Ordine: **ruolo più recente = 01**.

```yaml
---
title: "Job Title"
company: "Nome Azienda"
start: "2024"        # anno come stringa
end: "2025"          # anno come stringa, oppure null se ruolo attuale
skills:
  - "competenza uno"
  - "competenza due"
---

Descrizione del ruolo in Markdown. Usa **grassetto** per evidenziare risultati,
*corsivo* per note di riservatezza (es. NDA).
```

Esempi: `01-progesi.md`, `02-enel.md`, `03-freelance.md`

---

### `input/education/NN-titolo-ateneo.md` — formazione accademica

Un file per ogni laurea o periodo di scambio. Ordine: **titolo più recente = 01**.

```yaml
---
degree: "M.Sc. Nome Corso"
institution: "Nome Università"
location: "Città, Paese"
start: 2021          # intero
end: 2024            # intero, oppure null se in corso
grade: "106/110"     # stringa, oppure null
description: "Una riga di sintesi del percorso o focus del corso."
---
```

Il corpo Markdown è facoltativo (la `description` è sufficiente).

Esempi: `01-msc-polimi.md`, `02-erasmus-upv.md`, `03-bsc-polimi.md`

---

### `input/projects/NN-nome-progetto.md` — case study (pagina principale)

**Il tipo di file più importante.** Ogni file diventa una pagina dedicata su `/work/[slug]/` e una card nella griglia dei progetti. Ordine: **progetto più prominente = 01**.

Usa estensione `.md` per contenuto statico, `.mdx` solo se serve incorporare componenti Astro interattivi (es. grafici).

```yaml
---
title: "Titolo completo del progetto"
subtitle: "Una frase che appare sulla card e come sottotitolo della pagina."
hero_image: "/portfolio/img/NN-slug/hero.png"   # opzionale
client: "Ente / Corso o contesto"
year: "2024"
duration: "12 mesi"
tools:
  - "Python"
  - "QGIS"
  - "HEC-RAS"
---
```

Struttura consigliata del corpo:

```markdown
## ▸ The Challenge
## ▸ My Approach
## ▸ The Solution
## ▸ Key Results
## ▸ Business Impact
## ▸ Tech Stack
```

Le immagini si inseriscono con la sintassi standard Markdown — il testo `alt` diventa automaticamente la didascalia della figura:

```markdown
![Descrizione che diventa didascalia](/portfolio/img/01-po/figura.png)
```

Esempi: `01-po-river.md`, `02-olona.mdx`, `03-statistical-paleoclimate.md`

---

### `input/portfolio/NN-progetto.md` — side project o esperimenti

Un file per ogni progetto personale. Non genera una pagina dedicata: solo una card con link esterno.

```yaml
---
title: "Nome Progetto"
year: "2023"
type: "Side Project"       # badge visibile sulla card
description: "2–3 frasi di descrizione."
tools:
  - "Python"
  - "FastAPI"
repo: "https://github.com/handle/repo"   # opzionale
url: "https://demo-live.com"             # opzionale
---
```

Nessun corpo Markdown necessario.

Esempi: `01-three-gorges.md`, `02-nome-tool.md`

---

### `input/assets/` — file binari (CV, documenti)

Nessun prefisso numerico. Nomi descrittivi e senza spazi.

Dopo aver copiato il file qui, spostarlo anche in `public/assets/` (Astro serve i file statici da `public/`, non da `input/`). Referenziarlo poi nel frontmatter come:

```yaml
avatar: "/assets/dani.png"
```

---

## Directory `public/portfolio/img/` — dove caricare le immagini

Le immagini dei case study vanno organizzate **in sottocartelle che corrispondono al prefisso del file progetto**:

```
public/portfolio/img/
├── 01-po/
│   ├── 01_po_basin_map.png
│   ├── 02_po_discharge_timeseries.png
│   └── 03_sensitivity_tornado.png
├── 02-olona/
│   ├── 01_olona_basin_dem.png
│   └── 03_hecras_profile.png
└── NN-slug/
    └── ...
```

**Convenzione per i file immagine** (dentro ogni sottocartella):

```
NN_nome-descrittivo.png
```

- `NN` = ordine di apparizione nel testo del case study
- Nessuna maiuscola, underscore come separatore tra numero e nome

Le immagini sono referenziate nel Markdown con percorso assoluto dalla root del sito:

```markdown
![Alt text / didascalia](/portfolio/img/01-po/01_po_basin_map.png)
```

---

## Pagine generate e loro sorgente

| URL | Sorgente principale |
|-----|---------------------|
| `/` | `input/about.md` + `input/projects/` |
| `/about/` | `input/about.md` + `input/work/` + `input/education/` |
| `/work/` | `input/projects/` (griglia card) |
| `/work/[slug]/` | `input/projects/NN-slug.md` (pagina completa) |
| `/projects/` | `input/projects/` (alias della griglia) |
| `/contact/` | `input/about.md` (email) |

Lo slug dell'URL viene derivato automaticamente dal nome file, senza il prefisso numerico:
`01-po-river.md` → `/work/case-study-1-po-river/`

---

## Aggiungere un nuovo case study — procedura

1. Creare `input/projects/NN-nome-progetto.md` con il frontmatter corretto
2. Creare la cartella `public/portfolio/img/NN-nome-progetto/`
3. Caricare le immagini nella cartella appena creata
4. Referenziarle nel body del file Markdown con `/portfolio/img/NN-nome-progetto/nome-immagine.png`
5. Avviare il dev server (`npm run dev`) per verificare

---

## Pipeline di conversione — setup e utilizzo

### 1. Installare le dipendenze Python

```bash
pip install -r scripts/requirements.txt
```

### 2. Impostare la chiave API

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Caricare i file sorgente in `raw/`

Mettere i file nella sottocartella giusta con il nome corretto:

```
raw/projects/01-po-river.pdf
raw/work/01-progesi.docx
raw/education/01-msc-polimi.txt
raw/portfolio/01-three-gorges.md
```

### 4. Eseguire la conversione

```bash
# tutti i file in raw/
python scripts/convert.py

# solo una sezione
python scripts/convert.py --section projects

# un singolo file
python scripts/convert.py --file 01-po-river.pdf

# anteprima senza chiamare l'API
python scripts/convert.py --dry-run

# sovrascrivi output esistenti
python scripts/convert.py --force
```

Lo script scrive:
- `input/[sezione]/NN-slug.md` — il file Markdown pronto per Astro
- `wiki/[sezione]/NN-slug.md` — log di conversione con riferimento al sorgente e spazio per note manuali

### 5. Aggiungere le immagini

Le immagini non vengono estratte automaticamente dai PDF. Vanno caricate manualmente:

```
public/portfolio/img/NN-slug/NN_nome-immagine.png
```

Poi referenziate nel `.md` generato aggiungendo:

```markdown
![Didascalia](/portfolio/img/01-po/01_basin_map.png)
```

---

## Sviluppo locale

```bash
npm install
npm run dev       # dev server su http://localhost:4321 (o porta successiva libera)
npm run build     # build statica in dist/
npm run preview   # anteprima della build produzione
```

Node.js ≥ 22.12.0 richiesto.

---

## Documentazione interna

La cartella `wiki/` contiene guide di riferimento per il sistema di contenuti:

- [`wiki/content-guide.md`](wiki/content-guide.md) — schema frontmatter dettagliato per ogni tipo di file
- [`wiki/naming-conventions.md`](wiki/naming-conventions.md) — regole di nomenclatura per directory e file
