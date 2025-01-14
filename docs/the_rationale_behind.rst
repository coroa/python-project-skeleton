The rationale behind the project
================================

In the following sections I explain the rationale I used to configure this
template repository. Also, these are the same strategies I adopt in my current
projects. In summary, the following sections represent my view on software
development practices, either it is open or closed source, done in teams or by
single individuals. Yes, I also follow these *rules* when I am the sole
developer.

Branch organization
-------------------

This repository complies with the ideas of agile development. Why? Because I
found the agile strategy to fit best the kind of projects I develop. Is this
the best strategy for your project? Well, you have to evaluate that.

In the "python-project-skeleton" layout, there is only one production branch,
the `main` branch, representing the latest state of the software. This layout
contrasts with the opposite strategy where the `stable` and the `latest`
branches are kept separate. For the kind of projects I develop, keeping the
`stable` and the `latest` separated offers no benefit. Honestly, I believe
such separation defeats the purpose of agile development with Semantic
Versioning 2, which is the versioning scheme I adopted here, and in most of my
projects.

Versioning
----------

The versioning scheme adopted here is the `Semantic Versioning 2`_.

The development process
-----------------------

Code additions SHOULD come in the form of pull requests from forked
repositories. Any merged pull request SHOULD include a manual description in
`CHANGELOG.rst`. Versions are created manually by revising CHANGELOG.rst, and
creating a version tag on the ``main`` branch with the correct semantic
version increment. Deployment of the new version to PyPI is automated.

The release proceedure is described in more depth in :ref:`version release <Version
release>`.

.. _Semantic Versioning 2: https://semver.org/#semantic-versioning-200
