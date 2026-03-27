# 🗺️ Knowledge Mapper - Layout Structure

## 📋 Overview

The redesigned **map.html** is organized into **5 main sections** with an optimal pattern for knowledge mapping and visualization.

---

## 🎯 Layout Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                         NAVBAR (Sticky)                          │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                          MAIN CONTAINER (Two Column Layout)                  │
│  ┌─────────────────────────────────────────────────────┐  ┌──────────────┐ │
│  │           MAIN CONTENT (Left Column)                │  │ AI CHAT      │ │
│  │                                                     │  │ SIDEBAR      │ │
│  │  ┌─ SECTION 1: HEADER + QUICK STATS ──────────┐   │  │ (Sticky)     │ │
│  │  │ Title, Description, Breadcrumb             │   │  │              │ │
│  │  │ [4 Quick Stat Cards]                       │   │  │ • Chat H     │ │
│  │  └────────────────────────────────────────────┘   │  │ • Messages   │ │
│  │                                                    │  │ • Input      │ │
│  │  ┌─ SECTION 2: INPUT AREA (Compact) ─────────┐   │  │              │ │
│  │  │ [Paste Text Tab] [Upload File Tab]         │   │  └──────────────┘ │
│  │  │ [Textarea / File Input]                    │   │                    │
│  │  │ [Analyze Button]                           │   │                    │
│  │  └────────────────────────────────────────────┘   │                    │
│  │                                                    │                    │
│  │  ┌─ SECTION 3: KNOWLEDGE GRAPH (HERO) ───────┐   │                    │
│  │  │ [Large Interactive Visualization]         │   │                    │
│  │  │ [600px Height - Center of Attention]      │   │                    │
│  │  │ [Graph Info Bar at Bottom]                │   │                    │
│  │  └────────────────────────────────────────────┘   │                    │
│  │                                                    │                    │
│  │  ┌─ SECTION 4: DETAILED ANALYSIS TABS ───────┐   │                    │
│  │  │ [Entities] [Relations] [POS] [Summary]     │   │                    │
│  │  │ [Detailed Table/Content View]              │   │                    │
│  │  └────────────────────────────────────────────┘   │                    │
│  │                                                    │                    │
│  │  ┌─ SECTION 5: EXPORT + RESEARCH TOOLS ──────┐   │                    │
│  │  │ [CSV Download Buttons]                     │   │                    │
│  │  │ [Quick Links to Other Tools]               │   │                    │
│  │  └────────────────────────────────────────────┘   │                    │
│  │                                                    │                    │
│  └────────────────────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 📍 Sections Breakdown

### **SECTION 1: Header + Quick Stats**
**Location:** Top of page  
**Purpose:** Immediate context & key metrics at a glance  
**Components:**
- Title: "Knowledge Mapper"
- Description: What the tool does
- Quick action buttons (Dashboard, Paper Analyzer)
- 4 stat cards showing:
  - Number of Entities Extracted
  - Number of Relations Found
  - AI Confidence Score (%)
  - Total Words Analyzed

**Why:** Users see key insights immediately without scrolling

---

### **SECTION 2: Input Area (Compact)**
**Location:** Upper-middle (below stats)  
**Purpose:** Quick text input or file upload  
**Components:**
- Tabbed interface: "Paste Text" | "Upload File"
- Textarea for text input (monospace font)
- File input with drag-drop support
- "Analyze & Extract" button

**Design:** Compact gradient background to stand out from stats  
**Why:** Entry point for analysis - users don't have to scroll far

---

### **SECTION 3: Knowledge Graph (MAIN FOCUS)**
**Location:** Center-left, large 600px height  
**Purpose:** Visual representation of entity relationships  
**Components:**
- Interactive Cytoscape.js visualization
- Drag-to-rearrange nodes
- Click to highlight connections
- Info bar below graph with usage instructions

**Design:** Gradient background, rounded borders, shadows  
**Why:** Knowledge graph is the PRIMARY deliverable - takes visual priority

---

### **SECTION 4: Detailed Analysis Tabs**
**Location:** Below knowledge graph  
**Purpose:** Deep dive into specific data  
**Tabs:**
1. **Named Entities** - Color-coded entity badges (PERSON, ORG, GPE, LOC, DATE, MONEY)
2. **Relations (SVO)** - Subject-Verb-Object triples in table format
3. **POS Tags** - Token-level linguistic analysis (Token, POS, Lemma, Dependency)
4. **AI Summary** - Groq LLaMA-generated abstractive summary
5. **Cleaned Text** - Original input text after preprocessing

**Design:** Tabbed interface with smooth transitions  
**Why:** Users can explore data progressively without info overload

---

### **SECTION 5: Export & Research Tools**
**Location:** Bottom  
**Purpose:** Actions after analysis  
**Components:**

**Part A: Export Results**
- Download Named Entities as CSV
- Download Relations as CSV
- Download AI Summary as CSV
- Download Metrics Report as CSV

**Part B: Research Tools Quick Links**
- Paper Analyzer (/research)
- Model Benchmarking (/benchmark)
- Dataset Explorer (/datasets)
- Citation Tracker (/citations)

