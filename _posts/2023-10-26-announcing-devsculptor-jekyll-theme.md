---
layout: post
title: "Announcing the DevSculptor Jekyll Theme"
summary: >-
  In this post, I introduce DevSculptor, a Jekyll blog theme for developers. DevSculptor is compatible with GitHub pages and has many features to help you create a stunning blog.
  You can install it as a gem, a remote theme, or by downloading the source code. You can also customize it to fit your personal brand. You can check out the demo site, the source
  code, and the documentation on GitHub. I hope you like DevSculptor and let me know your feedback.
excerpt: >-
  In this post, I introduce DevSculptor, a Jekyll blog theme for developers. DevSculptor is compatible with GitHub pages and has many features to help you create a stunning blog.
  You can install it as a gem, a remote theme, or by downloading the source code. You can also customize it to fit your personal brand. You can check out the demo site, the source
  code, and the documentation on GitHub. I hope you like DevSculptor and let me know your feedback.
description: >-
  In this post, I introduce DevSculptor, a Jekyll blog theme for developers. DevSculptor is compatible with GitHub pages and has many features to help you create a stunning blog.
  You can install it as a gem, a remote theme, or by downloading the source code. You can also customize it to fit your personal brand. You can check out the demo site, the source
  code, and the documentation on GitHub. I hope you like DevSculptor and let me know your feedback.
canonical_url:  https://jlsunday.com/jekyll/2023/10/26/announcing-devsculptor-jekyll-theme.html
category: Jekyll
tags: [announcement,jekyll-theme,github-pages,ruby-gem,remote-theme,project]
image:  https://jlsunday.com/assets/images/projects/devsculptor/home-page-example.png
comments: true
date: 2023-10-26
author: Justin L. Sunday
include_TOC: true
featured: true
sort: 0
---

##  Introduction

I'm super excited to share with you my latest project: [DevSculptor](https://jlsunday.com/DevSculptor/){:target="_blank"}{:rel="noopener noreferrer"}, a Jekyll blog theme designed for developers who want to showcase their skills and projects. DevSculptor is
compatible with GitHub pages, so you can easily host your blog on your own domain without any hassle. You can also install DevSculptor as a gem or a remote theme,
depending on your preference. DevSculptor has a sleek and modern design, with features such as syntax highlighting, responsive layout, social media icons, pagination, and
more. You can customize DevSculptor to suit your personal style and brand, by changing the colors, fonts, logo, and other elements. DevSculptor is also SEO-friendly and fast-loading,
so you can reach more readers and rank higher on search engines.

### What is Jekyll?

