---
layout: main
title: Newsletter
description: Notes on physics, AI, and building practical systems from first principles.
permalink: /newsletter/
---

<style>
  .newsletter-back-nav {
    padding: 68px 0 5px 23px;
  }

  .newsletter-home {
    padding-top: 0;
  }

  .newsletter-home .page-hero {
    padding-top: 24px;
  }

  .back-to-home-newsletter {
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

  .back-to-home-newsletter::before {
    content: "←";
    font-size: 24px;
    transition: transform 0.3s ease;
  }

  .back-to-home-newsletter:hover {
    color: #ff0a16;
  }

  .back-to-home-newsletter:hover::before {
    transform: translateX(-4px);
  }

  .newsletter-section {
    margin: 0 auto 2rem;
    padding: 0 23px;
    max-width: 900px;
  }

  .newsletter-panel {
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 12px;
    padding: 1.25rem;
    background: rgba(255, 255, 255, 0.04);
    color: #fff;
  }

  .newsletter-panel h2,
  .newsletter-panel p,
  .newsletter-panel li {
    color: inherit;
  }

  .newsletter-panel .contact-form {
    padding: 0;
  }

  .newsletter-panel .contact-form fieldset {
    padding: 0;
    margin: 0;
  }

  .newsletter-panel .contact-form input[type="email"] {
    width: 100%;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.3);
    padding: 0.75rem;
    color: #fff;
    background: rgba(0, 0, 0, 0.25);
    margin: 0 0 0.75rem;
  }

  .newsletter-panel .contact-form button[type="submit"] {
    border: 1px solid #ff0a16;
    background: #ff0a16;
    color: #fff;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    padding: 0.7rem 1rem;
  }

  .newsletter-panel .contact-form button[type="submit"]:hover {
    background: #d50812;
    border-color: #d50812;
  }

  .newsletter-helper {
    margin: 0;
    color: #f6d178;
  }

  .newsletter-archive-list {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .newsletter-archive-list li {
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
    padding: 0.85rem 0;
    color: #fff;
  }

  .newsletter-archive-list li:last-child {
    border-bottom: 0;
  }

  .newsletter-archive-list a {
    color: #fff;
    text-decoration: none;
    font-weight: 600;
  }

  .newsletter-archive-list a:hover {
    color: #ff0a16;
  }

  .newsletter-archive-date {
    display: block;
    color: rgba(255, 255, 255, 0.8);
    font-size: 0.9rem;
    margin-bottom: 0.25rem;
  }

  @media (min-width: 37.5rem) {
    .newsletter-back-nav {
      padding-top: 76px;
    }

    .newsletter-home .page-hero {
      padding-top: 28px;
    }

    .back-to-home-newsletter {
      font-size: 20px;
    }

    .back-to-home-newsletter::before {
      font-size: 28px;
    }
  }
</style>

{% assign newsletters = site.newsletters | sort: "date" | reverse %}

<nav class="newsletter-back-nav">
  <a href="/" class="back-to-home-newsletter">Back to Home</a>
</nav>

<main class="home no-padding newsletter-home" role="main">
  {% include page-hero.html title="NEWSLETTER" description=page.description %}

  <section class="newsletter-section">
    <div class="newsletter-panel">
      <h2>Subscribe</h2>
      <p>Get monthly updates on my projects, essays, and experiments.</p>
      {% include buttondown-signup.html %}
    </div>
  </section>

  <section class="newsletter-section">
    <div class="newsletter-panel">
      <h2>Archive</h2>
      {% if newsletters.size > 0 %}
        <ul class="newsletter-archive-list">
          {% for issue in newsletters %}
            <li>
              <span class="newsletter-archive-date">{{ issue.date | date: "%B %-d, %Y" }}</span>
              <a href="{{ issue.url | prepend: site.baseurl }}">{{ issue.title }}</a>
            </li>
          {% endfor %}
        </ul>
      {% else %}
        <p>No issues published yet.</p>
      {% endif %}
    </div>
  </section>
</main>
