---
layout: post
title: "Comparing Pixel Art Editors"
summary: >-
    Part one of a series of posts comparing various Pixel Art Editors. Part one gives an intro to this series of posts
    and gives a short review of Aseprite. A comparison of various pixel art editing tools.
excerpt: >-
    Part one of a series of posts comparing various Pixel Art Editors. Part one gives an intro to this series of posts
    and gives a short review of Aseprite. A comparison of various pixel art editing tools.
description: >-
    Part one of a series of posts comparing various Pixel Art Editors. Part one gives an intro to this series of posts
    and gives a short review of Aseprite. A comparison of various pixel art editing tools.
canonical_url: https://JLSunday.com/tools/2022/06/11/Comparing-Pixel-Art-Editors.html
category: Tools
tags: [tools,pixel-art,game-development,tool-comparison,tool-review]
image: https://JLSunday.com/images/posts/undraw_design_components_9vy6.png
comments: true
date: 2022-06-11
last_modified_at: 2023/10/30
author: {{ site.author.name }}
include_TOC: true
featured: false
sort: 0
---

<figure style="margin-top: 20px;">
        <img alt="Design Components" src="{{ '/assets/images/posts/undraw/undraw_design_components_9vy6.png' | prepend: site.url }}" loading="lazy" title="Design Components">
    <figcaption>
        Image provided by <a href="https://undraw.co/search" target="_blank" rel="noopener noreferrer">unDraw.co</a>
    </figcaption>
</figure>
  
## Intro

<div class="alert alert-primary d-flex align-items-center" role="alert">
  <div>
    GENERAL BLOG UPDATE
  <hr>
    I know it's been a few months since I last posted, and I sincerely apologize if you were following my Angular series.
    I started a new job as a senior developer back in February, and it has consumed most of my time.
    I do plan to get back to the Angular tutorial eventually, but I have no immediate plans for it.
    If anyone is really interested in the Angular series, then please contact me; I'm much more likely to get back to it
    if I know there are people interested or dependent on the series.
  </div>
</div>

Hello again! In this post I will be comparing various pixel art editing tools. My ADD has decided it is time for me to
create my own video game, which is something I have been wanting to do for years. I may decide to do more posts on video
game development as my journey progresses, but who knows? I've known for a long time now that I want my game to have pixel
graphics, and, with my experience as an artist, I knew that I wanted to create my own art for my game. However, with my
propensity for abandoning personal projects, I figure it is best to create my game with as many free/open-source tools
as possible. While searching for the best pixel editor, I've come across many tools, and have downloaded and tested them
all to some degree. This post is as much to help myself decide on a final tool as to help any of you, good readers, that
may face a similar dilemma.

Of course, each of these tools have their pros and cons, which we will explore, but they also vary in their offered
features. It is those features that I will be comparing the most deeply. Hopefully, by the end of this post, I will have
chosen the editor for me, and, with any luck, you will have a better idea of the editor you'd like to use, as well.

## Feature Comparison Table

---

First, probably the most important part of this whole post: The Feature Comparison Table! The header row and first
column are sticky, so you can freely scroll in order to cross-reference each feature with each of the reviewed tools.
Also, clicking on one of the tools' names in the table header will take you straight to its respective review in the post
below.

