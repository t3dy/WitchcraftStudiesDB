#!/usr/bin/env python3
"""
Generate static HTML website from WitchcraftStudiesDB JSON data.
Output: web/ directory with 7 standalone HTML pages.
All data is embedded as JS so pages work on file:// protocol.
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
WEB = ROOT / "web"

# ── helpers ──────────────────────────────────────────────────────────────────

def load_dir(entity_type: str) -> list[dict]:
    d = DATA / entity_type
    if not d.exists():
        return []
    out = []
    for f in sorted(d.glob("*.json")):
        try:
            out.append(json.loads(f.read_text()))
        except Exception as e:
            print(f"  WARN: {f.name}: {e}", file=sys.stderr)
    return out

def js_embed(name: str, data) -> str:
    return f"const {name} = {json.dumps(data, ensure_ascii=False, indent=None)};\n"

def escape(s) -> str:
    if not s:
        return ""
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

# ── shared CSS ────────────────────────────────────────────────────────────────

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --ink:      #1a1208;
  --parchment:#fdf6e3;
  --cream:    #f5ead0;
  --border:   #c8a96e;
  --accent:   #7b3f00;
  --accent2:  #4a1c00;
  --muted:    #7a6a50;
  --link:     #5c2d00;
  --card-bg:  #fffdf5;
  --shadow:   rgba(90,50,10,.15);
  --radius:   6px;
  --max:      1100px;
}

body {
  font-family: Georgia, "Times New Roman", serif;
  background: var(--parchment);
  color: var(--ink);
  font-size: 16px;
  line-height: 1.65;
  min-height: 100vh;
}

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; color: var(--accent); }

/* ── header ── */
header {
  background: var(--accent2);
  color: #f5deb3;
  padding: 0;
  border-bottom: 3px solid var(--border);
}
.header-inner {
  max-width: var(--max);
  margin: 0 auto;
  padding: 18px 24px 14px;
  display: flex;
  align-items: baseline;
  gap: 16px;
  flex-wrap: wrap;
}
.site-title {
  font-size: 1.45rem;
  font-weight: bold;
  letter-spacing: .03em;
  color: #f5deb3;
}
.site-title a { color: inherit; }
.site-subtitle {
  font-size: .85rem;
  color: #c8a96e;
  font-style: italic;
}

/* ── nav ── */
nav {
  background: var(--accent);
  border-bottom: 2px solid var(--border);
}
.nav-inner {
  max-width: var(--max);
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  gap: 0;
  flex-wrap: wrap;
}
nav a {
  color: #f5deb3;
  padding: 10px 16px;
  font-size: .9rem;
  display: inline-block;
  border-right: 1px solid rgba(255,255,255,.15);
  letter-spacing: .02em;
}
nav a:hover, nav a.active {
  background: var(--accent2);
  text-decoration: none;
  color: #fff;
}

/* ── main ── */
main {
  max-width: var(--max);
  margin: 0 auto;
  padding: 32px 24px 64px;
}

h1 { font-size: 1.8rem; color: var(--accent2); margin-bottom: 6px; }
h2 { font-size: 1.3rem; color: var(--accent); margin: 24px 0 12px; }
h3 { font-size: 1.05rem; color: var(--accent2); margin: 16px 0 6px; }

p { margin-bottom: .9em; }
p:last-child { margin-bottom: 0; }

.page-intro {
  color: var(--muted);
  font-style: italic;
  margin-bottom: 24px;
  font-size: .95rem;
  border-left: 3px solid var(--border);
  padding-left: 12px;
}

/* ── search / filter bar ── */
.search-bar {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
  flex-wrap: wrap;
  align-items: center;
}
.search-bar input, .search-bar select {
  padding: 8px 12px;
  border: 1px solid var(--border);
  border-radius: var(--radius);
  background: var(--card-bg);
  color: var(--ink);
  font-size: .9rem;
  font-family: inherit;
}
.search-bar input { flex: 1; min-width: 200px; }
.count-label { font-size: .85rem; color: var(--muted); margin-left: auto; }

/* ── cards / grid ── */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 18px;
}
.card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 18px 20px;
  box-shadow: 0 2px 6px var(--shadow);
  display: flex;
  flex-direction: column;
  gap: 8px;
  cursor: pointer;
  transition: box-shadow .15s, border-color .15s;
}
.card:hover { box-shadow: 0 4px 14px var(--shadow); border-color: var(--accent); }
.card-title { font-size: 1.05rem; font-weight: bold; color: var(--accent2); }
.card-meta { font-size: .8rem; color: var(--muted); }
.card-body { font-size: .88rem; line-height: 1.55; }
.tag {
  display: inline-block;
  background: var(--cream);
  border: 1px solid var(--border);
  border-radius: 3px;
  padding: 1px 7px;
  font-size: .75rem;
  color: var(--accent);
  margin: 1px 2px 1px 0;
}
.badge {
  display: inline-block;
  background: var(--accent);
  color: #fff;
  border-radius: 3px;
  padding: 1px 8px;
  font-size: .73rem;
  letter-spacing: .04em;
  font-variant: small-caps;
}
.badge.sceptic { background: #3a6e3a; }
.badge.advocate { background: #8b2000; }
.badge.systematizer { background: #1a4a7a; }

/* ── detail modal / overlay ── */
#overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,.55);
  z-index: 100;
  overflow-y: auto;
  padding: 40px 16px;
}
#overlay.open { display: block; }
.detail-box {
  background: var(--card-bg);
  border: 2px solid var(--border);
  border-radius: var(--radius);
  max-width: 740px;
  margin: 0 auto;
  padding: 32px 36px;
  position: relative;
  box-shadow: 0 8px 32px rgba(0,0,0,.35);
}
.detail-close {
  position: absolute;
  top: 14px;
  right: 18px;
  font-size: 1.4rem;
  cursor: pointer;
  color: var(--muted);
  line-height: 1;
  background: none;
  border: none;
}
.detail-close:hover { color: var(--accent); }
.detail-title { font-size: 1.4rem; color: var(--accent2); margin-bottom: 4px; }
.detail-meta { color: var(--muted); font-size: .85rem; margin-bottom: 16px; }
.detail-section { margin-top: 16px; }
.detail-section h4 { font-size: .9rem; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin-bottom: 6px; border-bottom: 1px solid var(--border); padding-bottom: 3px; }
.detail-section p { font-size: .9rem; }
.detail-section ul { font-size: .88rem; padding-left: 20px; }
.detail-section li { margin-bottom: 4px; }
.source-note { font-size: .78rem; color: var(--muted); font-style: italic; margin-top: 16px; border-top: 1px solid var(--border); padding-top: 10px; }
.confidence-HIGH { color: #2a7a2a; font-weight: bold; }
.confidence-MEDIUM { color: #8a6000; font-weight: bold; }
.confidence-LOW { color: #9a2000; font-weight: bold; }

/* ── timeline ── */
.timeline-list { position: relative; padding-left: 0; list-style: none; }
.timeline-list::before {
  content: "";
  position: absolute;
  left: 80px;
  top: 0; bottom: 0;
  width: 2px;
  background: var(--border);
}
.tl-item {
  display: flex;
  gap: 0;
  margin-bottom: 20px;
  position: relative;
}
.tl-year {
  width: 80px;
  min-width: 80px;
  text-align: right;
  padding-right: 18px;
  font-size: .85rem;
  font-weight: bold;
  color: var(--accent);
  padding-top: 4px;
}
.tl-dot {
  width: 12px;
  min-width: 12px;
  height: 12px;
  border-radius: 50%;
  background: var(--accent);
  border: 2px solid var(--parchment);
  margin-top: 6px;
  flex-shrink: 0;
  position: relative;
  z-index: 1;
}
.tl-dot.trial_event { background: #8b2000; }
.tl-dot.primary_source_publication { background: #1a4a7a; }
.tl-dot.institutional_event { background: #5a4000; }
.tl-dot.political_event { background: #3a6e3a; }
.tl-dot.biographical { background: #7a7a7a; }
.tl-content {
  padding-left: 18px;
  flex: 1;
  cursor: pointer;
}
.tl-name { font-size: .95rem; font-weight: bold; color: var(--accent2); }
.tl-name:hover { color: var(--accent); text-decoration: underline; }
.tl-loc { font-size: .8rem; color: var(--muted); }
.tl-sig { font-size: .85rem; margin-top: 4px; }
.tl-legend { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 24px; font-size: .82rem; }
.tl-legend-item { display: flex; align-items: center; gap: 6px; }
.tl-legend-dot { width: 10px; height: 10px; border-radius: 50%; }

/* ── map placeholder ── */
.map-container { background: var(--cream); border: 2px dashed var(--border); border-radius: var(--radius); padding: 60px 24px; text-align: center; color: var(--muted); font-style: italic; margin-bottom: 32px; }

/* ── stats bar ── */
.stats-grid { display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 32px; }
.stat-box { background: var(--card-bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 16px 24px; text-align: center; flex: 1; min-width: 130px; }
.stat-num { font-size: 2rem; font-weight: bold; color: var(--accent); display: block; }
.stat-lbl { font-size: .8rem; color: var(--muted); text-transform: uppercase; letter-spacing: .05em; }

/* ── footer ── */
footer { background: var(--accent2); color: #c8a96e; text-align: center; padding: 18px; font-size: .8rem; border-top: 2px solid var(--border); margin-top: 40px; }

/* responsive */
@media (max-width: 600px) {
  .card-grid { grid-template-columns: 1fr; }
  .detail-box { padding: 20px 16px; }
  .tl-list::before { left: 60px; }
  .tl-year { width: 60px; }
}
"""

