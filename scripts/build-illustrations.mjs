// Editable vector artwork for the collection. Run: node scripts/build-illustrations.mjs
import { mkdir, writeFile } from 'node:fs/promises';
const out = new URL('../web/illustrations/', import.meta.url);
await mkdir(out, { recursive:true });

const palettes = {
  market:['#153638','#426a60','#9a9e79','#213e3c','#e8c38b'],
  winter:['#193d48','#557b80','#bfd1c6','#284a51','#eed29b'],
  desert:['#3c5555','#b49b7c','#dfc5a0','#49645d','#f2d6a0'],
  coast:['#173a42','#527775','#adb9a1','#23464a','#ead09b'],
  orchard:['#193d3f','#537469','#bbc0a1','#244b43','#ecc88c'],
  flood:['#213f47','#567f7a','#a8b8a1','#244b4b','#e3c790'],
  refuge:['#24454d','#729391','#d3ddd0','#355b60','#f0d39b'],
};
const ground = p => `<path d="M0 670h800v330H0z" fill="url(#ground)"/><path d="M0 701h800M0 840h800" stroke="${p[2]}" stroke-opacity=".12"/>`;
const glow = (x,y,r=80) => `<ellipse cx="${x}" cy="${y}" rx="${r}" ry="${r*1.2}" fill="url(#glow)"/>`;
function windowAt(x,y,w,h,p,lit=true) {
  return `${lit?glow(x+w/2,y+h/2,w*1.7):''}<rect x="${x-5}" y="${y-5}" width="${w+10}" height="${h+10}" rx="3" fill="${p[3]}" stroke="${p[2]}" stroke-width="3"/><rect x="${x}" y="${y}" width="${w}" height="${h}" fill="${lit?'url(#warm)':p[0]}"/><path d="M${x+w/2} ${y}v${h}m${-w/2} ${-h/2}h${w}" stroke="${p[3]}" stroke-width="5"/>`;
}
function house(x,y,w,h,p,lit=false,snow=false) {
  return `<g><path d="M${x} ${y}h${w}v${h}h-${w}z" fill="url(#stone)"/><path d="m${x-12} ${y} ${w/2+12} -${w*.3} ${w/2+12} ${w*.3}-9 15-${w/2+3}-${w*.25}-${w/2+3} ${w*.25}z" fill="${p[3]}"/>${snow?`<path d="m${x-9} ${y-5} ${w/2+9}-${w*.3} ${w/2+9} ${w*.3}" stroke="${p[2]}" stroke-width="9"/>`:''}${windowAt(x+w*.18,y+h*.27,w*.24,h*.24,p,lit)}<path d="M${x+w*.63} ${y+h*.45}h${w*.23}v${h*.55}h-${w*.23}z" fill="${p[3]}"/><path d="M${x+w*.74} ${y+h*.53}v${h*.4}" stroke="${p[2]}" stroke-opacity=".3"/></g>`;
}
function sky(p,dawn=false) {
  const stars=[[93,180],[176,275],[333,132],[493,206],[694,282],[551,352]];
  return `<path d="M0 0h800v1000H0z" fill="url(#sky)"/><ellipse cx="500" cy="400" rx="460" ry="360" fill="url(#haze)"/>${dawn?`<circle cx="570" cy="490" r="68" fill="${p[4]}" opacity=".8"/>`:`<circle cx="611" cy="223" r="41" fill="${p[2]}" opacity=".8"/><circle cx="595" cy="208" r="40" fill="${p[0]}"/>${stars.map(([x,y])=>`<circle cx="${x}" cy="${y}" r="1.8" fill="${p[2]}" opacity=".6"/>`).join('')}`}`;
}
function weather(type,p) {
  return type==='snow'?`<path d="M0 0h800v1000H0z" fill="url(#snow)"/>`:type==='rain'?`<path d="M0 0h800v1000H0z" fill="url(#rain)"/>`:'';
}
function person(x,y,scale,p) {
  return `<g transform="translate(${x} ${y}) scale(${scale})" fill="${p[3]}"><ellipse cx="0" cy="72" rx="30" ry="6" opacity=".35"/><circle cy="-2" r="11"/><path d="M-10 10q10-7 20 0l10 59h-40z"/><path d="M-7 67v15m14-15v15" stroke="${p[3]}" stroke-width="7" stroke-linecap="round"/></g>`;
}
function stove(p) {
  return `<g>${glow(405,700,260)}<path d="M354 300h42v230h-42z" fill="${p[3]}" stroke="${p[2]}" stroke-width="3"/><path d="M357 337h37m-37 75h37m-37 75h37" stroke="${p[2]}" opacity=".45"/><rect x="276" y="539" width="266" height="251" rx="22" fill="${p[3]}" stroke="${p[2]}" stroke-width="6"/><rect x="309" y="577" width="201" height="152" rx="12" fill="${p[0]}" stroke="${p[1]}" stroke-width="6"/><path d="M337 706c-44-63 63-71 38-124 68 40 76 65 40 124 56-27 25-47 70-83-4 45 26 57 2 83z" fill="url(#warm)"/><path d="M332 741h149" stroke="${p[2]}" stroke-width="6"/><path d="M305 790v28m208-28v28" stroke="${p[3]}" stroke-width="13"/><path d="M317 539h166v-40q-30-33-83-33t-83 33z" fill="${p[2]}"/><path d="M353 462q-26-44 4-76m46 76q-19-40 6-83m46 83q-24-33 2-58" stroke="${p[2]}" stroke-width="5" stroke-linecap="round" opacity=".35"/></g>`;
}
function interior(p,type) {
  return `<path d="M0 0h800v1000H0z" fill="url(#stone)"/><path d="M0 200h800M0 330h800M0 465h800M0 610h800" stroke="${p[3]}" stroke-width="5" opacity=".28"/><rect x="50" y="305" width="205" height="290" rx="4" fill="${p[0]}" stroke="${p[2]}" stroke-width="10"/><path d="M57 535l80-152 98 120v82H57z" fill="${p[1]}"/><path d="M146 305v290m-95-145h205" stroke="${p[3]}" stroke-width="10"/>${type==='refuge'?'<path d="m66 480 70-106 79 101" stroke="#c4d6cd" stroke-width="5"/>':''}${ground(p)}${stove(p)}<path d="M75 807h171v-92H75zm0 0-17 82m188-82 18 82" stroke="${p[2]}" stroke-width="9"/><path d="M657 810h86v-125h-86z" fill="${p[3]}"/><path d="M683 680v-107" stroke="${p[2]}" stroke-width="6"/><path d="m646 575 35-53 35 53z" fill="${p[4]}"/>${glow(681,559,90)}<path d="M0 1000h800V872l-390-76z" fill="${p[3]}" opacity=".32"/>`;
}
function market(p,scene) {
  if(scene==='kitchen')return `<path d="M0 0h800v1000H0z" fill="url(#stone)"/>${windowAt(493,280,155,210,p)}<path d="M0 385h414M0 520h414" stroke="${p[3]}" stroke-width="12"/>${[82,178,277,365].map(x=>`<path d="M${x} 365v-66" stroke="${p[2]}" stroke-width="3"/><ellipse cx="${x}" cy="292" rx="24" ry="9" fill="${p[4]}"/>`).join('')}${ground(p)}${glow(365,650,230)}<path d="M65 691h661v40H65zM86 731v203m617-203v203" fill="${p[3]}" stroke="${p[2]}" stroke-width="7"/><path d="M236 635h249l-22 60H257z" fill="${p[1]}" stroke="${p[2]}" stroke-width="5"/><ellipse cx="360" cy="635" rx="124" ry="19" fill="${p[2]}"/><path d="M306 612q-30-65 12-105m44 105q-27-51 6-99m43 99q-19-50 14-89" stroke="${p[2]}" stroke-width="5" opacity=".4"/><path d="M132 666h75m-60-26h51m326 14 70-121" stroke="${p[4]}" stroke-width="7"/><ellipse cx="170" cy="625" rx="50" ry="16" fill="${p[2]}"/><path d="M582 630h62l-11 54h-40z" fill="${p[4]}"/>`;
  const stalls=[[-95,525,240],[120,472,330],[570,509,240]];
  let art=`${sky(p,scene==='closing')}<path d="M0 520V355h109v-88h81v184h58V331h131v156h50V272h102v169h78V352h104v145h87v209H0z" fill="${p[3]}" opacity=".6"/>${ground(p)}<path d="m330 650-90 350h295l-65-350z" fill="${p[2]}" opacity=".16"/>`;
  for(const [x,y,w] of stalls)art+=`${glow(x+w/2,y+140,120)}<path d="M${x} ${y}h${w}v206H${x}z" fill="url(#stone)"/><path d="m${x-10} ${y} 26-56h${w-32}l26 56z" fill="${p[3]}" stroke="${p[2]}" stroke-width="4"/>${[0,1,2,3,4].map(i=>`<path d="m${x+16+i*w/5} ${y-55} 8 55" stroke="${p[1]}" stroke-width="10"/>`).join('')}<path d="M${x+18} ${y+122}h${w-36}v32H${x+18}z" fill="${p[4]}" opacity=".65"/><path d="M${x+26} ${y+207}v36m${w-52}-36v36" stroke="${p[3]}" stroke-width="9"/>`;
  art+=`<path d="M0 283q400-93 800 12" stroke="${p[2]}" stroke-width="3"/>${[82,203,334,469,602,733].map((x,i)=>{const y=310-Math.sin(i/5*Math.PI)*40;return `${glow(x,y,60)}<path d="M${x} ${y-80}v45" stroke="${p[2]}" stroke-width="3"/><ellipse cx="${x}" cy="${y}" rx="26" ry="36" fill="url(#warm)"/><path d="M${x-14} ${y-31}v61m28-61v61" stroke="${p[1]}" stroke-opacity=".3" stroke-width="3"/>`;}).join('')}`;
  if(scene==='table')art+=`<path d="m60 818 420-35 258 97-453 44z" fill="${p[2]}"/><path d="M241 800h152l-21 59H265z" fill="${p[4]}"/><ellipse cx="317" cy="800" rx="75" ry="16" fill="${p[0]}"/><path d="M507 810h61l-10 46h-38z" fill="${p[4]}"/><path d="M582 801h34l-5 53h-28z" fill="${p[1]}"/><path d="M90 831v122m574-84v115" stroke="${p[3]}" stroke-width="12"/>`;
  else art+=person(505,664,1.1,p)+person(568,676,.7,p);
  return art;
}
function winter(p,scene) {
  if(scene==='hearth')return interior(p,'winter');
  let art=sky(p,scene==='dawn')+`<path d="M0 570 150 403 310 500 528 356 800 546v454H0z" fill="${p[1]}" opacity=".5"/>${ground(p)}<path d="M0 690q230-70 421 0t379 0v310H0z" fill="${p[2]}" opacity=".85"/>`;
  art+=house(-46,550,229,193,p,false,true)+house(558,510,259,211,p,false,true)+house(212,447,330,263,p,true,true);
  art+=`<path d="m314 710-78 290h319l-90-290z" fill="${p[1]}" opacity=".4"/><path d="M0 802q172-40 269 0m211 21q188-49 320-5" stroke="${p[2]}" stroke-width="9"/>`;
  if(scene==='ice')art+=`<ellipse cx="440" cy="851" rx="223" ry="112" fill="${p[1]}"/><path d="m280 810 92 50-65 60m150-111-41 74 78 59m-113-55 52-10" stroke="${p[2]}" stroke-width="5" opacity=".8"/>`;
  else art+=person(444,724,.85,p)+`<path d="M275 740v96m0-54 38-24" stroke="${p[3]}" stroke-width="7"/>${glow(314,756,70)}<path d="M302 742h25v32h-25z" fill="${p[4]}" stroke="${p[3]}" stroke-width="4"/>`;
  return art+weather('snow',p);
}
function desert(p,scene) {
  let art=sky(p,true)+`<path d="M0 493 170 344 310 462 555 317 800 474v526H0z" fill="${p[1]}"/><path d="m0 596 168-128 155 83 158-110 319 131v428H0z" fill="${p[2]}"/><path d="m0 773 234-166 241 130 325-98v361H0z" fill="${p[1]}" opacity=".9"/><path d="m294 592-110 408h407L423 592z" fill="${p[3]}"/><path d="m357 668-9 33m-13 48-13 45m-15 56-15 59" stroke="${p[4]}" stroke-width="8"/>`;
  if(scene==='well')art+=`<path d="M240 638h294v101H240z" fill="url(#stone)" stroke="${p[3]}" stroke-width="6"/><ellipse cx="387" cy="638" rx="147" ry="33" fill="${p[3]}" stroke="${p[2]}" stroke-width="8"/><path d="M263 631V448m250 183V448m-274 0 148-101 149 101z" fill="${p[3]}" stroke="${p[1]}" stroke-width="7"/><path d="M386 430v196" stroke="${p[4]}" stroke-width="4"/><path d="M357 600h58l-8 56h-42z" fill="${p[1]}"/><path d="M650 607V360m-37 210 37-82 38 82M650 385l-75-46m75 46 65-44m-65 44v-79" stroke="${p[3]}" stroke-width="9"/>`;
  else if(scene!=='road')art+=`<g transform="translate(172 524)"><path d="M0 16q0-26 30-26h374q27 0 27 27v185H0z" fill="${p[2]}" stroke="${p[3]}" stroke-width="8"/><path d="M0 138h431v45H0z" fill="${p[1]}"/><path d="M37 26h355v68H37z" fill="${p[0]}"/><path d="M110 25v70m90-70v70m92-70v70" stroke="${p[2]}" stroke-width="7"/><rect x="350" y="111" width="54" height="90" fill="${p[3]}"/><circle cx="82" cy="201" r="32" fill="${p[3]}"/><circle cx="351" cy="201" r="32" fill="${p[3]}"/><circle cx="82" cy="201" r="14" fill="${p[1]}"/><circle cx="351" cy="201" r="14" fill="${p[1]}"/></g>${person(490,753,.83,p)}${person(546,775,.5,p)}`;
  if(scene==='evening')art+=`<path d="M0 0h800v1000H0z" fill="${p[0]}" opacity=".17"/>`;
  return art;
}
function coast(p,scene) {
  if(scene==='lamp-room')return interior(p,'coast');
  let art=sky(p,scene==='dawn')+`<path d="M0 564h800v436H0z" fill="url(#water)"/><path d="m0 708 151-164 127 135 119-170 120 128-20 137-262 77-235 87z" fill="${p[3]}"/>`;
  const tower=`${glow(395,359,154)}<path d="m322 696 37-271h75l39 271z" fill="url(#stone)" stroke="${p[2]}" stroke-width="4"/><path d="M333 604h129m-119-87h106" stroke="${p[1]}" stroke-width="26"/><path d="M353 356h88v71h-88z" fill="${p[4]}" stroke="${p[3]}" stroke-width="7"/><path d="m344 353 51-53 57 53z" fill="${p[3]}"/><path d="M349 430h98m-48-73v69" stroke="${p[3]}" stroke-width="7"/><path d="M371 636h52v61h-52z" fill="${p[3]}"/><path d="m441 361 359-129v255l-359-72z" fill="url(#beam)"/>`;
  art+=scene==='shore'?`<g transform="translate(72 170) scale(.67)">${tower}</g>`:tower;
  for(let i=0;i<5;i++)art+=`<path d="M${-60+i*19} ${703+i*54}q105-61 206 0t206 0t206 0t206 0" stroke="${p[2]}" stroke-width="${5-i*.6}" opacity="${.5-i*.06}"/>`;
  art+=`<path d="m547 742 120 5-23 40h-83z" fill="${p[3]}"/><path d="M593 745v-58m0 0 52 49h-52z" fill="${p[2]}" stroke="${p[3]}" stroke-width="4"/>${glow(580,743,58)}<rect x="572" y="736" width="13" height="13" fill="${p[4]}"/>`;
  return art+(scene==='dawn'?'':weather('rain',p));
}
function tree(x,y,s,p) {
  return `<g transform="translate(${x} ${y}) scale(${s})"><path d="M0 200V37m0 67-75-59m75 19 73-68M-35 77l-23-86m112 26 15-57M0 53l-17-66" stroke="${p[3]}" stroke-width="14" stroke-linecap="round"/>${[[-79,42],[-57,-12],[-21,-19],[17,-10],[48,23],[72,-4],[-49,44],[17,45]].map(([a,b])=>`<ellipse cx="${a}" cy="${b}" rx="30" ry="23" fill="${p[2]}" opacity=".85"/><g fill="${p[4]}" opacity=".55"><circle cx="${a-7}" cy="${b-3}" r="4"/><circle cx="${a+9}" cy="${b+8}" r="3"/></g>`).join('')}</g>`;
}
function firepot(x,y,s,p) {
  return `<g transform="translate(${x} ${y}) scale(${s})">${glow(0,-13,105)}<path d="M-45 0h90l-9 61h-72z" fill="${p[3]}" stroke="${p[2]}" stroke-width="4"/><path d="M-26 0c-43-39 30-51 17-101C41-62 1-26 30 0z" fill="url(#warm)"/><path d="M-32 68h64m-30-80-6-8m35 6-8-3" stroke="${p[2]}" stroke-width="4"/></g>`;
}
function orchard(p,scene) {
  let art=sky(p,scene==='dawn')+`<path d="M0 543q193-143 401-26t399-13v496H0z" fill="${p[1]}" opacity=".6"/>${ground(p)}<path d="m325 581-109 419h365L438 581z" fill="${p[2]}" opacity=".22"/>`;
  for(const [x,y,s]of[[286,472,.4],[513,479,.4],[234,530,.6],[560,547,.6],[170,618,.9],[639,631,.9],[44,729,1.25],[751,755,1.3]])art+=tree(x,y,s,p);
  if(scene==='pond')art+=`<ellipse cx="422" cy="850" rx="246" ry="110" fill="url(#water)"/><path d="M273 850h140m-34 32h165m-75-54h105" stroke="${p[2]}" stroke-width="4" opacity=".5"/>${person(210,779,.7,p)}`;
  else art+=firepot(320,720,.6,p)+firepot(500,819,.9,p)+firepot(241,890,scene==='fire'?1.4:.9,p)+person(456,730,.75,p);
  return art;
}
function flood(p,scene) {
  let art=sky(p,scene==='dawn')+`<path d="M0 565 190 409 408 526 611 435 800 527v473H0z" fill="${p[1]}" opacity=".45"/>`;
  art+=house(-56,490,253,229,p)+house(204,465,244,245,p,true)+house(469,505,312,218,p);
  art+=`<path d="M0 710h800v290H0z" fill="url(#water)"/><path d="m274 710-26 290h221l-92-290z" fill="${p[4]}" opacity=".12"/>`;
  if(scene==='bridge')art+=`<path d="M-20 697q421-248 840-20v97q-412-249-840 27z" fill="${p[3]}" stroke="${p[2]}" stroke-width="5"/><path d="M-20 670q421-247 840-20m-815 21v-60m120 2v-67m145 25v-72m160 47v-70m155 75v-65m127 129v-65" stroke="${p[2]}" stroke-width="7"/>`;
  else if(scene==='shelter')art+=`<g transform="translate(50 90) scale(1.2)">${house(150,435,360,300,p,true)}</g>`;
  else{for(let row=0;row<3;row++)for(let i=0;i<7;i++)art+=`<rect x="${-40+i*135+(row%2)*58}" y="${752+row*33}" width="128" height="44" rx="21" fill="${row%2?p[2]:p[1]}" stroke="${p[3]}" stroke-width="3"/>`;art+=person(491,696,.8,p)+`${glow(547,751,85)}<rect x="533" y="735" width="27" height="37" rx="3" fill="${p[4]}" stroke="${p[3]}" stroke-width="5"/>`;}
  for(let i=0;i<7;i++)art+=`<path d="M${i%2?35:110} ${854+i*21}h${140+i*18}m110 0h145" stroke="${p[2]}" stroke-width="3" opacity=".35"/>`;
  return art+(scene==='dawn'?'':weather('rain',p));
}
function refuge(p,scene) {
  if(scene==='stove')return interior(p,'refuge');
  let art=sky(p,scene==='dawn')+`<path d="m0 485 184-214 162 164 144-244 310 316v493H0z" fill="${p[1]}"/><path d="m79 377 105-106 76 85-46-17-29-39-48 63zm312-60 99-126 122 124-62-37-57-59-66 88z" fill="${p[2]}"/><path d="m0 712 262-293 185 293 126-167 227 204v251H0z" fill="${p[2]}"/>`;
  const hut=`<path d="M229 517h319v229H229z" fill="url(#stone)"/><path d="m201 520 185-119 186 119-18 28-168-103-166 103z" fill="${p[3]}"/><path d="m207 509 179-108 180 108" stroke="${p[2]}" stroke-width="15"/><path d="M239 557h294m-294 48h294m-294 48h294m-294 48h294" stroke="${p[3]}" stroke-width="4" opacity=".35"/>${windowAt(275,573,85,91,p,true)}<path d="M431 603h69v143h-69z" fill="${p[3]}"/><path d="M499 448v-87h27v104" fill="${p[3]}"/><path d="M513 342q-28-50-1-76t-5-65" stroke="${p[2]}" stroke-width="6" stroke-linecap="round" opacity=".4"/>`;
  art+=scene==='ridge'?`<g transform="translate(353 143) scale(.58)">${hut}</g><path d="m0 932 215-156 187 54 160-168 238 210v128H0z" fill="${p[1]}"/><path d="m93 832 118-35 83 25 81-43 83-94" stroke="${p[3]}" stroke-width="4"/>${person(283,767,.9,p)}`:hut+`<path d="m347 747-100 253h333l-135-253z" fill="${p[1]}" opacity=".5"/><path d="M384 819l-16 23m33 24-18 25m16 26-18 24" stroke="${p[3]}" stroke-width="6" opacity=".45"/>`;
  return art+(scene==='dawn'?'':weather('snow',p));
}
const renderers={market,winter,desert,coast,orchard,flood,refuge};
function svg(kind,scene) {
  const p=palettes[kind], dawn=scene==='dawn'||scene==='closing'||scene==='evening';
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 1000" fill="none"><defs>
  <linearGradient id="sky" x1="400" y1="0" x2="400" y2="800" gradientUnits="userSpaceOnUse"><stop stop-color="${dawn?p[1]:p[0]}"/><stop offset="1" stop-color="${dawn?p[4]:p[1]}"/></linearGradient>
  <linearGradient id="stone" x2="700" y2="800" gradientUnits="userSpaceOnUse"><stop stop-color="${p[1]}"/><stop offset="1" stop-color="${p[3]}"/></linearGradient>
  <linearGradient id="ground" y1="600" y2="1000" gradientUnits="userSpaceOnUse"><stop stop-color="${p[1]}"/><stop offset="1" stop-color="${p[0]}"/></linearGradient>
  <linearGradient id="water" y1="550" y2="1000" gradientUnits="userSpaceOnUse"><stop stop-color="${p[1]}"/><stop offset="1" stop-color="${p[0]}"/></linearGradient>
  <linearGradient id="warm" x2="0" y2="1"><stop stop-color="${p[4]}"/><stop offset="1" stop-color="#bd895d"/></linearGradient>
  <linearGradient id="beam"><stop stop-color="${p[4]}" stop-opacity=".62"/><stop offset="1" stop-color="${p[4]}" stop-opacity="0"/></linearGradient>
  <radialGradient id="glow"><stop stop-color="${p[4]}" stop-opacity=".48"/><stop offset="1" stop-color="${p[4]}" stop-opacity="0"/></radialGradient>
  <radialGradient id="haze"><stop stop-color="${p[2]}" stop-opacity=".2"/><stop offset="1" stop-color="${p[2]}" stop-opacity="0"/></radialGradient>
  <pattern id="snow" width="103" height="139" patternUnits="userSpaceOnUse"><circle cx="17" cy="33" r="2" fill="${p[2]}" opacity=".7"/><circle cx="67" cy="107" r="1.5" fill="${p[2]}" opacity=".5"/><path d="m37 69-8 9" stroke="${p[2]}" stroke-width="2" opacity=".3"/></pattern>
  <pattern id="rain" width="93" height="121" patternUnits="userSpaceOnUse"><path d="m12 8-9 25m68 52-7 20" stroke="${p[2]}" stroke-opacity=".15"/></pattern>
  </defs>${renderers[kind](p,scene)}</svg>`;
}
const books = [
  ['the-night-market','market','market', {market:['lantern','stall','rain','sign','arch','companions','phone','photo'],kitchen:['pot','flame','ladle','steamer','dumpling'],table:['bowl','teacup','stool','hand','child','coin'],closing:['dawn']}],
  ['first-light','winter','town',{town:['snowflake','house','van','sign','photo','coin','phone'],hearth:['heater','candle','flame','blanket','bed','door','window','child','companions','lantern','torch'],ice:['ice'],dawn:['dawn']}],
  ['cool-of-evening','desert','bus',{bus:['bus','crate','companions','child','radio','tarp'],road:['road','sun','map','dune','ridge','pickup','truck','shimmer','sign'],well:['well','bottle','windmill','station','hand','door','coin'],evening:['dawn','photo']}],
  ['the-keeper','coast','beacon',{beacon:['lighthouse','beam','lantern','oilcan'],shore:['wave','boat','quay','rock','cliff','gull','rain','coin','map','sign'], 'lamp-room':['flame','companions','rope','hand','radio','house','door','blanket'],dawn:['dawn']}],
  ['the-orchard','orchard','orchard',{orchard:['tree','frost','rows','lantern','photo','coin','map','sign','phone'],fire:['flame','firepot','straw','companions','house','door','blanket'],pond:['child','pond','hand'],dawn:['dawn','gull']}],
  ['high-water','flood','flood',{flood:['rain','shimmer','house','photo','phone'],wall:['crate','hand','companions','child','coin'],bridge:['bridge','van','road','sign'],shelter:['blanket','bed','door','lamp','lantern'],dawn:['dawn']}],
  ['the-refuge','refuge','refuge',{refuge:['snowflake','house','photo','phone','lamp','window','lantern'],stove:['heater','flame','blanket','bed','door','companions','hand'],ridge:['ridge','child','sign','coin','torch'],dawn:['dawn']}],
];
const titles={arch:'Through the market gate',lantern:'Lanterns in the dusk',stall:'Your corner of the market',pot:'In the stall kitchen',flame:'Keeping the fire alive',ladle:'One bowl at a time',steamer:'Steam in the night',dumpling:'The family recipe',bowl:'A place at the table',teacup:'A moment of warmth',stool:'Someone to sit beside',hand:'A helping hand',child:'Someone counting on you',coin:'The price of a choice',phone:'A call in the night',photo:'Something to remember',snowflake:'Into the snow',house:'A light in the window',van:'Help on the road',heater:'Keeping the warmth',candle:'One small light',blanket:'A little shelter',bed:'A place to rest',door:'An open door',window:'The light in the window',companions:'Stronger together',torch:'A light to follow',ice:'Across the ice',dawn:'At first light',bus:'The desert road',crate:'What you can carry',radio:'A voice through the silence',tarp:'A patch of shade',road:'The long road',sun:'Under the afternoon sun',map:'Finding a way',dune:'Beyond the dunes',ridge:'Along the ridge',pickup:'A passing chance',truck:'Help on the horizon',shimmer:'Across the water',well:'The old well',bottle:'A little water',windmill:'The distant windmill',station:'A place to stop',lighthouse:'The light on the headland',beam:'Holding the beam',oilcan:'A little fuel',wave:'Against the sea',boat:'A light offshore',quay:'Beside the water',rock:'The rocks below',cliff:'Along the cliff',gull:'A change in the sky',rain:'Into the rain',rope:'Holding on',tree:'The blossoming orchard',frost:'Against the frost',rows:'Between the rows',firepot:'Fires in the orchard',straw:'What the fire needs',pond:'The still water',bridge:'Across the rising river',lamp:'The lamp in the window',sign:'A sign to follow'};
const catalog={'the-address':{cover:'/cover-station.svg',alt:'A quiet station at night with warm windows, a crescent moon and a letter on a bench.',focal:'center',social:'/og-collection-the-address.png'}};
for(const [slug,kind,cover,scenes]of books){
  const entry={cover:`/illustrations/${slug}-${cover}.svg`,focal:'center',social:`/og-collection-${slug}.png`,scenes:{},sceneTitles:{}};
  for(const [scene,motifs]of Object.entries(scenes)){
    const src=`/illustrations/${slug}-${scene}.svg`;
    await writeFile(new URL(`${slug}-${scene}.svg`,out),svg(kind,scene));
    for(const motif of motifs){entry.scenes[motif]=src;entry.sceneTitles[motif]=titles[motif];}
  }
  entry.endings={good:`/illustrations/${slug}-${Object.keys(scenes).at(-1)}.svg`,neutral:entry.cover,bad:entry.cover};
  entry.alt={market:'Warm paper lanterns above a family food stall in a quiet night market.',winter:'A snowbound hillside town with one warm doorway beneath a winter sky.',desert:'A bus on an empty desert road, with distant hills and a low golden sun.',coast:'A stone lighthouse casting a warm beam across a stormy sea.',orchard:'Blossoming orchard trees on a frosty night, with warm fires along the rows.',flood:'A flooded village street with warm windows and a sandbag wall against the river.',refuge:'A stone mountain refuge with a glowing window in a snowy mountain landscape.'}[kind];
  catalog[slug]=entry;
}
await writeFile(new URL('catalog.json',out),JSON.stringify(catalog,null,2)+'\n');
console.log(`Built ${books.length} illustrated book identities and their scene sets.`);
