Balance Sheet
#############

Articles and pages
==================

Pelican considers "articles" to be chronological content, such as posts on a
blog, and thus associated with a date.

The idea behind "pages" is that they are usually not temporal in nature and are
used for content that does not change very often (e.g., "About" or "Contact"
pages).

You can find sample content in the repository at ``samples/content/``.

.. _internal_metadata:

File metadata
=============

Pelican tries to be smart enough to get the information it needs from the
file system (for instance, about the category of your articles), but some
information you need to provide in the form of metadata inside your files.

If you are writing your content in reStructuredText format, you can provide
this metadata in text files via the following syntax (give your file the
``.rst`` extension)::

    My super title
    ##############

    :date: 2010-10-03 10:20
    :modified: 2010-10-04 18:40
    :tags: thats, awesome
    :category: yeah
    :slug: my-super-post
    :authors: Alexis Metaireau, Conan Doyle
    :summary: Short version for index and feeds

Author and tag lists may be semicolon-separated instead, which allows
you to write authors and tags containing commas::

    :tags: pelican, publishing tool; pelican, bird
    :authors: Metaireau, Alexis; Doyle, Conan

Pelican implements an extension to reStructuredText to enable support for the
``abbr`` HTML tag. To use it, write something like this in your post::

    This will be turned into :abbr:`HTML (HyperText Markup Language)`.

You can also use Markdown syntax (with a file ending in ``.md``, ``.markdown``,
``.mkd``, or ``.mdown``). Markdown generation requires that you first
explicitly install the Python-Markdown_ package, which can be done via ``pip
install Markdown``.

Pelican also supports `Markdown Extensions`_, which might have to be installed
separately if they are not included in the default ``Markdown`` package and can
be configured and loaded via the ``MARKDOWN`` setting.

Metadata syntax for Markdown posts should follow this pattern::

    Title: My super title
    Date: 2010-12-03 10:20
    Modified: 2010-12-05 19:30
    Category: Python
    Tags: pelican, publishing
    Slug: my-super-post
    Authors: Alexis Metaireau, Conan Doyle
    Summary: Short version for index and feeds

    This is the content of my super blog post.

You can also have your own metadata keys (so long as they don't conflict with
reserved metadata keywords) for use in your templates. The following table
contains a list of reserved metadata keywords:

=============== ===============================================================
    Metadata                              Description
=============== ===============================================================
``title``       Title of the article or page
``date``        Publication date (e.g., ``YYYY-MM-DD HH:SS``)
``modified``    Modification date (e.g., ``YYYY-MM-DD HH:SS``)
``tags``        Content tags, separated by commas
``keywords``    Content keywords, separated by commas (HTML content only)
``category``    Content category (one only — not multiple)
``slug``        Identifier used in URLs and translations
``author``      Content author, when there is only one
``authors``     Content authors, when there are multiple
``summary``     Brief description of content for index pages
``lang``        Content language ID (``en``, ``fr``, etc.)
``translation`` If content is a translation of another (``true`` or ``false``)
``status``      Content status: ``draft``, ``hidden``, or ``published``
``template``    Name of template to use to generate content (without extension)
``save_as``     Save content to this relative file path
``url``         URL to use for this article/page
=============== ===============================================================

