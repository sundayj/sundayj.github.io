---
layout: post
title: Writing and managing content in Ghost, an advanced guide
tags:
- getting-started
---

Ghost comes with a best-in-class editor which does its very best to get out of the way, and let you focus on your content. Don't let its minimal looks fool you, though, beneath the surface lies a powerful editing toolset designed to accommodate the extensive needs of modern creators.

For many, the base canvas of the Ghost editor will feel familiar. You can start writing as you would expect, highlight content to access the toolbar you would expect, and generally use all of the keyboard shortcuts you would expect.

Our main focus in building the Ghost editor is to try and make as many things that you hope/expect might work: actually work.

- You can copy and paste raw content from web pages, and Ghost will do its best to correctly preserve the formatting. 
- Pasting an image from your clipboard will upload inline.
- Pasting a social media URL will automatically create an embed.
- Highlight a word in the editor and paste a URL from your clipboard on top: Ghost will turn it into a link.
- You can also paste (or write!) Markdown and Ghost will usually be able to auto-convert it into fully editable, formatted content.
<figure class="kg-card kg-image-card kg-width-wide kg-card-hascaption"><img src="https://static.ghost.org/v4.0.0/images/editor.png" class="kg-image" alt loading="lazy" width="3182" height="1500"><figcaption>The Ghost editor. Also available in dark-mode, for late night writing sessions.</figcaption></figure>

The goal, as much as possible, is for things to work so that you don't have to _think_ so much about the editor. You won't find any disastrous "block builders" here, where you have to open 6 submenus and choose from 18 different but identical alignment options. That's not what Ghost is about.

What you will find though, is dynamic cards which allow you to embed rich media into your posts and create beautifully laid out stories.

## Using cards

You can insert dynamic cards inside post content using the `+` button, which appears on new lines, or by typing `/` on a new line to trigger the card menu. Many of the choices are simple and intuitive, like bookmark cards, which allow you to create rich links with embedded structured data:

<figure class="kg-card kg-bookmark-card"><a class="kg-bookmark-container" href="https://opensubscriptionplatforms.com/"><div class="kg-bookmark-content">
<div class="kg-bookmark-title">Open Subscription Platforms</div>
<div class="kg-bookmark-description">A shared movement for independent subscription data.</div>
<div class="kg-bookmark-metadata">
<img class="kg-bookmark-icon" src="https://opensubscriptionplatforms.com/images/favicon.png" alt=""><span class="kg-bookmark-author">Open Subscription Platforms</span>
</div>
</div>
<div class="kg-bookmark-thumbnail"><img src="https://opensubscriptionplatforms.com/images/osp-card.png" alt=""></div></a></figure>

or embed cards which make it easy to insert content you want to share with your audience, from external services:

<figure class="kg-card kg-embed-card"><iframe width="200" height="113" src="https://www.youtube.com/embed/hmH3XMlms8E?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></figure>

But, dig a little deeper, and you'll also find more advanced cards, like one that only shows up in email newsletters (great for personalized introductions) and a comprehensive set of specialized cards for different types of images and galleries.

> Once you &nbsp;start mixing text and image cards creatively, the whole narrative of the story changes. Suddenly, you're working in a new format.

<figure class="kg-card kg-image-card kg-width-full"><img src="https://static.ghost.org/v4.0.0/images/andreas-selter-xSMqGH7gi6o-unsplash.jpg" class="kg-image" alt loading="lazy" width="6000" height="4000"></figure>

As it turns out, sometimes pictures and a thousand words go together really well. Telling people a great story often has much more impact if they can feel, even for a moment, as though they were right there with you.

<figure class="kg-card kg-gallery-card kg-width-wide"><div class="kg-gallery-container"><div class="kg-gallery-row">
<div class="kg-gallery-image"><img src="https://static.ghost.org/v4.0.0/images/andreas-selter-e4yK8QQlZa0-unsplash.jpg" width="4572" height="3048" loading="lazy" alt></div>
<div class="kg-gallery-image"><img src="https://static.ghost.org/v4.0.0/images/steve-carter-Ixp4YhCKZkI-unsplash.jpg" width="4032" height="2268" loading="lazy" alt></div>
</div></div></figure><figure class="kg-card kg-image-card kg-width-wide"><img src="https://static.ghost.org/v4.0.0/images/lukasz-szmigiel-jFCViYFYcus-unsplash.jpg" class="kg-image" alt loading="lazy" width="2560" height="1705"></figure><figure class="kg-card kg-gallery-card kg-width-wide kg-card-hascaption"><div class="kg-gallery-container"><div class="kg-gallery-row">
<div class="kg-gallery-image"><img src="https://static.ghost.org/v4.0.0/images/jd-mason-hPiEFq6-Eto-unsplash.jpg" width="5184" height="3888" loading="lazy" alt></div>
<div class="kg-gallery-image"><img src="https://static.ghost.org/v4.0.0/images/jp-valery-OBpOP9GVH9U-unsplash.jpg" width="5472" height="3648" loading="lazy" alt></div>
</div></div>
<figcaption>Peaceful places</figcaption></figure>

Galleries and image cards can be combined in so many different ways — the only limit is your imagination.

## Build workflows with snippets

One of the most powerful features of the Ghost editor is the ability to create and re-use content snippets. If you've ever used an email client with a concept of _saved replies_ then this will be immediately intuitive.

To create a snippet, select a piece of content in the editor that you'd like to re-use in future, then click on the snippet icon in the toolbar. Give your snippet a name, and you're all done. Now your snippet will be available from within the card menu, or you can search for it directly using the `/` command.

This works really well for saving images you might want to use often, like a company logo or team photo, links to resources you find yourself often linking to, or introductions and passages that you want to remember.

<figure class="kg-card kg-image-card kg-width-wide"><img src="https://static.ghost.org/v4.0.0/images/createsnippet.png" class="kg-image" alt loading="lazy" width="2282" height="1272"></figure>

You can even build entire post templates or outlines to create a quick, re-usable workflow for publishing over time. Or build custom design elements for your post with an HTML card, and use a snippet to insert it.

Once you get a few useful snippets set up, it's difficult to go back to the old way of diving through media libraries and trawling for that one thing you know you used somewhere that one time.

* * *

## Publishing and newsletters the easy way

When you're ready to publish, Ghost makes it as simple as possible to deliver your new post to all your existing members. Just hit the _Preview_ link and you'll get a chance to see what your content looks like on Web, Mobile, Email and Social.

<figure class="kg-card kg-image-card kg-width-wide"><img src="https://static.ghost.org/v4.0.0/images/preview.png" class="kg-image" alt loading="lazy" width="3166" height="2224"></figure>

You can send yourself a test newsletter to make sure everything looks good in your email client, and then hit the _Publish_ button to decide who to deliver it to.

Ghost comes with a streamlined, optimized email newsletter template that has settings built-in for you to customize the colors and typography. We've spent countless hours refining the template to make sure it works great across all email clients, and performs well for email deliverability.

So, you don't need to fight the awful process of building a custom email template from scratch. It's all done already!

* * *

The Ghost editor is powerful enough to do whatever you want it to do. With a little exploration, you'll be up and running in no time.

