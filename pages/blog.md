---
layout: main
title: Blog
description: My thoughts on physics, AI, and innovation.
permalink: /blog/
---

{% comment %} Use only real posts and skip generated paginated parts. {% endcomment %}
{% assign posts = site.posts | where_exp:"post","post.is_generated != true" %}

<main class="home" role="main">
  
  {% comment %} Reusable page hero: large page title + short description + divider. {% endcomment %}
  {% include page-hero.html title="BLOG" description=page.description %}

  {% comment %} Standard post card grid, matching home page visuals. {% endcomment %}
  <section id="grid" class="row flex-grid">
    {% for post in posts %}
      {% include tile-card.html item=post show_category=true show_date=true show_tags=true show_new_tag=true %}
    {% endfor %}
  </section>
</main>
