# AI Code Review Assistant v2

**Architecture: Fetch → Chunk → Store → Display**

```
┌─────────────────────────────────────────────────────────────┐
│  STEP 1  Fetch all files from GitHub repo or file upload    │
│  STEP 2  Chunk large files (> 6 000 chars) at boundaries    │
│  STEP 3  Send ONE Gemini request per file (or chunk)        │
│  STEP 4  Store each FileResult in ResultStore immediately   │
│  STEP 5  All tabs read from ResultStore — zero re-calls     │
└─────────────────────────────────────────────────────────────┘
```

This reduces Gemini API calls by **70–90%** compared to calling per-tab or per-user-action.

---

## Get Your FREE Gemini API Key

1. Go to **https://aistudio.google.com/apikey**
2. Sign in with Google account
3. Click **Create API Key**
4. Copy it (starts with `AIza...`)

Free tier: 15 requests/minute · No credit card needed.

---

## Run

```cmd
cd ai_code_review_v2

pip install -r requirements.txt

set GEMINI_API_KEY=AIzaYourKeyHere

python -m streamlit run app.py
```

Opens at **http://localhost:8501**

> Tip: You can also paste the key directly in the app sidebar.

---

## Project Structure

```
ai_code_review_v2/
│
├── app.py                     # Main entry · 3-phase state machine
│                              #   input → analyzing → results
│
├── storage/
│   └── result_store.py        # ★ Central in-memory store
│                              #   Written once, read many times
│                              #   FileResult + Issue dataclasses
│
├── utils/
│   ├── ai_analyzer.py         # Gemini calls (one per file)
│   │                          # analyze_and_store() fills ResultStore
│   ├── chunker.py             # Splits large files at boundaries
│   ├── github_utils.py        # Clone repo + recursive file scan
│   ├── file_utils.py          # Supported extension list
│   ├── report_generator.py    # Markdown + JSON export from store
│   └── styling.py             # Dark-theme CSS
│
└── components/
    ├── sidebar.py             # API key config + file explorer
    └── views.py               # Dashboard, Summary, Issues,
                               # Optimized Code — all read from store
```

---

## Key Design Decisions

| Decision | Reason |
|---|---|
| One Gemini call per file | Avoids batch token limits, easier to retry individually |
| Chunking at code boundaries | Preserves context; merges results after |
| ResultStore singleton | Single source of truth; tabs never call Gemini |
| Per-file progress updates | User sees live status as each file completes |
| Store written immediately | If analysis crashes mid-way, completed files are not lost |
| JSON + Markdown export | Both human-readable and machine-processable |
