---
layout: page
title: Follow
permalink: /subscribe
---

{%- assign linkedin = site.data.social | where: "name", "linkedin" | first -%}

If you would like to follow new notes, musings, and project updates from {{ site.title }}, use the RSS feed below.

<div id="rss-button"><a href="/feed.xml" target="_blank" rel="noopener noreferrer"><i class="bi bi-rss-fill" style="font-size: 6rem;"></i></a></div>


With RSS, you do not have to worry about emails, and unsubscribing is as simple as removing the feed from your reader. Free RSS readers are available everywhere. One easy option is the Chrome extension [FeedBro](https://nodetics.com/feedbro/){:target="_blank"}{:rel="noopener noreferrer"}.

{%- if linkedin and linkedin.url -%}

## LinkedIn

If you prefer shorter updates and in-progress thoughts, you can also follow me on LinkedIn:

- [{{ linkedin.url }}]({{ linkedin.url }}){:target="_blank"}{:rel="noopener noreferrer"}

Featured LinkedIn cards on the homepage are managed manually through `_data/linkedin_posts.yml` so the site stays fast and does not depend on third-party feed scripts.
{%- endif -%}
