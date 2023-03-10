|pipeline status| |coverage report| |pypi| |conda| |version|

=====
Bilby
=====

A user-friendly Bayesian inference library.
Fulfilling all your Bayesian dreams.

Online material to help you get started:

-  `Installation instructions <https://lscsoft.docs.ligo.org/bilby/installation.html>`__
-  `Documentation <https://lscsoft.docs.ligo.org/bilby/index.html>`__

If you need help, find an issue, or just have a question/suggestion you can

- Join our `Slack workspace <https://bilby-code.slack.com/>`__ (you may need to email the support desk to request an invite)
- Email our support desk: contact+lscsoft-bilby-1846-issue-@support.ligo.org
- Ask questions (or search through other users questions and answers) on `StackOverflow <https://stackoverflow.com/questions/tagged/bilby>`__ using the bilby tag
- For www.git.ligo.org users, submit issues directly through `the issue tracker <https://git.ligo.org/lscsoft/bilby/issues>`__
- For www.chat.ligo.org users, join the `#bilby-help <https://chat.ligo.org/ligo/channels/bilby-help>`__ or `#bilby-devel <https://chat.ligo.org/ligo/channels/bilby-devel>`__ channels

We encourage you to contribute to the development of bilby. This is done via a merge request.  For
help in creating a merge request, see `this page
<https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html>`__ or contact
us directly. For advice on contributing, see `the contributing guide <https://git.ligo.org/lscsoft/bilby/blob/master/CONTRIBUTING.md>`__.


--------------
Citation guide
--------------

If you use :code:`bilby` in a scientific publication, please cite

* `Bilby: A user-friendly Bayesian inference library for gravitational-wave
  astronomy
  <https://ui.adsabs.harvard.edu/#abs/2018arXiv181102042A/abstract>`__
* `Bayesian inference for compact binary coalescences with BILBY: validation and application to the first LIGO-Virgo gravitational-wave transient catalogue <https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.3295R/abstract>`__

The first of these papers introduces the software, while the second introduces advances in the sampling approaches and validation of the software.
If you use the :code:`bilby_mcmc` sampler, please additionally cite

* `BILBY-MCMC: an MCMC sampler for gravitational-wave inference <https://ui.adsabs.harvard.edu/abs/2021MNRAS.507.2037A/abstract>`__

Additionally, :code:`bilby` builds on a number of open-source packages. If you
make use of this functionality in your publications, we recommend you cite them
as requested in their associated documentation.

**Samplers**

* `dynesty <https://github.com/joshspeagle/dynesty>`__
* `nestle <https://github.com/kbarbary/nestle>`__
* `pymultinest <https://github.com/JohannesBuchner/PyMultiNest>`__
* `cpnest <https://github.com/johnveitch/cpnest>`__
* `emcee <https://github.com/dfm/emcee>`__
* `nessai <https://github.com/mj-will/nessai>`_
* `ptemcee <https://github.com/willvousden/ptemcee>`__
* `ptmcmcsampler <https://github.com/jellis18/PTMCMCSampler>`__
* `pypolychord <https://github.com/PolyChord/PolyChordLite>`__
* `PyMC3 <https://github.com/pymc-devs/pymc3>`_


**Gravitational-wave tools**

* `gwpy <https://github.com/gwpy/gwpy>`__
* `lalsuite <https://git.ligo.org/lscsoft/lalsuite>`__
* `astropy <https://github.com/astropy/astropy>`__

**Plotting**

* `corner <https://github.com/dfm/corner.py>`__ for generating corner plot
* `matplotlib <https://github.com/matplotlib/matplotlib>`__ for general plotting routines


.. |pipeline status| image:: https://git.ligo.org/lscsoft/bilby/badges/master/pipeline.svg
   :target: https://git.ligo.org/lscsoft/bilby/commits/master
.. |coverage report| image:: https://git.ligo.org/lscsoft/bilby/badges/master/coverage.svg
   :target: https://lscsoft.docs.ligo.org/bilby/htmlcov/
.. |pypi| image:: https://badge.fury.io/py/bilby.svg
   :target: https://pypi.org/project/bilby/
.. |conda| image:: https://img.shields.io/conda/vn/conda-forge/bilby.svg
   :target: https://anaconda.org/conda-forge/bilby
.. |version| image:: https://img.shields.io/pypi/pyversions/bilby.svg
   :target: https://pypi.org/project/bilby/
