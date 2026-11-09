"""Builds the Nov8rs (Innovators) static site.
python3 build.py            -> dist/     (Vercel, clean URLs)
python3 build.py --preview  -> preview/  (.html links, for local viewing)
"""
import json, os, re, shutil, sys
import build_lib as L
import build_vis as V
from build_lib import quote, ic, url, asset, BRAND, SITE, esc

PREVIEW = "--preview" in sys.argv
L.PREVIEW = PREVIEW
OUT = "preview" if PREVIEW else "dist"

FAQ = json.load(open("faqs.json"))
def clean(items):
    out = []
    for q, a in items:
        q = q.replace("NOV8RS", "Nov8rs"); a = a.replace("NOV8RS", "Nov8rs").replace(" ,", ",")
        out.append((q, a))
    return out

pages = []
def page(**kw):
    pages.append(kw)

# =====================================================================
# HOME
# =====================================================================
home_faq = clean(FAQ["home"])
home_faq = [x for x in home_faq if not x[0].startswith("Do you work with businesses on an ongoing")][:11]
home_faq = [(q, a) if q != "How do I get started with Nov8rs?" else
            (q, "Open the instant quote builder, pick the services you need and you'll see your price straight away. If you'd rather talk first, send us a message and we'll find the right next step together.") for q, a in home_faq]

orbit_tiles = "".join(
    f'<a class="tile" href="{url(h)}" data-i="{i}"><span class="ic">{ic(k)}</span>{n}</a>'
    for i, (k, n, h, d) in enumerate(L.SERVICES))