# ── nav helper ────────────────────────────────────────────────────────────────

def nav_html(active: str) -> str:
    pages = [
        ("index.html",    "Home"),
        ("trials.html",   "Trials"),
        ("scholars.html", "Scholars"),
        ("concepts.html", "Concepts"),
        ("timeline.html", "Timeline"),
        ("sources.html",  "Sources"),
        ("about.html",    "About"),
    ]
    links = ""
    for href, label in pages:
        cls = ' class="active"' if href == active else ""
        links += f'<a href="{href}"{cls}>{label}</a>'
    return f"""
<header>
  <div class="header-inner">
    <span class="site-title"><a href="index.html">WitchcraftStudiesDB</a></span>
    <span class="site-subtitle">A digital humanities knowledge portal for the history of European witch trials</span>
  </div>
</header>
<nav><div class="nav-inner">{links}</div></nav>
"""

def page_wrap(title: str, active: str, body: str, extra_js: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} — WitchcraftStudiesDB</title>
<style>{CSS}</style>
</head>
<body>
{nav_html(active)}
<main>
{body}
</main>
<footer>WitchcraftStudiesDB &mdash; Digital humanities project &mdash; Data licensed CC BY 4.0</footer>
<div id="overlay"><div class="detail-box"><button class="detail-close" onclick="closeDetail()">&#x2715;</button><div id="detail-content"></div></div></div>
<script>
function closeDetail() {{
  document.getElementById('overlay').classList.remove('open');
}}
document.getElementById('overlay').addEventListener('click', function(e) {{
  if (e.target === this) closeDetail();
}});
document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') closeDetail();
}});
function showDetail(html) {{
  document.getElementById('detail-content').innerHTML = html;
  document.getElementById('overlay').classList.add('open');
  document.getElementById('overlay').scrollTop = 0;
}}
{extra_js}
</script>
</body>
</html>"""

# ── index.html ────────────────────────────────────────────────────────────────

def build_index(data: dict) -> str:
    n_trials    = len(data["trial_events"])
    n_scholars  = len(data["scholars"])
    n_concepts  = len(data["concepts"])
    n_timeline  = len(data["timeline"])
    n_sources   = len(data["scholarly_texts"])
    n_accused   = len(data["accused_persons"])

    featured_trials = data["trial_events"][:3]
    featured_cards  = ""
    for t in featured_trials:
        name = escape(t.get("name", t.get("id", "")))
        loc  = escape(t.get("location_id", ""))
        yr   = t.get("year_start", "")
        ex   = t.get("executed_count", "?")
        summ = escape((t.get("summary") or "")[:200] + "…")
        featured_cards += f"""
