"""Shared templates for the Nov8rs (Innovators) static site."""
import json, html, re

SITE = "https://nov8rs.com"
QUOTE = "https://nov8rs-quote-new.vercel.app/"
BRAND = "Nov8rs (Innovators)"
EMAIL = "hello@nov8rs.com"
YEAR = 2026
PREVIEW = False  # set by build.py: preview links use .html files

def url(path):
    """Internal link. '/' -> home. Clean URLs on Vercel, .html in preview."""
    if path.startswith("http") or path.startswith("#"):
        return path
    base, _, frag = path.partition("#")
    frag = ("#" + frag) if frag else ""
    if PREVIEW:
        if base in ("", "/"):
            return "index.html" + frag
        return base.strip("/") + ".html" + frag
    return (base or "/") + frag

def esc(s):
    return html.escape(s, quote=True)

def plain(s):
    return esc(re.sub(r"<[^>]+>", "", s).replace("//", "·"))

ARROW = '<span class="ar" aria-hidden="true">→</span>'

def quote(slot, label, cls="btn", size=""):
    href = f"{QUOTE}?utm_source=nov8rs.com&amp;utm_medium=website&amp;utm_campaign=instant_quote&amp;utm_content={slot}"
    c = cls + (" " + size if size else "")
    return f'<a class="{c}" href="{href}" data-cta="{slot}">{label} {ARROW}</a>'

# ---------------- icons ----------------
def ic(name, size=None):
    p = ICONS[name]
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'

ICONS = {
 "web": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 13h6M7 16h4"/>',
 "gas": '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m20 20-4.6-4.6M10.5 7.5v6M7.5 10.5h6"/>',
 "ads": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 "crm": '<path d="M4 5h16v10H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 "wl": '<path d="M12 3 3 8l9 5 9-5-9-5z"/><path d="m3 13 9 5 9-5"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 "spark": '<path d="m12 3 2 6 6 2-6 2-2 6-2-6-6-2 6-2z"/>',
 "chart": '<path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/>',
 "code": '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',
 "funnel": '<path d="M3 4h18l-7 8v6l-4 2v-8z"/>',
 "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
 "bolt": '<path d="M13 2 3 14h9l-1 8 10-12h-9z"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7l.7 2.7-1.8 3.4a16 16 0 0 0 6 6l3.4-1.8 2.7.7a2 2 0 0 1 1.7 2z"/>',
 "cal": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
 "star": '<path d="m12 3 2.6 5.6 6.4.7-4.8 4.3 1.3 6.4L12 17l-5.5 3 1.3-6.4L3 9.3l6.4-.7z"/>',
 "users": '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M17 3a4 4 0 0 1 0 8M22 21a7 7 0 0 0-4-6.3"/>',
 "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/>',
 "layers": '<path d="M12 3 2 8l10 5 10-5z"/><path d="m2 16 10 5 10-5M2 12l10 5 10-5"/>',
 "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><path d="M12 12 21 3"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "inbox": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z"/>',
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "gauge": '<path d="M12 14 16 9"/><path d="M3.3 17a9 9 0 1 1 17.4 0"/>',
}

SERVICES = [
 ("web", "Websites", "/web-development", "Websites, landing pages and funnels built to convert."),
 ("gas", "GAS-EO", "/seo-services", "SEO, AEO and GEO so Google and AI name you."),
 ("ads", "Paid media", "/paid-media-agency", "Google, Microsoft, Meta and LinkedIn ads, tracked to bookings."),
 ("crm", "AI CRM", "/ai-crm", "AI agents that reply, qualify, book and request reviews."),
]

