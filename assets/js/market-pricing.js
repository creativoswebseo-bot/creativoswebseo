(function () {
  const prices = {
    latam: { value: 69, currency: 'USD' },
    us: { value: 149, currency: 'USD' },
    fr: { value: 149, currency: 'EUR' }
  };
  const latamCountries = new Set([
    'AR', 'BO', 'BR', 'BZ', 'CL', 'CO', 'CR', 'CU', 'DO', 'EC', 'SV', 'GT',
    'HN', 'MX', 'NI', 'PA', 'PE', 'PY', 'UY', 'VE'
  ]);
  const selector = document.getElementById('market-select');
  const priceNodes = document.querySelectorAll('[data-promo-price]');
  const cta = document.querySelector('[data-promo-cta]');
  if (!selector || !priceNodes.length) return;

  const lang = document.documentElement.lang;
  const routeDefault = lang === 'fr' ? 'fr' : (lang === 'en' ? 'us' : 'latam');
  const labels = {
    es: 'Hola, quiero la Landing Flash de 72 horas',
    en: 'Hi, I am interested in the 72-hour Landing Page offer',
    fr: 'Bonjour, je suis intéressé par l’offre landing page sous 72 h'
  };

  function setMarket(market) {
    const selected = prices[market] ? market : routeDefault;
    const offer = prices[selected];
    selector.value = selected;
    priceNodes.forEach((node) => {
      node.textContent = offer.currency === 'EUR'
        ? `${offer.value} €`
        : `${offer.currency} ${offer.value}`;
    });
    if (cta) {
      const message = labels[lang] || labels.es;
      cta.href = `https://wa.me/593978747864?text=${encodeURIComponent(message)}`;
    }
  }

  selector.addEventListener('change', () => setMarket(selector.value));
  setMarket(routeDefault);

  fetch('https://ipwho.is/?fields=success,country_code', { cache: 'no-store' })
    .then((response) => response.ok ? response.json() : null)
    .then((location) => {
      if (!location || !location.success || !location.country_code) return;
      const country = location.country_code.toUpperCase();
      const detected = country === 'FR' ? 'fr'
        : country === 'US' ? 'us'
          : latamCountries.has(country) ? 'latam'
            : routeDefault;
      setMarket(detected);
    })
    .catch(() => { /* Keep the language-specific default price if lookup fails. */ });
})();
