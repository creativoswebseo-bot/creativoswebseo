from pathlib import Path
from urllib.parse import quote, unquote
import re

root = Path(__file__).parent
source = (root / "index.html").read_text(encoding="utf-8")

translations = {
    "en": {
        'title': 'Creativos WebSEO | Websites and landing pages',
        'description': 'Website and landing page design for businesses. Mobile-friendly pages with a direct WhatsApp contact path. Online service.',
        'pairs': [
            ('Nosotros', 'About'), ('Servicios', 'Services'), ('Precios', 'Pricing'), ('Contacto', 'Contact'),
            ('Hablar por WhatsApp', 'Chat on WhatsApp'), ('Menú', 'Menu'),
            ('Consultar por WhatsApp', 'Ask on WhatsApp'), ('Consultar', 'Ask about this service'),
            ('Diseño web · Atención online en español', 'Website design · Online service'),
            ('Una página clara para que tus clientes sepan ', 'A clear page that helps customers understand '),
            ('qué ofreces y cómo contactarte', 'what you offer and how to reach you'),
            ('Diseñamos páginas ligeras y adaptadas a móviles para presentar tu negocio, servicio o promoción con un camino de contacto directo.', 'We build lightweight, mobile-friendly pages to present your business, service, or offer and make it easy for visitors to contact you.'),
            ('Hablar sobre mi proyecto', 'Discuss my project'), ('Ver servicios', 'View services'),
            ('1 página', '1 page'), ('Un objetivo y contacto directo', 'One goal and a direct contact path'),
            ('Entrega de la promo desde recibir el material', '72-hour delivery after materials arrive'), ('Promo Landing Flash', '72-hour landing offer'),
            ('Tu negocio en código', 'Your business in code'), ('Clientes', 'Customers'),
            ('¿Por qué elegirnos?', 'Why work with us?'),
            ('Una web enfocada en tu ', 'A website focused on your '), ('oferta', 'offer'),
            ('Cuidamos la estructura, la lectura en móvil y el camino para que una persona interesada pueda contactarte.', 'We focus on clear structure, mobile readability, and an easy way for interested visitors to contact you.'),
            ('Carga ligera', 'Lightweight pages'), ('Usamos una estructura ligera y cuidamos que la página funcione bien en móviles y conexiones habituales.', 'We use a lightweight structure and make sure the page works well on phones and everyday connections.'),
            ('Menos dependencias', 'Fewer dependencies'), ('Una página estática evita depender de una base de datos o de muchos complementos para mostrar tu oferta.', 'A static page can present your offer without relying on a database or a large number of plugins.'),
            ('Adaptada a móviles', 'Mobile-friendly'), ('La información y los botones se ajustan a celulares, tabletas y computadores.', 'The content and buttons adapt to phones, tablets, and computers.'),
            ('Contacto visible', 'Easy to contact you'), ('Organizamos la página alrededor de tu oferta y facilitamos que una persona interesada te escriba.', 'We organize the page around your offer and make it easy for interested visitors to get in touch.'),
            ('Alcance claro', 'Clear project scope'), ('Definimos qué incluye el proyecto antes de empezar. Los servicios recurrentes se cotizan por separado.', 'We agree on what the project includes before work begins. Ongoing services are quoted separately.'),
            ('Atención online', 'Online service'), ('Trabajamos a distancia y coordinamos el proyecto por WhatsApp.', 'We work remotely and coordinate projects on WhatsApp.'),
            ('Portafolio de Servicios', 'Services'), ('Todo lo que tu negocio <em>necesita</em>', 'Services your business <em>may need</em>'),
            ('Desde tu primera presencia digital hasta campañas completas de publicidad. Tú eliges lo que necesitas.', 'From a first online presence to campaign setup. Choose the service that fits your needs.'),
            ('Paquete completo', 'Complete package'), ('El Combo "Máquina de Ventas"', 'Website + Ads Setup Package'),
            ('Landing page y preparación inicial de publicidad en un solo paquete. El presupuesto de anuncios se define por separado.', 'A landing page and initial ad campaign setup in one package. The ad spend is separate.'),
            ('Landing Page HTML', 'HTML landing page'), ('Configuración inicial de Ads', 'Initial Ads setup'),
            ('3 artes para redes', '3 social media graphics'), ('Conexión WhatsApp', 'WhatsApp integration'), ('Segmentación de audiencia', 'Audience targeting'),
            ('Valor por separado: $198', 'Separate services: USD 198'), ('Quiero este combo', 'Choose this package'),
            ('Landing Express', 'Express Landing Page'), ('Una página enfocada en presentar una oferta o servicio y facilitar el contacto.', 'A single page focused on presenting one offer or service and making it easy to get in touch.'),
            ('Diseño en HTML puro', 'Built with HTML'), ('Optimizada para móviles', 'Mobile-friendly'), ('Botón de WhatsApp integrado', 'WhatsApp contact button'), ('Carga ultrarrápida', 'Lightweight page'), ('Lista para hosting compatible', 'Ready for compatible hosting'),
            ('Web Corporativa', 'Business Website'), ('Hasta 7 secciones para presentar tu empresa, sus servicios y formas de contacto.', 'Up to 7 sections to present your company, services, and contact options.'),
            ('Hasta 7 secciones (Nosotros, Servicios, Blog, Galería, etc.)', 'Up to 7 sections (About, Services, Blog, Gallery, and more)'), ('Configuración SEO técnica básica', 'Basic technical SEO setup'), ('Diseño exclusivo a medida', 'Custom design'), ('Integración WhatsApp', 'WhatsApp integration'), ('Entrega en 7 días hábiles', 'Delivery in 7 business days'),
            ('Plan Lanzamiento Ads', 'Ads Launch Setup'), ('Configuración inicial de una campaña. El presupuesto de anuncios no está incluido.', 'Initial campaign setup. Ad spend is not included.'), ('Setup de cuenta publicitaria', 'Ad account setup'), ('3 artes o videos diseñados', '3 designed graphics or videos'), ('Segmentación de audiencia', 'Audience targeting'), ('Configuración de píxeles de rastreo', 'Tracking pixel setup'),
            ('Mantenimiento Mensual', 'Monthly Maintenance'), ('Soporte recurrente y actualizaciones de contenido según el alcance acordado.', 'Ongoing support and content updates within the agreed scope.'), ('Actualizaciones según el plan acordado', 'Updates under the agreed plan'), ('Gestión de hosting incluida', 'Hosting management included'), ('Soporte prioritario', 'Priority support'), ('Actualizaciones de contenido', 'Content updates'),
            ('Servicios y <em>precios</em>', 'Services and <em>pricing</em>'), ('Los precios corresponden al alcance indicado. Solicita una cotización si necesitas funciones adicionales.', 'Prices apply to the scope shown. Ask for a quote if you need additional features.'),
            ('Servicio', 'Service'), ('Descripción', 'Description'), ('Precio (USD)', 'Price (USD)'), ('RECOMENDADO', 'FEATURED'),
            ('Combo Web + Ads', 'Website + Ads Package'), ('Landing Page HTML + Plan Lanzamiento Ads completo', 'HTML landing page + complete Ads launch setup'), ('Web de una sección, HTML puro, lista para publicar', 'One-page website, built with HTML, ready to publish'), ('Hasta 7 secciones, SEO técnico y diseño exclusivo', 'Up to 7 sections, technical SEO, and custom design'), ('Setup de ads, 3 artes, segmentación y píxeles', 'Ads setup, 3 graphics, targeting, and tracking pixels'),
            ('Gestión de Campaña', 'Campaign Setup'), ('Montaje y optimización por cada campaña adicional', 'Setup and optimization for each additional campaign'), ('Actualización de Contenido', 'Content Update'), ('Cambio de foto, precio o texto en tu web existente', 'Update a photo, price, or text on your existing website'), ('Cambios ilimitados + hosting + soporte total', 'Updates + hosting + support under the agreed plan'),
            ('Empecemos', 'Let’s get started'), ('¿Quieres presentar mejor tu ', 'Want to present your '), ('Cuéntanos qué necesitas por WhatsApp y te responderemos con el siguiente paso.', 'Tell us what you need on WhatsApp and we’ll reply with the next step.'), ('Escribir al WhatsApp', 'Message us on WhatsApp'),
            ('Hecho con HTML puro · ', 'Built with HTML · '), ('Seleccionar idioma', 'Choose language'), ('Oferta especial · entrega en 72 horas', 'Special offer · delivered in 72 hours'), ('Una landing page lista para presentar tu oferta', 'A landing page ready to present your offer'), ('Una sola página, adaptada a móviles y con botón de WhatsApp. El plazo de 72 horas empieza cuando recibimos el contenido, las imágenes y los datos necesarios.', 'One mobile-friendly page with a WhatsApp button. The 72-hour delivery window starts once we receive your copy, images, and required details.'), ('Ver precio para', 'Show price for'), ('Latinoamérica · USD', 'Latin America · USD'), ('Estados Unidos · USD', 'United States · USD'), ('Francia · EUR', 'France · EUR'), ('Elegir mercado de precios', 'Choose pricing market'), ('Sugerimos un mercado según el país aproximado de tu conexión. Puedes cambiarlo; la detección puede fallar con VPN.', 'We suggest a market based on your connection’s approximate country. You can change it; VPNs may affect detection.'), ('Precio promocional', 'Promotional price'), ('Consultar por WhatsApp', 'Ask on WhatsApp'),
        ],
    },
    "fr": {
        'title': 'Creativos WebSEO | Sites web et landing pages',
        'description': 'Création de sites web et de landing pages légers, adaptés aux mobiles et avec contact direct par WhatsApp. Service en ligne.',
        'pairs': [
            ('Nosotros', 'À propos'), ('Servicios', 'Services'), ('Precios', 'Tarifs'), ('Contacto', 'Contact'),
            ('Hablar por WhatsApp', 'Écrire sur WhatsApp'), ('Menú', 'Menu'),
            ('Consultar por WhatsApp', 'Demander sur WhatsApp'), ('Consultar', 'Demander un devis'),
            ('Diseño web · Atención online en español', 'Création web · Service en ligne'),
            ('Una página clara para que tus clientes sepan ', 'Une page claire pour que vos clients comprennent '),
            ('qué ofreces y cómo contactarte', 'votre offre et sachent comment vous joindre'),
            ('Diseñamos páginas ligeras y adaptadas a móviles para presentar tu negocio, servicio o promoción con un camino de contacto directo.', 'Nous créons des pages légères et adaptées aux mobiles pour présenter votre activité, votre service ou votre offre et faciliter le contact.'),
            ('Hablar sobre mi proyecto', 'Parler de mon projet'), ('Ver servicios', 'Voir les services'),
            ('1 página', '1 page'), ('Un objetivo y contacto directo', 'Un objectif et un contact direct'),
            ('Entrega de la promo desde recibir el material', 'Livraison sous 72 h après réception des éléments'), ('Promo Landing Flash', 'Offre landing page 72 h'),
            ('Tu negocio en código', 'Votre activité en code'), ('Clientes', 'Clients'),
            ('¿Por qué elegirnos?', 'Pourquoi nous choisir ?'),
            ('Una web enfocada en tu ', 'Un site centré sur votre '), ('oferta', 'offre'),
            ('Cuidamos la estructura, la lectura en móvil y el camino para que una persona interesada pueda contactarte.', 'Nous soignons la structure, la lecture sur mobile et le parcours de contact pour les personnes intéressées.'),
            ('Carga ligera', 'Pages légères'), ('Usamos una estructura ligera y cuidamos que la página funcione bien en móviles y conexiones habituales.', 'Nous utilisons une structure légère et veillons au bon fonctionnement sur mobile et avec des connexions courantes.'),
            ('Menos dependencias', 'Moins de dépendances'), ('Una página estática evita depender de una base de datos o de muchos complementos para mostrar tu oferta.', 'Une page statique présente votre offre sans dépendre d’une base de données ni de nombreux modules.'),
            ('Adaptada a móviles', 'Adaptée aux mobiles'), ('La información y los botones se ajustan a celulares, tabletas y computadores.', 'Le contenu et les boutons s’adaptent aux téléphones, tablettes et ordinateurs.'),
            ('Contacto visible', 'Contact facile'), ('Organizamos la página alrededor de tu oferta y facilitamos que una persona interesada te escriba.', 'Nous organisons la page autour de votre offre et facilitons la prise de contact.'),
            ('Alcance claro', 'Périmètre clair'), ('Definimos qué incluye el proyecto antes de empezar. Los servicios recurrentes se cotizan por separado.', 'Nous définissons le contenu du projet avant de commencer. Les services récurrents sont chiffrés séparément.'),
            ('Atención online', 'Service en ligne'), ('Trabajamos a distancia y coordinamos el proyecto por WhatsApp.', 'Nous travaillons à distance et coordonnons le projet par WhatsApp.'),
            ('Portafolio de Servicios', 'Services'), ('Todo lo que tu negocio <em>necesita</em>', 'Les services dont votre activité <em>a besoin</em>'),
            ('Desde tu primera presencia digital hasta campañas completas de publicidad. Tú eliges lo que necesitas.', 'De votre première présence en ligne à la préparation de campagnes publicitaires. Choisissez le service adapté à vos besoins.'),
            ('Paquete completo', 'Pack complet'), ('El Combo "Máquina de Ventas"', 'Pack site web + publicité'),
            ('Landing page y preparación inicial de publicidad en un solo paquete. El presupuesto de anuncios se define por separado.', 'Une landing page et la préparation initiale d’une campagne dans un seul pack. Le budget publicitaire est facturé séparément.'),
            ('Landing Page HTML', 'Landing page HTML'), ('Configuración inicial de Ads', 'Configuration initiale des publicités'),
            ('3 artes para redes', '3 visuels pour les réseaux sociaux'), ('Conexión WhatsApp', 'Intégration WhatsApp'), ('Segmentación de audiencia', 'Ciblage de l’audience'),
            ('Valor por separado: $198', 'Prix séparé : 198 USD'), ('Quiero este combo', 'Choisir ce pack'),
            ('Landing Express', 'Landing page express'), ('Una página enfocada en presentar una oferta o servicio y facilitar el contacto.', 'Une page pour présenter une offre ou un service et faciliter la prise de contact.'),
            ('Diseño en HTML puro', 'Création en HTML'), ('Optimizada para móviles', 'Adaptée aux mobiles'), ('Botón de WhatsApp integrado', 'Bouton WhatsApp intégré'), ('Carga ultrarrápida', 'Page légère'), ('Lista para hosting compatible', 'Prête pour un hébergement compatible'),
            ('Web Corporativa', 'Site vitrine professionnel'), ('Hasta 7 secciones para presentar tu empresa, sus servicios y formas de contacto.', 'Jusqu’à 7 sections pour présenter votre entreprise, ses services et ses moyens de contact.'),
            ('Hasta 7 secciones (Nosotros, Servicios, Blog, Galería, etc.)', 'Jusqu’à 7 sections (À propos, Services, Blog, Galerie, etc.)'), ('Configuración SEO técnica básica', 'Configuration technique SEO de base'), ('Diseño exclusivo a medida', 'Design sur mesure'), ('Integración WhatsApp', 'Intégration WhatsApp'), ('Entrega en 7 días hábiles', 'Livraison sous 7 jours ouvrés'),
            ('Plan Lanzamiento Ads', 'Préparation de campagne publicitaire'), ('Configuración inicial de una campaña. El presupuesto de anuncios no está incluido.', 'Configuration initiale d’une campagne. Le budget publicitaire n’est pas inclus.'), ('Setup de cuenta publicitaria', 'Configuration du compte publicitaire'), ('3 artes o videos diseñados', '3 visuels ou vidéos conçus'), ('Segmentación de audiencia', 'Ciblage de l’audience'), ('Configuración de píxeles de rastreo', 'Configuration des pixels de suivi'),
            ('Mantenimiento Mensual', 'Maintenance mensuelle'), ('Soporte recurrente y actualizaciones de contenido según el alcance acordado.', 'Assistance récurrente et mises à jour du contenu selon le périmètre convenu.'), ('Actualizaciones según el plan acordado', 'Mises à jour selon le forfait convenu'), ('Gestión de hosting incluida', 'Gestion de l’hébergement incluse'), ('Soporte prioritario', 'Assistance prioritaire'), ('Actualizaciones de contenido', 'Mises à jour du contenu'),
            ('Servicios y <em>precios</em>', 'Services et <em>tarifs</em>'), ('Los precios corresponden al alcance indicado. Solicita una cotización si necesitas funciones adicionales.', 'Les tarifs correspondent au périmètre indiqué. Demandez un devis pour des fonctionnalités supplémentaires.'),
            ('Servicio', 'Service'), ('Descripción', 'Description'), ('Precio (USD)', 'Tarif (USD)'), ('RECOMENDADO', 'À LA UNE'),
            ('Combo Web + Ads', 'Pack site web + publicité'), ('Landing Page HTML + Plan Lanzamiento Ads completo', 'Landing page HTML + préparation complète de la campagne'), ('Web de una sección, HTML puro, lista para publicar', 'Site d’une page en HTML, prêt à être publié'), ('Hasta 7 secciones, SEO técnico y diseño exclusivo', 'Jusqu’à 7 sections, SEO technique et design sur mesure'), ('Setup de ads, 3 artes, segmentación y píxeles', 'Configuration publicitaire, 3 visuels, ciblage et pixels'),
            ('Gestión de Campaña', 'Configuration de campagne'), ('Montaje y optimización por cada campaña adicional', 'Configuration et optimisation de chaque campagne supplémentaire'), ('Actualización de Contenido', 'Mise à jour du contenu'), ('Cambio de foto, precio o texto en tu web existente', 'Modification d’une photo, d’un tarif ou d’un texte sur votre site'), ('Cambios ilimitados + hosting + soporte total', 'Mises à jour + hébergement + assistance selon le forfait convenu'),
            ('Empecemos', 'Commençons'), ('¿Quieres presentar mejor tu ', 'Vous souhaitez mieux présenter votre '), ('Cuéntanos qué necesitas por WhatsApp y te responderemos con el siguiente paso.', 'Expliquez-nous votre besoin sur WhatsApp et nous vous indiquerons la prochaine étape.'), ('Escribir al WhatsApp', 'Nous écrire sur WhatsApp'),
            ('Hecho con HTML puro · ', 'Créé en HTML · '), ('Seleccionar idioma', 'Choisir la langue'), ('Oferta especial · entrega en 72 horas', 'Offre spéciale · livraison sous 72 h'), ('Una landing page lista para presentar tu oferta', 'Une landing page prête à présenter votre offre'), ('Una sola página, adaptada a móviles y con botón de WhatsApp. El plazo de 72 horas empieza cuando recibimos el contenido, las imágenes y los datos necesarios.', 'Une page adaptée aux mobiles avec un bouton WhatsApp. Le délai de 72 h commence à réception des textes, images et informations nécessaires.'), ('Ver precio para', 'Voir le tarif pour'), ('Latinoamérica · USD', 'Amérique latine · USD'), ('Estados Unidos · USD', 'États-Unis · USD'), ('Francia · EUR', 'France · EUR'), ('Elegir mercado de precios', 'Choisir le marché tarifaire'), ('Sugerimos un mercado según el país aproximado de tu conexión. Puedes cambiarlo; la detección puede fallar con VPN.', 'Nous suggérons un marché selon le pays approximatif de votre connexion. Vous pouvez le modifier ; un VPN peut fausser la détection.'), ('Precio promocional', 'Tarif promotionnel'), ('Consultar por WhatsApp', 'Demander sur WhatsApp'),
        ],
    }
}

