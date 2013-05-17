# Vanilla Flask

A simple boilerplate [Flask](http://flask.pocoo.org) set up for me to use when making websites.

It loads in several useful libraries and preprocessors using [webassets](https://github.com/miracle2k/webassets), and sets up database guff ([Mongo](http://mongodb.org), right now) that I don't want to write every time.

So get cloning, guys!

## Preprocessors

+ [Scss](http://sass-lang.com)
+ [Coffeescript](http://jashkenas.github.com/coffee-script/)

## Libraries:

+ [jQuery](http://jquery.com)
+ [Bourbon](http://bourbon.io) and [Neat](http://neat.bourbon.io)

In the src/templates directory, you can create `.handlebars` files, that will be compiled and placed in the global `Handlebars.templates` object, indexed by filename.