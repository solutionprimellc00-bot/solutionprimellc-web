"""Arma la web de solutionprimellc.com (español en / y inglés en /en/) en la carpeta public/.

Uso: python3 construir.py
Todo el texto está en TEXTOS; la plantilla es la misma para los dos idiomas.
"""
import json
import pathlib

AQUI = pathlib.Path(__file__).resolve().parent
SITIO = AQUI / "public"
DOMINIO = "https://solutionprimellc.com"
CORREO = "admin@solutionprimellc.com"
ANIO = "2026"

TEXTOS = {
    "es": {
        "ruta": "/",
        "otra_ruta": "/en/",
        "otro_idioma": "en",
        "otro_idioma_nombre": "English",
        "og_locale": "es_US",
        "titulo": "Solution Prime LLC: Spliup, Golden Trays y saxofón en vivo",
        "descripcion": "Solution Prime LLC, de Queens Village, Nueva York: Spliup (IA que contesta y vende por WhatsApp e Instagram), Golden Trays (bandejas de regalo hechas a mano) y saxofón en vivo para eventos.",
        "saltar": "Saltar al contenido",
        "nav_aria": "Principal",
        "nav_proyectos": "Proyectos",
        "nav_contacto": "Contacto",
        "h1": "Tres proyectos,|hechos en Queens.",
        "entrada": "Uno vende por ti, otro llega con un regalo y otro pone la música. Solution Prime LLC es una empresa de Queens Village, Nueva York.",
        "puertas_aria": "Los tres proyectos",
        "p_spliup_que": "Contesta tus chats de WhatsApp e Instagram con IA.",
        "p_gt_que": "Bandejas de regalo hechas a mano en Nueva York.",
        "p_sax_nombre": "Saxofón en vivo",
        "p_sax_que": "Para bodas, cumpleaños y eventos.",
        "foto_bandeja_alt": "Bandeja de Golden Trays con fresas, waffles, frutas y una botella con lazo rojo",
        "foto_sax_alt": "Saxofonista tocando un saxofón alto dorado frente a una cortina clara",
        # Spliup
        "s_lema": "Tus chats pierden ventas que no ves.",
        "s_texto": "Spliup les contesta en segundos a los clientes que te escriben por WhatsApp e Instagram, con tus precios reales. Les da seguimiento, manda el link de pago en el mismo chat y te avisa cuando alguien está listo para comprar.",
        "s_hechos": [
            "Responde en menos de 3 segundos, a cualquier hora",
            "Agenda citas para barberías y salones",
            "Cobra con Stripe dentro de la conversación",
            "Un panel con cada chat, cada venta y cada seguimiento",
        ],
        "s_boton": "Ir a spliup.com",
        "s_nota": "Un producto de SPLIUP LLC.",
        "chat_aria": "Ejemplo de una conversación atendida por Spliup",
        "chat_negocio": "Barbería El Corte",
        "chat_estado": "en línea",
        "chat_msgs": [
            ("cliente", "Hola! ¿Tienen turno mañana para corte y barba?", "10:41"),
            ("ia", "¡Hola! 💈 Mañana tengo libre a las 10:30 am y a las 4:00 pm. Corte + barba: $35. ¿Cuál prefieres?", "10:41"),
            ("cliente", "A las 4 💪", "10:42"),
            ("ia", "Listo, te aparté mañana a las 4:00 pm ✂️ ¡Te esperamos!", "10:42"),
        ],
        "chat_ia": "IA",
        "chat_aviso": "Cita agendada para mañana a las 4:00 pm",
        "chat_pie": "Ejemplo con un negocio inventado.",
        # Golden Trays
        "g_lema": "Made for every special moment",
        "g_texto": "Bandejas de regalo armadas a mano para cumpleaños, aniversarios, un desayuno sorpresa o cualquier día que valga la pena celebrar. Puedes sumarle flores, una postal y un saxofonista en vivo que llega tocando.",
        "g_hechos": [
            "Desayunos, cenas y ocasiones especiales",
            "Flores y música en vivo",
            "Entrega en los 5 condados de NYC y en Long Island",
            "Pides en línea en menos de un minuto",
        ],
        "g_estado": "Abre muy pronto.",
        "g_boton": "Ver goldentrays.com",
        "g_boton2": "Seguir en Instagram",
        "g_fotos_aria": "Tres bandejas de Golden Trays",
        "g_fotos": [
            ("bandeja-classic", "Classic Tray", "Bandeja con frutas, rollitos de jamón, granola y una copa con servilleta de corazones"),
            ("bandeja-sweet", "Sweet Tray", "Bandeja con waffles, fresas, frutas, queso y una botella con lazo rojo"),
            ("bandeja-gourmet", "Gourmet Tray", "Bandeja con croquetas, rollitos, frutas, una bebida rosada y bombones"),
        ],
        "g_logo_alt": "Golden Trays",
        "g_nota": "Golden Trays es una marca de Solution Prime LLC.",
        # Saxofón
        "x_titulo": "Saxofón en vivo",
        "x_lema": "La música que se queda en la memoria del día.",
        "x_texto": "Saxofón para bodas, cumpleaños, aniversarios y eventos privados en Nueva York. Música para la entrada, la cena y la fiesta, con las canciones que tú elijas.",
        "x_hechos": [
            "Bodas, cumpleaños, aniversarios y eventos de empresa",
            "Tú eliges las canciones",
            "En Nueva York y sus alrededores",
        ],
        "x_boton": "Pide tu fecha",
        "x_asunto": "Saxofón para mi evento",
        "x_cuerpo": "Hola, quiero saxofón en vivo para mi evento.\n\nFecha:\nLugar:\nTipo de evento:\nCanciones que me gustaría:\n",
        "x_cruce": "¿Vas a regalar una bandeja de Golden Trays? Agrégale el saxofonista y llega tocando.",
        "x_cruce_enlace": "Ver Golden Trays",
        # Contacto
        "c_titulo": "Escríbenos",
        "c_texto": "Para cualquiera de los tres proyectos, o si quieres trabajar con nosotros.",
        "c_empresa": "Empresa",
        "c_lugar": "Lugar",
        "c_lugar_valor": "Queens Village, Nueva York",
        "c_proyectos": "Proyectos",
        # Pie
        "pie": "Golden Trays es una marca de Solution Prime LLC. Spliup es un producto de SPLIUP LLC.",
        # 404
        "n_titulo": "Esta página no existe",
        "n_texto": "Puede que el enlace esté mal escrito o que la página se haya movido.",
        "n_boton": "Volver al inicio",
    },
    "en": {
        "ruta": "/en/",
        "otra_ruta": "/",
        "otro_idioma": "es",
        "otro_idioma_nombre": "Español",
        "og_locale": "en_US",
        "titulo": "Solution Prime LLC: Spliup, Golden Trays and live saxophone",
        "descripcion": "Solution Prime LLC, from Queens Village, New York: Spliup (AI that answers and sells on WhatsApp and Instagram), Golden Trays (hand-built gift trays) and live saxophone for events.",
        "saltar": "Skip to content",
        "nav_aria": "Main",
        "nav_proyectos": "Projects",
        "nav_contacto": "Contact",
        "h1": "Three projects,|made in Queens.",
        "entrada": "One sells for you, one shows up with a gift and one brings the music. Solution Prime LLC is a company from Queens Village, New York.",
        "puertas_aria": "The three projects",
        "p_spliup_que": "Answers your WhatsApp and Instagram chats with AI.",
        "p_gt_que": "Hand-built gift trays in New York.",
        "p_sax_nombre": "Live saxophone",
        "p_sax_que": "For weddings, birthdays and events.",
        "foto_bandeja_alt": "Golden Trays tray with strawberries, waffles, fruit and a bottle with a red bow",
        "foto_sax_alt": "Saxophonist playing a gold alto saxophone in front of a light curtain",
        "s_lema": "Your chats are losing sales you never see.",
        "s_texto": "Spliup answers the customers who message you on WhatsApp and Instagram within seconds, with your real prices. It follows up, sends the payment link in the same chat and tells you when someone is ready to buy.",
        "s_hechos": [
            "Replies in under 3 seconds, at any hour",
            "Books appointments for barbershops and salons",
            "Takes payments with Stripe inside the chat",
            "One dashboard for every chat, sale and follow-up",
        ],
        "s_boton": "Go to spliup.com",
        "s_nota": "A product of SPLIUP LLC.",
        "chat_aria": "Example of a conversation handled by Spliup",
        "chat_negocio": "El Corte Barbershop",
        "chat_estado": "online",
        "chat_msgs": [
            ("cliente", "Hi! Do you have an opening tomorrow for a cut and beard trim?", "10:41"),
            ("ia", "Hi! 💈 Tomorrow I have 10:30 am and 4:00 pm open. Cut + beard: $35. Which one works for you?", "10:41"),
            ("cliente", "4 works 💪", "10:42"),
            ("ia", "Done, you're booked for tomorrow at 4:00 pm ✂️ See you then!", "10:42"),
        ],
        "chat_ia": "AI",
        "chat_aviso": "Appointment booked for tomorrow at 4:00 pm",
        "chat_pie": "Example with a made-up business.",
        "g_lema": "Made for every special moment",
        "g_texto": "Gift trays built by hand for birthdays, anniversaries, a surprise breakfast or any day worth celebrating. Add flowers, a postcard and a live saxophonist who arrives playing.",
        "g_hechos": [
            "Breakfast, dinner and special occasions",
            "Flowers and live music",
            "Delivery across the 5 NYC boroughs and Long Island",
            "Order online in under a minute",
        ],
        "g_estado": "Opening soon.",
        "g_boton": "Visit goldentrays.com",
        "g_boton2": "Follow on Instagram",
        "g_fotos_aria": "Three Golden Trays trays",
        "g_fotos": [
            ("bandeja-classic", "Classic Tray", "Tray with fruit, ham rolls, granola and a glass with a heart napkin"),
            ("bandeja-sweet", "Sweet Tray", "Tray with waffles, strawberries, fruit, cheese and a bottle with a red bow"),
            ("bandeja-gourmet", "Gourmet Tray", "Tray with croquettes, pinwheels, fruit, a pink drink and chocolates"),
        ],
        "g_logo_alt": "Golden Trays",
        "g_nota": "Golden Trays is a brand of Solution Prime LLC.",
        "x_titulo": "Live saxophone",
        "x_lema": "The music people remember from the day.",
        "x_texto": "Saxophone for weddings, birthdays, anniversaries and private events in New York. Music for the entrance, dinner and party, with the songs you choose.",
        "x_hechos": [
            "Weddings, birthdays, anniversaries and corporate events",
            "You pick the songs",
            "New York City and nearby",
        ],
        "x_boton": "Ask for your date",
        "x_asunto": "Saxophone for my event",
        "x_cuerpo": "Hi, I'd like live saxophone for my event.\n\nDate:\nPlace:\nType of event:\nSongs I'd like:\n",
        "x_cruce": "Sending a Golden Trays gift? Add the saxophonist and it arrives with music.",
        "x_cruce_enlace": "See Golden Trays",
        "c_titulo": "Write to us",
        "c_texto": "About any of the three projects, or if you'd like to work with us.",
        "c_empresa": "Company",
        "c_lugar": "Location",
        "c_lugar_valor": "Queens Village, New York",
        "c_proyectos": "Projects",
        "pie": "Golden Trays is a brand of Solution Prime LLC. Spliup is a product of SPLIUP LLC.",
        "n_titulo": "This page doesn't exist",
        "n_texto": "The link may be mistyped, or the page may have moved.",
        "n_boton": "Back to the home page",
    },
}


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def mailto(asunto, cuerpo):
    from urllib.parse import quote
    return f"mailto:{CORREO}?subject={quote(asunto)}&body={quote(cuerpo)}"


