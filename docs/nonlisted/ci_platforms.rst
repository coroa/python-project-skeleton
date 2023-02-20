Continuous Integration
----------------------

Here, I overview the implementation strategies for the different continuous
integration and quality report platforms. In the previous versions of this
skeleton template, I used `Travis-CI`_ and `AppVeyor-CI`_ to run the testing
workflows. In the current version, I have migrated all these operations to GitHub
Actions.

**Does this mean you should not use Travis or AppVeyor?** *Of course not.*
Simply, the needs of my projects and the time I have available to dedicate to
CI configuration do not require a dedicated segregation of strategies into
multiple servers and services and I can perfectly accommodate my needs in
GitHub actions.

**Are GitHub actions better than Travis or AppVeyor?** I am not qualified to
answer that question.

When using this repository, keep in mind that you don't need to use all
services adopted here. You can drop or add any other at your will by removing
the files or lines related to them or adding new ones following the patterns
presented here.

The following list summarizes the platforms adopted:

#. Building and testing
    * GitHub actions
#. Test Coverage
    * Codecov
#. Documentation
    * Read the Docs

I acknowledge the existence of many other platforms for the same purposes of
those listed. I chose these because they fit the size and scope of my projects
and are also the most used within my field of work.

Configuring GitHub Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~

You may wish to read about `GitHub actions
<https://github.com/features/actions>`_. Here, I have one Action workflow per
environment defined in ``tox``. Each of these workflows runs on each of the
python supported versions and OSes. These tests regard unit tests,
documentation build, lint, integrity checks, and, finally, package deploying on
PyPI.

The CI workflows trigger every time a new pull request is created and at each
commit to that PR or on other branches. The PyPI deploy workflow is only run
for tagged commits on the ``main`` branch.

In this repository you can find two PRs demonstrating: one where `tests pass
<https://github.com/joaomcteixeira/python-project-skeleton/pull/10>`_ and
another where `tests fail
<https://github.com/joaomcteixeira/python-project-skeleton/pull/11>`_.

Version release
```````````````

Version releases are initiated by creating version tags on the main branch. A commit can
be tagged manually with ``git tag -a v0.1.2`` and pushing it to the ``main`` branch or
by using `Github's UI
<https://github.com/joaomcteixeira/python-project-skeleton/releases/new>`_ for drafting
and publishing annotated release tags.

The PyPI deploy workflow will then create source and binary wheel package and deploy it
to PyPI or TestPyPI, if the `API token has been set-up
<https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/>`_
for the repository.


Code coverage
~~~~~~~~~~~~~

``Codecov`` is used very frequently to report test coverage rates. Activate
your repository under ``https://about.codecov.io/``, and follow their
instructions.

`Coverage`_ reports are sent to Codecov servers when the ``test.yml`` workflow
takes place. This happens for each PR and each merge commit to ``maint``.

The `.coveragerc`_ file, mirrored below, configures ``Coverage`` reports.

.. literalinclude:: ../.coveragerc

The :code:`.coveragerc` can be expanded to further restraint coverage analysis,
for example adding these lines to the :code:`exclude` tag:

::

    [report]
    exclude_lines =
    if self.debug:
    pragma: no cover
    raise NotImplementedError
    if __name__ == .__main__.:

Remember that if you don't want to use these services, you can simply remove
the respective files from your project.


.. _Travis-CI: https://travis-ci.org
.. _.travis.yml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.travis.yml
.. _tox: https://tox.readthedocs.io/en/latest/
.. _Appveyor-CI: https://www.appveyor.com/
.. _tox.ini: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/tox.ini
.. _.appveyor.yml: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.appveyor.yml
.. _coverage: https://pypi.org/project/coverage/
.. _.coveragerc: https://github.com/joaomcteixeira/python-project-skeleton/blob/latest/.coveragerc
