Alexa MBTA Skill
----------------

This skill uses the `MBTA-realtime API <http://realtime.mbta.com/Portal/Home/Documents>`_ to get nearby transit times.
The project is based on `Flask-Ask <https://github.com/johnwheeler/flask-ask/>`_, and is deployed to AWS S3 and Lambda
via `Zappa <https://github.com/Miserlou/Zappa>`_.

This project is a proof-of-concept. I have no plans to release this skill publicly. If you would like to get it
production-ready, go for it. Message me for assistance, if necessary.

Current Capabilities
====================

- Get bus arrival/departure time for nearby stop
- Get subway arrival/departure times for nearby stop

Future Improvements
===================

- Add an OAuth 2.0 server to store user/device location...unless Amazon starts providing this information.
- Allow user to specify departure station. The current mechanism of determining the closest station is naïve, and
  does not account for the fact that some stations are closer when walking.
- Add support for Green Line