# ---------------- head ----------------
def head(p):
    canon = SITE + ("/" if p["path"] == "/" else p["path"])
    og = SITE + "/assets/img/og/" + p["slug"] + ".jpg"
    robots = p.get("robots", "index,follow,max-image-preview:large")
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in p["schema"])
    pre = ""
    if p.get("preload_bulb"):
        pre = f'<link rel="preload" as="image" href="{asset("assets/img/bulb.webp")}" type="image/webp">'
    return f"""<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta name="author" content="{BRAND}">
<meta name="theme-color" content="#070707">
<meta name="format-detection" content="telephone=no">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{esc(p.get('og_title', p['title']))}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(p.get('og_title', p['title']))}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p.get('og_title', p['title']))}">
<meta name="twitter:description" content="{esc(p['desc'])}">
<meta name="twitter:image" content="{og}">
<link rel="icon" href="{asset('favicon.ico')}" sizes="48x48">
<link rel="icon" type="image/png" href="{asset('favicon-32.png')}" sizes="32x32">
<link rel="apple-touch-icon" href="{asset('apple-touch-icon.png')}">
<link rel="manifest" href="{asset('site.webmanifest')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&amp;family=Inter:wght@400;500;600&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap">
<link rel="stylesheet" href="{asset('assets/css/site.css')}">
{pre}
<script>document.documentElement.classList.add('js')</script>
<!-- Analytics: paste your GA4 / GTM snippet here (e.g. G-XXXXXXX). Quote clicks push {{event:'quote_click'}} to dataLayer. -->
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def bgurl(name):
    """Image used through a CSS variable: resolves relative to site.css."""
    return f"url(../img/{name}.webp)"

def asset(path):
    return path if PREVIEW else "/" + path

# ---------------- header / footer ----------------
def header(active):
    drop = "".join(
        f'<a href="{url(h)}"><span class="di">{ic(k)}</span><span><b>{n}</b><small>{d}</small></span></a>'
        for k, n, h, d in SERVICES)
    drop += f'<a href="{url("/white-label")}"><span class="di">{ic("wl")}</span><span><b>White label</b><small>Agency fulfilment under your brand.</small></span></a>'
    def cur(p):
        return ' aria-current="page"' if active == p else ""
    home_j = url("/#journey")
    mm = "".join(f'<a href="{url(h)}"{cur(h)}>{n}<small>0{i+1}</small></a>' for i, (k, n, h, d) in enumerate(SERVICES))
    return f"""<div class="prog" aria-hidden="true"></div>
<header class="nav">
  <div class="wrap in">
    <a class="logo" href="{url('/')}" aria-label="{BRAND} home"><img src="{asset('assets/img/bulb-sm.webp')}" alt="" width="34" height="34"><span><b>NOV8RS</b><small>Innovators</small></span></a>
    <nav aria-label="Main">
      <ul class="links">
        <li class="hasdrop"><button type="button" aria-expanded="false" aria-haspopup="true">Services <span aria-hidden="true">▾</span></button><div class="drop">{drop}</div></li>
        <li><a href="{url('/white-label')}"{cur('/white-label')}>White label</a></li>
        <li><a href="{home_j}">How it works</a></li>
        <li><a href="{url('/#faq') if active in ('/contact','/privacy','/terms','') else '#faq'}">FAQ</a></li>
      </ul>
    </nav>
    <div class="navr">
      {quote('nav', "Let's NOV8", 'btn', 'sm')}
      <button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mmenu"><span></span></button>
    </div>
  </div>
</header>
<div class="mmenu" id="mmenu">
  {mm}
  <a href="{url('/white-label')}"{cur('/white-label')}>White label<small>Agencies</small></a>
  <a href="{home_j}">How it works<small>Journey</small></a>
  {quote('mobile_menu', 'Get my instant quote', 'btn', 'lg')}
</div>
"""

def final_cta(slot, title="Ready to <em>NOV8?</em>", text=None, label="Build my custom quote"):
    text = text or "Pick your services and see your price straight away. No call needed to get a number."
    return f"""<section class="band dark sec" aria-label="Get your quote">
  <canvas class="rain" data-density=".7" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="final" data-rv>
      <div class="fbg" aria-hidden="true"></div>
      <div>
        <p class="kick mono"><i></i>Instant quote <span>// {BRAND}</span></p>
        <h2 class="wordrv">{title}</h2>
        <p class="lead" style="margin-top:18px;color:#C9C9C3">{text}</p>
        <div class="ctas">{quote(slot, label, 'btn', 'lg')}</div>
        <p class="alt">Rather talk to a person first? <a href="{url('/contact')}">Send us a message</a>.</p>
      </div>
      <img src="{asset('assets/img/bulb.webp')}" alt="" width="280" height="280" loading="lazy">
    </div>
  </div>