<div class="card">
  <div class="card-title">{name}</div>
  <div class="card-meta">{loc} &middot; {yr} &middot; ~{ex} executed</div>
  <div class="card-body">{summ}</div>
</div>"""

    body = f"""
<h1>WitchcraftStudiesDB</h1>
<p class="page-intro">A relational knowledge portal for the history of European and transatlantic witch trials, 1428–1692. Built on three scholarly traditions: Stuart Clark (intellectual history), Ronald Hutton (social history), and Carlo Ginzburg (microhistory).</p>

<div class="stats-grid">
  <div class="stat-box"><span class="stat-num">{n_trials}</span><span class="stat-lbl">Trial Events</span></div>
  <div class="stat-box"><span class="stat-num">{n_accused}</span><span class="stat-lbl">Accused Persons</span></div>
  <div class="stat-box"><span class="stat-num">{n_scholars}</span><span class="stat-lbl">Scholars</span></div>
  <div class="stat-box"><span class="stat-num">{n_concepts}</span><span class="stat-lbl">Concepts</span></div>
  <div class="stat-box"><span class="stat-num">{n_timeline}</span><span class="stat-lbl">Timeline Events</span></div>
  <div class="stat-box"><span class="stat-num">{n_sources}</span><span class="stat-lbl">Scholarly Texts</span></div>
</div>

<h2>Featured Trial Events</h2>
<div class="card-grid">{featured_cards}</div>

<h2>About the Database</h2>
<p>WitchcraftStudiesDB integrates three scholarly frameworks for the history of witchcraft persecution. Entries are sourced directly from primary documents and peer-reviewed secondary literature. Every claim carries provenance: a named source, confidence level, and statement of scholarly disagreement where it exists.</p>
<p>Navigate using the menu above. Use <a href="timeline.html">Timeline</a> for chronological overview, <a href="trials.html">Trials</a> for individual prosecutions, <a href="scholars.html">Scholars</a> for intellectual figures, and <a href="concepts.html">Concepts</a> for analytical categories.</p>
<p><a href="about.html">Read more about the project methodology &rarr;</a></p>
"""
    return page_wrap("Home", "index.html", body)

# ── trials.html ───────────────────────────────────────────────────────────────

def build_trials(data: dict) -> str:
    trials_js = js_embed("TRIALS", data["trial_events"])
    js = trials_js + """