CSS = r"""
@font-face{font-family:"Marcellus";src:url("/fuentes/marcellus.woff2") format("woff2");font-weight:400;font-style:normal;font-display:swap}
@font-face{font-family:"Hanken Grotesk";src:url("/fuentes/hanken-grotesk.woff2") format("woff2");font-weight:100 900;font-style:normal;font-display:swap}
:root{
  --fondo:#F1F4F0;--superficie:#FFFFFF;--tinta:#14231C;--tinta-suave:#4E5D55;--laton:#A97B2C;--laton-texto:#77561A;--linea:#CBD3CC;--foco:#0F3A2D;
  --vino:#4A1F30;--berry:#6D2E46;--crema-spliup:#F3EADB;--texto-spliup:#E9DCCB;--oro-spliup:#DDB06A;
  --crema-gt:#F6E9DB;--tinta-gt:#3A2914;--oro-gt:#7A5718;--linea-gt:#DCC5A6;
  --escenario:#0E1D17;--texto-escenario:#EEE7D8;--suave-escenario:#B9C2B8;--laton-claro:#E0BE74;
  --ancho:1136px;--margen:clamp(16px,4vw,32px);--hueco-puertas:clamp(12px,2vw,26px);
  color-scheme:light;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){--fondo:#0C1612;--superficie:#13211B;--tinta:#E6EDE8;--tinta-suave:#A9B7AF;--laton:#D2AE63;--laton-texto:#E0BE74;--linea:#2A3A32;--foco:#E0BE74;color-scheme:dark}
}
:root[data-theme="dark"]{--fondo:#0C1612;--superficie:#13211B;--tinta:#E6EDE8;--tinta-suave:#A9B7AF;--laton:#D2AE63;--laton-texto:#E0BE74;--linea:#2A3A32;--foco:#E0BE74;color-scheme:dark}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--fondo);color:var(--tinta);font-family:"Hanken Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif;font-size:1.0625rem;line-height:1.6;text-rendering:optimizeLegibility}
img{display:block;max-width:100%;height:auto}
a{color:inherit}
h1,h2,h3{font-family:"Marcellus",Georgia,"Times New Roman",serif;font-weight:400;line-height:1.08;margin:0;letter-spacing:.005em;text-wrap:balance}
p{margin:0}
ul{margin:0;padding:0;list-style:none}
:focus-visible{outline:3px solid var(--foco);outline-offset:3px;border-radius:4px}
.saltar{position:absolute;left:16px;top:-60px;z-index:10;background:var(--superficie);color:var(--tinta);padding:10px 16px;border-radius:8px;text-decoration:none;font-weight:600}
.saltar:focus{top:12px}
.visualmente-oculto{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap}

/* Cabecera */
.cabecera{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;padding:20px 0;display:flex;align-items:center;justify-content:space-between;gap:16px}
.marca{font-family:"Marcellus",Georgia,serif;font-size:1.375rem;text-decoration:none;white-space:nowrap;display:flex;align-items:baseline;gap:.35em}
.marca small{font-family:"Hanken Grotesk",system-ui,sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.06em;color:var(--laton-texto)}
.menu{display:flex;gap:clamp(14px,3vw,28px);font-size:.98rem}
.menu a{text-decoration:none;padding:6px 0;border-bottom:1px solid transparent}
.menu a:hover{border-bottom-color:var(--laton)}

/* Portada con las tres puertas */
.portada{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;padding:clamp(24px,6vw,72px) 0 clamp(56px,8vw,104px);display:grid;grid-template-columns:minmax(0,5fr) minmax(0,6fr);gap:clamp(36px,5vw,80px);align-items:end}
.portada h1{font-size:clamp(2.3rem,4.1vw,3.45rem);text-wrap:wrap}
.entrada{margin-top:22px;font-size:clamp(1.12rem,1.6vw,1.3rem);line-height:1.55;color:var(--tinta-suave);max-width:37ch}
.puertas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--hueco-puertas)}
.puerta{display:block;text-decoration:none;color:inherit;animation:subir .8s cubic-bezier(.2,.7,.2,1) both}
.puertas li:nth-child(2) .puerta{animation-delay:.12s}
.puertas li:nth-child(3) .puerta{animation-delay:.24s}
@keyframes subir{from{opacity:0;transform:translateY(22px)}}
@media (prefers-reduced-motion:reduce){.puerta{animation:none}}
.marco{display:block;position:relative;border:1px solid var(--laton);border-bottom:0;border-radius:999px 999px 0 0;padding:7px 7px 0}
.puertas .marco::after{content:"";position:absolute;left:calc(var(--hueco-puertas)/-2 - 1px);right:calc(var(--hueco-puertas)/-2 - 1px);bottom:0;height:1px;background:var(--laton)}
.puertas li:first-child .marco::after{left:-1px}
.puertas li:last-child .marco::after{right:-1px}
.vista{display:block;position:relative;aspect-ratio:3/5;border-radius:999px 999px 0 0;overflow:hidden;background:var(--linea)}
.vista img{width:100%;height:100%;object-fit:cover}
.vista-spliup{background:radial-gradient(120% 80% at 50% 28%,#8C3F5D 0%,#6D2E46 42%,#4A1F30 100%);display:grid;place-items:center}
.vista-spliup img{width:78%;height:auto;object-fit:contain;filter:drop-shadow(0 6px 14px rgba(0,0,0,.35))}
.vista-sax img{object-position:42% 30%}
.puerta-texto{display:block;padding:16px 2px 4px}
.puerta-nombre{display:block;font-family:"Marcellus",Georgia,serif;font-size:clamp(1.05rem,1.55vw,1.35rem);line-height:1.15}
.puerta-que{display:block;margin-top:6px;font-size:.95rem;line-height:1.45;color:var(--tinta-suave)}
.puerta:hover .puerta-nombre{text-decoration:underline;text-decoration-color:var(--laton);text-underline-offset:5px;text-decoration-thickness:1px}

/* Bandas de cada proyecto */
.banda{padding:clamp(64px,9vw,128px) 0}
.banda-interior{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;display:grid;gap:clamp(40px,6vw,88px);align-items:center}
.lema{font-family:"Marcellus",Georgia,serif;font-size:clamp(1.7rem,3.2vw,2.55rem);line-height:1.15;text-wrap:balance}
.cuerpo{margin-top:22px;max-width:58ch}
.hechos{margin-top:26px;display:grid;gap:10px}
.hechos li{display:flex;gap:14px;align-items:baseline}
.hechos li::before{content:"";flex:none;width:7px;height:7px;border-radius:50%;transform:translateY(-2px);background:currentColor}
.acciones{margin-top:34px;display:flex;flex-wrap:wrap;gap:12px 14px;align-items:center}
.boton{display:inline-flex;align-items:center;min-height:48px;padding:12px 24px;border-radius:999px;font-weight:600;text-decoration:none;font-size:1rem;line-height:1.2;border:1px solid transparent}
.nota{margin-top:22px;font-size:.92rem}

/* Spliup */
.banda-spliup{background:radial-gradient(110% 90% at 88% 8%,#6D2E46 0%,#4A1F30 52%,#3A1726 100%);color:var(--texto-spliup)}
.banda-spliup .banda-interior{grid-template-columns:minmax(0,7fr) minmax(0,5fr)}
.banda-spliup h2 img{width:clamp(170px,22vw,240px)}
.banda-spliup .lema{margin-top:26px;color:var(--crema-spliup)}
.banda-spliup .hechos li::before{background:var(--oro-spliup)}
.banda-spliup .boton{background:var(--oro-spliup);color:var(--vino)}
.banda-spliup .boton:hover{background:#E8C077}
.banda-spliup .nota{color:var(--oro-spliup)}
.banda-spliup :focus-visible{outline-color:var(--oro-spliup)}
.chat{justify-self:end;width:min(100%,380px);margin:0;border-radius:30px;overflow:hidden;background:#EFE6D8;color:#2B2325;box-shadow:0 40px 70px -36px rgba(0,0,0,.75),0 0 0 1px rgba(221,176,106,.35)}
.chat-cabeza{display:flex;align-items:center;gap:12px;padding:16px 18px;background:#5A2539;color:#F3EADB}
.chat-avatar{flex:none;width:38px;height:38px;border-radius:50%;display:grid;place-items:center;background:#DDB06A;color:#4A1F30;font-weight:700;font-size:.85rem}
.chat-nombre{font-weight:600;line-height:1.2}
.chat-estado{display:block;font-size:.78rem;color:#D9C6B0;font-weight:400}
.chat-mensajes{padding:18px 14px 16px;display:grid;gap:10px;font-size:.95rem;line-height:1.42}
.burbuja{max-width:84%;padding:9px 12px 6px;border-radius:16px;box-shadow:0 1px 0 rgba(43,35,37,.12)}
.burbuja-cliente{justify-self:end;background:#F3E3C4;border-bottom-right-radius:5px}
.burbuja-ia{justify-self:start;background:#FFFFFF;border-bottom-left-radius:5px}
.burbuja-meta{display:flex;justify-content:flex-end;gap:8px;margin-top:2px;font-size:.72rem;color:#6E615B}
.burbuja-ia .burbuja-meta{justify-content:space-between}
.etiqueta-ia{font-weight:700;color:#6D2E46}
.chat-aviso{margin:4px 14px 16px;padding:10px 14px;border-radius:12px;background:#FFFFFF;border:1px solid #DDB06A;font-size:.88rem;font-weight:600;color:#4A1F30;display:flex;gap:10px;align-items:center}
.chat-aviso::before{content:"";flex:none;width:9px;height:9px;border-radius:50%;background:#2E7D4F}
.chat figcaption{padding:0 18px 16px;font-size:.78rem;color:#6E615B}

/* Golden Trays */
.banda-gt{background:var(--crema-gt);color:var(--tinta-gt)}
.banda-gt .banda-interior{grid-template-columns:minmax(0,6fr) minmax(0,6fr)}
.gt-cabeza{display:flex;align-items:center;gap:clamp(16px,3vw,28px)}
.gt-logo{width:clamp(108px,14vw,150px);flex:none}
.banda-gt h2{font-size:clamp(2.2rem,4.4vw,3.4rem)}
.banda-gt .lema{font-size:clamp(1.2rem,2vw,1.5rem);margin-top:8px;color:var(--oro-gt)}
.banda-gt .cuerpo{margin-top:30px}
.banda-gt .hechos li::before{background:var(--oro-gt)}
.gt-estado{margin-top:26px;font-weight:600}
.banda-gt .boton{background:var(--tinta-gt);color:var(--crema-gt)}
.banda-gt .boton:hover{background:#523A1D}
.boton-linea{background:transparent!important;color:var(--tinta-gt)!important;border-color:var(--tinta-gt)!important}
.boton-linea:hover{background:rgba(58,41,20,.06)!important}
.banda-gt .nota{color:var(--oro-gt)}
.banda-gt :focus-visible{outline-color:var(--tinta-gt)}
.gt-fotos{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(14px,2.4vw,28px) clamp(14px,2.4vw,28px)}
.gt-fotos figure{margin:0;text-align:center}
.gt-fotos figure:first-child{grid-column:1/-1;width:min(100%,330px);justify-self:center}
.gt-fotos img{width:100%;aspect-ratio:1;object-fit:cover;border-radius:50%;box-shadow:0 0 0 1px var(--linea-gt),0 0 0 8px var(--crema-gt),0 0 0 9px var(--linea-gt)}
.gt-fotos figcaption{margin-top:18px;font-family:"Marcellus",Georgia,serif;font-size:1.15rem}

/* Saxofón */
.banda-sax{background:radial-gradient(70% 70% at 22% 30%,rgba(224,190,116,.16) 0%,rgba(224,190,116,0) 60%),var(--escenario);color:var(--texto-escenario)}
.banda-sax .banda-interior{grid-template-columns:minmax(0,5fr) minmax(0,7fr)}
.sax-foto{width:min(100%,420px);justify-self:center}
.sax-foto .marco{border-color:var(--laton-claro)}
.sax-foto .vista{aspect-ratio:4/5;background:#1B2A23}
.sax-foto .vista img{object-position:45% 20%}
.banda-sax h2{font-size:clamp(2.2rem,4.4vw,3.4rem)}
.banda-sax .lema{margin-top:16px;font-size:clamp(1.25rem,2.1vw,1.6rem);color:var(--laton-claro)}
.banda-sax .cuerpo{color:var(--texto-escenario)}
.banda-sax .hechos{color:var(--suave-escenario)}
.banda-sax .hechos li::before{background:var(--laton-claro)}
.banda-sax .boton{background:var(--laton-claro);color:var(--escenario)}
.banda-sax .boton:hover{background:#EBCB85}
.cruce{margin-top:30px;padding-top:22px;border-top:1px solid rgba(224,190,116,.35);color:var(--suave-escenario);max-width:52ch}
.cruce a{color:var(--laton-claro);text-underline-offset:4px;white-space:nowrap}
.banda-sax :focus-visible{outline-color:var(--laton-claro)}

/* Contacto */
.contacto{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;padding:clamp(72px,10vw,136px) 0 clamp(56px,8vw,96px);display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:clamp(40px,6vw,88px);align-items:end}
.contacto h2{font-size:clamp(2.4rem,5vw,4rem)}
.contacto .cuerpo{color:var(--tinta-suave)}
.correo{display:inline-block;margin-top:30px;font-family:"Marcellus",Georgia,serif;font-size:clamp(1.35rem,3.4vw,2.3rem);text-decoration:none;border-bottom:1px solid var(--laton);padding-bottom:4px;overflow-wrap:anywhere}
.correo:hover{color:var(--laton-texto)}
.datos{margin:0;display:grid;gap:18px;border-left:1px solid var(--laton);padding-left:24px}
.datos dt{font-size:.85rem;color:var(--tinta-suave)}
.datos dd{margin:2px 0 0}
.datos ul{display:grid;gap:4px}
.datos a{text-underline-offset:4px;text-decoration-color:var(--laton)}
.pie{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;padding:22px 0 40px;border-top:1px solid var(--linea);font-size:.88rem;color:var(--tinta-suave);display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:space-between}

/* Pantallas medianas y celulares */
@media (max-width:960px){
  .portada{grid-template-columns:1fr;align-items:start}
  .entrada{max-width:46ch}
  .banda-spliup .banda-interior,.banda-gt .banda-interior,.banda-sax .banda-interior,.contacto{grid-template-columns:1fr}
  .chat{justify-self:start}
  .gt-fotos{grid-template-columns:repeat(3,minmax(0,1fr))}
  .gt-fotos figure:first-child{grid-column:auto;width:auto}
  .sax-foto{justify-self:start;width:min(100%,360px)}
}
@media (max-width:560px){
  body{font-size:1rem}
  .menu-proyectos{display:none}
  .puerta-que{display:none}
  .puerta-texto{padding:12px 0 14px}
  .marco{padding:5px 5px 0}
  :root{--hueco-puertas:12px}
  .gt-fotos figcaption{font-size:.95rem;margin-top:12px}
  .gt-fotos img{box-shadow:0 0 0 1px var(--linea-gt),0 0 0 5px var(--crema-gt),0 0 0 6px var(--linea-gt)}
  .acciones .boton{width:100%;justify-content:center}
}
"""