[Jekyll](https://jekyllrb.com/){:target="_blank"}{:rel="noopener noreferrer"} is a static site generator that transforms your plain text into beautiful websites. Jekyll is perfect for blogs, portfolios, documentation, and more. Jekyll is easy to set up,
secure, and fast. You can write your content in Markdown, HTML, or any other format you like. You can also use themes, plugins, and custom layouts to make your site look
amazing. Jekyll is powered by [Ruby](https://www.ruby-lang.org/en/){:target="_blank"}{:rel="noopener noreferrer"} and works well with GitHub pages, which means you can host your site for free on GitHub.

## Features

DevSculptor has a lot of features that make it stand out from other Jekyll themes. Here are some of them:

- Responsive
- Dark and Light theme toggler
- SEO friendly
- Social Network friendly with Twitter Card support
- Site Search with [Algolia](https://www.algolia.com)
- Google Analytics Ready
- [Fabform](https://fabform.io/) Contact Form Ready
- [HTML Comment Box](https://www.htmlcommentbox.com/) Ready
- Code blocks use [GitHub Flavored Markdown](https://github.blog/2017-03-14-a-formal-spec-for-github-markdown/)
- Github gists for posts via the [jekyll-gist plugin](https://github.com/jekyll/jekyll-gist)
- Responsive Collapsible and Sticky TOC (Table of Contents) for posts
- Anchor links for headings within posts
- "Reading time" for posts to give readers estimates on how long it may take them to read.
- Includes Jekyll Admin (Optional)
- Emoji Ready
- RSS Feed for feed reader subscriptions
- Includes site map, privacy policy, cookie policy, and terms of service (It is your responsibility to
  make sure that the details outlined in the provided files match fit within your country/state's laws.)
- Blog Roll
- Résumé link opens your provided résumé as a PDF in a new tab
- Localization support with help from ChatGPT
    - English
    - Spanish (Español)
    - French (Français)
    - German (Deutsch)
    - Portuguese (Português)
    - Italian (Italiano)
    - Dutch (Nederlands)
    - Chinese (Simplified) - 中文 (Zhōngwén)
    - Japanese - 日本語 (Nihongo)
    - Polish - Polski
    - Korean - 한국어 (Hangugeo)
    - Russian - Русский (Russkiy)
    - Turkish - Türkçe
    - Indonesian - Bahasa Indonesia

You can customize the colors, fonts, and logo to suit your personal brand. You can also add more features by using Jekyll plugins or editing the code.

## Screen Shots

To give you a better idea of how DevSculptor looks, I've added some screenshots below. You can see the homepage, the post page, and the archive page. As you can
see, DevSculptor has a clean and minimalist aesthetic, with a focus on the content and the code. You can also see how DevSculptor adapts to different screen sizes and devices.

### Home Page

<figure style="margin-top: 20px;" class="figure">
    <img class="figure-img rounded" alt="Homepage Example - Dark Theme" src="{{ '/assets/images/projects/devsculptor/home-page-example.png' | prepend: site.url }}" loading="lazy" title="Homepage Example - Dark Theme">
    <figcaption class="figure-caption text-center">
        Home page example with the DevSculptor theme in dark mode.
    </figcaption>
</figure>

<figure style="margin-top: 20px;" class="figure">
    <img class="figure-img rounded" alt="Home Page Example - Light Theme" src="{{ '/assets/images/projects/devsculptor/home-page-example-light.png' | prepend: site.url }}" loading="lazy" title="Home Page Example - Light Theme">
    <figcaption class="figure-caption text-center">
        Home page example with the DevSculptor theme in light mode
    </figcaption>
</figure>

<div class="container">
  <div class="row row-cols-1 row-cols-md-2">
    <div class="col">
      <figure style="margin-top: 20px;">
          <img alt="Home Page Example on Mobile - Dark Theme" src="{{ '/assets/images/projects/devsculptor/20230926-samsung-galaxy-s20-ultra-homepage-screenshot-rocks.png' | prepend: site.url }}" loading="lazy" title="Home Page Example on Mobile - Dark Theme">
          <figcaption class="figure-caption text-center">
              Home page example on mobile in dark mode.
          </figcaption>
      </figure>
    </div>
    <div class="col">
      <figure style="margin-top: 20px;">
          <img alt="Home Page Example on Mobile - Light Theme" src="{{ '/assets/images/projects/devsculptor/20230926-samsung-galaxy-s20-ultra-homepage-screenshot-rocks-light-mode.png' | prepend: site.url }}" loading="lazy" title="Home Page Example on Mobile - Light Theme">
          <figcaption class="figure-caption text-center">
             Home page example on mobile in light mode.
          </figcaption>
      </figure>
    </div>
  </div>
</div>


## Installation

Now that you know what DevSculptor is and why you should use it, you might be wondering: how do I install DevSculptor? Well, there are two ways to install DevSculptor: as a
gem or as a remote theme. Let me explain the difference and how to do it.

### Using the Ruby Gem
If you install DevSculptor as a gem, you will need to add it to your Gemfile and run `bundle install`. Then you will need to add `theme: devsculptor` to your `_config.yml`
file. This way, you will have the theme files locally on your computer, and you can edit them as you wish. However, this also means that you will need to update the theme
manually whenever there is a new version available.

### Using the Remote Theme
If you install DevSculptor as a remote theme, you will need to add `remote_theme: sundayj/DevSculptor` to your `_config.yml` file. Then you will need to create a file
called `Gemfile` in your root directory and add the following lines:

[//]: # (TODO: Include details of what should be in Gemfile)
```gemfile

```

### Manual Conversion
To install DevSculptor without using a gem or a remote theme, you need to download the source code from GitHub and copy the files to your Jekyll site folder. You also need to
update your `_config.yml` file with the following settings:

```yaml
# Theme settings
theme: devsculptor
plugins:
  - jekyll-paginate
  - jekyll-seo-tag
  - jekyll-sitemap
  - jekyll-feed
  - jekyll-gist
  - jemoji

# Pagination settings
paginate: 5
paginate_path: "/page:num/"
```

Then run `bundle install`. This way, you will use the theme files directly from GitHub and you will always have the latest version of the theme. However, this also means that
you will not be able to edit the theme files directly, and you will need to use overrides or customizations instead.

You can choose whichever method suits you best. For more details on how to install DevSculptor, please refer to the [documentation](https://jlsunday.com/DevSculptor/documentation/2023/09/17/about-devsculptor.html){:target="_blank"}{:rel="noopener noreferrer"}.

## Final Words

If you're looking for a Jekyll blog theme that is easy to use, elegant, and powerful, look no further than DevSculptor. You can check out the demo site
[here](https://jlsunday.com/DevSculptor){:target="_blank"}{:rel="noopener noreferrer"} and the documentation
[here](https://jlsunday.com/DevSculptor/documentation/2023/09/17/about-devsculptor.html){:target="_blank"}{:rel="noopener noreferrer"}. You can also download or fork the source
code from GitHub, [sundayj/DevSculptor](https://github.com/sundayj/devsculptor){:target="_blank"}{:rel="noopener noreferrer"}. I hope you enjoy using DevSculptor
as much as I enjoyed creating it. Please let me know what you think of it and if you have any feedback or suggestions. Happy blogging!