Finally, a few notes about the icons in the table:
- If you see a <i class="fa fa-question"></i>, it is because I couldn't definitively tell if the feature exists in that tool.
- For LibreSprite Dotto, it is still very early in its development, so, while the features may be marked as absent, many
  of the features are planned for its future development and can be seen on their [roadmap](https://github.com/LibreSprite/Dotto#version-roadmap){:target="_blank"}{:rel="
  noopener noreferrer"}.

<br>
<div class="alert alert-primary d-flex align-items-center" role="alert">
  <div>
    The Comparison Table has been moved!
  <hr>
    Due to the large size of the comparison table, I decided to break it out into its own page. To see the table in a new tab, please click <a href="{{ '/Sprite-Editor-Comparison-Table' | prepend: site.url }}" target="_blank" rel="noopener noreferrer">here</a>. 
  </div>
</div>

<br>

<br>

### Feature Breakdown
<div class="tool-list">
    <details open>
        <summary style="cursor: pointer">
            <b>Pixel Perfect</b>
        </summary>
        Allows you to draw prettier lines an curves. Without a Pixel Perfect feature, lines drawn freehand will usually
        have extra pixels that give lines a distorted or bumpy look in places where it should look straighter. Pixel
        Perfect helps with this either by deleting extra pixels as you go, or by creating a pixel at a diagonal to
        give a better angled look.
        <figure>
            <img alt="Layer Example" src="{{ '/assets/images/posts/pixel-editors/pixel-perfect-example.png' | prepend: site.url }}" loading="lazy" title="Layer Example">
            <figcaption>
                Image borrowed from <a href="https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-7-e504bfa4ddf2" target="_blank" rel="noopener noreferrer">The Pixel Grimoire</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Layers</b>
        </summary>
        Layers are transparent sheets that allow you to separate elements of your art. This separation allows you to draw
        on one layer without fear of affecting other layers. This helps greatly with animation, or giving a feeling of
        depth to your art.
        <figure>
            <img alt="Pixel Perfect Example" src="{{ '/assets/images/posts/pixel-editors/1Layer-Layers-9.webp' | prepend: site.url }}" loading="lazy" title="Pixel Perfect Example">
            <figcaption>
                Image borrowed from <a href="https://learnindie.com/pixel-art-aseprite-1-layers/" target="_blank" rel="noopener noreferrer">LearnIndie.com</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Symmetry Mirror Pen</b>
        </summary>
        Symmetry tools, or mirror pens, allow you to draw art that is perfectly symmetrical vertically and/or horizontally.
        This can be useful for patterns and designs, or even drawing the front view of a characters face.
        <figure>
            <img alt="Symmetry Pen Example" src="{{ '/assets/images/posts/pixel-editors/symmetry-tool-example.gif' | prepend: site.url }}" loading="lazy" title="Symmetry Pen Example">
            <figcaption>
                Image borrowed from <a href="https://i.imgur.com/pj3ykyd.gif" target="_blank" rel="noopener noreferrer">https://i.imgur.com/pj3ykyd.gif</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Auto-Shade/Shading Mode</b>
        </summary>
        Auto-Shade tools allow you to darken or lighten an area of your art by simply drawing over it again.
        <figure>
            <img alt="Shading Example" src="{{ '/assets/images/posts/pixel-editors/shading_example.gif' | prepend: site.url }}" loading="lazy" title="Shading Example">
            <figcaption>
                Image borrowed from <a href="https://www.aseprite.org/docs/shading/" target="_blank" rel="noopener noreferrer">Aseprite.org</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>RotSprite Rotation</b>
        </summary>
        RotSprite allows you to rotate all, or part, of your artwork without losing any resolution. In the image below,
        the sprite on the left was rotated without RotSprite, but the sprite on the right was rotated with RotSprite.
        <figure>
            <img alt="RotSprite Example" src="{{ '/assets/images/posts/pixel-editors/rotsprite-example.png' | prepend: site.url }}" loading="lazy" title="RotSprite Example">
            <figcaption>
                Image borrowed from <a href="https://forum.yoyogames.com/index.php?threads/solved-image_angle-ruins-sprites.54514/#lg=_xfUid-2-1655259916&slide=0" target="_blank" rel="noopener noreferrer">https://i.imgur.com/vHOtruN.png</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Custom Brushes</b>
        </summary>
        Custom brushes allow you to recreate a look/feel of an area of art and use it as the pen itself.
        <figure>
            <img alt="Custom Brush Gif" src="{{ '/assets/images/posts/pixel-editors/custom-brush.gif' | prepend: site.url }}" loading="lazy" title="Custom Brush Gif">
            <figcaption>
                Image borrowed from <a href="https://www.aseprite.org/assets/images/custom-brush.gif" target="_blank" rel="noopener noreferrer">Aseprite.org</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Anti-Aliasing</b>
        </summary>
        Anti-Aliasing is useful for softening edges of your art and removing the bumpy look in places where the edges should be softer.
        <figure>
            <img alt="Anti-Aliasing Example" src="{{ '/assets/images/posts/pixel-editors/anti-alias-example.png' | prepend: site.url }}" loading="lazy" title="Anti-Aliasing Example">
            <figcaption>
                Image borrowed from <a href="https://medium.com/pixel-grimoire/how-to-start-making-pixel-art-4-ff4bfcd2d085" target="_blank" rel="noopener noreferrer">The Pixel Grimoire</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Tile Mode</b>
        </summary>
        Tiles are images that can be duplicated and placed throughout an artwork to create a pattern or texture.
        <figure>
            <img alt="Small Tile Tutorial" src="{{ '/assets/images/posts/pixel-editors/tile-tutorial.gif' | prepend: site.url }}" loading="lazy" title="Small Tile Tutorial">
            <figcaption>
                Image borrowed from <a href="https://blog.studiominiboss.com/pixelart" target="_blank" rel="noopener noreferrer">Studio Mini Boss</a>
            </figcaption>
        </figure>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>File Export</b>
        </summary>
        Most of these editors allow you to export in PNG, at least, but some allow you to export to a variety of other
        file types, including GIF, or even sprite sheets.
        <ul>
            <li>PNG</li>
            <li>Animated GIFs</li>
            <li>Sprite Sheets</li>
            <ul>
                <li>A <em>sprite sheet</em> is an image that consists of several smaller images. Combining the small
                images in one big image improves the game performance, reduces the memory usage, and speeds up the
                startup and loading time of the game.
                </li>
            </ul>
            <figure>
                <img alt="Sprite Sheet Example" src="{{ '/assets/images/posts/pixel-editors/sonic3_spritesheet_example.png' | prepend: site.url }}" loading="lazy" title="Sprite Sheet Example">
                <figcaption>
                    Image borrowed from <a href="https://demyanov.dev/javascript-canvas-sprite-animation" target="_blank" rel="noopener noreferrer">demyanov.dev</a>
                </figcaption>
            </figure>
        </ul>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Animation</b>
        </summary>
        Since I'm looking for an editor that I can use for game development assets, animation is a big thing for me. Because
        of this, we will look at several features related to animation.
        <ul>
            <li>Frames</li>
                <ul>
                    <li>
                    Frames are individual images, usually duplicates of a sprite with small changes that, when put together
                    in sequence, creates an animation.
                    </li>
                </ul>
            <li>Frame Tags</li>
                <ul>
                    <li>
                    Frame tags are just a little extra that helps to organize your frames. This one isn't as important
                    to me, but it is a nice bit of icing on the cake.
                    </li>
                </ul>
            <li>Onion Skin</li>
                <ul>
                    <li>
                    Onion skin is another great feature to have when creating sprite animations. I'd like to say it isn't
                    important, but I'd be lying, haha. Onion skins show the outline of frames, or frame, that are
                    adjacent to the frame you're currently editing. This allows you to see the placement of your sprite
                    before and/or after the image you're editing and helps to create more accurate animations. It is a
                    huge time saver.
                    </li>
                <figure>
                    <img alt="Onion Skin Example" src="{{ '/assets/images/posts/pixel-editors/screenshot_onion_skinning.jpg' | prepend: site.url }}" loading="lazy" title="Onion Skin Example">
                    <figcaption>
                        Image borrowed from <a href="https://www.cosmigo.com/" target="_blank" rel="noopener noreferrer">Cosmigo</a>
                    </figcaption>
                </figure>
                </ul>
            <li>Playback Modes</li>
                <ul>
                    <li>
                    Playback modes can encompass a few different things. Som can allow you to loop frame sections in
                    forward, reverse, and even ping-pong modes. Some just allow you to change preview speed.
                    </li>
                </ul>
        </ul>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Palette</b>
        </summary>
        Coming from a fine-art background, the palette is very important to me. Most of these tools have great features
        that allow you to adjust your palette.
        <ul>
            <li>Export/Import</li>
            <ul>
                <li>Some of these editors allow you to import from an existing image, which can be very useful if you want to keep to a certain style.</li>
                <li>Some of these tools have specific palette file formats, while others may let you import from palette
                file formats used by other programs, such as Photoshop's palette file format.Import from a specific palette file format.</li>
            </ul>
        </ul>
    </details>
    <details>
        <summary style="cursor: pointer">
            <b>Extensibility</b>
        </summary>
        In this context, extensibility refers to the ability to customize the editor to your needs. In this case, I
        don't just mean the ability to be able to change the tool's color theme; I mean the ability to extend the functions
        of the tool and add features, tools, or functions that either enhance the tool's current functionality or adds
        new capabilities to the tool. Now, this isn't a deal-breaker by any means, but it is a very-nice-to-have.
    </details>
</div>

<br>

## Tools

---

### [Aseprite](https://www.aseprite.org/){:target="_blank"}{:rel="noopener noreferrer"}

<figure style="margin-top: 20px;">
        <img alt="Aseprite Trial Screenshot" src="{{ '/assets/images/posts/pixel-editors/aseprite-trial-screenshot.png' | prepend: site.url }}" loading="lazy" title="Aseprite Trial Screenshot">
    <figcaption>
        Screenshot of a new sprite window in Aseprite.
    </figcaption>
</figure>

Aseprite seems to be the standard in pixel art circles. If you visit any pixel or game resource sites, or if you
just do a search for "pixels" in general, then you are likely to see Aseprite mentioned multiple times. Because of this,
I will cover this editor first, and I will be honest with you, after reviewing this editor, I've grown to like it quite
a bit. I will continue to review the others, but they will have to blow me away to make me choose them over Aseprite...

At first glance, when opening the editor, it isn't quite obvious why. The UI is a bit basic, very simple, and it doesn't
look very feature-rich. However, once you start digging into the program, playing with the tools and settings, then you
start to see that this editor actually has quite a lot to offer.

One thing that Aseprite does well that I was surprised, and disappointed, to find in regard to the other editors while
writing this post and doing my research, is that Aseprite is **very** well documented! Their website [Aseprite.org](https://www.aseprite.org/){:target="_
blank"}{:rel="noopener noreferrer"} does a great job listing its features and providing documentation. Also, if you're
new to pixel art, like I am, then you will also be happy to see that Aseprite has a thriving [community](https://community.aseprite.org/){:target="_blank"}{:
rel="noopener noreferrer"} with everything from [galleries](https://community.aseprite.org/c/artwork/8){:target="_blank"}{:rel="noopener noreferrer"}
and [guides](https://community.aseprite.org/c/guides/14){:target="_blank"}{:rel="noopener noreferrer"} to [help](https://community.aseprite.org/c/help/9){:
target="_blank"}{:rel="noopener noreferrer"} and [announcements](https://community.aseprite.org/c/announcements/10){:target="_blank"}{:rel="noopener noreferrer"}.
Getting started with Aseprite, or getting assistance, shouldn't be a hassle while utilizing this tool.

Aseprite's UI is unique to all the other editors on this list. You can see from the screenshot above that the UI has a
very pixelated design. While this is unique, and I personally like it, some professionals may be put off by this design
choice. True, it doesn't have the same modern polish as something like Photoshop, but it does give the editor a more beginner-friendly
feel while still offering all the professional features seen in the editors with a more modern UI. Besides, sometimes all
it takes to give something a modern feel is to simply update the theme, which Aseprite allows you to do by either creating your
own, or by downloading pre-made themes. Check out some of the most popular ones [here](https://github.com/aseprite/themes){:target="_blank"}{:rel="noopener
noreferrer"}.

#### Extras
Perhaps one of the best features about Aseprite is that it allows you to add extensions and custom scripts to help automate
some of the more tedious aspects of pixel art creation. Check out this [link](https://itch.io/tools/tag-aseprite){:target="_blank"}{:rel="noopener noreferrer"
} to find a plethora of extensions available for Aseprite. After a quick perusal of the link myself, I think my personal
favorite is the [Magic Pencil](https://thkaspar.itch.io/magic-pencil){:target="_blank"}{:rel="noopener noreferrer"}. Check
out this gif showing what the magic pencil can do:

<figure style="margin-top: 20px; width: 50%;">
        <img alt="Magic Pencil GIF" src="https://img.itch.zone/aW1hZ2UvMTU1NzE3Mi85MDg3MzIzLmdpZg==/347x500/JHRwSW.gif" loading="lazy" title="Magic Pencil GIF">
    <figcaption>
        Image provided by <a href="https://thkaspar.itch.io/magic-pencil" target="_blank" rel="noopener noreferrer">Magic Pencil</a>
    </figcaption>
</figure>

#### Where to Get It?
Until August 2016, Aseprite was completely [open source](https://opensource.org/osd){:target="_blank"}{:rel="noopener noreferrer"},
but now it is licensed under the [Aseprite EULA](https://github.com/aseprite/aseprite/blob/main/EULA.txt){:target="_blank"}{:rel="noopener noreferrer"}.
The TLDR of the EULA basically states that you can still clone the [source code](https://github.com/aseprite/aseprite){:target="_blank"}{:rel="noopener
noreferrer"}, modify it, and compile it for **FREE**, but you can't share or sell a compiled copy, or use its code in
your own project (unless it is code that existed before the introduction of the EULA).

##### Supported Platforms
- Windows
- macOS
- Ubuntu 32-bit and 64-bit .deb packages for Ubuntu 18.04 or greater. These packages can be uncompressed and executed in other Linux distributions, too (Fedora, etc.).
- Steam

##### Compile Your Own Copy
If you want Aseprite for **FREE**, as mentioned above, you can compile it yourself by following the instructions [here](https://github.com/aseprite/aseprite/blob/main/INSTALL.md){:
target="_blank"}{:rel="noopener noreferrer"}. ~~However, I will tell you from my own experience that it isn't easy. I spent
many days and a few sleepless nights trying to compile and run Aseprite for myself, but never had any success~~. I was able to
finally get it to compile, but I could never get it to open successfully, as it would crash and close immediately after opening.
There are a ton of tutorials and even some other blog posts and
[reddit posts](https://www.reddit.com/r/PixelArt/comments/i387m1/guide_how_to_build_aseprite_from_source_aseprite/){:target="_blank"}{:rel="noopener noreferrer"}
online that walk you through the process, ~~but even following those, I never got it to work~~. Now, I use my computer for
all sorts of development purposes, so it is possible that I have some conflicting packages, or something, but I don't
think it is worth the time to continue to troubleshoot for myself. Also, if you compile it yourself, and you ever want to
update the application, then you will have to repeat the process in order to update it. Now, if you have Windows, then you
may want to check out The Lite Crafter's [AsepriteTool](https://github.com/TheLiteCrafter/AsepriteTool){:target="_blank"}{:rel="noopener noreferrer"}
which supposedly builds Aseprite for you and will even update it for you, ~~but, again, I didn't have any luck with it~~.

So, when I started writing this post, I had been unsuccessful when I tried to compile Aseprite myself. However, I did figure
out my issue: I had MSys2 installed on my computer. Aseprite's `install.md` warns you about that, and I thought I had deleted
MSys from my system, but apparently an older install of Visual Studio that I had on my computer previously installed MSys
as part of some other feature I downloaded. So, I uninstalled the Visual Studio, and pretty much everything I've ever installed
for Visual Studio that I don't currently use in any projects and reran the Aseprite Tool, mentioned above, and it worked!

##### Download the Trial Version
Aseprite also offers a free official trial version that has all the full features of the editor unlocked, if you want to
give it a shot before paying for the full official version. Be aware, however, that any work you create using the trial
version **CANNOT** be saved. So, don't think that you can just live with the trial version forever :cry:. If you want to
give it a try, then you can download the trial [here](https://www.aseprite.org/trial/){:target="_blank"}{:rel="noopener noreferrer"}.

##### Buy an Official Copy
If you're really serious about Aseprite and really want your own copy, then you really should consider paying the $20 and
buying it directly from the developer. It's a one-time fee, and it includes all future upgrades. Plus, it supports the developer
and helps to keep the development and improvement of Aseprite ongoing. To see what you get when you buy the full version,
check their FAQ, [here](https://www.aseprite.org/faq/#what-do-i-get-when-i-buy-aseprite){:target="_blank"}{:rel="noopener noreferrer"}.
If you think Aseprite is the tool for you, and you're ready to pay for the full official version, then you can do so on their website
[here](https://www.aseprite.org/download/){:target="_blank"}{:rel="noopener noreferrer"}, [Steam](https://store.steampowered.com/app/431730/Aseprite/){:target="_blank"}{:rel="
noopener noreferrer"}, or [Itch.io](https://dacap.itch.io/aseprite){:target="_blank"}{:rel="noopener noreferrer"}.


### [GrafX2](http://grafx2.chez.com/){:target="_blank"}{:rel="noopener noreferrer"}

<figure style="margin-top: 20px;">
        <img alt="GrafX2 Screenshot" src="{{ '/assets/images/posts/pixel-editors/grafx2-screenshot.png' | prepend: site.url }}" loading="lazy" title="GrafX2 Screenshot">
    <figcaption>
        Image borrowed from <a href="http://grafx2.chez.com/index.php?static2/screenshots" target="_blank" rel="noopener noreferrer">grafx2.chez.com</a>
    </figcaption>
</figure>

GrafX2... Wow. Now *this* is an interesting program. Honestly, I almost didn't add it to the list. However, it has been
around for about twenty years and, when doing a search for pixel editors, this tool is listed quite a bit, so it must be
worth at least checking out, right?

Now, if you're a coder/programmer, then you've probably heard of Vi, Vim, and/or Emacs. To me, GrafX2 is the pixel
editors' equivalent those code editors. I say that, because, like the aforementioned code editors, GrafXx2 has a very minimal
UI and its design is very reminiscent of MSDOS, which makes sense, because it is actually an upgraded [port](http://grafx2.chez.com/index.php?article6/differences-with-the-dos-version){:target="_
blank"}{:rel="noopener noreferrer"}!

Unfortunately, for a program that has been around so long, finding information about its documentation and/or features is
a very hard task. Because of this, you may notice several <i class="fa fa-question"></i> icons in the comparison table under
GrafX2's name. However, the documentation that I did find does mention that you can press <kbd>F1</kbd> when selecting any
of GrafX2's tools and a help message will display with more info about the tool.

I played around in GrafX2 for a bit, but ultimately, I don't think this is the program for me. If you like a minimal UI,
tons of customizable keyboard shortcuts, and a no-fuss interface, then this may be the program for you. I definitely recommend
downloading it and playing with it, regardless. May review of this tool may seem negative, but I actually have a ton of
respect for this program and, if I had the time to spend on learning it through a ton of trial and error, then I would
certainly keep it in my toolbox, but as it stands, I think I will be going for a more modern pixel editor.

#### Where to Get It?

If you would like to try out GrafX2 for yourself, then you can download it for **FREE** from their website, [here](http://grafx2.chez.com/index.php?static3/downloads){:
target="_blank"}{:rel="noopener noreferrer"}

##### Supported Platforms
The main platforms supported for GrafX2 are:
- Windows
- Haiku
- Linux
- Atari: 2.8, Nightly builds
- GP2x
- Nintendo Switch

Other platforms supported, and usually provided by third-parties, can be found on their website, [here](http://grafx2.chez.com/index.php?static3/downloads){:target="_blank"
}{:rel="noopener noreferrer"}.

### [PixiEditor](https://pixieditor.net/){:target="_blank"}{:rel="noopener noreferrer"}

<figure style="margin-top: 20px;">
        <img alt="Pixi Editor Screenshot" src="{{ '/assets/images/posts/pixel-editors/pixi-editor-screenshot.png' | prepend: site.url }}" loading="lazy" title="Pixi Editor Screenshot">
    <figcaption>
        Image provided by <a href="https://pixieditor.net/" target="_blank" rel="noopener noreferrer">pixieditor.net.</a>
    </figcaption>
</figure>

### LibreSprite

<figure style="margin-top: 20px;">
        <img alt="LibreSprite Screenshot" src="{{ '/assets/images/posts/pixel-editors/libresprite-screenshot.png' | prepend: site.url }}" loading="lazy" title="LibreSprite Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in LibreSprite.
    </figcaption>
</figure>

  - Free to compile or download
  - Forked from Aseprite's last open source release

### LibreSprite Dotto

<figure style="margin-top: 20px;">
        <img alt="LibreSprite Dotto Screenshot" src="{{ '/assets/images/posts/pixel-editors/dotto-screenshot.png' | prepend: site.url }}" loading="lazy" title="LibreSprite Dotto Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in LibreSprite Dotto.
    </figcaption>
</figure>

  - Free to compile or download
  - A rewrite of the original LibreSprite that contains more features

### JPixel

<figure style="margin-top: 20px;">
        <img alt="JPixel Screenshot" src="{{ '/assets/images/posts/pixel-editors/jpixel-screenshot.png' | prepend: site.url }}" loading="lazy" title="JPixel Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in JPixel.
    </figcaption>
</figure>

  - Free

### Pixelorama

<figure style="margin-top: 20px;">
        <img alt="Pixelorama Screenshot" src="{{ '/assets/images/posts/pixel-editors/pixelorama-screenshot.png' | prepend: site.url }}" loading="lazy" title="Pixelorama Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in Pixelorama.
    </figcaption>
</figure>

  - Free
  - Online and Desktop

### Pixel Studio

<figure style="margin-top: 20px;">
        <img alt="Pixel Studio Screenshot" src="{{ '/assets/images/posts/pixel-editors/pixel-studio-screenshot.png' | prepend: site.url }}" loading="lazy" title="Pixel Studio Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in Pixel Studio.
    </figcaption>
</figure>

  - Free
  - Online, Desktop, and Mobile
  - Tablet Support

### Graphics Gale

<figure style="margin-top: 20px;">
        <img alt="Graphics Gale Screenshot" src="{{ '/assets/images/posts/pixel-editors/graphics-gale-screenshot.png' | prepend: site.url }}" loading="lazy" title="Graphics Gale Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in Graphics Gale.
    </figcaption>
</figure>

  - Free

### Piskel

<figure style="margin-top: 20px;">
        <img alt="Piskel Screenshot" src="{{ '/assets/images/posts/pixel-editors/piskel-screenshot.png' | prepend: site.url }}" loading="lazy" title="Piskel Screenshot">
    <figcaption>
        A screenshot of a project inside Piskel.
    </figcaption>
</figure>

  - Free
  - Online

### LoSpec Pixel Editor

<figure style="margin-top: 20px;">
        <img alt="LoSpec Editor Screenshot" src="{{ '/assets/images/posts/pixel-editors/lospec-editor-screenshot.png' | prepend: site.url }}" loading="lazy" title="LoSpec Editor Screenshot">
    <figcaption>
        A screenshot of a project inside the LoSpec editor. This beautiful artwork has been provided by my 4-year-old. :heart_eyes:
    </figcaption>
</figure>

  - Free
  - Online

### PixilArt

<figure style="margin-top: 20px;">
        <img alt="Pixil Art Screenshot" src="{{ '/assets/images/posts/pixel-editors/pixil-art-screenshot.png' | prepend: site.url }}" loading="lazy" title="Pixil Art Screenshot">
    <figcaption>
        A screenshot of a new window and canvas in Pixil Art.
    </figcaption>
</figure>

  - Free

[//]: # (### Pyxel Edit)
[//]: # (  - Paid)

### Pro Motion

<figure style="margin-top: 20px;">
        <img alt="Promotion Screenshot" src="{{ '/assets/images/posts/pixel-editors/promotion-screenshot.jpg' | prepend: site.url }}" loading="lazy" title="Promotion Screenshot">
    <figcaption>
        Image provided by <a href="https://www.cosmigo.com/" target="_blank" rel="noopener noreferrer">Cosmigo</a>
    </figcaption>
</figure>

  - Paid

## Other Resources

---

### Pixel Art Tutorials
- [Les Forges Pixel Art Course](https://opengameart.org/content/les-forges-pixel-art-course){:target="_blank"}{:rel="noopener noreferrer"}
- [Studio Mini Boss' Blog - Pixel Art Tutorials](https://blog.studiominiboss.com/pixelart){:target="_blank"}{:rel="noopener noreferrer"}
- [Pedro Medeiros' Pixel Grimoire](https://medium.com/pixel-grimoire/intro/home){:target="_blank"}{:rel="noopener noreferrer"}

### Free Game Resources
- [OpenGameArt.org](https://opengameart.org/){:target="_blank"}{:rel="noopener noreferrer"}
- [Itch.io](){:target="_blank"}{:rel="noopener noreferrer"}
- [Lospec](https://lospec.com/){:target="_blank"}{:rel="noopener noreferrer"}
  - Pixel Art Tutorials
  - Palettes
  - Other Resources
  - Jobs Board
