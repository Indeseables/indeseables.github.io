---
layout: page
title: Entradas
---


{% for post in site.posts %}
  {% assign author = site.authors[post.author] %}
  * [{{ author.display_name}}]({{author.github}}) , {{ post.date | date_to_string }} &raquo; [ {{ post.title }} ]({{ post.url }}) 
{% endfor %}
