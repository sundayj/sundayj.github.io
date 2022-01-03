---
layout: page
title: Search
permalink: /search/
---

<div id="search-searchbar"></div>

<div class="post-list" id="search-hits">
   <!--- {% for post in site.posts %} -->
      <!--- <div class="post-item"> -->
        <!--- <span class="post-meta">{{ post.date }}</span> -->
       <!---  <h2> -->
          <!--- <a class="post-link" href="{{ post.url | relative_url }}"> -->
          <!---   {{ post.title | escape }} -->
          <!--- </a> -->
        <!--- </h2> -->
        <!--- <div class="post-snippet">{{ post.summary }}</div> -->
      <!--- </div> -->
    <!--- {% endfor %} -->
</div>

{% include algolia.html %}