function trunc(s, n) { return s && s.length > n ? s.slice(0,n)+'…' : (s||''); }
function renderTrials(list) {
  const el = document.getElementById('trial-list');
  const cnt = document.getElementById('trial-count');
  cnt.textContent = list.length + ' result' + (list.length===1?'':'s');
  if (!list.length) { el.innerHTML='<p style="color:var(--muted)">No results.</p>'; return; }
  el.innerHTML = list.map(t => {
    const name = t.name || t.id;
    const loc  = t.location_id || '';
    const yr   = t.year_start || '';
    const ex   = t.executed_count != null ? '~'+t.executed_count+' executed' : '';
    const acc  = t.alleged_accused_count != null ? '~'+t.alleged_accused_count+' accused' : '';
    const summ = trunc(t.summary, 220);
    return `<div class="card" onclick="showTrialDetail(${JSON.stringify(t.id)})">
      <div class="card-title">${name}</div>
      <div class="card-meta">${[loc,yr,ex,acc].filter(Boolean).join(' &middot; ')}</div>
      <div class="card-body">${summ}</div>
    </div>`;
  }).join('');
}
function showTrialDetail(id) {
  const t = TRIALS.find(x=>x.id===id);
  if (!t) return;
  const sections = [];
  if (t.summary) sections.push(`<div class="detail-section"><h4>Summary</h4><p>${t.summary}</p></div>`);
  if (t.historiographical_significance) sections.push(`<div class="detail-section"><h4>Historiographical Significance</h4><p>${t.historiographical_significance}</p></div>`);
  if (t.demonological_framework) sections.push(`<div class="detail-section"><h4>Demonological Framework</h4><p>${t.demonological_framework}</p></div>`);
  if (t.scholarly_disagreement) sections.push(`<div class="detail-section"><h4>Scholarly Disagreement</h4><p>${t.scholarly_disagreement}</p></div>`);
  if (t.accused_persons && t.accused_persons.length) sections.push(`<div class="detail-section"><h4>Accused Persons</h4><ul>${t.accused_persons.map(p=>`<li>${p}</li>`).join('')}</ul></div>`);
  const src = t.source_method ? `<div class="source-note">Source: ${t.source_method} &mdash; Confidence: <span class="confidence-${t.confidence}">${t.confidence||''}</span></div>` : '';
  showDetail(`<div class="detail-title">${t.name||t.id}</div>
    <div class="detail-meta">${[t.location_id, t.year_start, t.year_end ? '–'+t.year_end : ''].filter(Boolean).join(' ')}</div>
    ${sections.join('')}${src}`);
}
function filterTrials() {
  const q = document.getElementById('search').value.toLowerCase();
  renderTrials(TRIALS.filter(t => {
    const blob = [t.name,t.location_id,t.summary,t.regional_context].join(' ').toLowerCase();
    return blob.includes(q);
  }));
}
document.addEventListener('DOMContentLoaded', function() {
  renderTrials(TRIALS);
  document.getElementById('search').addEventListener('input', filterTrials);
});
"""
    body = """
<h1>Trial Events</h1>
<p class="page-intro">Major witch prosecution events, cross-referenced with accused persons, locations, and demonological concepts.</p>
<div class="search-bar">
  <input id="search" type="search" placeholder="Search trials by name, location, summary…">
  <span class="count-label" id="trial-count"></span>
</div>
<div class="card-grid" id="trial-list"></div>
"""
    return page_wrap("Trials", "trials.html", body, js)

# ── scholars.html ─────────────────────────────────────────────────────────────

def build_scholars(data: dict) -> str:
    scholars_js = js_embed("SCHOLARS", data["scholars"])
    js = scholars_js + """
function trunc(s, n) { return s && s.length > n ? s.slice(0,n)+'…' : (s||''); }
function positionBadge(pos) {
  if (!pos) return '';
  const cls = pos.includes('SCEPTIC') ? 'sceptic' : pos.includes('ADVOCATE') ? 'advocate' : 'systematizer';
  return `<span class="badge ${cls}">${pos}</span>`;
}
function renderScholars(list) {
  const el  = document.getElementById('scholar-list');
  const cnt = document.getElementById('scholar-count');
  cnt.textContent = list.length + ' result' + (list.length===1?'':'s');
  if (!list.length) { el.innerHTML='<p style="color:var(--muted)">No results.</p>'; return; }
  el.innerHTML = list.map(s => {
    const name  = s.name || s.id;
    const dates = [s.birth_year, s.death_year].filter(Boolean).join('–');
    const disc  = s.academic_discipline || '';
    const inst  = s.primary_institution || '';
    const pos   = positionBadge(s.historiographical_position);
    const core  = trunc(s.core_argument, 200);
    return `<div class="card" onclick="showScholarDetail(${JSON.stringify(s.id)})">
      <div class="card-title">${name} ${pos}</div>
      <div class="card-meta">${[dates, disc].filter(Boolean).join(' &middot; ')}</div>
      ${inst ? `<div class="card-meta">${inst}</div>` : ''}
      <div class="card-body">${core}</div>
    </div>`;
  }).join('');
}
function showScholarDetail(id) {
  const s = SCHOLARS.find(x=>x.id===id);
  if (!s) return;
  const sections = [];
  if (s.core_argument) sections.push(`<div class="detail-section"><h4>Core Argument</h4><p>${s.core_argument}</p></div>`);
  if (s.major_works && s.major_works.length) {
    const wks = s.major_works.map(w=>`<li><em>${w.title}</em> (${w.year||'n.d.'}) — ${w.significance||''}</li>`).join('');
    sections.push(`<div class="detail-section"><h4>Major Works</h4><ul>${wks}</ul></div>`);
  }
  if (s.historiographical_significance) sections.push(`<div class="detail-section"><h4>Historiographical Significance</h4><p>${s.historiographical_significance}</p></div>`);
  if (s.scholarly_disagreement) sections.push(`<div class="detail-section"><h4>Scholarly Disagreement</h4><p>${s.scholarly_disagreement}</p></div>`);
  if (s.scholarly_relationships) {
    const a = (s.scholarly_relationships.alignment_with||[]).map(x=>`<li>${x}</li>`).join('');
    const c = (s.scholarly_relationships.creative_tension_with||[]).map(x=>`<li>${x}</li>`).join('');
    if (a) sections.push(`<div class="detail-section"><h4>Alignment With</h4><ul>${a}</ul></div>`);
    if (c) sections.push(`<div class="detail-section"><h4>Creative Tension With</h4><ul>${c}</ul></div>`);
  }
  const src = s.source_method ? `<div class="source-note">Source: ${s.source_method} &mdash; Confidence: <span class="confidence-${s.confidence}">${s.confidence||''}</span></div>` : '';
  const dates = [s.birth_year, s.death_year].filter(Boolean).join('–');
  showDetail(`<div class="detail-title">${s.name||s.id}</div>
    <div class="detail-meta">${[dates, s.birth_place, s.academic_discipline].filter(Boolean).join(' &middot; ')}</div>
    ${sections.join('')}${src}`);
}
function filterScholars() {
  const q   = document.getElementById('search').value.toLowerCase();
  const cat = document.getElementById('filter-pos').value;
  renderScholars(SCHOLARS.filter(s => {
    const pos = s.historiographical_position || '';
    const blob = [s.name, s.academic_discipline, s.primary_institution, s.core_argument, pos].join(' ').toLowerCase();
    const matchQ   = !q   || blob.includes(q);
    const matchCat = !cat || pos.includes(cat);
    return matchQ && matchCat;
  }));
}
document.addEventListener('DOMContentLoaded', function() {
  renderScholars(SCHOLARS);
  document.getElementById('search').addEventListener('input', filterScholars);
  document.getElementById('filter-pos').addEventListener('change', filterScholars);
});
"""
    body = """
