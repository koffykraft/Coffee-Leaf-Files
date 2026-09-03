#!/usr/bin/env python3
from __future__ import annotations

import collections
import html
import json
import os
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "audit-output"
OUT.mkdir(exist_ok=True)

EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "javascript", "data"}
STALE_PATTERNS = {
    "all six doors": re.compile(r"all\s+six\s+doors", re.I),
    "six doors": re.compile(r"\bsix\s+doors\b", re.I),
    "all eight doors": re.compile(r"all\s+eight\s+doors", re.I),
    "old contact email": re.compile(r"hello@koffykraft\.com", re.I),
    "legacy Netlify function": re.compile(r"/\.netlify/functions/", re.I),
    "Netlify reference": re.compile(r"\bnetlify\b", re.I),
}

CANONICAL_ENTRY = {
    "engere": "engere-intro.html",
    "kuti": "kuti-intro.html",
    "chemo": "chemo-intro.html",
    "kawa-daun": "kawa-daun-intro.html",
    "sensory": "buna-sensory-school.html",
    "culinary": "buna-culinary.html",
    "vocab": "vocab/index.html",
    "biology": "coffee-leaf-human-biology.html",
    "processing": "citane-process-compass.html",
    "tools": "citane-terrain-map.html",
}

HIGH_LEVEL = {"index.html", "catalogue.html", "begin-with-a-cup.html"}
LEGACY_TRADITION_MIDDLE = {"engere.html", "kuti.html", "chemo.html", "kawa-daun.html"}

@dataclass
class PageInfo:
    path: str
    title: str = ""
    h1: list[str] = field(default_factory=list)
    ids: set[str] = field(default_factory=set)
    hrefs: list[str] = field(default_factory=list)
    scripts: list[str] = field(default_factory=list)
    meta_refresh: list[str] = field(default_factory=list)
    text: str = ""

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hrefs=[]; self.ids=set(); self.scripts=[]; self.meta_refresh=[]
        self.title_parts=[]; self.h1=[]; self.text_parts=[]
        self._in_title=False; self._in_h1=False; self._h1buf=[]
    def handle_starttag(self, tag, attrs):
        d=dict(attrs)
        if "id" in d and d["id"]: self.ids.add(d["id"])
        if tag=="a" and d.get("href") is not None: self.hrefs.append(d["href"].strip())
        if tag=="script" and d.get("src"): self.scripts.append(d["src"].strip())
        if tag=="meta" and (d.get("http-equiv") or "").lower()=="refresh": self.meta_refresh.append(d.get("content", ""))
        if tag=="title": self._in_title=True
        if tag=="h1": self._in_h1=True; self._h1buf=[]
    def handle_endtag(self, tag):
        if tag=="title": self._in_title=False
        if tag=="h1":
            self._in_h1=False
            val=" ".join("".join(self._h1buf).split())
            if val: self.h1.append(val)
    def handle_data(self, data):
        self.text_parts.append(data)
        if self._in_title: self.title_parts.append(data)
        if self._in_h1: self._h1buf.append(data)


def parse_page(p: Path) -> PageInfo:
    raw=p.read_text(encoding="utf-8", errors="replace")
    parser=Parser(); parser.feed(raw)
    return PageInfo(
        path=p.relative_to(ROOT).as_posix(),
        title=" ".join("".join(parser.title_parts).split()),
        h1=parser.h1, ids=parser.ids, hrefs=parser.hrefs, scripts=parser.scripts,
        meta_refresh=parser.meta_refresh, text=" ".join(parser.text_parts)
    )


def resolve_internal(src: str, href: str, existing: set[str]):
    h=html.unescape(href.strip())
    if not h: return None
    u=urlsplit(h)
    if u.scheme.lower() in EXTERNAL_SCHEMES or u.netloc: return None
    if h.startswith("//"): return None
    frag=unquote(u.fragment)
    path=unquote(u.path)
    if not path:
        target=src
    else:
        base=Path(src).parent
        if path.startswith("/"):
            cand=Path(path.lstrip("/"))
        else:
            cand=base / path
        norm=Path(os.path.normpath(cand.as_posix())).as_posix()
        if norm==".": norm="index.html"
        if norm.endswith("/"): norm += "index.html"
        target=norm
        if target not in existing and Path(target).suffix=="":
            if target + ".html" in existing: target += ".html"
            elif f"{target}/index.html" in existing: target=f"{target}/index.html"
    return target, frag


