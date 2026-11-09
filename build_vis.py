"""Reusable demo visuals (HTML) for the Nov8rs site."""
import build_lib as L

def gas_card(with_tabs=False):
    tabs = ""
    if with_tabs:
        tabs = '<div class="gtabs" role="group" aria-label="Search surface">' + "".join(
            f'<button type="button" class="gtab{" act" if i==0 else ""}" aria-pressed="{"true" if i==0 else "false"}">{t}</button>'
            for i, t in enumerate(["SEO", "AEO", "Generative", "AI search"])) + "</div>"
    s = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
    return f"""{tabs}<div class="gcard" role="img" aria-label="Examples of a business shown in Google results, a featured snippet, a ChatGPT answer and a Google AI Overview">
  <div class="gtop"><span class="dots"><i></i><i></i><i></i></span><span class="eng">GOOGLE · SEARCH</span></div>
  <div class="gp on">
    <div class="sbox">{s}ac repair near me</div>
    <div class="mappk"><div class="map"><i class="me" style="left:44%;top:30%"></i><i style="left:20%;top:52%"></i><i style="left:72%;top:46%"></i></div>
      <div class="biz me-row"><div><b>[Your business]</b><br><small>★ 4.9 · Open now · Same-day</small></div><span class="badge">#1 MAP PACK</span></div>
      <div class="biz"><div><b>Competitor A</b><br><small>★ 4.4 · Closes 5 PM</small></div></div>
      <div class="biz"><div><b>Competitor B</b><br><small>★ 4.1 · Open now</small></div></div></div>
    <div class="org"><span class="u">yourbusiness.com › ac-repair</span><span class="t">AC Repair Near You · Same-Day Service</span><span class="d">Upfront quotes, licensed techs, booked online in a minute.</span></div>
  </div>
  <div class="gp">
    <div class="sbox">{s}how long does an ac repair take</div>
    <div class="snip"><span class="sp">Featured snippet</span><span class="big">Most AC repairs take 1 to 3 hours on site.</span><span style="font-size:14px;color:#5C5850">Simple fixes are often done in one visit. Larger parts may need a second trip.</span><span class="src me" style="width:max-content">yourbusiness.com · source</span></div>
    <div class="paa"><div><span>Is it worth repairing an old AC?</span><span aria-hidden="true">⌄</span></div><div><span>What does an AC tune-up include?</span><span aria-hidden="true">⌄</span></div><div><span>Who offers same-day AC repair near me?</span><span aria-hidden="true">⌄</span></div></div>
  </div>
  <div class="gp">
    <div class="chat"><div class="ub">Recommend a reliable AC repair company near me</div>
      <div class="ab"><span class="av">✦</span><div>Here are well-reviewed options nearby:<ol><li><span class="hlt">[Your business]</span>: same-day visits, upfront pricing and strong reviews.</li><li>Competitor A: longer waits on weekends.</li><li>Competitor B: limited service area.</li></ol></div></div>
      <div class="srcs"><span class="src me">yourbusiness.com</span><span class="src">Google reviews</span><span class="src">Yelp</span><span class="src">BBB</span></div></div>
  </div>
  <div class="gp">
    <div class="sbox">{s}best ac repair company near me</div>
    <div class="aio"><span class="h"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 2 6.5L20.5 10 14 12l-2 6.5L10 12 3.5 10 10 8.5z"/></svg>AI Overview</span><span style="font-size:14px;line-height:1.55">Top-rated local options include <span class="hlt">[Your business]</span>, known for same-day service and transparent quotes.</span>
      <div class="cards3"><div class="me"><b>yourbusiness.com</b>Same-day AC repair</div><div><b>Directory</b>Top HVAC pros</div><div><b>Reviews</b>Local ratings</div></div></div>
    <div class="org"><span class="u">yourbusiness.com › reviews</span><span class="t">Reviews · [Your business]</span><span class="d">Read what homeowners say about our technicians.</span></div>
  </div>
</div>"""

