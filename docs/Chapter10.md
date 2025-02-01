##  My Building Guide

#### Topic : Boostrap Styling
- 
---

1. Add CDN link to base template : CSS 1 & JS 3
2. Decorate the base, home templates
3. Install django_crispy_forms, crispy_bootstrap5
4. Set up `project/setting.py` : `CRISPY_ALLOW_TEMPLATE_PACKS`,`CRISPY_TEMPLATE_PACK`
5. Decorate form with `{%load crispy_forms_tags%}` and pipe tag in `{form|crispy}`