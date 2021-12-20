<script src="/js/lunr.js"></script>

<script>
  {% assign counter = 0 %}
  window.store = [
      {% for page in site.pages %}
      {% if page.url contains '.xml' or page.url contains 'assets' %}
      {% else %}
      {
        "id": {{ counter }},
        "url": "{{ site.url }}{{ page.url }}",
        "title": "{{ page.title }}",
        "tags": "",
        "body": "{{ page.content | markdownify | replace: '.', '. ' | replace: '</h2>', ': ' | replace: '</h3>', ': ' | replace: '</h4>', ': ' | replace: '</p>', ' ' | strip_html | strip_newlines | replace: '  ', ' ' | replace: '"', ' ' }}"
        {% assign counter = counter | plus: 1 %}
      },
      {% endif %}
      {% endfor %}
      {% for page in site.posts %}
      {
        "id": {{ counter }},
        "url": "{{ site.url }}{{ page.url }}",
        "title": "{{ page.title }}",
        "tags": "{{page.tags | array_to_sentence_string}}",
        "body": "{{ page.date | date: "%Y/%m/%d" }} - {{ page.content | markdownify | replace: '.', '. ' | replace: '</h2>', ': ' | replace: '</h3>', ': ' | replace: '</h4>', ': ' | replace: '</p>', ' ' | strip_html | strip_newlines | replace: '  ', ' ' | replace: '"', ' ' }}"
        {% assign counter = counter | plus: 1 %}
      }
      {% if forloop.last %}
      {% else %},
      {% endif %}
      {% endfor %}];  
</script>