home_body = f"""
<div class="loader" id="loader" aria-hidden="true">
  <div class="lglow"></div>
  <div class="lmid"><div class="lb" id="lb"><img class="l-off" alt="" src="{asset('assets/img/bulb.webp')}"><img class="l-on" alt="" src="{asset('assets/img/bulb.webp')}"></div>
  <div class="ltag"><b>NOV8RS</b><span>Innovators</span></div></div>
  <canvas id="sparks"></canvas>
</div>

<section id="hero" class="pin band dark" aria-label="{BRAND}: we innovate, you grow">
  <div class="stage">
    <canvas class="rain" data-density=".9" aria-hidden="true"></canvas>
    <div class="wrap hgrid">
      <div class="hleft">
        <div class="steps" aria-hidden="true"><span class="stp on">We innovate</span><span class="stp">Websites</span><span class="stp">GAS-EO</span><span class="stp">Ads</span><span class="stp">AI CRM</span></div>
        <div class="chaps">
          <div class="chap on">
            <p class="hl mono"><i></i>Strategy · Visibility · AI · Automation</p>
            <h1 class="h1">We <em>innovate.</em><br>You grow.<span class="spell"><b>Nov8rs</b> (Innovators), the digital marketing agency built for Google and AI search.</span></h1>
            <p class="hsub">Websites, GAS-EO, paid media and an AI-powered CRM, run as one system that turns searches into booked customers across the USA.</p>
            <div class="ctas">{quote('hero', 'Get my instant quote', 'btn', 'lg')}<a class="btn ghost" href="#services">See what we build</a></div>
          </div>
          <div class="chap"><p class="hl mono"><i></i>01 · Websites</p><h2 class="ch2">Websites that <em>sell.</em></h2><p class="hsub">Fast, mobile-first websites, landing pages and funnels with one job: turn the visit into an enquiry.</p>
            <div class="live"><span class="ti">{ic('check')}</span><div><b>Quote request</b><small>From the services page</small></div><span class="tm">LIVE</span></div></div>
          <div class="chap"><p class="hl mono"><i></i>02 · GAS-EO</p><h2 class="ch2">Found on Google. <em>Named by AI.</em></h2><p class="hsub">Generative, answer-engine and search optimization (GEO, AEO and SEO) run as one program.</p>
            <div class="live"><span class="ti">{ic('spark')}</span><div><b>Cited in AI Overview</b><small>Google · source #1</small></div><span class="tm">LIVE</span></div></div>
          <div class="chap"><p class="hl mono"><i></i>03 · Paid media</p><h2 class="ch2">Every ad dollar, <em>tracked to a booking.</em></h2><p class="hsub">Google, Microsoft, Meta and LinkedIn ads, measured on qualified leads, not clicks.</p>
            <div class="live"><span class="ti">{ic('ads')}</span><div><b>Ad lead booked</b><small>Google search campaign</small></div><span class="tm">LIVE</span></div></div>
          <div class="chap"><p class="hl mono"><i></i>04 · AI CRM</p><h2 class="ch2">Every lead <em>answered in seconds.</em></h2><p class="hsub">AI agents text back missed calls, qualify, book and ask for the review.</p>
            <div class="ctas">{quote('hero_end', 'Make my quote', 'btn')}</div></div>
        </div>
      </div>
      <div class="hstage" id="hstage">
        <canvas id="heroCv" aria-hidden="true"></canvas>
        <div class="orbitring" aria-hidden="true"></div>
        <div class="hbulb" id="hbulb"><img src="{asset('assets/img/bulb.webp')}" alt="The Nov8rs gold bulb with a figure-eight filament" width="880" height="880" fetchpriority="high"></div>
        {orbit_tiles}
      </div>
    </div>
    <div class="scrollhint" aria-hidden="true"><i></i>Scroll</div>
  </div>
</section>

{L.marquee(["OpenAI", "Claude", "GoHighLevel", "HubSpot", "n8n", "Zapier", "Google Ads", "Microsoft Ads", "Meta", "LinkedIn", "WordPress", "Shopify", "Webflow", "Stripe", "Supabase", "Vercel", "Cloudflare", "ClickFunnels"])}

<section id="problem" class="pin show paper" aria-label="The real problem">
  <div class="stage">
    <div class="wrap sg">
      <div>
        <p class="kick mono"><i></i>The real problem <span>// sound familiar?</span></p>
        <div class="strk"><div class="sl first">Invisible online.<i></i></div><div class="sl">Tools that don't talk.<i></i></div><div class="sl">Demand you can't scale.<i></i></div></div>
        <div class="res">You don't need more services. <em>You need the right ones.</em></div>
        <p class="sdesc">{BRAND} figures out which problem is actually yours before recommending what comes next.</p>
      </div>
      <div class="vis" aria-hidden="true">
        <div class="phone"><div class="scr"><span class="notch"></span><div class="sbar"><span>9:41</span><span>●●●</span></div>
          <div class="ph-h"><b>Leak report</b><span>THIS WEEK</span></div>
          <div class="leak" data-at=".08"><span class="x">✕</span><div><b>AI answer</b><small>Your business not mentioned</small></div></div>
          <div class="leak" data-at=".2"><span class="x">✕</span><div><b>Google Maps</b><small>Ranking on page 2</small></div></div>
          <div class="leak" data-at=".32"><span class="x">✕</span><div><b>Web form</b><small>Unanswered for 2 days</small></div></div>
          <div class="leak" data-at=".44"><span class="x">✕</span><div><b>Missed call</b><small>No text-back, no follow-up</small></div></div>
          <div class="leak" data-at=".56"><span class="x">✕</span><div><b>Ad spend</b><small>No link to booked jobs</small></div></div>
          <div class="sumbar">5 leaks found · example report</div></div></div>
      </div>
    </div>
  </div>
</section>

<section class="band dark sec spotsec" aria-label="The Nov8rs method">
  <div class="spotbg" style="--bgimg:{L.bgurl('bg-grid')}" aria-hidden="true"><i></i></div>
  <canvas class="rain" data-density=".35" aria-hidden="true"></canvas>
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>The Nov8rs method <span>// move your cursor</span></p><h2 class="h2 wordrv">Three defined stages. <em>Zero guesswork.</em></h2></div>
      <p class="lead">We don't sell random deliverables or force-fit packages. We diagnose the real bottleneck, build visible authority, then engineer systems that scale.</p></div>
    <div class="stages">
      <article class="stage3 hc" data-rv="1"><span class="num">01 // Understand</span><h3>Find the real constraint.</h3><p>A diagnostic of your business, audience, competitors and unit economics, so we fix what's actually holding growth back.</p><div class="tags"><span>Business</span><span>Audience</span><span>Competition</span><span>Goals</span><span>Constraints</span></div></article>
      <article class="stage3 hc" data-rv="2"><span class="num">02 // Visible</span><h3>Own the search moment.</h3><p>Capture high-intent demand through Google, AI answer engines, paid media and a website that earns trust.</p><div class="tags"><span>Search</span><span>AI answers</span><span>Paid media</span><span>Content</span><span>Brand</span></div></article>
      <article class="stage3 hc" data-rv="3"><span class="num">03 // Scale</span><h3>Automate what follows.</h3><p>Connected CRM pipelines, AI agents and automation that keep every lead moving without adding headcount.</p><div class="tags"><span>CRM</span><span>Automation</span><span>AI agents</span><span>Funnels</span><span>Systems</span></div></article>
    </div>
  </div>
</section>

<section id="services" class="band paper sec" aria-label="Services">
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>What we do <span>// one team, one system</span></p><h2 class="h2 wordrv">Focus only on what <em>drives growth.</em></h2></div>
      <div><p class="lead">We assess your needs first, then deliver the precise mix. Each service fixes a leak; together they take a customer from search to booked.</p><div class="ctas" style="margin-top:22px">{quote('services', 'Build my custom quote')}</div></div></div>
    <div class="svgrid">
      <a class="sv hc" href="{url('/web-development')}" data-rv="1"><span class="ic">{ic('web')}</span><span class="n">01</span><h3>Websites &amp; development</h3><p>High-performance websites, landing pages and funnels designed to convert.</p><ul><li>Strategy-first structure</li><li>SEO and speed built in</li><li>GoHighLevel integrations</li></ul><span class="go">Explore websites <i>→</i></span></a>
      <a class="sv hc" href="{url('/seo-services')}" data-rv="2"><span class="ic">{ic('gas')}</span><span class="n">02</span><h3>GAS-EO</h3><p>SEO, AEO and GEO in one program, so you rank on Google and get named by AI.</p><ul><li>Technical &amp; on-page SEO</li><li>Local SEO &amp; GBP</li><li>AI search visibility</li></ul><span class="go">Explore GAS-EO <i>→</i></span></a>
      <a class="sv hc" href="{url('/paid-media-agency')}" data-rv="3"><span class="ic">{ic('ads')}</span><span class="n">03</span><h3>Paid media</h3><p>Google, Microsoft, Meta, LinkedIn and YouTube, run as one strategy.</p><ul><li>Full setup &amp; tracking</li><li>Weekly optimisation</li><li>Pipeline-linked reporting</li></ul><span class="go">Explore paid media <i>→</i></span></a>
      <a class="sv hc" href="{url('/ai-crm')}" data-rv="4"><span class="ic">{ic('crm')}</span><span class="n">04</span><h3>AI CRM</h3><p>One inbox, AI agents and automation that answer, book and follow up.</p><ul><li>Missed-call text-back</li><li>AI chat &amp; voice agents</li><li>Reviews on autopilot</li></ul><span class="go">Explore AI CRM <i>→</i></span></a>
    </div>
    <p class="micro" style="margin-top:24px">Running an agency? <a class="tlink" href="{url('/white-label')}">See white-label fulfilment →</a></p>
  </div>
</section>

<section id="gaseo-show" class="pin show dark" aria-label="GAS-EO: SEO, AEO, generative and AI search">
  <div class="stage">
    <canvas class="rain" data-density=".4" aria-hidden="true"></canvas>
    <div class="wrap sg">
      <div>
        <p class="kick mono"><i></i>GAS-EO <span>// generative + AEO + SEO</span></p>
        <div class="gwords">
          <div class="gw act">SEO <span class="ck">Google ranks</span></div>
          <div class="gw">AEO <span class="ck">Answer boxes</span></div>
          <div class="gw">Generative <span class="ck">ChatGPT · Perplexity</span></div>
          <div class="gw">AI search <span class="ck">AI Overviews</span></div>
        </div>
        <div class="gdef"><span class="on">Rank in the map pack and the top organic spots for searches that bring jobs.</span><span>Become the source Google quotes in featured snippets and “People also ask”.</span><span>Get named when someone asks ChatGPT, Claude or Perplexity who to hire.</span><span>Get cited in Google's AI Overviews and AI Mode answers.</span></div>
        <div class="sact"><a class="tlink" href="{url('/seo-services')}">How GAS-EO works →</a></div>
      </div>
      <div class="vis">{V.gas_card()}</div>
    </div>
  </div>
</section>

<section id="journey" class="pin band paper" aria-label="The lead journey" data-steps='[["Step 1 · Searched","“ac repair near me”"],["Step 2 · Clicked","From the map pack"],["Step 3 · Landed","Fast page, one clear next step"],["Step 4 · Answered","AI replied in seconds"],["Step 5 · Booked","Thu 10:00 · review requested"]]'>
  <div class="stage">
    <div class="wrap head2" style="margin-bottom:0">
      <div><p class="kick mono"><i></i>The lead journey <span>// how it works</span></p><h2 class="h2">From search <em>to booked.</em></h2></div>
      <p class="lead">Every customer takes the same trip. {BRAND} builds each step, so nobody drops off on the way.</p>
    </div>
    <div class="wrap">
      <div class="wave" id="wave">
        <svg viewBox="0 0 1200 400" preserveAspectRatio="none" aria-hidden="true"><path class="wbg" d="M60 140 C200 140 220 300 360 300 S 520 140 600 140 S 760 300 840 300 S 1000 140 1140 140"/><path class="wfg" id="wpath" pathLength="1" d="M60 140 C200 140 220 300 360 300 S 520 140 600 140 S 760 300 840 300 S 1000 140 1140 140"/></svg>
        <div class="jn top first" data-t="0" style="left:5%"><span class="t">01 · Searched</span><b>Asks Google or AI</b><small>“Who's the best near me?”</small><span class="tag">GAS-EO</span></div>
        <div class="jn bot" data-t=".25" style="left:30%"><span class="t">02 · Clicked</span><b>Sees you first</b><small>Top result, cited answer or ad</small><span class="tag">ADS</span></div>
        <div class="jn top" data-t=".5" style="left:50%"><span class="t">03 · Landed</span><b>Fast, clear page</b><small>One next step: the quote</small><span class="tag">WEBSITE</span></div>
        <div class="jn bot" data-t=".75" style="left:70%"><span class="t">04 · Answered</span><b>Hears back in seconds</b><small>AI replies, qualifies, books</small><span class="tag">AI CRM</span></div>
        <div class="jn top last" data-t="1" style="left:95%"><span class="t">05 · Booked</span><b>Job done, review in</b><small>And back next season</small><span class="tag">AI CRM</span></div>
        <span class="jdot" id="jdot"></span>
      </div>
      <div class="jstatus" aria-live="polite"><span class="chip"><b id="jtb">Step 1 · Searched</b><span id="jts">“ac repair near me”</span></span></div>
      <div class="jv"><span class="rail"></span><span class="fill" id="jfill"></span>
        <div class="it" data-t="0"><b>Searched</b><small>Asks Google or AI · GAS-EO</small></div>
        <div class="it" data-t=".25"><b>Clicked</b><small>Sees you first · Paid media</small></div>
        <div class="it" data-t=".5"><b>Landed</b><small>Fast, clear page · Website</small></div>
        <div class="it" data-t=".75"><b>Answered</b><small>AI replies in seconds · AI CRM</small></div>
        <div class="it" data-t="1"><b>Booked</b><small>Job done, review requested</small></div></div>
    </div>
  </div>
</section>

<section class="band dark sec" aria-label="Proof">
  <div class="facetbg" aria-hidden="true"></div>
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>Proof <span>// evidence over theatre</span></p><h2 class="h2 wordrv">Problem <em>→</em> solution <em>→</em> result.</h2></div><p class="lead">Outcomes are published only when they can be verified. Full case studies are on the way.</p></div>
    <div class="proof">
      <article class="pc hc" data-rv="1"><span class="mono">01 · SEO · GEO</span><h3>Multi-location visibility system</h3><div class="path">Invisible <i>→</i> AEO / Maps <i>→</i> Dominance</div><span class="soon">CASE STUDY COMING SOON</span></article>
      <article class="pc hc" data-rv="2"><span class="mono">02 · Paid media · CRM</span><h3>Lead-to-opportunity infrastructure</h3><div class="path">Leaky spend <i>→</i> CRM / tracking <i>→</i> ROI scale</div><span class="soon">CASE STUDY COMING SOON</span></article>
      <article class="pc hc" data-rv="3"><span class="mono">03 · AI · Automation</span><h3>Operations without repetitive work</h3><div class="path">Bottlenecks <i>→</i> n8n / agents <i>→</i> Autonomy</div><span class="soon">CASE STUDY COMING SOON</span></article>
    </div>
  </div>
</section>

<section class="band paper sec" aria-label="How we work">
  <div class="wrap">
    <div class="head2"><div><p class="kick mono"><i></i>How we work <span>// clarity before complexity</span></p><h2 class="h2 wordrv">Six steps. <em>No guesswork.</em></h2></div><p class="lead">We work out which problem is actually yours before recommending what comes next.</p></div>
    <div class="hwgrid">
      <article class="hw hc" data-rv="1"><span class="n">01</span><h3>Meet</h3><p>We talk about your business, team, growth constraints and market.</p></article>
      <article class="hw hc" data-rv="2"><span class="n">02</span><h3>Understand</h3><p>We find the real problem across visibility, tools and scaling bottlenecks.</p></article>
      <article class="hw hc" data-rv="3"><span class="n">03</span><h3>Recommend</h3><p>We assemble the exact mix of strategy, media and technology you need.</p></article>
      <article class="hw hc" data-rv="1"><span class="n">04</span><h3>Build</h3><p>Senior delivery across search, advertising, automation and development.</p></article>
      <article class="hw hc" data-rv="2"><span class="n">05</span><h3>Measure</h3><p>Verified tracking, real conversion data and end-to-end attribution.</p></article>
      <article class="hw hc" data-rv="3"><span class="n">06</span><h3>Scale</h3><p>We expand what works, compounding your visibility and revenue.</p></article>
    </div>
  </div>
</section>

{L.faq(home_faq, sub=f"Clear answers on how {BRAND} helps you get found, generate leads and scale what works.")}
{L.final_cta('final_home')}
"""

