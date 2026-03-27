# 🗺️ MAP.HTML - 5 SECTIONS VISUAL BREAKDOWN

## Quick Visual Guide

```
═══════════════════════════════════════════════════════════════════════════════
                                  NAVBAR
                    (Logo, Nav Links, Theme Toggle)
═══════════════════════════════════════════════════════════════════════════════

╔═════════════════════════════════════════════════════════════════════════════╗
║                          SECTION 1: HEADER + STATS                          ║
║  📊 Knowledge Mapper - Extract entities & visualize relationships          ║
║                                                                             ║
║  [📈 10 Entities] [🔗 5 Relations] [🎯 92% Confidence] [📝 250 Words]    ║
╚═════════════════════════════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════════════════════╗
║                        SECTION 2: INPUT AREA                                ║
║  [📋 Paste Text] [📁 Upload File]                                          ║
║                                                                             ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │ Paste your text here... (academic papers, research excerpts...)    │  ║
║  │                                                                     │  ║
║  │                                                                     │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                             ║
║  [⚡ Analyze & Extract]                                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════════════════════╗
║                   SECTION 3: KNOWLEDGE GRAPH (HERO)                         ║
║  Interactive visualization of entities and relationships                    ║
║                                                                             ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │                                                                     │  ║
║  │                    🔵 Entity Nodes 🔵                              │  ║
║  │                   /        |        \                              │  ║
║  │              verb1      verb2      verb3                           │  ║
║  │               /           |          \                             │  ║
║  │            🔵          🔵           🔵                             │  ║
║  │                                                                     │  ║
║  │           (600px Height - Drag to rearrange)                       │  ║
║  │                                                                     │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║  💡 Drag to rearrange nodes · Click to highlight connections               ║
╚═════════════════════════════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════════════════════╗
║                  SECTION 4: DETAILED ANALYSIS TABS                          ║
║                                                                             ║
║  [📌 Entities] [🔄 Relations] [🔤 POS Tags] [🤖 Summary] [📄 Text]    ║
║  ─────────────────────────────────────────────────────────────────────      ║
║                                                                             ║
║  ┌─────────────────────────────────────────────────────────────────────┐  ║
║  │ Named Entities (Active Tab)                                         │  ║
║  │                                                                     │  ║
║  │ 🟢 [Apple] 🔵 [Google] 🟡 [California] 🟣 [January 2024]         │  ║
║  │ 🟣 [CEO] 🟡 [San Francisco] 🔵 [Microsoft] 🟢 [$1.2B]            │  ║
║  │                                                                     │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                             ║
║  Other Tabs (Hidden):                                                      ║
║  • Relations: Subject → Verb → Object (Table format)                       ║
║  • POS Tags: Token analysis with grammar details                           ║
║  • Summary: AI-generated document summary                                  ║
║  • Text: Preprocessed input text                                           ║
╚═════════════════════════════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════════════════════════════╗
║              SECTION 5: EXPORT & RESEARCH TOOLS                             ║
║                                                                             ║
║  Download Results:                                                          ║
║  ┌─────────────────────┐  ┌─────────────────────┐                         ║
║  │ 👤 Named Entities   │  │ 🔗 Relations        │                         ║
║  │    CSV              │  │    CSV              │                         ║
║  └─────────────────────┘  └─────────────────────┘                         ║
║  ┌─────────────────────┐  ┌─────────────────────┐                         ║
║  │ 🤖 AI Summary       │  │ 📊 Metrics Report   │                         ║
║  │    CSV              │  │    CSV              │                         ║
║  └─────────────────────┘  └─────────────────────┘                         ║
║                                                                             ║
║  Research Tools:                                                            ║
║  ┌─────────────────────┐  ┌─────────────────────┐                         ║
║  │ 📋 Paper Analyzer   │  │ 🏆 Model Benchmark  │                         ║
║  └─────────────────────┘  └─────────────────────┘                         ║
║  ┌─────────────────────┐  ┌─────────────────────┐                         ║
║  │ 📊 Dataset Explorer │  │ 📖 Citation Tracker │                         ║
║  └─────────────────────┘  └─────────────────────┘                         ║
╚═════════════════════════════════════════════════════════════════════════════╝
```

