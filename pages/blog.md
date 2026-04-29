---
layout: main
title: Blog
description: My thoughts on physics, AI, and innovation.
permalink: /blog/
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

{% comment %} Use only real posts and skip generated paginated parts. {% endcomment %}
{% assign posts = site.posts | where_exp:"post","post.is_generated != true" %}

<nav class="collection-back-nav">
  <a href="/" class="back-to-home-collection">Back to Home</a>
</nav>

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
