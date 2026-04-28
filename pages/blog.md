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
      <article class="box-item">
        <span class="category">
          <a href="{{ site.baseurl }}/{{ site.categories_folder | default: 'category' }}/{{ post.category }}">
            <span>{{ post.category }}</span>
          </a>
        </span>
        <div class="box-body">
          <a class="cover" href="{{ post.url | prepend: site.baseurl }}">
            {% include loader.html %}
            {% if post.optimized_image %}
              <img src="/assets/img/placeholder.png" width="100%" data-url="{{ post.optimized_image }}" class="preload">
              <noscript>
                <img src="{{ post.optimized_image }}" width="100%">
              </noscript>
            {% elsif post.image %}
              <img src="/assets/img/placeholder.png" width="100%" data-url="{{ post.image }}" class="preload">
              <noscript>
                <img src="{{ post.image }}" width="100%">
              </noscript>
            {% else %}
              <img src="/assets/img/placeholder.png" width="100%" data-url="/assets/img/off.jpg" class="preload">
              <noscript>
                <img src="/assets/img/off.jpg" width="100%">
              </noscript>
            {% endif %}
            {% include new-post-tag.html date=post.date %}
            {% include read-icon.html %}
          </a>
          <div class="box-info">
            <time datetime="{{ post.date | date_to_xmlschema }}" class="date">
              {% include date.html date=post.date %}
            </time>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">
              <h2 class="post-title">
                {{ post.title }}
              </h2>
            </a>
            <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">
              <p class="description">{{ post.description }}</p>
            </a>
            <div class="tags">
              {% for tag in post.tags %}
                {% if tag != "" %}
                  <a href="{{ site.baseurl}}/tags/#{{tag | slugify }}">#{{ tag }}</a>
                {% endif %}
              {% endfor %}
            </div>
          </div>
        </div>
      </article>
    {% endfor %}
  </section>
</main>
