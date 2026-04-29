---
layout: main
title: Projects
description: My project portfolio.
permalink: /projects/
---

<style>
  .collection-back-nav {
    padding: 80px 0 5px 23px;
  }
  
  .back-to-home-collection {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    color: #999;
    text-decoration: none;
    font-size: 18px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    transition: all 0.3s ease;
  }
  
  .back-to-home-collection::before {
    content: "←";
    font-size: 24px;
    transition: transform 0.3s ease;
  }
  
  .back-to-home-collection:hover {
    color: #ff0a16;
  }
  
  .back-to-home-collection:hover::before {
    transform: translateX(-4px);
  }
  
  @media (min-width: 37.5rem) {
    .collection-back-nav {
      padding-top: 90px;
    }
    
    .back-to-home-collection {
      font-size: 20px;
    }
    
    .back-to-home-collection::before {
      font-size: 28px;
    }
  }
</style>

{% comment %} Project collection documents, sorted alphabetically for now. {% endcomment %}
{% assign projects = site.projects | sort: "title" %}

<nav class="collection-back-nav">
  <a href="/" class="back-to-home-collection">Back to Home</a>
</nav>

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