<h1>Scholars &amp; Demonologists</h1>
<p class="page-intro">Historical demonological authorities and modern historians whose work shapes the database's analytical framework.</p>
<div class="search-bar">
  <input id="search" type="search" placeholder="Search by name, discipline, institution…">
  <select id="filter-pos">
    <option value="">All positions</option>
    <option value="SCEPTIC">Sceptics</option>
    <option value="ADVOCATE">Witch-trial advocates</option>
    <option value="SYSTEMATIZER">Systematizers</option>
    <option value="PROCEDURAL">Procedural reformers</option>
  </select>
  <span class="count-label" id="scholar-count"></span>
</div>
<div class="card-grid" id="scholar-list"></div>
"""
    return page_wrap("Scholars", "scholars.html", body, js)

# ── concepts.html ─────────────────────────────────────────────────────────────

def build_concepts(data: dict) -> str:
    concepts_js = js_embed("CONCEPTS", data["concepts"])
    js = concepts_js + """
function trunc(s, n) { return s && s.length > n ? s.slice(0,n)+'…' : (s||''); }
function renderConcepts(list) {
  const el  = document.getElementById('concept-list');
  const cnt = document.getElementById('concept-count');
  cnt.textContent = list.length + ' result' + (list.length===1?'':'s');
  if (!list.length) { el.innerHTML='<p style="color:var(--muted)">No results.</p>'; return; }
  el.innerHTML = list.map(c => {
    const name = c.name || c.id;
    const cat  = c.category_type || '';
    const tp   = c.time_period || '';
    const def  = trunc(c.scholarly_definition, 220);
    return `<div class="card" onclick="showConceptDetail(${JSON.stringify(c.id)})">
      <div class="card-title">${name}</div>
      <div class="card-meta">${[cat ? '<span class="tag">'+cat+'</span>' : '', tp].filter(Boolean).join(' ')}</div>
      <div class="card-body">${def}</div>
    </div>`;
  }).join('');
}
function showConceptDetail(id) {
  const c = CONCEPTS.find(x=>x.id===id);
  if (!c) return;
  const sections = [];
  if (c.scholarly_definition) sections.push(`<div class="detail-section"><h4>Scholarly Definition</h4><p>${c.scholarly_definition}</p></div>`);
  if (c.clark_intellectual_analysis) sections.push(`<div class="detail-section"><h4>Clark: Intellectual Analysis</h4><p>${c.clark_intellectual_analysis}</p></div>`);
  if (c.hutton_social_analysis) sections.push(`<div class="detail-section"><h4>Hutton: Social Analysis</h4><p>${c.hutton_social_analysis}</p></div>`);
  if (c.ginzburg_interrogation_analysis) sections.push(`<div class="detail-section"><h4>Ginzburg: Interrogation Analysis</h4><p>${c.ginzburg_interrogation_analysis}</p></div>`);
  if (c.historiographical_significance) sections.push(`<div class="detail-section"><h4>Historiographical Significance</h4><p>${c.historiographical_significance}</p></div>`);
  if (c.scholarly_disagreement) sections.push(`<div class="detail-section"><h4>Scholarly Disagreement</h4><p>${c.scholarly_disagreement}</p></div>`);
  const src = c.source_method ? `<div class="source-note">Source: ${c.source_method} &mdash; Confidence: <span class="confidence-${c.confidence}">${c.confidence||''}</span></div>` : '';
  showDetail(`<div class="detail-title">${c.name||c.id}</div>
    <div class="detail-meta">${[c.category_type, c.time_period, c.primary_locale].filter(Boolean).join(' &middot; ')}</div>
    ${sections.join('')}${src}`);
}
function filterConcepts() {
  const q   = document.getElementById('search').value.toLowerCase();
  const cat = document.getElementById('filter-cat').value;
  renderConcepts(CONCEPTS.filter(c => {
    const blob = [c.name, c.scholarly_definition, c.clark_intellectual_analysis].join(' ').toLowerCase();
    const matchQ   = !q   || blob.includes(q);
    const matchCat = !cat || (c.category_type||'') === cat;
    return matchQ && matchCat;
  }));
}
document.addEventListener('DOMContentLoaded', function() {
  renderConcepts(CONCEPTS);
  document.getElementById('search').addEventListener('input', filterConcepts);
  document.getElementById('filter-cat').addEventListener('change', filterConcepts);
});
"""
    body = """
