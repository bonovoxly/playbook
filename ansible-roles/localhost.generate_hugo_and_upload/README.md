localhost.generate_hugo_and_upload
=========

Generates a Hugo static web page and uploads it to AWS S3 as a static inventory web page.

Requirements
------------

Requires `lunr-hugo` for search, but will fail gracefully (I think).


Role Variables
--------------

TBD

Dependencies
------------

Requires the role `instance.get_inventory` to fetc the Hugo Markdown files.