def pagina(idioma):
    t = TEXTOS[idioma]
    otro = t["otro_idioma"]
    url = DOMINIO + t["ruta"]
    img = "/img/"

    def lista(items):
        return "\n".join(f"            <li>{esc(i)}</li>" for i in items)

    msgs = []
    for quien, texto, hora in t["chat_msgs"]:
        if quien == "cliente":
            msgs.append(f'          <p class="burbuja burbuja-cliente">{esc(texto)}<span class="burbuja-meta"><span>{hora}</span></span></p>')
        else:
            msgs.append(f'          <p class="burbuja burbuja-ia">{esc(texto)}<span class="burbuja-meta"><span class="etiqueta-ia">{t["chat_ia"]}</span><span>{hora}</span></span></p>')
    msgs = "\n".join(msgs)

    fotos = "\n".join(
        f'          <figure><img src="{img}{archivo}.webp" width="500" height="500" loading="lazy" decoding="async" alt="{esc(alt)}"><figcaption>{esc(nombre)}</figcaption></figure>'
        for archivo, nombre, alt in t["g_fotos"]
    )

    ld = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Solution Prime LLC",
        "url": DOMINIO + "/",
        "email": CORREO,
        "address": {"@type": "PostalAddress", "addressLocality": "Queens Village", "addressRegion": "NY", "addressCountry": "US"},
        "brand": [{"@type": "Brand", "name": "Golden Trays", "url": "https://goldentrays.com/"}],
    }

    return f"""<!doctype html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["titulo"])}</title>
<meta name="description" content="{esc(t["descripcion"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{DOMINIO}/">
<link rel="alternate" hreflang="en" href="{DOMINIO}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMINIO}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Solution Prime LLC">
<meta property="og:title" content="{esc(t["titulo"])}">
<meta property="og:description" content="{esc(t["descripcion"])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t["og_locale"]}">
<meta property="og:image" content="{DOMINIO}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0F3A2D">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fuentes/marcellus.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fuentes/hanken-grotesk.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
<a class="saltar" href="#contenido">{esc(t["saltar"])}</a>
<header class="cabecera">
  <a class="marca" href="{t["ruta"]}">Solution Prime <small>LLC</small></a>
  <nav class="menu" aria-label="{esc(t["nav_aria"])}">
    <a class="menu-proyectos" href="#proyectos">{esc(t["nav_proyectos"])}</a>
    <a href="#contacto">{esc(t["nav_contacto"])}</a>
    <a href="{t["otra_ruta"]}" hreflang="{otro}" lang="{otro}">{esc(t["otro_idioma_nombre"])}</a>
  </nav>
</header>
<main id="contenido">
  <section class="portada" aria-labelledby="titulo">
    <div>
      <h1 id="titulo">{"<br>".join(esc(x) for x in t["h1"].split("|"))}</h1>
      <p class="entrada">{esc(t["entrada"])}</p>
    </div>
    <ul class="puertas" id="proyectos" aria-label="{esc(t["puertas_aria"])}">
      <li><a class="puerta" href="#spliup">
        <span class="marco"><span class="vista vista-spliup"><img src="{img}spliup-logo-oro.webp" width="446" height="165" alt=""></span></span>
        <span class="puerta-texto"><span class="puerta-nombre">Spliup</span><span class="puerta-que">{esc(t["p_spliup_que"])}</span></span>
      </a></li>
      <li><a class="puerta" href="#golden-trays">
        <span class="marco"><span class="vista"><img src="{img}bandeja-sweet.webp" width="500" height="499" alt=""></span></span>
        <span class="puerta-texto"><span class="puerta-nombre">Golden Trays</span><span class="puerta-que">{esc(t["p_gt_que"])}</span></span>
      </a></li>
      <li><a class="puerta" href="#saxofon">
        <span class="marco"><span class="vista vista-sax"><img src="{img}saxofon-chica.webp" width="450" height="538" alt=""></span></span>
        <span class="puerta-texto"><span class="puerta-nombre">{esc(t["p_sax_nombre"])}</span><span class="puerta-que">{esc(t["p_sax_que"])}</span></span>
      </a></li>
    </ul>
  </section>

  <section class="banda banda-spliup" id="spliup" aria-labelledby="t-spliup">
    <div class="banda-interior">
      <div>
        <h2 id="t-spliup"><img src="{img}spliup-logo-oro.webp" width="446" height="165" alt="Spliup"></h2>
        <p class="lema">{esc(t["s_lema"])}</p>
        <p class="cuerpo">{esc(t["s_texto"])}</p>
        <ul class="hechos">
{lista(t["s_hechos"])}
        </ul>
        <p class="acciones"><a class="boton" href="https://spliup.com/">{esc(t["s_boton"])}</a></p>
        <p class="nota">{esc(t["s_nota"])}</p>
      </div>
      <figure class="chat" aria-label="{esc(t["chat_aria"])}">
        <div class="chat-cabeza" aria-hidden="true"><span class="chat-avatar">EC</span><span class="chat-nombre">{esc(t["chat_negocio"])}<span class="chat-estado">{esc(t["chat_estado"])}</span></span></div>
        <div class="chat-mensajes">
{msgs}
        </div>
        <p class="chat-aviso">{esc(t["chat_aviso"])}</p>
        <figcaption>{esc(t["chat_pie"])}</figcaption>
      </figure>
    </div>
  </section>

  <section class="banda banda-gt" id="golden-trays" aria-labelledby="t-gt">
    <div class="banda-interior">
      <div>
        <div class="gt-cabeza">
          <img class="gt-logo" src="{img}golden-trays-logo.webp" width="440" height="440" alt="">
          <div><h2 id="t-gt">Golden Trays</h2><p class="lema" lang="en">{esc(t["g_lema"])}</p></div>
        </div>
        <p class="cuerpo">{esc(t["g_texto"])}</p>
        <ul class="hechos">
{lista(t["g_hechos"])}
        </ul>
        <p class="gt-estado">{esc(t["g_estado"])}</p>
        <p class="acciones"><a class="boton" href="https://goldentrays.com/">{esc(t["g_boton"])}</a><a class="boton boton-linea" href="https://www.instagram.com/goldentraysnyc/">{esc(t["g_boton2"])}</a></p>
        <p class="nota">{esc(t["g_nota"])}</p>
      </div>
      <div class="gt-fotos" role="group" aria-label="{esc(t["g_fotos_aria"])}">
{fotos}
      </div>
    </div>
  </section>

  <section class="banda banda-sax" id="saxofon" aria-labelledby="t-sax">
    <div class="banda-interior">
      <div class="sax-foto"><div class="marco"><div class="vista"><img src="{img}saxofon.webp" width="900" height="1075" loading="lazy" decoding="async" alt="{esc(t["foto_sax_alt"])}"></div></div></div>
      <div>
        <h2 id="t-sax">{esc(t["x_titulo"])}</h2>
        <p class="lema">{esc(t["x_lema"])}</p>
        <p class="cuerpo">{esc(t["x_texto"])}</p>
        <ul class="hechos">
{lista(t["x_hechos"])}
        </ul>
        <p class="acciones"><a class="boton" href="{esc(mailto(t["x_asunto"], t["x_cuerpo"]))}">{esc(t["x_boton"])}</a></p>
        <p class="cruce">{esc(t["x_cruce"])} <a href="#golden-trays">{esc(t["x_cruce_enlace"])}</a></p>
      </div>
    </div>
  </section>

  <section class="contacto" id="contacto" aria-labelledby="t-contacto">
    <div>
      <h2 id="t-contacto">{esc(t["c_titulo"])}</h2>
      <p class="cuerpo">{esc(t["c_texto"])}</p>
      <a class="correo" href="mailto:{CORREO}">{CORREO}</a>
    </div>
    <dl class="datos">
      <div><dt>{esc(t["c_empresa"])}</dt><dd>Solution Prime LLC</dd></div>
      <div><dt>{esc(t["c_lugar"])}</dt><dd>{esc(t["c_lugar_valor"])}</dd></div>
      <div><dt>{esc(t["c_proyectos"])}</dt><dd><ul>
        <li><a href="https://spliup.com/">spliup.com</a></li>
        <li><a href="https://goldentrays.com/">goldentrays.com</a></li>
        <li><a href="https://www.instagram.com/goldentraysnyc/">@goldentraysnyc</a></li>
      </ul></dd></div>
    </dl>
  </section>
</main>
<footer class="pie">
  <p>© {ANIO} Solution Prime LLC</p>
  <p>{esc(t["pie"])}</p>
</footer>
</body>
</html>
"""