</section>"""

def footer():
    svc = "".join(f'<li><a href="{url(h)}">{n}</a></li>' for k, n, h, d in SERVICES)
    return f"""<footer>
  <div class="wrap">
    <div class="ftop">
      <div>
        <a class="logo" href="{url('/')}" aria-label="{BRAND} home"><img src="{asset('assets/img/bulb-sm.webp')}" alt="" width="34" height="34" loading="lazy"><span><b>NOV8RS</b><small>Innovators</small></span></a>
        <p>{BRAND} is a digital marketing agency for websites, GAS-EO (SEO, AEO and GEO), paid media and AI CRM automation. Pronounced “innovators”.</p>
      </div>
      <div class="fcol"><h4>Services</h4><ul>{svc}<li><a href="{url('/white-label')}">White label</a></li></ul></div>
      <div class="fcol"><h4>Company</h4><ul><li><a href="{url('/#journey')}">How it works</a></li><li><a href="{url('/#faq')}">FAQ</a></li><li><a href="{url('/contact')}">Contact us</a></li></ul></div>
      <div class="fcol"><h4>Start</h4><ul><li><a href="{QUOTE}?utm_source=nov8rs.com&amp;utm_medium=website&amp;utm_campaign=instant_quote&amp;utm_content=footer" data-cta="footer">My instant quote</a></li><li><span style="color:var(--muted);font-size:15px;user-select:all">{EMAIL}</span></li></ul></div>
    </div>
    <div class="fbig" aria-hidden="true">NOV8RS</div>
  </div>
  <div class="wrap fbot">
    <span>© {YEAR} {BRAND}. All rights reserved.</span>
    <nav aria-label="Legal"><a href="{url('/privacy')}">Privacy</a><a href="{url('/terms')}">Terms</a><a href="{url('/sitemap.xml') if not PREVIEW else '#'}">Sitemap</a></nav>
  </div>
</footer>
<div class="mbar">{quote('mobile_bar', 'Get my instant quote', 'btn')}</div>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js" defer></script>
<script src="{asset('assets/js/site.js')}" defer></script>
</body>
</html>
"""

# ---------------- reusable blocks ----------------
def faq(items, title="Questions, <em>answered.</em>", sub=None, band="dark", sid="faq"):
    sub = sub or f"Straight answers on how {BRAND} works."
    rows = "".join(
        f'<details{" open" if i == 0 else ""}><summary>{esc(q)}<span class="pm" aria-hidden="true">+</span></summary><div class="ans"><p>{esc(a)}</p></div></details>'
        for i, (q, a) in enumerate(items))
    return f"""<section id="{sid}" class="band {band} sec" aria-label="Frequently asked questions">
  <div class="wrap faq">
    <div class="side"><p class="kick mono"><i></i>FAQ</p><h2 class="h2 wordrv">{title}</h2><p class="lead" style="margin-top:18px">{sub}</p></div>
    <div data-rv>{rows}</div>
  </div>
