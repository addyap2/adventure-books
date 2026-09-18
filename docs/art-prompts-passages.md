# The Address — painted-art prompt pack (per passage)

One prompt for every one of the 123 passages, in a single locked style. Generate each with
any image model, export **WebP 1200×800, ≤120 KB**, and drop it at the filename shown — the
reader loads it automatically and it replaces the emblem for that passage. No code changes.

## The one rule: consistency
All 123 must feel like one hand. Lock the style below, generate the first five, agree the look,
then hold it. Reuse a **style reference image** (or a fixed seed / `--sref`) across the whole set,
and keep a **character reference** for the recurring people (Ms Rowe ~60 with a takeaway coffee;
the good-suited agency man; the kiosk woman; the fellow traveller Mara; the girl at the window) —
always faceless or from behind.

## Locked style (prepend to every prompt — already baked into the CSV)

> Painterly atmospheric illustration, cinematic nocturne: a cold, unfamiliar city at night lit by a single warm sodium-amber source against deep navy-and-teal blues; limited muted palette, soft volumetric fog, gentle film grain and visible painterly brushwork; faceless viewpoint — show the world from behind or over the shoulder, or only hands and objects, never a clear face or eye contact; culturally neutral modern European-ish port city, no readable text or signage, no flags or landmarks; quiet, uncertain, atmospheric but not frightening.

**Framing:** 3:2 landscape, subject held in the central 90%, cinematic lighting.

**Negative:** no text, no lettering, no watermark, no logos, no visible faces or eye contact, no bright saturated colours, no daytime blue sky, no cartoon style.

## Delivery
- WebP, quality ~80, ≤120 KB (hard ceiling 200 KB — phone-first, mobile data).
- 3:2, 1200×800; keep the subject in the central 90% (cards crop on tall phones).
- File path: `images/new-city/ep-01/<passage-id>.webp` (e.g. `1.webp`).
- Full ready-to-run prompts (style + scene + negative) are in `content/art/episode-01.prompts.csv`.

## The 123 passages