<h1>Demonological Concepts</h1>
<p class="page-intro">Analytical categories and actor terms drawn from the demonological tradition and modern historical scholarship.</p>
<div class="search-bar">
  <input id="search" type="search" placeholder="Search concepts…">
  <select id="filter-cat">
    <option value="">All types</option>
    <option value="ACTOR_TERM">Actor Terms (contemporary)</option>
    <option value="ANALYST_TERM">Analyst Terms (modern scholarly)</option>
  </select>
  <span class="count-label" id="concept-count"></span>
</div>
<div class="card-grid" id="concept-list"></div>
"""
    return page_wrap("Concepts", "concepts.html", body, js)

# ── timeline.html ─────────────────────────────────────────────────────────────

def build_timeline(data: dict) -> str:
    # Sort timeline by date
    events = sorted(data["timeline"], key=lambda e: int(e.get("date", "0") or 0))
    tl_js = js_embed("TIMELINE", events)
    js = tl_js + """
const TYPE_LABELS = {
  trial_event:                 'Trial',
  primary_source_publication:  'Publication',
  institutional_event:         'Institutional',
  political_event:             'Political',
  biographical:                'Biographical',
};
function renderTimeline(list) {
  const el  = document.getElementById('tl-list');
  const cnt = document.getElementById('tl-count');
  cnt.textContent = list.length + ' events';
  if (!list.length) { el.innerHTML='<li style="color:var(--muted);padding:20px 0 0 100px">No results.</li>'; return; }
  el.innerHTML = list.map(e => {
    const yr   = e.date || '?';
    const type = e.event_type || '';
    const sig  = e.significance ? e.significance.slice(0, 180) + (e.significance.length>180?'…':'') : '';
    return `<li class="tl-item">
      <span class="tl-year">${yr}</span>
      <span class="tl-dot ${type}"></span>
      <span class="tl-content" onclick="showTLDetail(${JSON.stringify(e.id)})">
        <span class="tl-name">${e.event_name||e.id}</span>
        ${e.location ? `<span class="tl-loc"> &middot; ${e.location}</span>` : ''}
        ${sig ? `<div class="tl-sig">${sig}</div>` : ''}
      </span>
    </li>`;
  }).join('');
}
function showTLDetail(id) {
  const e = TIMELINE.find(x=>x.id===id);
  if (!e) return;
  const sections = [];
  if (e.significance) sections.push(`<div class="detail-section"><h4>Significance</h4><p>${e.significance}</p></div>`);
  if (e.related_entities && e.related_entities.length) {
    sections.push(`<div class="detail-section"><h4>Related Entities</h4><ul>${e.related_entities.map(r=>`<li>${r}</li>`).join('')}</ul></div>`);
  }
  const src = e.source_method ? `<div class="source-note">Source: ${e.source_method} &mdash; Confidence: <span class="confidence-${e.confidence}">${e.confidence||''}</span></div>` : '';
  showDetail(`<div class="detail-title">${e.event_name||e.id}</div>
    <div class="detail-meta">${[e.date, e.location, TYPE_LABELS[e.event_type]||e.event_type].filter(Boolean).join(' &middot; ')}</div>
    ${sections.join('')}${src}`);
}
function filterTimeline() {
  const q    = document.getElementById('search').value.toLowerCase();
  const type = document.getElementById('filter-type').value;
  renderTimeline(TIMELINE.filter(e => {
    const blob = [e.event_name, e.location, e.significance].join(' ').toLowerCase();
    const matchQ = !q || blob.includes(q);
    const matchT = !type || e.event_type === type;
    return matchQ && matchT;
  }));
}
document.addEventListener('DOMContentLoaded', function() {
  renderTimeline(TIMELINE);
  document.getElementById('search').addEventListener('input', filterTimeline);
  document.getElementById('filter-type').addEventListener('change', filterTimeline);
});
"""
    legend_items = [
        ("trial_event",                "#8b2000", "Trial"),
        ("primary_source_publication", "#1a4a7a", "Publication"),
        ("institutional_event",        "#5a4000", "Institutional"),
        ("political_event",            "#3a6e3a", "Political"),
        ("biographical",               "#7a7a7a", "Biographical"),
    ]
    legend = "".join(
        f'<span class="tl-legend-item"><span class="tl-legend-dot" style="background:{col}"></span>{lbl}</span>'
        for _, col, lbl in legend_items
    )
    body = f"""