</section>"""

def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def crumbs_schema(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}

ORG = {"@context": "https://schema.org", "@type": "ProfessionalService", "@id": SITE + "/#org",
       "name": "Nov8rs", "alternateName": ["NOV8RS", "Nov8rs (Innovators)", "Innovators"],
       "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "image": SITE + "/assets/img/og/home.jpg",
       "email": EMAIL, "slogan": "We innovate. You grow.",
       "description": "Digital marketing agency for websites, SEO, AEO and GEO (GAS-EO), paid media, AI CRM automation and white-label fulfilment.",
       "areaServed": {"@type": "Country", "name": "United States"},
       "knowsAbout": ["Search engine optimization", "Answer engine optimization", "Generative engine optimization", "Paid media", "Google Ads", "Microsoft Advertising", "LinkedIn Ads", "Web development", "GoHighLevel", "Marketing automation", "AI agents", "White label marketing"]}

def service_schema(name, stype, path, desc):
    return {"@context": "https://schema.org", "@type": "Service", "name": name, "serviceType": stype,
            "description": desc, "url": SITE + path, "provider": {"@id": SITE + "/#org"},
            "areaServed": {"@type": "Country", "name": "United States"}}

def phases(items, band="dark", title="", kick="", lead="", bgimg="bg-grid"):
    blocks = []
    for i, ph in enumerate(items):
        its = "".join(f'<div class="item"><b>{a}</b><span class="badge2">{c}</span><p>{b}</p></div>' for a, b, c in ph["items"])
        blocks.append(f"""<article class="phase hc" data-rv>
      <div class="pk"><span class="mono">Phase 0{i+1} // {ph['tag']}</span><h3>{ph['h']}</h3><p>{ph['p']}</p>
        <div class="deliv"><small>Key deliverable</small>{ph['deliv']}</div></div>
      <div class="items">{its}</div>
    </article>""")
    return f"""<section class="band {band} sec spotsec" aria-label="Our method">
  <div class="spotbg" style="--bgimg:{bgurl(bgimg)}" aria-hidden="true"><i></i></div>
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>{kick}</p><h2 class="h2 wordrv">{title}</h2></div><p class="lead">{lead}</p></div>
    <div class="phases">{''.join(blocks)}</div>
  </div>
</section>"""

def features(items, band="paper", title="", kick="", lead="", cols=3):
    cards = "".join(f'<article class="fc hc" data-rv="{(i%3)+1}"><span class="ic">{ic(k)}</span><h3>{h}</h3><p>{p}</p></article>' for i, (k, h, p) in enumerate(items))
    return f"""<section class="band {band} sec" aria-label="{plain(kick)}">
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>{kick}</p><h2 class="h2 wordrv">{title}</h2></div><p class="lead">{lead}</p></div>
    <div class="fgrid">{cards}</div>
  </div>
</section>"""

def outcomes(items, band="paper", title="", kick="", lead="", slot="outcomes", label="Make my quote"):
    cards = "".join(f'<article class="pc hc" data-rv="{i+1}"><span class="mono">0{i+1} · {t}</span><h3>{h}</h3><div class="path">{" <i>→</i> ".join(path)}</div><p style="color:var(--pMuted);font-size:15px">{p}</p></article>' for i, (t, h, path, p) in enumerate(items))
    return f"""<section class="band {band} sec" aria-label="{plain(kick)}">
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>{kick}</p><h2 class="h2 wordrv">{title}</h2></div><div><p class="lead">{lead}</p><div class="ctas" style="margin-top:22px">{quote(slot, label)}</div></div></div>
    <div class="proof">{cards}</div>
  </div>
</section>"""

def chips(items, title, kick, band="dark2"):
    c = "".join(f"<span>{x}</span>" for x in items)
    return f"""<section class="band {band} sec" aria-label="{plain(kick)}">
  <div class="wrap center"><p class="kick mono"><i></i>{kick}</p><h2 class="h2 wordrv" style="max-width:18ch">{title}</h2><div class="chipcloud" data-rv style="margin-top:36px">{c}</div></div>
</section>"""

def marquee(words):
    s = "".join(f"<span>{w}</span>" for w in words)
    return f'<div class="mq" aria-hidden="true"><div class="tr">{s}{s}</div></div>'

def phero(p):
    chips_ = "".join(f"<span>{c}</span>" for c in p["chips"])
    return f"""<section class="band dark phero" aria-label="{esc(p['crumb'])}">
  <div class="bgimg" style="--bgimg:{bgurl(p['bg'])}" aria-hidden="true"></div>
  <canvas class="rain" data-density=".6" aria-hidden="true"></canvas>
  <div class="wrap pgrid">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{url('/')}">Home</a><span aria-hidden="true">/</span><span aria-current="page">{p['crumb']}</span></nav>
      <p class="kick mono"><i></i>{p['kick']}</p>
      <h1 class="ph1 wordrv">{p['h1']}</h1>
      <p class="pintro" data-rv>{p['intro']}</p>
      <div class="pchips" data-rv="2">{chips_}</div>
      <div class="ctas" data-rv="3">{quote(p['slot'], p['cta'], 'btn', 'lg')}</div>
    </div>
    <div class="pvis" data-rv="2">{p['vis']}</div>
  </div>
</section>"""
