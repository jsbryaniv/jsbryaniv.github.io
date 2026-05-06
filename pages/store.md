---
layout: main
title: Shop
description: Where ideas become products you can actually use.
permalink: /shop/
---

<style>
  .collection-back-nav {
    padding: 68px 0 5px 23px;
  }

  .shop-home {
    padding-top: 0;
  }

  .shop-home .page-hero {
    padding-top: 24px;
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
      padding-top: 76px;
    }

    .shop-home .page-hero {
      padding-top: 28px;
    }

    .back-to-home-collection {
      font-size: 20px;
    }

    .back-to-home-collection::before {
      font-size: 28px;
    }
  }
</style>

{% assign visible_products = site.shop | where_exp: "p", "p.shop_hidden != true" %}
{% assign featured_products = visible_products | where_exp: "p", "p.shop_featured == true" | sort: "shop_order" %}
{% assign regular_products = visible_products | where_exp: "p", "p.shop_featured != true" | sort: "shop_order" %}
{% assign products = featured_products | concat: regular_products %}

<nav class="collection-back-nav">
  <a href="/" class="back-to-home-collection">Back to Home</a>
</nav>

<main class="home no-padding shop-home" role="main">
  {% include page-hero.html title="SHOP" description=page.description %}

  <section id="grid" class="row flex-grid">
    {% for product in products %}
      {% assign product_title = product.title | default: product.slug %}
      {% assign product_image = "" %}

      {% if product.image %}
        {% assign image_first_char = product.image | slice: 0 %}
        {% if product.image contains "://" or image_first_char == "/" %}
          {% assign product_image = product.image %}
        {% else %}
          {% assign product_image = "/shop/" | append: product.slug | append: "/" | append: product.image %}
        {% endif %}
      {% endif %}

      {% if product_image != "" %}
        {% assign product_image_url = product_image %}
      {% else %}
        {% assign product_image_url = "/assets/img/off.jpg" %}
      {% endif %}

      {% include tile-card.html item=product display_title=product_title description=product.subtitle image_url=product_image_url no_category=true %}
    {% endfor %}
  </section>
</main>