---

## Desktop Layout (1400px+)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  NAVBAR                                                                       │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                               │
│  MAIN LAYOUT (Two Column: Content + Sidebar)                                │
│  ┌─────────────────────────────────────────────────────┐  ┌──────────────┐ │
│  │                                                      │  │              │ │
│  │  SECTION 1: Header + Stats (Top)                   │  │              │ │
│  │                                                      │  │   AI CHAT    │ │
│  │  SECTION 2: Input Area                             │  │   SIDEBAR    │ │
│  │                                                      │  │   (Sticky)   │ │
│  │  SECTION 3: KNOWLEDGE GRAPH (Hero - 600px)        │  │              │ │
│  │  ████████████████████████████████████████          │  │              │ │
│  │  ██          (Cytoscape Visualization)           ██  │              │ │
│  │  ████████████████████████████████████████          │  │  💬 Chat     │ │
│  │                                                      │  │   Messages   │ │
│  │  SECTION 4: Detailed Tabs                          │  │              │ │
│  │  [Entities] [Relations] [POS] [Summary] [Text]     │  │              │ │
│  │  ┌──────────────────────────────────────────────┐  │  │              │ │
│  │  │ Named Entities Tab Content                   │  │  │  🔹 User     │ │
│  │  │ [Entity Badges here...]                      │  │  │  🔹 AI       │ │
│  │  └──────────────────────────────────────────────┘  │  │  🔹 User     │ │
│  │                                                      │  │              │ │
│  │  SECTION 5: Export & Tools                         │  │  [Input Box] │ │
│  │  [CSV Buttons] [Research Tools]                    │  │              │ │
│  │                                                      │  │              │ │
│  └─────────────────────────────────────────────────────┘  └──────────────┘ │
│                                                                               │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Tablet Layout (768px - 1400px)

```
┌──────────────────────────────────────────────────────┐
│  NAVBAR                                              │
├──────────────────────────────────────────────────────┤
│                                                      │
│  SECTION 1: Header + Stats (2x2 grid)             │
│                                                      │
│  SECTION 2: Input Area (Full Width)                │
│                                                      │
│  SECTION 3: Knowledge Graph (400px)                │
│  ████████████████████████████                       │
│  ██    (Smaller visualization)                  ██  │
│  ████████████████████████████                       │
│                                                      │
│  SECTION 4: Tabs (Full Width)                     │
│                                                      │
│  SECTION 5: Export & Tools (Full Width)           │
│                                                      │
│  AI CHAT SIDEBAR (Below, stacked)                  │
│  ┌──────────────────────────────────────────────┐   │
│  │  AI Chat (300px height)                      │   │
│  └──────────────────────────────────────────────┘   │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## Mobile Layout (< 768px)

```
┌──────────────────────────┐
│  NAVBAR (Collapsed)      │
├──────────────────────────┤
│                          │
│  SECTION 1: Stats        │
│  (2x2 grid, smaller)     │
│                          │
│  SECTION 2: Input        │
│  (Stacked)               │
│                          │
│  SECTION 3: Graph        │
│  ██████████████████      │
│  ██  (300px height)  ██  │
│  ██████████████████      │
│                          │
│  SECTION 4: Tabs         │
│  (Full width)            │
│                          │
│  SECTION 5: Tools        │
│  (Single column)         │
│                          │
│  (Chat hidden)           │
│                          │
└──────────────────────────┘
```

---

## Color Scheme by Section

| Section | Primary | Secondary | Used For |
|---------|---------|-----------|----------|
| Header | Blue (#2563eb) | Neutral | Context & navigation |
| Stats | Blue gradient | Green accent | KPI display |
| Input | Light blue (#f0f4ff) | Text gray | User action area |
| Graph | Blue nodes | Cyan edges | Main visualization |
| Tabs | White background | Blue active | Data organization |
| Export | Multi-color icons | Gray borders | Call-to-action |
| Chat | Blue gradient | Light gray | Assistant interaction |

---

## Interactive Elements by Section

### Section 1: Header + Stats
- Buttons: Dashboard, Paper Analyzer
- Static stat cards with hover effects
- Responsive text sizing

### Section 2: Input Area
- Tab switching (Text ↔ File)
- Textarea with monospace font
- File input with visual feedback
- Submit button with loading state

### Section 3: Knowledge Graph
- **Interactive Cytoscape.js:**
  - Drag nodes to rearrange
  - Click nodes to select/highlight
  - Zoom with mouse wheel
  - Pan by dragging empty space
  - Auto-layout algorithm (COSE)

### Section 4: Detailed Tabs
- **5 Tabs with different content:**
  1. Entities: Color-coded badges
  2. Relations: Sortable table
  3. POS: Scrollable token list
  4. Summary: Formatted text
  5. Text: Monospace display

### Section 5: Export & Tools
- CSV download buttons (clickable)
- Quick links to other pages
- Hover effects on all buttons

### Right Sidebar: Chat
- Real-time message display
- User/AI message styling
- Send button + input field
- Auto-scroll to latest message
- Typing indicator

---

## User Journey Through Sections

```
User Arrives
    ↓
