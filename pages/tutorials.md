---
layout: page
menu: false
date: '2026-04-24 00:00:01'
title: Tutorials
description: A collection of tutorials on physics and coding.
permalink: /tutorials/
---

<ul>
  {% assign tutorials = site.tutorials | sort: "date" | reverse %}
  {% for tutorial in tutorials %}
    <li>
      <a href="{{ tutorial.url | relative_url }}">{{ tutorial.title }}</a>
      {% if tutorial.excerpt %}<p>{{ tutorial.excerpt }}</p>{% endif %}
    </li>
  {% endfor %}
</ul>