<h1>Timeline</h1>
<p class="page-intro">Chronological overview of publications, trials, and institutional events from 1428 to 1692.</p>
<div class="tl-legend">{legend}</div>
<div class="search-bar">
  <input id="search" type="search" placeholder="Search timeline…">
  <select id="filter-type">
    <option value="">All event types</option>
    <option value="trial_event">Trials</option>
    <option value="primary_source_publication">Publications</option>
    <option value="institutional_event">Institutional</option>
    <option value="political_event">Political</option>
    <option value="biographical">Biographical</option>
  </select>
  <span class="count-label" id="tl-count"></span>
</div>
<ul class="timeline-list" id="tl-list"></ul>
"""
    return page_wrap("Timeline", "timeline.html", body, js)

# ── sources.html ──────────────────────────────────────────────────────────────

def build_sources(data: dict) -> str:
    texts_js = js_embed("TEXTS", data["scholarly_texts"])
    js = texts_js + """
function trunc(s, n) { return s && s.length > n ? s.slice(0,n)+'…' : (s||''); }
function renderTexts(list) {
  const el  = document.getElementById('text-list');
  const cnt = document.getElementById('text-count');
  cnt.textContent = list.length + ' result' + (list.length===1?'':'s');
  if (!list.length) { el.innerHTML='<p style="color:var(--muted)">No results.</p>'; return; }
  el.innerHTML = list.map(t => {
    const title  = t.title || t.id;
    const author = t.author || '';
    const yr     = t.year_published || t.original_year || '';
    const type   = t.text_type || '';
    const summ   = trunc(t.summary, 200);
    return `<div class="card" onclick="showTextDetail(${JSON.stringify(t.id)})">
      <div class="card-title">${title}</div>
      <div class="card-meta">${[author, yr, '<span class="tag">'+type+'</span>'].filter(x=>x&&x!=='<span class="tag"></span>').join(' &middot; ')}</div>
      <div class="card-body">${summ}</div>
    </div>`;
  }).join('');
}
function showTextDetail(id) {
  const t = TEXTS.find(x=>x.id===id);
  if (!t) return;
  const sections = [];
  if (t.subject_focus) sections.push(`<div class="detail-section"><h4>Subject Focus</h4><p>${t.subject_focus}</p></div>`);
  if (t.summary) sections.push(`<div class="detail-section"><h4>Summary</h4><p>${t.summary}</p></div>`);
  if (t.scholarly_significance) sections.push(`<div class="detail-section"><h4>Scholarly Significance</h4><p>${t.scholarly_significance}</p></div>`);
  if (t.key_arguments && t.key_arguments.length) {
    const args = t.key_arguments.map(a=>`<li><strong>${a.concept}</strong>: ${a.claim}</li>`).join('');
    sections.push(`<div class="detail-section"><h4>Key Arguments</h4><ul>${args}</ul></div>`);
  }
  if (t.scholarly_disagreement) sections.push(`<div class="detail-section"><h4>Scholarly Disagreement</h4><p>${t.scholarly_disagreement}</p></div>`);
  const src = t.source_method ? `<div class="source-note">Source: ${t.source_method} &mdash; Confidence: <span class="confidence-${t.confidence}">${t.confidence||''}</span></div>` : '';
  showDetail(`<div class="detail-title">${t.title||t.id}</div>
    <div class="detail-meta">${[t.author, t.year_published, t.publisher, t.text_type].filter(Boolean).join(' &middot; ')}</div>
    ${sections.join('')}${src}`);
}
function filterTexts() {
  const q    = document.getElementById('search').value.toLowerCase();
  const type = document.getElementById('filter-type').value;
  renderTexts(TEXTS.filter(t => {
    const blob = [t.title, t.author, t.summary, t.subject_focus].join(' ').toLowerCase();
    const matchQ = !q || blob.includes(q);
    const matchT = !type || t.text_type === type;
    return matchQ && matchT;
  }));
}
document.addEventListener('DOMContentLoaded', function() {
  renderTexts(TEXTS);
  document.getElementById('search').addEventListener('input', filterTexts);
  document.getElementById('filter-type').addEventListener('change', filterTexts);
});
"""
    body = """
<h1>Scholarly Texts &amp; Primary Sources</h1>
<p class="page-intro">Academic monographs, edited volumes, and demonological primary sources that underpin the database's analysis.</p>
<div class="search-bar">
  <input id="search" type="search" placeholder="Search texts by title, author, content…">
  <select id="filter-type">
    <option value="">All types</option>
    <option value="monograph">Monographs</option>
    <option value="edited_volume">Edited Volumes</option>
    <option value="primary_source">Primary Sources</option>
    <option value="primary_source_edition">Primary Source Editions</option>
  </select>
  <span class="count-label" id="text-count"></span>
</div>
<div class="card-grid" id="text-list"></div>
"""
    return page_wrap("Sources", "sources.html", body, js)

# ── about.html ────────────────────────────────────────────────────────────────

def build_about(data: dict) -> str:
    body = """
<h1>About WitchcraftStudiesDB</h1>
<p class="page-intro">Methodology, scope, and scholarly framework for this digital humanities knowledge portal.</p>

