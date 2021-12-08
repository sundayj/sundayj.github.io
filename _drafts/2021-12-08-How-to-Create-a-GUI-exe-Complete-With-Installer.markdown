---
layout: post
title: How to Create an Easily Distributable GUI Executable Complete With a Setup Installer Using Python
categories: Tutorials
tags: [tools, software, tutorial, Python, code-generators, Gooey, PyInstaller, Inno-Setup, PySimpleGUI]
comments: true
summary: This tutorial will teach you how to create a Python GUI app that can be installed via a setup installer.
---

## Required Tools

| Package/App | Site                                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gooey       | [GitHub - chriskiehl/Gooey: Turn (almost) any Python command line program into a full GUI application with one line](https://github.com/chriskiehl/Gooey#gooey) |
| PyInstaller | [PyInstaller Manual — PyInstaller 4.0 documentation](https://pyinstaller.readthedocs.io/en/stable/index.html)                                                   |
| Inno Setup  | [Inno Setup](https://jrsoftware.org/isinfo.php)                                                                                                                 |
| PySimpleGUI | [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/)                                                                                                    |

## Gooey
* Functions and APIs to create lists for the dropdown options
* Persisting user choices within the User's AppData folder


## PyInstaller
* Including files
* Writing script to run PyInstaller with preset options
    * IE. --onedir/--onefile, --windowed, etc.
* Editing and using spec files
    * Adding options that don't display inconsequential errors

## PySimpleGUI
* PySimpleGUI to create another window if additional choices or actions are required

## Inno Setup
* 
