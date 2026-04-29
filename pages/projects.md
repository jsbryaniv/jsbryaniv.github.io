---
layout: main
title: Projects
description: My project portfolio.
permalink: /projects/
---

{% comment %} Project collection documents, sorted alphabetically for now. {% endcomment %}
{% assign projects = site.projects | sort: "title" %}

<main class="home" role="main">

  {% comment %} Reusable page hero: large page title + short description + divider. {% endcomment %}
  {% include page-hero.html title="PROJECTS" description=page.description %}

  {% comment %} Project card grid using the same visual system as the blog tiles. {% endcomment %}
  <section id="grid" class="row flex-grid">
    {% for project in projects %}
      {% assign project_display_name = project.name | default: project.title | default: project.slug %}
      {% assign project_image = "" %}
      {% if project.image %}
        {% assign image_first_char = project.image | slice: 0 %}
        {% if project.image contains "://" or image_first_char == "/" %}
          {% assign project_image = project.image %}
        {% else %}
          {% assign project_image = "/projects/" | append: project.slug | append: "/" | append: project.image %}
        {% endif %}
      {% endif %}

      {% if project_image != "" %}
        {% if project_image contains "://" %}
          {% assign project_image_url = project_image %}
        {% else %}
          {% assign project_image_url = project_image %}
        {% endif %}
      {% else %}
        {% assign project_image_url = "/assets/img/off.jpg" %}
      {% endif %}

      {% include tile-card.html item=project display_title=project_display_name image_url=project_image_url no_category=true %}
    {% endfor %}
  </section>
</main>
