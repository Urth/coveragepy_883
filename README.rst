Coverage #883
-------------

.. code-block:: shell

   mkvirtualenv --python=/usr/bin/python3 coverage_883
   pip install tox
   tox  # Succeeds
   tox -- --cov-append  # Fails