**Design:** 2-column grid with icon + text + arrow  
**Why:** Natural workflow end - users can export or explore more tools

---

### **RIGHT SIDEBAR: AI Chat Assistant**
**Location:** Sticky on right, full viewport height  
**Purpose:** Real-time Q&A about the analysis  
**Components:**
- Header: "AI Assistant"
- Message display area (scrollable)
- Input field + Send button
- Typing indicator while AI responds

**Design:** Sticky positioning, matches sidebar width (380px)  
**Why:** Always available for user questions without interrupting main workflow

---

## 🎨 Color & Visual Hierarchy

| Section | Color Scheme | Priority |
|---------|--------------|----------|
| Header | Neutral gray | Navigation only |
| Stats | Blue gradient gradient | High - Key metrics |
| Input | Light blue (#f0f4ff) | Medium - Required |
| Graph | White + gradient BG | **HIGHEST** - Main focus |
| Tabs | Clean white cards | Medium - Details |
| Export | Multi-color icons | Low - Optional |
| Chat | Blue gradient header | Medium - Assistance |

---

## 📱 Responsive Breakpoints

### Desktop (1400px+)
- Two-column layout: Content + Sidebar
- Graph height: 600px
- Full sidebar visible

### Tablet (768px - 1400px)
- Single column layout
- Sidebar below content
- Graph height: 400px
- Collapsed stats (2x2 grid)

### Mobile (< 768px)
- Full-width single column
- Chat sidebar hidden
- Graph height: 300px
- Stacked inputs
- Simplified navigation

---

## 🔄 User Journey

```
1. User arrives at /map
   ↓
2. Sees header + quick stats (orientation)
   ↓
3. Pastes text or uploads file (input section)
   ↓
4. Clicks "Analyze & Extract"
   ↓
5. Sees:
   - Updated stats
   - Large interactive knowledge graph (visual wow!)
   - Quick entity badges preview
   ↓
6. Explores in tabs (deep dive)
   ↓
7. Asks AI questions (right sidebar)
   ↓
8. Exports results as CSV
   ↓
9. Links to other research tools
```

---

## 💡 Design Decisions

### Why this layout?
1. **Knowledge graph centered** - It's the key deliverable, not an afterthought
2. **Quick stats first** - Users see value immediately
3. **Input compact** - Doesn't take up too much space
4. **Tabs for details** - Progressive disclosure, no info overload
5. **Sidebar chat** - Assistance without disrupting workflow
6. **Right sidebar sticky** - Always available, easy to access

### Why these sections?
- **Section 1** → Context
- **Section 2** → Action
- **Section 3** → Results (visual)
- **Section 4** → Analysis (detailed)
- **Section 5** → Next steps

---

## 🚀 Key Features

✅ **Modern Design** - Glassmorphism, gradients, smooth transitions  
✅ **Tab-based Interface** - Organize 5 different data views  
✅ **Interactive Graph** - Cytoscape.js for knowledge visualization  
✅ **CSV Export** - Download all results  
✅ **AI Chat Sidebar** - Real-time Q&A  
✅ **Fully Responsive** - Desktop, tablet, mobile  
✅ **Accessibility** - Semantic HTML, ARIA labels  
✅ **Performance** - Lazy load heavy components  

---

## 📊 File Structure

```
map.html
├── Navbar (sticky)
├── Main Container (grid: 1fr 380px)
│   ├── Main Content
│   │   ├── Section 1: Header + Stats
│   │   ├── Section 2: Input
│   │   ├── Section 3: Graph (600px)
│   │   ├── Section 4: Tabs
│   │   └── Section 5: Export
│   └── Sidebar Chat (sticky)
└── Scripts
    ├── Input tab switching
    ├── Cytoscape graph initialization
    ├── Chat functionality
    └── CSV download handlers
```

---

## 🔧 Integration with Backend

The map.html expects Flask to provide:

```python
@app.route("/map", methods=["GET", "POST"])
def map_page():
    # Returns:
    return render_template("map.html",
        raw_text=raw_text,
        result=result,  # dict with entities, relations, summary, etc.
        graph_data=json.dumps(graph_data)  # Cytoscape elements
    )
```

**Result object structure:**
```json
{
  "entities": [{"text": "...", "label": "PERSON"}, ...],
  "relations": [{"subject": "...", "verb": "...", "object": "..."}, ...],
  "pos_tags": [{"token": "...", "pos": "...", "lemma": "...", "dep": "..."}, ...],
  "summary": "AI-generated summary...",
  "metrics": {"entity_count": 10, "relation_count": 5, "confidence_score": 92},
  "cleaned_text": "Preprocessed text..."
}
```

---

## 🎯 Future Enhancements

- [ ] Graph customization (node colors, edge weights)
- [ ] Advanced filtering (by entity type, relation strength)
- [ ] Comparison mode (analyze 2 documents side-by-side)
- [ ] Export to JSON/RDF
- [ ] History of previous analyses
- [ ] Collaborative sharing
- [ ] Graph-to-presentation export

---

Generated with ❤️ for GenAI Knowledge Mapper