def make_locale(code, config):
    html = source.replace('<html lang="es">', f'<html lang="{code}">')
    html = html.replace('<title>Creativos WebSEO | Diseño web y landing pages</title>', f'<title>{config["title"]}</title>')
    html = html.replace('content="Diseño de páginas web y landing pages rápidas, adaptadas a móviles y con contacto directo por WhatsApp. Atención online en español."', f'content="{config["description"]}"')
    html = html.replace('<link rel="canonical" href="https://creativoswebseo.xyz/">', f'<link rel="canonical" href="https://creativoswebseo.xyz/{code}/">')
    for old, new in config['pairs']:
        html = html.replace(old, new)
    lang_nav = f'''<div class="language-switch" aria-label="{ 'Choose language' if code == 'en' else 'Choisir la langue' }">
      <a href="/" lang="es">ES</a>
      <a href="/en/" lang="en"{' aria-current="page"' if code == 'en' else ''}>EN</a>
      <a href="/fr/" lang="fr"{' aria-current="page"' if code == 'fr' else ''}>FR</a>
    </div>'''
    html = re.sub(r'<div class="language-switch"[^>]*>.*?</div>', lang_nav, html, count=1, flags=re.S)
    html = html.replace('      <li><a href="/blog/">Blog</a></li>\n', '')
    html = html.replace('href="/" lang="es" aria-current="page">ES', 'href="/" lang="es">ES')
    default_price = 'USD 149' if code == 'en' else '149 €'
    html = html.replace('data-promo-price>USD 69</', f'data-promo-price>{default_price}</')
    html = html.replace('  <script src="/assets/js/market-pricing.js"></script>\n', '')
    html = html.replace('<script>\n    // Hamburger menu', f'<script src="../assets/js/market-pricing.js"></script>\n  <script>\n    // Hamburger menu')
    wa_messages = {
        'en': 'Hi, I am interested in the 72-hour Landing Page offer',
        'fr': 'Bonjour, je suis intéressé par l’offre landing page sous 72 h',
    }
    message = quote(wa_messages[code], safe='')
    html = re.sub(r'(<a data-promo-cta href="https://wa\.me/593978747864\?text=)[^"]+',
                  rf'\g<1>{message}', html)
    wa_phrases = {
        'en': [
            ('Hola,%20quiero%20más%20información%20sobre%20sus%20servicios', 'Hi, I would like more information about your services'),
            ('Hola,%20quiero%20el%20Combo%20Máquina%20de%20Ventas%20por%20$190', 'Hi, I am interested in the Website and Ads package for USD 190'),
            ('Hola,%20quiero%20una%20Landing%20Express%20por%20$99', 'Hi, I am interested in an Express Landing Page for USD 99'),
            ('Hola,%20quiero%20una%20Web%20Corporativa%20por%20$350', 'Hi, I am interested in a Business Website for USD 350'),
            ('Hola,%20quiero%20el%20Plan%20de%20Lanzamiento%20Ads%20por%20$99', 'Hi, I am interested in Ads launch setup for USD 99'),
            ('Hola,%20me%20interesa%20el%20Mantenimiento%20Mensual%20por%20$100', 'Hi, I am interested in monthly maintenance for USD 100'),
            ('Hola,%20quiero%20información%20sobre%20sus%20servicios%20de%20diseño%20web', 'Hi, I would like information about your web design services'),
        ],
        'fr': [
            ('Hola,%20quiero%20más%20información%20sobre%20sus%20servicios', 'Bonjour, je voudrais en savoir plus sur vos services'),
            ('Hola,%20quiero%20el%20Combo%20Máquina%20de%20Ventas%20por%20$190', 'Bonjour, je suis intéressé par le pack site web et publicité à 190 USD'),
            ('Hola,%20quiero%20una%20Landing%20Express%20por%20$99', 'Bonjour, je suis intéressé par une landing page express à 99 USD'),
            ('Hola,%20quiero%20una%20Web%20Corporativa%20por%20$350', 'Bonjour, je suis intéressé par un site vitrine à 350 USD'),
            ('Hola,%20quiero%20el%20Plan%20de%20Lanzamiento%20Ads%20por%20$99', 'Bonjour, je suis intéressé par la préparation publicitaire à 99 USD'),
            ('Hola,%20me%20interesa%20el%20Mantenimiento%20Mensual%20por%20$100', 'Bonjour, je suis intéressé par la maintenance mensuelle à 100 USD'),
            ('Hola,%20quiero%20información%20sobre%20sus%20servicios%20de%20diseño%20web', 'Bonjour, je voudrais en savoir plus sur vos services de création web'),
        ],
    }
    def localize_wa(match):
        original = unquote(match.group(2)).lower()
        for spanish, localized in wa_phrases[code]:
            if unquote(spanish).lower() in original:
                return match.group(1) + quote(localized, safe='')
        return match.group(0)
    html = re.sub(r'(https://wa\.me/593978747864\?text=)([^"\s]+)', localize_wa, html)
    note_es = 'Sugerimos un mercado según el país aproximado de tu conexión mediante una consulta de IP. Puedes cambiarlo; la detección puede fallar con VPN.'
    note_localized = {
        'en': 'We suggest a market using your approximate country, checked through an IP lookup service. You can change it; VPNs may affect detection.',
        'fr': 'Nous suggérons un marché selon votre pays approximatif, estimé par un service de localisation IP. Vous pouvez le modifier ; un VPN peut fausser la détection.',
    }[code]
    html = html.replace(note_es, note_localized)
    path = root / code / 'index.html'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding='utf-8')

make_locale('en', translations['en'])
make_locale('fr', translations['fr'])
