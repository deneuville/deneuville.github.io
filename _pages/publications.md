---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

You can also find my articles on my <u><a href="https://scholar.google.fr/citations?user=zwOOX2IAAAAJ&hl=fr&oi=ao">Google Scholar profile</a></u>, <u><a href="https://www.researchgate.net/profile/Jean-Christophe_Deneuville">ResearchGate profile</a></u>, or <u><a href="https://dblp.org/pers/hd/d/Deneuville:Jean=Christophe">DBLP profile</a></u>.

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
