# Vanilla Flask

A simple boilerplate flask set up for me to use when making websites.

It loads in several useful libraries and preprocessors using webassets, and sets up database guff (mongo, right now) that I don't want to write every time.

So get cloning, guys!

## Preprocessors

+ Scss
+ Coffeescript

## Libraries:

+ jQuery
+ Bourbon and Neat

In the src/templates directory, you can create `.handlebars` files, that will be compiled and placed in the global `Handlebars.templates` object, indexed by filename.