def door_of(path: str) -> str:
    name=Path(path).name
    if path.startswith("vocab/") or path.startswith("assets/vocab/"): return "D8 Vocabulary"
    if name in {"coffee-leaf-human-biology.html","post-cup-landscape.html","gut-barrier-microbiome.html","metabolic-signals.html","rest-stress-response.html","restorative-traditions.html","safety-dose-variability.html","research-gaps.html","door-nine-sources.html","coffee-leaf-health-benefits.html"}: return "D9 Biology"
    if name.startswith("buna-culinary"): return "D7 Culinary"
    if name.startswith("sensory-") or name=="buna-sensory-school.html": return "D6 Sensory"
    if name in {"citane-terrain-map.html","clt-flavour-wheel.html","citane-logic-board.html","citane-epsilon-board.html"}: return "D5 Tools"
    if name in {"citane-reactive-landscape.html"}: return "D4 Chemistry"
    if name.startswith("citane-processing") or name=="citane-process-compass.html" or name.startswith("citane-hack-") or name=="cinnamon-smoke-trial.html": return "D3 Processing"
    if any(name.startswith(x) for x in ("engere","kuti","chemo","kawa-daun")) or name in {"the-foliage-of-buna.html","foliage-of-buna.html","the-foliage-of-buna-minimal.html"}: return "D2 Traditions"
    if name=="begin-with-a-cup.html": return "D1 Begin"
    if name=="sensory-landscape-of-coffee-leaf.html": return "D1/D4 Shared"
    if name in {"index.html","catalogue.html","visitor-lounge.html"}: return "Site shell"
    return "Outside / legacy"

html_files=sorted(ROOT.rglob("*.html"))
# Ignore generated audit output if rerun.
html_files=[p for p in html_files if "audit-output" not in p.parts]
pages={p.relative_to(ROOT).as_posix(): parse_page(p) for p in html_files}
existing={p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and "audit-output" not in p.parts}

broken=[]; missing_frag=[]; dupes=[]; edges=[]; external=[]
for src,info in pages.items():
    seen=collections.Counter()
    for href in info.hrefs:
        r=resolve_internal(src,href,existing)
        if r is None:
            if href and not href.startswith(("#","mailto:","tel:","javascript:","data:")):
                external.append((src,href))
            continue
        target,frag=r
        key=target + ("#"+frag if frag else "")
        seen[key]+=1
        if target not in existing:
            broken.append((src,href,target))
            continue
        edges.append((src,target,frag,href))
        if frag and target in pages and frag not in pages[target].ids:
            missing_frag.append((src,href,target,frag))
    for target,count in seen.items():
        if count>1: dupes.append((src,target,count))

incoming=collections.defaultdict(set); outgoing=collections.defaultdict(set)
for src,target,frag,href in edges:
    if target in pages:
        incoming[target].add(src); outgoing[src].add(target)

# JS references to HTML can drive navigation too.
js_refs=[]; js_broken=[]
for p in ROOT.rglob("*.js"):
    if "audit-output" in p.parts: continue
    raw=p.read_text(encoding="utf-8",errors="replace")
    for m in re.finditer(r"(?<![A-Za-z0-9_])(?:\.\./|\./)?[A-Za-z0-9_./-]+\.html(?:#[A-Za-z0-9_.:-]+)?",raw):
        ref=m.group(0)
        src=p.relative_to(ROOT).as_posix()
        r=resolve_internal(src,ref,existing)
        if r:
            target,frag=r; js_refs.append((src,ref,target,frag))
            if target not in existing: js_broken.append((src,ref,target))

shared_nav_targets=sorted({t for s,r,t,f in js_refs if s=="buna-nav.js" and t in pages})

zero_in=[]; one_in=[]
for p in pages:
    if p=="index.html": continue
    c=len(incoming.get(p,set()))
    if c==0: zero_in.append(p)
    elif c==1: one_in.append((p,sorted(incoming[p])[0]))

# Hierarchy / protocol checks.
bypasses=[]
for src,target,frag,href in edges:
    if src in HIGH_LEVEL and target in LEGACY_TRADITION_MIDDLE:
        fam=target.split(".")[0]
        bypasses.append((src,target,CANONICAL_ENTRY.get(fam,""),"High-level page bypasses tradition intro"))
    if src=="index.html" and target.startswith("vocab/") and target!="vocab/index.html":
        bypasses.append((src,target,"vocab/index.html","Homepage links directly into vocabulary branch"))

# Potential family deep pages with low discoverability.
underlinked=[]
for p in sorted(pages):
    c=len(incoming.get(p,set()))
    d=door_of(p)
    if c<=1 and d not in {"Site shell"}:
        underlinked.append((p,c,sorted(incoming.get(p,set())),d,p in shared_nav_targets))

# Structural checks.
struct=[]
for p,info in pages.items():
    if not info.title: struct.append((p,"missing-title","No <title> element"))
    if len(info.h1)==0: struct.append((p,"missing-h1","No H1 heading"))
    if len(info.h1)>1: struct.append((p,"multiple-h1",f"{len(info.h1)} H1 headings"))
    if info.meta_refresh: struct.append((p,"meta-refresh", "; ".join(info.meta_refresh)))
    lowtitle=info.title.lower()
    if p=="catalogue.html" and "foliage" in lowtitle:
        struct.append((p,"wrong-title","Catalogue document title identifies itself as The Foliage of Buna"))
    raw=(ROOT/p).read_text(encoding="utf-8",errors="replace")
    for label,pat in STALE_PATTERNS.items():
        if pat.search(raw): struct.append((p,"stale-text",label))

