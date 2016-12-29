Alexa Transit Skill
-------------------

This skill uses the `MBTA-realtime API <http://realtime.mbta.com/Portal/Home/Documents>`_ to get nearby transit times.
The project is based on `Flask-Ask <https://github.com/johnwheeler/flask-ask/>`_, and is deployed to AWS S3 and Lambda
via `Zappa <https://github.com/Miserlou/Zappa>`_.

Current Capabilities
====================

- Get bus arrival/departure time for nearby stop

TODO: Future Development
========================

- Add an OAuth 2.0 server to store user/device location
- Add support for rail/subway times
