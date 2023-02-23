Configuration Files
-------------------

MANIFEST.in
~~~~~~~~~~~

The ``MANIFEST.in`` file configures which files in the repository/folder are grabbed or
ignored when assembling the distributed package. Originally this was at the discretion
of the user to keep up-to-date, but recently tooling has evolved, to auto-generate most
things which would have been listed here.  The default setting is to ship everything
that is committed to the git repository except for what is excluded or prune explicitly
in ``MANIFEST.in``. 

All configuration files, tests, and other Python related or IDE related files are
excluded. There is a debate on whether tests should be deployed along with the library
source. Should they? Tox and the CI integration guarantees tests are run on
*installed* versions of the software. So, I am the kind of person that
considers there is no need to deploy tests alongside with the source. Users aren't going
to run tests. Developers will.

It is actually easy to work with MANIFEST.in file. Feel free to add or remove
files as your project needs.

tox.ini
~~~~~~~

Tox configuration file might be the trickiest one to learn and operate with
until you are familiar with tox's workflows. `Read all about tox in their
documentation pages <https://tox.readthedocs.io/en/latest/>`_. The ``tox.ini``
file contains several comments explaining the implementations I adopted.
