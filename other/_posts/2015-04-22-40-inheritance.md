---
layout: post
categories: lectures
title: Inheritance
---

# Inheritance

Inheritance allows us to define common behaviors in a base class that
derived classes inherit. The derived class may add new methods, but it
gets all of the base class methods for free.

Polymorphism allows us to attach many method definitions to a single
name. In the example below, `speak` is a polymorphic method defined in
the base class. The derived class overrides the base class behavior with
a custom implementation.

Late binding refers to the runtime process of determining which version
of the `speak` method is invoked. The data type of receiver of the
`speak` method determines which method is executed.

This extra lookup step causes late-bound methods to perform more
slowly than early-bound methods.

<script src="https://gist.github.com/dgraham/45e3e761bce426729073.js"></script>