<h2>Project Scope</h2>
<p>WitchcraftStudiesDB is a relational knowledge database for the history of European and transatlantic witch trials, covering the period c.1428–1692. It integrates structured data about trial events, accused persons, demonological concepts, intellectual authorities, and primary sources into a searchable, cross-referenced portal.</p>
<p>The database draws on three complementary scholarly traditions and applies their methodologies consistently across all entries:</p>

<h2>Three Scholarly Frameworks</h2>

<div class="card-grid">
  <div class="card">
    <div class="card-title">Stuart Clark — Intellectual History</div>
    <div class="card-meta"><em>Thinking with Demons</em> (1997)</div>
    <div class="card-body">Demonology as coherent theological and natural-philosophical tradition. Witch prosecution as intellectually serious — applying scholastic causation theory, not irrational superstition. The database treats demonological concepts with the same analytical seriousness Clark argues the demonologists themselves applied.</div>
  </div>
  <div class="card">
    <div class="card-title">Ronald Hutton — Social History</div>
    <div class="card-meta"><em>The Witch</em> (2017)</div>
    <div class="card-body">Cunning folk as legitimate practitioners whose community role was distinct from the accused witch. Demographic and regional analysis of trial victims. The 'refusal-quarrel-misfortune' sequence as the social mechanism of accusation. Gender and occupation as structural vulnerability factors.</div>
  </div>
  <div class="card">
    <div class="card-title">Carlo Ginzburg — Microhistory</div>
    <div class="card-meta"><em>Night Battles</em> (1983), <em>Ecstasies</em> (1991)</div>
    <div class="card-body">Interrogation analysis and torture-shaped confession. Recovery of subaltern voices and indigenous folk beliefs from beneath the demonological overlay. The benandanti case as model for distinguishing what practitioners believed from what prosecutors alleged against them.</div>
  </div>
</div>

<h2>Eight Working Principles</h2>
<ol style="padding-left:22px;line-height:2">
  <li><strong>Provenance on every claim</strong> — named source, not just confidence level</li>
  <li><strong>Rationality within framework</strong> — accusers and accused acted within coherent belief systems</li>
  <li><strong>Actor/Analyst distinction</strong> — contemporary terms in quotation marks; modern scholarly categories identified as such</li>
  <li><strong>Regional variation as primary</strong> — no monolithic "witch hunt"; context is always specific</li>
  <li><strong>Microhistorical attention to individuals</strong> — structural analysis must not erase personal specificity</li>
  <li><strong>Material grounding</strong> — what people actually did, not only what was alleged</li>
  <li><strong>Intellectual history taken seriously</strong> — demonological theory is theology, not superstition</li>
  <li><strong>Ambiguity preserved</strong> — historiographical disagreement stated explicitly, with named scholars</li>
</ol>

<h2>Data Format</h2>
<p>All database entries are stored as structured JSON files in a versioned git repository. Cross-references use slug-based IDs throughout — no UUIDs, no numeric foreign keys. Every entry carries provenance fields: <code>source_method</code>, <code>confidence</code> (HIGH/MEDIUM/LOW), <code>review_status</code> (DRAFT/REVIEWED/VERIFIED), and <code>scholarly_disagreement</code> naming the historians on each side of contested questions.</p>

<h2>Confidence Levels</h2>
<ul style="padding-left:22px;line-height:1.8">
  <li><strong class="confidence-HIGH">HIGH</strong> — Archival or published primary source; secure scholarly consensus</li>
  <li><strong class="confidence-MEDIUM">MEDIUM</strong> — Scholarly reconstruction from fragmentary evidence; inference required</li>
  <li><strong class="confidence-LOW">LOW</strong> — Named in one source only; no independent corroboration; identity uncertain</li>
</ul>

<h2>Current Phase</h2>
<p>Phase 2: Academic Corpus Ingestion. The PDF extraction pipeline is complete and Stuart Clark's <em>Thinking with Demons</em> (47,942 lines of Markdown) is the primary source for the current batch of entries. Ginzburg, Hutton, and the Ankarloo/Clark volumes are queued for ingestion.</p>
"""
    return page_wrap("About", "about.html", body)

# ── main ──────────────────────────────────────────────────────────────────────

def main():
    print("Loading data…")
    data = {
        "trial_events":    load_dir("trial_event"),
        "accused_persons": load_dir("accused_person"),
        "concepts":        load_dir("demonological_concept"),
        "scholars":        load_dir("demonological_scholar"),
        "scholarly_texts": load_dir("scholarly_text"),
        "locations":       load_dir("location"),
        "timeline":        load_dir("timeline"),
        "persecuted_groups": load_dir("persecuted_group"),
        "inquisitorial_bodies": load_dir("inquisitorial_body"),
    }

    for k, v in data.items():
        print(f"  {k}: {len(v)} entries")

    WEB.mkdir(exist_ok=True)

    pages = {
        "index.html":    build_index(data),
        "trials.html":   build_trials(data),
        "scholars.html": build_scholars(data),
        "concepts.html": build_concepts(data),
        "timeline.html": build_timeline(data),
        "sources.html":  build_sources(data),
        "about.html":    build_about(data),
    }

    for fname, html in pages.items():
        path = WEB / fname
        path.write_text(html, encoding="utf-8")
        print(f"  wrote {path}  ({len(html):,} bytes)")

    print(f"\nDone. Open {WEB}/index.html")

if __name__ == "__main__":
    main()