def pagina_404():
    t = TEXTOS["es"]
    e = TEXTOS["en"]
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["n_titulo"])} | Solution Prime LLC</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<style>{CSS}
.no-existe{{width:min(100% - 2*var(--margen),var(--ancho));margin-inline:auto;padding:clamp(48px,10vw,140px) 0;display:grid;gap:22px;justify-items:start}}
.no-existe h1{{font-size:clamp(2.4rem,6vw,4.4rem)}}
.no-existe .boton{{background:var(--tinta);color:var(--fondo)}}
</style>
</head>
<body>
<header class="cabecera"><a class="marca" href="/">Solution Prime <small>LLC</small></a></header>
<main class="no-existe">
  <h1>{esc(t["n_titulo"])}</h1>
  <p class="entrada">{esc(t["n_texto"])}</p>
  <p class="entrada" lang="en">{esc(e["n_titulo"])}. {esc(e["n_texto"])}</p>
  <p class="acciones"><a class="boton" href="/">{esc(t["n_boton"])}</a> <a href="/en/" lang="en">{esc(e["n_boton"])}</a></p>
</main>
</body>
</html>
"""


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F3A2D"/><path d="M21 49V30a11 11 0 0 1 22 0v19" fill="none" stroke="#E0BE74" stroke-width="4"/><path d="M14 49h36" stroke="#E0BE74" stroke-width="4" stroke-linecap="round"/></svg>
"""

ROBOTS = f"""User-agent: *
Allow: /

Sitemap: {DOMINIO}/sitemap.xml
"""

SITEMAP = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>{DOMINIO}/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{DOMINIO}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMINIO}/en/"/>
  </url>
  <url>
    <loc>{DOMINIO}/en/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{DOMINIO}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMINIO}/en/"/>
  </url>
</urlset>
"""

if __name__ == "__main__":
    (SITIO / "en").mkdir(parents=True, exist_ok=True)
    (SITIO / "index.html").write_text(pagina("es"), encoding="utf-8")
    (SITIO / "en" / "index.html").write_text(pagina("en"), encoding="utf-8")
    (SITIO / "404.html").write_text(pagina_404(), encoding="utf-8")
    (SITIO / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    (SITIO / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (SITIO / "sitemap.xml").write_text(SITEMAP, encoding="utf-8")
    for f in sorted(SITIO.rglob("*")):
        if f.is_file():
            print(f.relative_to(SITIO), f.stat().st_size)