page(slug="home", path="/", active="/", title=f"Digital Marketing Agency USA | {BRAND}",
     og_title=f"{BRAND} · Digital marketing agency USA",
     desc=f"{BRAND} is a digital marketing agency in the USA for websites, SEO, AEO & GEO, paid media and AI CRM automation. Get your instant quote.",
     body=home_body, preload_bulb=True, og_sub="Websites · GAS-EO · Paid media · AI CRM",
     schema=[L.ORG, {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": BRAND, "url": SITE + "/", "publisher": {"@id": SITE + "/#org"}}, L.faq_schema(home_faq)])

# =====================================================================
# SERVICE PAGES
# =====================================================================
def service_page(slug, path, crumb, title, desc, hero, sections, faq_items, schema_name, stype, og_sub, final_title, final_label, final_slot):
    body = L.phero(hero) + "\n".join(sections) + L.faq(faq_items, sub=f"Common questions about {crumb.lower()} with {BRAND}.") + L.final_cta(final_slot, final_title, label=final_label)
    page(slug=slug, path=path, active=path, title=title, desc=desc, body=body, og_sub=og_sub,
         schema=[L.ORG, L.service_schema(schema_name, stype, path, desc), L.crumbs_schema(crumb, path), L.faq_schema(faq_items)])

# ---------- GAS-EO / SEO ----------
seo_faq = clean(FAQ["seo-gaseo"])
service_page(
 "seo-services", "/seo-services", "SEO & GAS-EO",
 f"SEO, AI SEO & GEO Agency USA | {BRAND}",
 f"{BRAND} is an SEO agency in the USA. GAS-EO combines SEO, AEO and GEO to get you found on Google, Maps and AI search like ChatGPT and AI Overviews.",
 dict(crumb="SEO & GAS-EO", bg="bg-network", kick="GAS-EO · SEO agency USA",
      h1="Get found in search. <em>Get named by AI.</em>",
      intro=f"{BRAND} is an organic search and AI visibility agency. GAS-EO is our program that runs SEO, answer engine optimization (AEO) and generative engine optimization (GEO) as one, so you show up on Google, in Maps and in the answers ChatGPT, Perplexity and Google's AI Overviews give.",
      chips=["SEO services USA", "Local SEO & GBP", "AI SEO", "AEO", "GEO agency"],
      slot="hero_seo", cta="Quote my GAS-EO",
      vis=f'<div class="gwrap" data-loop="gas">{V.gas_card(True)}</div>'),
 [
  L.features([
    ("search", "SEO & organic search", "Technical SEO, on-page optimisation, content strategy and keyword targeting built around real search intent."),
    ("pin", "Local SEO & Google Business Profile", "Location pages, citations, GBP optimisation and reviews strategy so you win the map pack where you work."),
    ("spark", "AI SEO, AEO & GEO", "Clear structure, entities, FAQs and schema so answer engines and generative search can understand and cite you."),
    ("gauge", "Technical foundations", "Crawlability, indexation, Core Web Vitals, canonicals and structured data, fixed in priority order."),
    ("layers", "Content & authority", "Intent-led pages and topical coverage that earn rankings, links and mentions over time."),
    ("chart", "Search analytics", "Impressions, clicks, high-intent keyword movement and leads, reported in plain language."),
  ], band="paper", kick="One organic strategy <span>// every place they search</span>", title="SEO, AEO and GEO. <em>One program.</em>",
     lead="Organic search is more than rankings. We optimise the technical foundation, content, local presence and AI search signals together."),
  L.phases([
    dict(tag="Discover", h="Research before optimisation", p="Understand what your customers search, who already ranks and where your strongest opportunities are.", deliv="Organic search strategy & opportunity map",
         items=[("Keyword & search intent research", "Valuable terms, customer intent and the questions that matter to your business.", "RESEARCH"),
                ("Competitor & SERP analysis", "Competing sites, content coverage and authority gaps.", "INTEL"),
                ("Technical & visibility audit", "Indexing, structure, local visibility and the foundations affecting performance.", "AUDIT")]),
    dict(tag="Optimise", h="Optimise every search signal", p="Strengthen the site, content and local presence for traditional and AI-powered search.", deliv="Optimised search visibility foundation",
         items=[("Technical & on-page SEO", "Crawlability, metadata, internal linking and on-page relevance.", "SEO"),
                ("Local SEO & GBP", "Profile optimisation, location signals and local content.", "LOCAL"),
                ("AEO & GEO", "Content and brand information structured for answer engines and generative search.", "AI SEARCH")]),
    dict(tag="Grow", h="Grow with continuous optimisation", p="Measure, find new opportunities and keep improving visibility and qualified traffic.", deliv="Ongoing organic visibility & growth",
         items=[("Performance analysis", "Rankings, impressions, clicks, conversions and visibility trends.", "DATA"),
                ("Content expansion", "New pages around keywords, questions and intent revealed by data.", "CONTENT"),
                ("AI & local visibility growth", "Ongoing gains in Maps, GBP and AI-generated results.", "VISIBILITY")]),
  ], kick="The GAS-EO method <span>// discover · optimise · grow</span>", title="From search strategy to <em>measurable visibility.</em>",
     lead="We don't optimise pages and wait. We build a structured plan across SEO, local and AI search, then improve it every month.", bgimg="bg-network"),
  L.outcomes([
    ("Foundation", "Strengthen what your rankings stand on.", ["Technical SEO", "Content", "Visibility"], "Fix the issues that block growth first, then build pages that deserve to rank."),
    ("Visibility", "Get discovered across Google, Maps and AI.", ["SEO", "Local & GBP", "AI search"], "One presence across every place your customers search and ask."),
    ("Growth", "Turn visibility into business results.", ["Search data", "Optimisation", "Growth"], "Report on leads and revenue signals, not vanity rankings."),
  ], kick="What we optimise <span>// compounding visibility</span>", title="Build visibility that <em>compounds.</em>",
     lead=f"Looking for the best SEO company in the USA? Ask how they measure success. {BRAND} reports on what moves revenue.", slot="outcomes_seo", label="See my price"),
  L.chips(["Google Search", "Google Maps", "Google Business Profile", "AI Overviews", "AI Mode", "ChatGPT", "Perplexity", "Claude", "Gemini", "Bing", "Schema.org", "Search Console", "GA4"],
          "Optimised for every place your <em>customers ask.</em>", "Search surfaces"),
 ], seo_faq, "GAS-EO: SEO, AEO and GEO services", "Search engine optimization", "SEO · AEO · GEO · AI search",
 "Get named by <em>Google and AI.</em>", "Quote my GAS-EO", "final_seo")

# ---------- PAID MEDIA ----------
paid_faq = clean(FAQ["paid-media"])
service_page(
 "paid-media-agency", "/paid-media-agency", "Paid media",
 "Paid Media Agency USA | PPC & Performance | Nov8rs",
 f"{BRAND} is a paid media and performance marketing agency managing Google, Microsoft (Bing), Meta and LinkedIn ads for qualified leads and growth.",
 dict(crumb="Paid media", bg="bg-trails", kick="Paid media agency · PPC · Performance",
      h1="Smarter ads. <em>More qualified customers.</em>",
      intro=f"{BRAND} is a performance marketing and paid media agency. We build, manage and optimise campaigns across Google, Microsoft Advertising, Meta, LinkedIn and emerging AI ad platforms, and track every lead back to the campaign that paid for it.",
      chips=["Google Ads", "Microsoft Advertising", "Meta Ads", "LinkedIn ads agency", "Performance Max"],
      slot="hero_paid", cta="Quote my ads",
      vis=f'<div data-loop="ads">{V.ads_phone()}</div>'),
 [
  L.features([
    ("search", "Google & Microsoft search ads", "Capture high-intent buyers the moment they search, with Search, Performance Max and Bing ads."),
    ("users", "Meta & LinkedIn ads", "Audience targeting, creative testing and retargeting for B2C and B2B lead generation."),
    ("spark", "AI & emerging platforms", "Get ready for AI-powered and conversational ad placements as they open up."),
    ("target", "Conversion tracking", "Clean tracking from click to call, form and booking, so spend is judged on outcomes."),
    ("funnel", "Landing page CRO", "Ads and landing pages built together: one message, one offer, one action."),
    ("chart", "Pipeline reporting", "Cost per lead, ROAS and booked jobs in one clear report, not a pile of platform screenshots."),
  ], band="paper", kick="Advertising platforms <span>// one strategy</span>", title="One paid media strategy. <em>Every platform.</em>",
     lead="We build the right ad mix around your audience, offer, budget and conversion goals. Ad spend is managed and paid directly by you."),
  L.phases([
    dict(tag="Strategise", h="Research before ad spend", p="Know who you want to reach, what you're selling and what acquisition needs to cost.", deliv="Paid media strategy & campaign blueprint",
         items=[("Audience & search intent", "Segments, buying intent and the opportunities worth pursuing.", "RESEARCH"),
                ("Offer & competitor analysis", "Competitor ads, messaging and positioning gaps.", "INTEL"),
                ("Goals, budget & KPIs", "Acquisition targets, budget split and success metrics.", "METRIC")]),
    dict(tag="Launch", h="Build on the right platforms", p="Campaigns on the platforms that fit your audience, offer and goals.", deliv="Live campaigns & tracking infrastructure",
         items=[("Search & performance", "Google Ads, Performance Max and Microsoft Advertising.", "SEARCH"),
                ("Social & B2B", "Meta, Instagram and LinkedIn lead generation.", "SOCIAL"),
                ("AI & emerging", "New AI-driven ad environments as they mature.", "AI ADS")]),
    dict(tag="Optimise", h="Optimised by real campaign data", p="Continuous analysis and change to improve efficiency and lead quality.", deliv="Ongoing performance & optimisation",
         items=[("Performance analysis", "Clicks, conversions, CPL, ROAS, search terms and creative.", "DATA"),
                ("Testing & CRO", "Ads, audiences, landing pages and offers tested in a structured way.", "TEST"),
                ("Scale what works", "Budget moved to winning campaigns, waste cut.", "SCALE")]),
  ], kick="The Nov8rs ads method <span>// strategise · launch · optimise</span>", title="From campaign strategy to <em>continuous optimisation.</em>",
     lead="We don't launch ads and hope. We plan, build, track and keep improving towards better leads and return on ad spend.", bgimg="bg-grid"),
  L.outcomes([
    ("Paid media", "Reduce wasted ad spend.", ["Wasted spend", "Targeting", "Efficiency"], "Negative keywords, audience pruning and bid strategy that stop the leaks."),
    ("Conversion", "Turn clicks into better leads.", ["Ad click", "Landing page", "Conversion"], "Message match and faster pages that lift conversion rate."),
    ("Performance", "Scale the campaigns that perform.", ["Campaign data", "Testing", "Scale"], "Clear rules for when to push budget and when to pull it."),
  ], kick="What we optimise <span>// better campaigns</span>", title="Better campaigns start with <em>better optimisation.</em>",
     lead="We use campaign data, audience signals, creative tests and conversion data to make your budget work harder.", slot="outcomes_paid", label="Make my quote"),
  L.chips(["Google Search Ads", "Performance Max", "YouTube Ads", "Microsoft Advertising", "Bing Ads", "Meta Ads", "Facebook Ads", "Instagram Ads", "LinkedIn Ads", "AI advertising", "Retargeting", "Call tracking"],
          "Campaigns on the platforms <em>that matter.</em>", "Platforms we manage"),
 ], paid_faq, "Paid media management", "Pay-per-click advertising", "Google · Microsoft · Meta · LinkedIn",
 "Make every ad dollar <em>count.</em>", "Quote my ads", "final_paid")

# ---------- WEB DEVELOPMENT ----------
web_faq = clean(FAQ["web-development"])
service_page(
 "web-development", "/web-development", "Web development",
 "Web Development Agency USA | Websites & Funnels | Nov8rs",
 f"{BRAND} is a web development agency building fast, conversion-focused websites, landing pages, sales funnels and GoHighLevel builds.",
 dict(crumb="Web development", bg="bg-grid", kick="Web development services · Websites · Funnels",
      h1="Websites that <em>sell.</em> Funnels that <em>convert.</em>",
      intro=f"{BRAND} is a web development and conversion-focused agency. We build high-performing websites, landing pages and sales funnels, with GoHighLevel, ClickFunnels and automation connected so every visitor has a clear path to becoming a lead.",
      chips=["Web development services", "Custom websites", "Landing pages", "Sales funnels", "GoHighLevel"],
      slot="hero_web", cta="Quote my website",
      vis=f'<div class="vis" data-loop="web" style="width:100%">{V.laptop(True)}</div>'),
 [
  L.features([
    ("web", "Websites & custom development", "Responsive, SEO-ready websites built around your brand, audience and sales process."),
    ("funnel", "Landing pages & sales funnels", "One message, one offer, one action, with booking and follow-up steps built in."),
    ("plug", "GoHighLevel & ClickFunnels", "Websites, funnels, forms, calendars and pipelines built and connected inside your platform."),
    ("bolt", "Speed & Core Web Vitals", "Lightweight builds that load fast on phones, because slow pages lose leads."),
    ("search", "SEO-friendly foundations", "Clean structure, metadata, schema and internal linking ready for GAS-EO."),
    ("chart", "Tracking & CRO", "Analytics, conversion events and testing so the site keeps improving after launch."),
  ], band="paper", kick="What we build <span>// one development partner</span>", title="Websites, funnels and systems <em>built to convert.</em>",
     lead="From business websites to custom web development, we create fast, scalable digital experiences."),
  L.phases([
    dict(tag="Plan", h="Plan before development", p="Understand your business, audience, offer and the actions visitors should take.", deliv="Site map, funnel map & build plan",
         items=[("Goals & conversion actions", "The offers, audience needs and actions the site must support.", "STRATEGY"),
                ("Competitor & UX review", "Competing sites, positioning and user journeys.", "INTEL"),
                ("Architecture & integrations", "Pages, funnel steps, functionality and tools to connect.", "SCOPE")]),
    dict(tag="Build", h="Build every touchpoint", p="Responsive, conversion-focused pages with strong UX and the functionality you need.", deliv="Launched website & funnels",
         items=[("Website development", "Professional, responsive, SEO-ready builds.", "WEB"),
                ("Landing pages & funnels", "Journeys that guide visitors from click to enquiry or sale.", "FUNNELS"),
                ("GoHighLevel & ClickFunnels", "Platform builds configured around your sales process.", "PLATFORM")]),
    dict(tag="Connect", h="Connect & automate the journey", p="Forms, CRM, follow-up and automation so leads move without manual work.", deliv="Connected growth system",
         items=[("Conversion review", "Lead flow, drop-offs and behaviour analysed after launch.", "DATA"),
                ("Optimisation", "Messaging, CTAs and funnel steps refined on real data.", "CRO"),
                ("CRM & automation", "Form-to-CRM routing, reminders and workflows.", "AUTOMATE")]),
  ], kick="The Nov8rs build method <span>// plan · build · connect</span>", title="From website strategy to <em>conversion.</em>",
     lead="We don't build a site and hand it over. We plan it, build it and connect it to the rest of your growth system.", bgimg="bg-grid"),
  L.outcomes([
    ("Website", "A site built around your customers.", ["Strategy", "Design", "Launch"], "Every page has a job, and every job ends in a clear next step."),
    ("Funnels", "Turn traffic into leads.", ["Landing page", "Funnel", "Booking"], "Focused pages for campaigns, offers and lead magnets."),
    ("Systems", "One connected growth system.", ["Website", "CRM", "Follow-up"], "Your site, funnels and follow-up working as one."),
  ], kick="What you get <span>// built for growth</span>", title="Digital experiences that <em>attract, convert and grow.</em>",
     lead="Web development is more than putting pages online. It's the engine your ads, SEO and CRM all run through.", slot="outcomes_web", label="Build my custom quote"),
  L.chips(["Custom code", "WordPress", "Webflow", "Shopify", "GoHighLevel", "ClickFunnels", "Vercel", "Cloudflare", "Stripe", "Zapier", "n8n", "GA4"],
          "Built on the stack <em>that fits.</em>", "Platforms"),
 ], web_faq, "Web development services", "Web development", "Websites · Landing pages · Funnels",
 "Let's build something that <em>sells.</em>", "Quote my website", "final_web")

# ---------- AI CRM ----------
crm_faq = [
 ("What is the Nov8rs AI CRM?", "It's our own CRM and automation platform with AI built in. It brings calls, texts, emails, chats and social messages into one inbox, then uses AI agents and workflows to reply, qualify, book appointments and request reviews automatically."),
 ("What is missed call text back?", "When a call goes unanswered, the system instantly sends the caller a text so the conversation continues. Our AI agent can then answer questions, qualify the lead and offer appointment times, so a missed call no longer means a lost customer."),
 ("Can AI agents make outbound calls?", "Yes. AI voice agents can call new leads, follow up on quotes and confirm appointments, using a script and tone you approve. Calls are logged in the CRM so your team can see every conversation."),
 ("Can the AI CRM request reviews automatically?", "Yes. Automated review requests go out after a job is marked complete, by text or email, with a direct link to your Google review page. Happy customers get a nudge and your reputation grows without manual chasing."),
 ("Will it work with my website and ads?", "Yes. Website forms, landing pages, ad lead forms, calendars and phone numbers all feed the same pipeline. That's how we track a lead from the first click to the booked job."),
 ("Is it a replacement for HubSpot or Zoho?", "For many service businesses, yes. It covers CRM, pipelines, inbox, booking, automation and reviews in one place, often at a lower cost than stitching several tools together. If you need to keep an existing CRM, we can integrate instead."),
 ("Do you set everything up for me?", "Yes. Nov8rs (Innovators) sets up your pipelines, inbox, calendars, workflows, AI agent prompts and integrations, then trains your team. We keep improving the automations as we see real lead data."),
 ("Can agencies resell the AI CRM?", "Yes. We offer a white label CRM option for agencies that want to provide their clients a branded CRM and automation platform. See our white-label page or build a partner quote."),
]
service_page(
 "ai-crm", "/ai-crm", "AI CRM",
 f"AI CRM & Marketing Automation | {BRAND}",
 f"The {BRAND} AI CRM: missed call text back, AI voice and chat agents, booking, review requests and one inbox for every channel.",
 dict(crumb="AI CRM", bg="bg-network", kick="AI CRM · Marketing automation",
      h1="Every lead answered. <em>Every job booked.</em>",
      intro=f"The {BRAND} AI CRM puts every call, text, form and chat in one inbox, then lets AI agents do the follow-up: missed call text back, qualification, booking, reminders and review requests, around the clock.",
      chips=["Missed call text back", "AI voice agents", "Booking", "Review requests", "Unified inbox"],
      slot="hero_crm", cta="Quote my AI CRM",
      vis=f'<div data-loop="crm">{V.crm_phone()}</div>'),
 [
  L.features([
    ("phone", "Missed call text back", "Every unanswered call gets an instant text, so the lead keeps talking to you instead of calling a competitor."),
    ("mic", "AI voice & chat agents", "Agents that answer questions, qualify leads and make outbound calls in a tone you approve."),
    ("cal", "Booking & reminders", "Online booking, confirmations and reminders that cut no-shows."),
    ("star", "Automated review requests", "Review asks sent after every job, with a direct link to your Google profile."),
    ("inbox", "One inbox", "Calls, SMS, email, web chat, Facebook and Instagram messages in one place."),
    ("layers", "Pipelines & workflows", "Visual pipelines and business automation systems that move every lead to the next step."),
  ], band="paper", kick="What it does <span>// nothing slips</span>", title="Your follow-up, <em>on autopilot.</em>",
     lead="Most leads are lost after they reach out, not before. The AI CRM makes sure every one gets an answer in seconds."),
  L.phases([
    dict(tag="Map", h="Map your lead flow", p="We trace how leads arrive today and where they stall or go cold.", deliv="Lead flow map & automation plan",
         items=[("Channel audit", "Calls, forms, chats, ads and social messages.", "AUDIT"),
                ("Pipeline design", "Stages that match how you actually sell.", "PIPELINE"),
                ("AI agent brief", "Tone, questions and hand-off rules for your agents.", "AI")]),
    dict(tag="Build", h="Build the system", p="Pipelines, inbox, calendars, workflows and AI agents configured and connected.", deliv="Live AI CRM",
         items=[("Inbox & numbers", "Every channel feeding one conversation view.", "INBOX"),
                ("Workflows", "Text-back, reminders, nurture and review requests.", "AUTOMATE"),
                ("Integrations", "Website, ads, Stripe, calendars and existing tools.", "CONNECT")]),
    dict(tag="Improve", h="Improve on real conversations", p="We review transcripts and pipeline data, then tune agents and workflows.", deliv="Ongoing optimisation",
         items=[("Speed to lead", "Response times tracked and tightened.", "DATA"),
                ("Agent tuning", "Prompts refined on real questions.", "AI"),
                ("Reporting", "Leads, bookings and revenue by source.", "REPORT")]),
  ], kick="The setup <span>// map · build · improve</span>", title="Built around how <em>you sell.</em>",
     lead="No generic templates. We build the CRM around your services, team and customers.", bgimg="bg-trails"),
  L.chips(["Calls", "SMS", "Email", "Web chat", "Facebook", "Instagram", "Google Business Profile", "Calendars", "Stripe", "Zapier", "n8n", "OpenAI"],
          "Every channel. <em>One inbox.</em>", "Connects with"),
 ], crm_faq, "AI CRM and marketing automation", "Customer relationship management software", "Missed call text back · AI agents · Reviews",
 "Never miss <em>another lead.</em>", "Quote my AI CRM", "final_crm")

# ---------- WHITE LABEL ----------
wl_faq = clean(FAQ["white-label"])
wl_faq = [(q, a) if not q.startswith("How do I become") else
          (q, "Build a partner quote in our instant quote builder with the services you want fulfilled, or send us a message with your agency details, number of active clients and average client ticket. Our partnerships team will confirm the right fulfilment model.") for q, a in wl_faq]
service_page(
 "white-label", "/white-label", "White label",
 f"White Label Digital Marketing Agency | {BRAND}",
 f"White label digital marketing services from {BRAND}: white label SEO, PPC, web design, social media and CRM, delivered under your brand.",
 dict(crumb="White label", bg="bg-facets", kick="White label marketing agency · Agency fulfilment",
      h1="Your clients. Your brand. <em>Our fulfilment.</em>",
      intro=f"Scale your agency without scaling your overhead. {BRAND} provides white label digital marketing services you sell under your own brand, from white label SEO and Google Ads to web design, local SEO and social media management.",
      chips=["White label SEO services", "White label PPC", "White label web design", "White label social media", "White label CRM"],
      slot="hero_wl", cta="Get partner pricing",
      vis=f'<div data-loop="flow" style="width:100%">{V.wl_flow()}</div>'),
 [
  L.features([
    ("users", "Your team is stretched", "More clients mean more delivery pressure. Add capacity without adding salaries."),
    ("bolt", "Delivery shouldn't slow sales", "Sell with confidence while our specialists fulfil behind your brand."),
    ("shield", "Protect your margins", "Turn specialist delivery into a scalable service line with wholesale pricing."),
    ("search", "White label SEO & local SEO", "On-page, technical, content, GBP and reporting, fully unbranded."),
    ("ads", "White label PPC & Google Ads", "Setup, optimisation, tracking and reports under your agency's name."),
    ("web", "White label web design & social", "Websites, landing pages and social media management for your clients."),
  ], band="paper", kick="Built for agencies <span>// more capacity, better margins</span>", title="Grow your agency without <em>a bigger team.</em>",
     lead="White label digital marketing services built around your agency, your brand and your client relationships."),
  L.outcomes([
    ("Brief", "You win the client.", ["Requirements", "Scope", "Assets"], "Send the brief. We align it with your delivery model."),
    ("Fulfil", "We handle the delivery.", ["Plan", "Assign", "Fulfil"], "Specialists matched to the work, delivered behind your brand."),
    ("Deliver", "Your clients see your brand.", ["Review", "Deliver", "Report"], "Quality-checked work handed over as your own."),
  ], band="dark", kick="How it works <span>// you sell, we deliver</span>", title="You win the client. <em>We handle delivery.</em>",
     lead="A straightforward workflow that keeps your brand, client relationship and commercial control with you.", slot="outcomes_wl", label="Get partner pricing"),
  L.chips(["White label SEO", "White label local SEO", "White label PPC", "Google Ads fulfilment", "White label web design", "Landing pages", "WordPress builds", "GoHighLevel", "White label CRM", "Social media management", "Content", "Reporting"],
          "Your systems. <em>Our fulfilment.</em>", "What we fulfil", band="paper"),
 ], wl_faq, "White label digital marketing services", "White label marketing", "White label SEO · PPC · Web · Social",
 "Add capacity, <em>keep the margin.</em>", "Get partner pricing", "final_wl")

# =====================================================================
# CONTACT (the one buried secondary CTA)
# =====================================================================
contact_body = f"""
<section class="band dark phero" aria-label="Contact">
  <div class="bgimg" style="--bgimg:{L.bgurl('bg-facets')}" aria-hidden="true"></div>
  <div class="wrap pgrid" style="align-items:start">
    <div>
      <nav class="crumbs" aria-label="Breadcrumb"><a href="{url('/')}">Home</a><span aria-hidden="true">/</span><span aria-current="page">Contact</span></nav>
      <p class="kick mono"><i></i>Contact {BRAND}</p>
      <h1 class="ph1">Let's talk about <em>your business.</em></h1>
      <p class="pintro">Tell us where you are, where you want to go and what's in the way. We reply within one business day.</p>
      <p class="pintro">Want a price right now? The quote builder is faster.</p>
      <div class="ctas" style="margin-top:24px">{quote('contact_page', 'Get my instant quote')}</div>
      <p class="micro" style="margin-top:24px">Or email <span style="user-select:all;color:var(--silver)">{L.EMAIL}</span></p>
    </div>
    <div class="formcard hc">
      <form id="contactForm" class="form" novalidate>
        <label>Your name<input id="f-name" name="name" autocomplete="name" required></label>
        <label>Company<input id="f-company" name="company" autocomplete="organization"></label>
        <label>Email<input id="f-email" name="email" type="email" autocomplete="email" required></label>
        <label>Phone<input id="f-phone" name="phone" type="tel" autocomplete="tel"></label>
        <label class="full">Website<input id="f-site" name="website" type="url" inputmode="url" placeholder="https://"></label>
        <fieldset class="full" style="border:0;padding:0;margin:0"><legend style="font:600 14px var(--display);margin-bottom:8px">I'm a</legend>
          <div class="seg"><label><input type="radio" name="profile" value="Business" checked> Business</label><label><input type="radio" name="profile" value="Agency"> Agency</label></div></fieldset>
        <label class="full">What do you need?<select id="f-need" name="need"><option>Not sure yet</option><option>Website or funnels</option><option>GAS-EO (SEO, AEO, GEO)</option><option>Paid media</option><option>AI CRM &amp; automation</option><option>White label fulfilment</option></select></label>
        <label class="full">Message<textarea id="f-msg" name="message" placeholder="What are you looking to solve?"></textarea></label>
        <div class="full"><button class="btn" type="submit">Send message {L.ARROW}</button></div>
        <p class="formmsg" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>
"""
page(slug="contact", path="/contact", active="/contact", title=f"Contact {BRAND}",
     desc=f"Contact {BRAND} about websites, GAS-EO, paid media, AI CRM or white label fulfilment. Or get your instant quote online.",
     body=contact_body, og_sub="We reply within one business day",
     schema=[L.ORG, L.crumbs_schema("Contact", "/contact")])

# =====================================================================
# LEGAL (drafts — review before launch)
# =====================================================================
def legal(slug, name, sections):
    s = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{p}</p>" for p in ps) for h, ps in sections)
    body = f"""<section class="band dark phero" aria-label="{name}"><div class="wrap"><nav class="crumbs" aria-label="Breadcrumb"><a href="{url('/')}">Home</a><span aria-hidden="true">/</span><span aria-current="page">{name}</span></nav>
<h1 class="ph1">{name}</h1><p class="pintro">Last updated: [DATE]. Draft for review before launch.</p></div></section>
<section class="band dark sec" style="padding-top:0"><div class="wrap prose">{s}</div></section>"""
    page(slug=slug, path="/" + slug, active="/" + slug, title=f"{name} | {BRAND}", desc=f"{name} for the {BRAND} website.",
         body=body, og_sub=name, robots="noindex,follow", schema=[L.ORG])

legal("privacy", "Privacy policy", [
 ("Who we are", [f"{BRAND} (“we”, “us”) runs this website. Contact us at {L.EMAIL}. [ADD LEGAL ENTITY NAME AND ADDRESS]"]),
 ("What we collect", ["Information you give us through our contact form or quote builder, such as your name, company, email, phone, website and message.", "Basic usage data from analytics tools, such as pages visited and device type."]),
 ("How we use it", ["To reply to you, prepare quotes, deliver services you request and improve our website. We do not sell your personal information."]),
 ("Sharing", ["We use service providers to run our CRM, analytics and hosting. They process data on our behalf. [LIST PROVIDERS]"]),
 ("Your choices", [f"You can ask us to access, correct or delete your information by emailing {L.EMAIL}."]),
])
legal("terms", "Terms of use", [
 ("Using this website", [f"By using this website you agree to these terms. The content is for general information about {BRAND} services."]),
 ("Quotes", ["Prices shown in the quote builder are estimates until confirmed in a signed agreement. [ADD YOUR TERMS]"]),
 ("Intellectual property", [f"All content on this site belongs to {BRAND} unless stated otherwise."]),
 ("Liability", ["[ADD LIABILITY AND GOVERNING LAW TERMS]"]),
])

# =====================================================================
# 404
# =====================================================================
nf_body = f"""<section class="band dark phero" aria-label="Page not found" style="min-height:80vh">
  <canvas class="rain" data-density=".8" aria-hidden="true"></canvas>
  <div class="wrap center"><img src="{asset('assets/img/bulb.webp')}" alt="" width="200" height="200" style="width:200px;filter:grayscale(.6) brightness(.35)">
  <p class="kick mono" style="margin-top:24px"><i></i>404</p><h1 class="ph1">This idea <em>didn't light up.</em></h1>
  <p class="pintro" style="margin-inline:auto">The page you're looking for has moved or never existed.</p>
  <div class="ctas" style="justify-content:center;margin-top:28px"><a class="btn ghost" href="{url('/')}">Back to home</a>{quote('404', 'Get my instant quote')}</div></div>
</section>"""
page(slug="404", path="/404", active="", title=f"Page not found | {BRAND}", desc="This page could not be found.", body=nf_body, og_sub="", robots="noindex", schema=[])

# =====================================================================
# WRITE
# =====================================================================
if os.path.exists(OUT):
    shutil.rmtree(OUT)
shutil.copytree("site", OUT)
for p in pages:
    p.setdefault("og_title", p["title"])
    p["slug"] = p["slug"] if p["slug"] != "404" else "home"
    html = L.head(p) + L.header(p["active"]) + f'<main id="main">{p["body"]}</main>' + L.footer()
    if p["path"] == "/404":
        name = "404.html"
    elif p["path"] == "/":
        name = "index.html"
    else:
        name = p["path"].strip("/") + ".html"
    open(os.path.join(OUT, name), "w").write(html)

# sitemap / robots / vercel / manifest
idx = [p for p in pages if "noindex" not in p.get("robots", "")]
pri = {"/": "1.0"}
sm = "\n".join(f"  <url><loc>{SITE}{'/' if p['path']=='/' else p['path']}</loc><lastmod>2026-11-09</lastmod><priority>{pri.get(p['path'], '0.8')}</priority></url>" for p in idx)
open(f"{OUT}/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
open(f"{OUT}/llms.txt", "w").write(
f"""# {BRAND}

> Nov8rs (pronounced “innovators”) is a US-focused digital marketing agency. Services: websites and funnels, GAS-EO (SEO + AEO + GEO), paid media (Google, Microsoft, Meta, LinkedIn), the Nov8rs AI CRM, and white label fulfilment for agencies.

- [Home]({SITE}/): overview, method and FAQ
- [SEO & GAS-EO]({SITE}/seo-services): SEO, answer engine and generative engine optimization
- [Paid media]({SITE}/paid-media-agency): PPC and performance marketing
- [Web development]({SITE}/web-development): websites, landing pages, funnels, GoHighLevel, ClickFunnels
- [AI CRM]({SITE}/ai-crm): missed call text back, AI agents, booking, review requests
- [White label]({SITE}/white-label): agency fulfilment under your brand
- [Instant quote]({L.QUOTE}): pick services and see pricing
""")
open(f"{OUT}/site.webmanifest", "w").write(json.dumps({"name": BRAND, "short_name": "Nov8rs", "start_url": "/", "display": "standalone", "background_color": "#070707", "theme_color": "#070707",
    "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=1))
vercel = {"cleanUrls": True, "trailingSlash": False,
  "headers": [
    {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=31536000, immutable"}]},
    {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "X-Frame-Options", "value": "SAMEORIGIN"}, {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=()"}]},
    {"source": "/(.*)", "has": [{"type": "host", "value": "(?<sub>.*)\\.vercel\\.app"}], "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]}],
  "redirects": [
    {"source": "/seo", "destination": "/seo-services", "permanent": True},
    {"source": "/gas-eo", "destination": "/seo-services", "permanent": True},
    {"source": "/ads", "destination": "/paid-media-agency", "permanent": True},
    {"source": "/paid-media", "destination": "/paid-media-agency", "permanent": True},
    {"source": "/crm", "destination": "/ai-crm", "permanent": True},
    {"source": "/quote", "destination": L.QUOTE, "permanent": False}]}
open(f"{OUT}/vercel.json", "w").write(json.dumps(vercel, indent=2))

# OG images
from PIL import Image, ImageDraw, ImageFont
def font(size, w="ExtraBold"):
    for f in [f"/usr/share/fonts/opentype/inter/Inter-{w}.otf", "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]:
        if os.path.exists(f): return ImageFont.truetype(f, size)
    return ImageFont.load_default()
os.makedirs(f"{OUT}/assets/img/og", exist_ok=True)
base = Image.open("site/assets/img/og-base.png").convert("RGB")
seen = set()
for p in pages:
    if p["slug"] in seen or p["path"] == "/404": continue
    seen.add(p["slug"])
    im = base.copy(); d = ImageDraw.Draw(im)
    d.text((70, 70), "NOV8RS", font=font(30), fill=(242, 242, 239))
    d.text((70, 108), "INNOVATORS", font=font(16, "Medium"), fill=(217, 164, 65))
    t = re.sub(r"\s*\|.*$", "", p["og_title"]).replace(f" {BRAND}", "").strip(" ·|") or BRAND
    words, lines, cur = t.split(), [], ""
    for w in words:
        if len(cur + " " + w) > 20: lines.append(cur.strip()); cur = w
        else: cur += " " + w
    lines.append(cur.strip())
    y = 250
    for ln in lines[:3]:
        d.text((70, y), ln, font=font(58), fill=(242, 242, 239)); y += 70
    d.text((70, y + 18), p.get("og_sub", ""), font=font(24, "Medium"), fill=(229, 180, 84))
    im.save(f"{OUT}/assets/img/og/{p['slug']}.jpg", quality=84, optimize=True)
os.remove(f"{OUT}/assets/img/og-base.png")
print("built", OUT, [p["path"] for p in pages])