- **§1** · _station_ · `1.webp` — An almost-empty night railway platform under cold light; a lone traveller with a small case and a letter, seen from behind.
- **§2** · _map_ · `2.webp` — A tired night clerk at a lit information window sliding across a small hand-drawn map; an unread letter on the counter.
- **§3** · _taxi_ · `3.webp` — A wet station forecourt at night, three idling taxis and a bus-stop sign, cold river air, breath visible.
- **§4** · _bus_ · `4.webp` — The warm, near-empty interior of a night bus; a letter reread on an empty seat, dark wet streets sliding past the window.
- **§5** · _kiosk_ · `5.webp` — A woman pulling down the shutter of a corner kiosk on an empty night street — the only person around.
- **§6** · _taxi_ · `6.webp` — The view from a taxi's back seat, the driver laughing over his shoulder, an empty night avenue ahead.
- **§7** · _building_ · `7.webp` — A grey, dusty, abandoned office building behind builders' hoarding at night; a dark doorway and an old dead sign.
- **§8** · _bus_ · `8.webp` — A night bus halted at its last stop, the driver glancing back; an empty depot, one in the morning, no more buses.
- **§9** · _kiosk_ · `9.webp` — A kiosk woman pointing down a dark corner toward a distant café light, a letter in her other hand.
- **§10** · _bed_ · `10.webp` — A small, clean, cheap hotel lobby at night; a key on the desk, a yellow agency sign glimpsed across the road.
- **§11** · _window_ · `11.webp` — Looking through a dusty office window: an overturned chair, a stopped calendar, one small light behind a glass door at the back.
- **§12** · _door_ · `12.webp` — A neighbour's half-open door at night, a figure in a dressing gown, warm hall light spilling onto the step.
- **§13** · _bench_ · `13.webp` — A hard station bench at first light, a coat pulled close, a cleaner's trolley approaching.
- **§14** · _lamp_ · `14.webp` — Empty repeating night streets and a single street lamp; back near the station at three in the morning, nothing learned.
- **§15** · _card_ · `15.webp` — A business card taped inside a dark café window, a new address just legible; cold hands raising a phone to photograph it.
- **§16** · _bed_ · `16.webp` — A small clean room at first light, its window looking down on a big yellow agency sign across the road.
- **§17** · _building_ · `17.webp` — The empty abandoned building at eight in the morning, grey and shut, an hour before the interview.
- **§18** · _door_ · `18.webp` — A cleaner half-opening an inner glass door onto empty offices, waving you away.
- **§19** · _quay_ · `19.webp` — Walking toward the river near two in the morning; new all-glass offices dark across the black water.
- **§20** · _building_ · `20.webp` — A cold grey morning, exhausted, standing before the empty building.
- **§21** · _cup_ · `21.webp` — A warm, expensive café at night — a cup and a letter on the table — weighing whether to go on.
- **§22** · _bench_ · `22.webp` — A station bench at eight in the morning, numb feet, the pull to simply go home.
- **§23** · _quay_ · `23.webp` — A new riverside building's brass company directory; the fourth name legible only as a name-plate, second floor.
- **§24** · _suit_ · `24.webp` — A too-bright new job-agency office, a yellow sign, a man in a good suit sliding a form across the counter.
- **§25** · _quay_ · `25.webp` — The river quay at half past eight, grey water and gulls, arriving early and almost clean.
- **§26** · _door_ · `26.webp` — A young woman opening a door at night, pointing toward a night bus at the corner.
- **§27** · _keys_ · `27.webp` — A woman arriving at a riverside door with a key and a coffee — she turns out to be the firm.
- **§28** · _quay_ · `28.webp` — Identical dark quay buildings at night; the number you found is only a car park, so you sit by the water.
- **§29** · _card_ · `29.webp` — A café counter at night, a hand writing an address on a paper napkin.
- **§30** · _desk_ · `30.webp` — A warm reception desk smelling of coffee, a name typed twice on a screen, no interview found.
- **§31** · _cup_ · `31.webp` — A woman near sixty approaching a glass door with a takeaway coffee; a small yellow luggage tag on her bag.
- **§32** · _coin_ · `32.webp` — A plain receipt bearing only a number, money just handed across a counter and gone.
- **§33** · _coin_ · `33.webp` — Across a desk, a good-suited man's smile vanishing as the form is pushed back, unpaid.
- **§34** · _letter_ · `34.webp` — Quarter past nine on an empty street; a now-useless letter in hand, pockets nearly empty.
- **§35** · _desk_ · `35.webp` — An office over the water; a woman reading your letter, a chair drawn up for you.
- **§36** · _desk_ · `36.webp` — Warm office light at last — a desk, a tray of letters to correct, a job honestly begun.
- **§37** · _notebook_ · `37.webp` — A hand writing your name on a real sheet of paper; a door held open to the street.
- **§38** · _desk_ · `38.webp` — On an office step, a woman turning and half-smiling, recognised before a word is said, warm morning.
- **§39** · _coin_ · `39.webp` — A locked glass door with an empty office behind it and a receipt bearing only a number.
- **§40** · _board_ · `40.webp` — A departures board at a station, a two-o'clock train back the way you came.
- **§41** · _companions_ · `41.webp` — An emptying platform; a young traveller with a big backpack rereading a scrap of paper, as lost as you.
- **§42** · _companions_ · `42.webp` — Two travellers with cases under station light comparing addresses — for a moment, not alone.
- **§43** · _kiosk_ · `43.webp` — A newsstand man at night reading your letter among stacks of papers.
- **§44** · _kiosk_ · `44.webp` — A kiosk man gesturing toward the river, explaining the firm moved years ago.
- **§45** · _sign_ · `45.webp` — A torn old company notice on builders' hoarding, a marker word and an arrow pointing east.
- **§46** · _door_ · `46.webp` — A narrow side door at night with a thin line of warm light beneath it.
- **§47** · _door_ · `47.webp` — A woman leaving an office, pulling on her coat, gesturing toward the river.
- **§48** · _bench_ · `48.webp` — A station bench at night; a man with only a paper cup, no bag and no coat, quietly beside you.
- **§120** · _desk_ · `120.webp` — A question across a desk: why hire a stranger arrived almost by chance.
- **§121** · _coin_ · `121.webp` — Recounting the agency that nearly took the last of your money; you were right to walk away.
- **§141** · _desk_ · `141.webp` — A plain handshake in a plain office, morning light — everything earned.
- **§142** · _desk_ · `142.webp` — Walking in rested and owing nothing, the river bright through the office window.
- **§143** · _notebook_ · `143.webp` — A hand closing a notebook with your name in it, the city going on outside.
- **§144** · _suit_ · `144.webp` — New carpet, a lanyard, a screen — everything correct and nothing felt.
- **§145** · _keys_ · `145.webp` — A borrowed kettle and a spare key on a stranger's table — not hired, not alone.
- **§146** · _notebook_ · `146.webp` — A closed appointment diary and full chairs in a reception, a kind final shake of the head.
- **§147** · _bench_ · `147.webp` — Grey morning over an empty bench, nine o'clock come and gone, too cold to move.
- **§49** · _lamp_ · `49.webp` — The same closed shop passing twice, a useless map, the city belonging to no one at one in the morning.
- **§50** · _lamp_ · `50.webp` — A lone all-night launderette spilling yellow light; an attendant folding towels, sketching a route.
- **§51** · _door_ · `51.webp` — A glass door at the back, a name half-scraped away, still reading as a surname.
- **§52** · _window_ · `52.webp` — A lit upstairs window; a child of about ten watching the street, quite calm.
- **§53** · _bus_ · `53.webp` — A night bus surging past, warm yellow windows, only seconds to decide.
- **§54** · _bridge_ · `54.webp` — A bridge over black water; dark glass offices on the far bank and one window lit high up, a crescent moon.
- **§55** · _quay_ · `55.webp` — A night watchman leaning from a lit booth at the new offices, waving you in to warm up.
- **§56** · _card_ · `56.webp` — A closed café at night, a light at the back, someone stacking chairs, a card on the glass.
- **§57** · _cup_ · `57.webp` — A café door opened on its chain; a voice telling you the woman comes each morning for coffee.
- **§58** · _cup_ · `58.webp` — A station cleaner pouring half a cup from a thermos at dawn.
- **§59** · _companions_ · `59.webp` — A modest breakfast table; a fellow traveller warning against the agency across the road.
- **§60** · _suit_ · `60.webp` — A queue before a yellow WORK-FOR-ALL sign at dawn, tired faces, breath in the cold.
- **§61** · _suit_ · `61.webp` — A good-suited man sliding a registration form across a counter, hand out for the money.
- **§62** · _coin_ · `62.webp` — A man leaning on a wall outside, a receipt like yours in hand, never called back.
- **§63** · _envelopes_ · `63.webp` — A reception tray of returned letters, old crossed-out addresses, one of them yours.
- **§65** · _taxi_ · `65.webp` — From a taxi at night, the driver warning about the agencies near the station.
- **§67** · _quay_ · `67.webp` — Grey dawn on the river quay: a coffee cart opening, delivery vans, gulls on grey water.
- **§68** · _suit_ · `68.webp` — Watching the quay doors; the agency's good-suited man entering a nameless building two doors down.
- **§69** · _letter_ · `69.webp` — An open bag under a lamp — a letter, a little money, a photograph left unturned.
- **§72** · _phone_ · `72.webp` — A phone showing a single bar of battery, night, an unfamiliar city — a kind of countdown.
- **§73** · _phone_ · `73.webp` — An old web page loading a riverside address, then a black dead screen, a paper letter left in hand.
- **§75** · _companions_ · `75.webp` — Two travellers deciding to go on together rather than walk the wrong way alone at night.
- **§77** · _station_ · `77.webp` — A guard switching off station lights bench by bench, the great hall darkening, cold coming in.
- **§79** · _bus_ · `79.webp` — The city sliding dark and wet past a bus window, weighing whether to get off early.
- **§84** · _desk_ · `84.webp` — A kind receptionist reading the night on you — creased coat, tired eyes — but saying nothing.
- **§85** · _desk_ · `85.webp` — An office over the water; your own letter, returned to sender, lying on the desk.
- **§86** · _letter_ · `86.webp` — An explanation across a desk: someone has sent the old address for two years; you came anyway.
- **§88** · _keys_ · `88.webp` — A woman on the office step, coffee and keys in hand, waving you in out of the cold.
- **§89** · _quay_ · `89.webp` — The quay waking — gulls, a coffee cart, vans — time to spare and clean hands after a hard night.
- **§90** · _suit_ · `90.webp` — The agency's good-suited man meeting your eyes, then vanishing into a nameless building.
- **§91** · _companions_ · `91.webp` — Another candidate confiding, close by, that they nearly paid the agency too.
- **§92** · _bridge_ · `92.webp` — Through a window, the bridge you crossed in the dark, now grey and ordinary by day.
- **§94** · _desk_ · `94.webp` — A manager and a blushing young colleague over old letterhead, resolving to fix it.
- **§95** · _kiosk_ · `95.webp` — A kiosk woman pointing to a passage behind a building, through a courtyard.
- **§96** · _envelopes_ · `96.webp` — A courtyard tray of envelopes ready to post — all addressed to the wrong old street.
- **§97** · _window_ · `97.webp` — A child leaning from an upper window, telling you the firm is at the river now.
- **§98** · _window_ · `98.webp` — A child's directions given from a window — a bus number, an address — then the window closing.
- **§99** · _oars_ · `99.webp` — A lit boathouse by the water at night, long oars carried toward the river, low voices.
- **§100** · _oars_ · `100.webp` — A rower with an oar on the shoulder pointing straight on, past the second bridge.
- **§101** · _quay_ · `101.webp` — A lit, empty glass hall; a guard's cap on an abandoned desk, everything newer than your letter.
- **§102** · _cup_ · `102.webp` — The sky going from black to dishwater grey, feet gone numb, a café light finally coming on.
- **§103** · _cup_ · `103.webp` — A café regular looking up from his tea, recalling the firm — good people, bad with the post.
- **§104** · _bed_ · `104.webp` — A hotel owner warning against the yellow-sign agency across the road.
- **§105** · _bus_ · `105.webp` — The first warm, near-empty bus of the day, a choice of two directions.
- **§106** · _fence_ · `106.webp` — A fenced, weedy empty lot behind the agency — no job that was ever real.
- **§107** · _suit_ · `107.webp` — A woman in the queue folding the form back, calling it a scam, leading others out.
- **§108** · _taxi_ · `108.webp` — A taxi through deserted streets, a night café's yellow light on wet tarmac, a fox.
- **§109** · _map_ · `109.webp` — A man at a window drawing a better map on the back of a receipt, marking the river.
- **§110** · _quay_ · `110.webp` — Walking toward the quay in rising light among people who know where they are going.
- **§111** · _bus_ · `111.webp` — A young woman going the same way, offering to show where to get off the bus.
- **§112** · _door_ · `112.webp` — Climbing an office stair, late and breathless, rehearsing an apology.
- **§113** · _cup_ · `113.webp` — A coffee-cart woman adding a free extra shot — a warm cup held in both hands, long night.
- **§114** · _letter_ · `114.webp` — A cold cup left untouched, the letter put away, standing to go on.
- **§115** · _lamp_ · `115.webp` — A deserted market square, stalls folded, wet cobbles under a lamp, a fox in the gutter.
- **§116** · _taxi_ · `116.webp` — A taxi idling at the curb, engine running, the driver reading a paper.
- **§117** · _notebook_ · `117.webp` — A cleaner propping a door with a foot, taking a note for the desk, no promise.
- **§118** · _phone_ · `118.webp` — Photographing a half-scraped name on glass, twice, as proof you came.
- **§119** · _card_ · `119.webp` — Stamping in the cold outside a café, staring at the card taped to the glass.
- **§122** · _taxi_ · `122.webp` — A night worker sharing a taxi — ten minutes where someone else knows the way.
- **§123** · _cup_ · `123.webp` — A warm watchman's booth, something poured from a thermos into a tin cup, before nine.
- **§124** · _cup_ · `124.webp` — A café queue where a name is overheard — two second-floor staff, so close now.
- **§125** · _companions_ · `125.webp` — A breakfast decision to walk to the river together.
- **§126** · _bench_ · `126.webp` — A station cleaner of twenty years urging you on, kindly and firmly.
- **§127** · _notebook_ · `127.webp` — Leaving a name and number with a counter man, noted on the back of a voucher.
- **§128** · _bench_ · `128.webp` — Dawn on a bench, back wrecked, not ready to give up; a bus coming your way.
- **§129** · _bed_ · `129.webp` — A hotel man softening, letting you stay by a lobby radiator until day.