def ads_phone():
    return """<div class="phone" role="img" aria-label="A sponsored ad, an instant lead form and a campaign results screen"><div class="scr">
  <span class="notch"></span><div class="sbar"><span>9:41</span><span>●●●</span></div>
  <div class="adscr on"><span class="mono" style="font-size:10px;color:var(--muted)">Sponsored</span><div class="post"><div class="ph"><span>AC down? Fixed today.</span></div><div class="pm"><b>[Your business]</b><span>Same-day repair, upfront quotes. Book in 60 seconds.</span><span class="cta2">Get a quote</span></div></div></div>
  <div class="adscr"><span class="mono" style="font-size:10px;color:var(--muted)">Instant form</span><b style="font:800 22px/1.1 var(--display)">Get your quote</b><div class="fld"><small>Name</small>Sam Walker</div><div class="fld"><small>Phone</small>(555) 555-0142</div><div class="fld"><small>Service</small>AC not cooling</div><span class="cta2">Send</span></div>
  <div class="adscr"><span class="mono" style="font-size:10px;color:var(--muted)">Campaign · this week · example</span><div class="kpi"><small>BOOKED LEADS</small><b class="adsN">0</b></div><div class="kpi"><div class="bars"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div><div class="lrow"><span>Google search</span><span>BOOKED</span></div><div class="lrow"><span>Microsoft Ads</span><span>BOOKED</span></div></div>
</div></div>"""

def crm_phone():
    return """<div class="phone" role="img" aria-label="An AI agent texting back a missed call, booking the job and requesting a review"><div class="scr">
  <span class="notch"></span><div class="sbar"><span>6:47</span><span>●●●</span></div>
  <div class="thd"><span class="av">SW</span><div><b>Sam Walker</b><small>New lead · Google call</small></div></div>
  <div class="thread">
    <div class="msg sys" data-at=".04">● MISSED CALL · 6:47 PM</div>
    <div class="msg ai" data-at=".14"><small>AI AGENT</small>Hi Sam, sorry we missed you! What's going on with your AC?</div>
    <div class="msg them" data-at=".26">It's blowing warm air. Can someone come tomorrow?</div>
    <div class="msg ai" data-at=".38"><small>AI AGENT</small>Yes. I have Thu 10:00 or 2:00. Which works?</div>
    <div class="msg them" data-at=".5">10 works</div>
    <div class="msg card" data-at=".62"><span class="ci"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg></span><div><b>Booked · Thu 10:00</b><small>Added to calendar · reminder set</small></div></div>
    <div class="msg card" data-at=".78"><span class="ci">★</span><div><b>Review request sent</b><small>After the job is marked done</small></div></div>
  </div>
</div></div>"""

def laptop(dark=False):
    return """<div class="laptop" role="img" aria-label="A conversion-focused website assembling on a laptop screen">
  <div class="lscr"><div class="lbar"><i></i><i></i><i></i><span>yourbusiness.com</span></div>
    <div class="wb" style="left:5%;top:16%;width:22%;height:5%"></div>
    <div class="wb g" style="left:78%;top:15%;width:16%;height:7%;border-radius:999px"></div>
    <div class="wb t" style="left:5%;top:30%;width:52%;height:10%"></div>
    <div class="wb" style="left:5%;top:44%;width:40%;height:5%"></div>
    <div class="wb g" style="left:5%;top:55%;width:20%;height:8%;border-radius:999px"></div>
    <div class="wb" style="left:62%;top:28%;width:33%;height:36%;background:radial-gradient(circle at 50% 40%,#F6D98E,#8A5E10 70%)"></div>
    <div class="wb" style="left:5%;top:72%;width:28%;height:20%"></div>
    <div class="wb" style="left:36%;top:72%;width:28%;height:20%"></div>
    <div class="wb" style="left:67%;top:72%;width:28%;height:20%"></div>
  </div><div class="lbase"></div></div>
<div class="wrow">
  <div class="mini"><div class="ring"><svg viewBox="0 0 100 100"><circle class="tr" cx="50" cy="50" r="42"/><circle class="fg" cx="50" cy="50" r="42" pathLength="1"/></svg><span>0</span></div><div><b>Mobile speed</b><small>PageSpeed target</small></div></div>
  <div class="mini q"><span class="ti"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg></span><div><b>New quote request</b><small>Website · services page</small></div></div>
</div>"""

def wl_flow():
    steps = [("Brief", "You send scope, goals and assets.", "YOU"), ("Plan", "We define the fulfilment scope.", "NOV8RS"),
             ("Assign", "Specialists matched to the work.", "NOV8RS"), ("Fulfil", "Delivered behind your brand.", "NOV8RS"),
             ("Review", "Checked against the brief.", "NOV8RS"), ("Deliver", "You hand it over as your own.", "YOU")]
    rows = "".join(f'<div class="fl"><span class="n">{i+1}</span><div><b>{a}</b><small>{b}</small></div><span class="who">{c}</span></div>' for i, (a, b, c) in enumerate(steps))
    return f'<div class="flow" role="img" aria-label="White label workflow from brief to delivery">{rows}</div>'