Section 1: See quick stats & header
    ↓
Section 2: Paste text or upload file
    ↓
Click "Analyze"
    ↓
Section 1: Stats update with results
    ↓
Section 3: Wow! 👀 Beautiful knowledge graph appears
    ↓
Section 4: Explore details in tabs
    ↓
Right Sidebar: Ask AI questions
    ↓
Section 5: Export results or try other tools
```

---

## Key Design Principles

### 1. **Visual Hierarchy**
- Section 3 (Graph) is the largest and most prominent
- Header and stats draw eyes upward
- Input area invites action
- Tabs organize details
- Export/tools at bottom for natural workflow end

### 2. **Progressive Disclosure**
- Quick stats first (high-level overview)
- Large graph second (visual aha moment)
- Detailed tabs third (deep dive)
- Export last (action)
- Chat always available (assistance)

### 3. **Information Architecture**
- **Top** → Context & Metrics
- **Middle** → Visualization & Input
- **Bottom** → Details & Actions
- **Right** → Support (Chat)

### 4. **Responsive Design**
- Desktop: 2-column with sticky sidebar
- Tablet: Single column, sidebar below
- Mobile: Full-width, chat hidden

### 5. **Color Coding**
- Entities: Different colors by type
- Relations: Consistent verb styling
- Export buttons: Visual distinction by function
- Chat: Blue for AI, light for user

---

## Performance Optimizations

- ✅ Cytoscape.js lazy loads on demand
- ✅ Tabs use show/hide, not reload
- ✅ Chat messages streamed in real-time
- ✅ CSV exports generated client-side
- ✅ Graphs use efficient rendering

---

## Accessibility Features

- ✅ Semantic HTML (nav, section, button)
- ✅ ARIA labels on interactive elements
- ✅ Keyboard navigation (Tab, Enter)
- ✅ Color contrast ratios meet WCAG AA
- ✅ Form labels associated with inputs

---

## Best Practices Implemented

✅ **Mobile-first responsive design**  
✅ **Sticky navigation and sidebar**  
✅ **Clear visual hierarchy**  
✅ **Consistent spacing & typography**  
✅ **Smooth animations & transitions**  
✅ **Loading states & error handling**  
✅ **Accessible color schemes**  
✅ **Intuitive user workflows**  
✅ **Fast & performant interactions**  
✅ **Professional, modern aesthetic**

---

Perfect for knowledge mapping, NLP research, and document analysis! 🚀