# Similar / duplicate filename families.
alternates=[]
for family in ["the-foliage-of-buna","foliage-of-buna","the-foliage-of-buna-minimal"]:
    if family+".html" in pages: alternates.append(family+".html")

# Title collisions.
titles=collections.defaultdict(list)
for p,i in pages.items():
    if i.title: titles[i.title.strip().lower()].append(p)
title_dupes={k:v for k,v in titles.items() if len(v)>1}

# Door inventory.
doors=collections.defaultdict(list)
for p in pages: doors[door_of(p)].append(p)

report={
    "summary": {
        "html_pages": len(pages),
        "internal_edges": len(edges),
        "broken_internal_links": len(broken),
        "missing_fragments": len(missing_frag),
        "duplicate_link_targets": len(dupes),
        "zero_incoming_pages": len(zero_in),
        "one_incoming_pages": len(one_in),
        "js_html_references": len(js_refs),
        "broken_js_html_references": len(js_broken),
        "shared_nav_targets": len(shared_nav_targets),
        "potential_hierarchy_bypasses": len(bypasses),
    },
    "pages": sorted(pages),
    "door_inventory": {k:sorted(v) for k,v in sorted(doors.items())},
    "broken_internal_links": broken,
    "missing_fragments": missing_frag,
    "duplicate_link_targets": dupes,
    "zero_incoming_pages": zero_in,
    "one_incoming_pages": one_in,
    "underlinked_pages": underlinked,
    "shared_nav_targets": shared_nav_targets,
    "potential_hierarchy_bypasses": bypasses,
    "structural_flags": struct,
    "js_broken_html_references": js_broken,
    "title_collisions": title_dupes,
    "alternate_foliage_pages": alternates,
    "incoming_counts": {p:len(incoming.get(p,set())) for p in sorted(pages)},
    "incoming_sources": {p:sorted(incoming.get(p,set())) for p in sorted(pages)},
    "outgoing_counts": {p:len(outgoing.get(p,set())) for p in sorted(pages)},
}
(OUT/"site-audit.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")

md=[]
md.append("# Buna Site Structure and Link Audit\n")
md.append("Generated from the production repository snapshot on this audit branch. No production files are modified by this report.\n")
md.append("## Summary\n")
for k,v in report["summary"].items(): md.append(f"- **{k.replace('_',' ').title()}:** {v}")

def section(title, rows, fmt):
    md.append(f"\n## {title}\n")
    if not rows: md.append("None detected."); return
    for row in rows: md.append("- "+fmt(row))

section("Broken internal links", broken, lambda r:f"`{r[0]}` -> `{r[1]}` (resolved `{r[2]}`)")
section("Missing fragment targets", missing_frag, lambda r:f"`{r[0]}` -> `{r[1]}`; `{r[2]}` has no `#{r[3]}`")
section("Duplicate link targets on the same page", dupes, lambda r:f"`{r[0]}` links to `{r[1]}` **{r[2]} times**")
section("Pages with zero incoming HTML links", zero_in, lambda r:f"`{r}` ({door_of(r)})")
section("Pages with exactly one incoming HTML link", one_in, lambda r:f"`{r[0]}` <- `{r[1]}`")
section("Potential hierarchy bypasses", bypasses, lambda r:f"`{r[0]}` links to `{r[1]}` instead of canonical `{r[2]}` — {r[3]}")
section("Broken HTML references embedded in JavaScript", js_broken, lambda r:f"`{r[0]}` -> `{r[1]}` (resolved `{r[2]}`)")
section("Structural flags", struct, lambda r:f"`{r[0]}` — **{r[1]}**: {r[2]}")

md.append("\n## Under-linked pages requiring editorial review\n")
for p,c,srcs,d,in_nav in underlinked:
    nav="yes" if in_nav else "no"
    sources=", ".join(f"`{s}`" for s in srcs) if srcs else "none"
    md.append(f"- `{p}` — {d}; incoming={c}; shared-nav={nav}; source(s): {sources}")

md.append("\n## Door inventory\n")
for d,items in sorted(doors.items()):
    md.append(f"\n### {d}\n")
    for p in sorted(items): md.append(f"- `{p}` — incoming {len(incoming.get(p,set()))}, outgoing {len(outgoing.get(p,set()))}")

md.append("\n## Title collisions\n")
if not title_dupes: md.append("None detected.")
for title,items in sorted(title_dupes.items()): md.append(f"- `{title}`: " + ", ".join(f"`{p}`" for p in items))

(OUT/"site-audit.md").write_text("\n".join(md)+"\n",encoding="utf-8")
print(json.dumps(report["summary"],indent=2))
print(f"Wrote {OUT/'site-audit.md'} and {OUT/'site-audit.json'}")
