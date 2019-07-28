# hand-or-foot

This project contains a proof of concept web application that takes a FastAI machine learning model and deploys it as a web-application.

All commits to this project are automatically built and deployed on Heroku at http://hand-or-foot.herokuapp.com/

This project owes its inspiration mostly from:
* https://github.com/simonw/cougar-or-not (deployed on ZeitNow as a docker image)
* https://medium.com/@lankinen/fastai-model-to-production-this-is-how-you-make-web-app-that-use-your-model-57d8999450cf (deployed on AWS)

The main difference here is that this project is set up for (and tested with) deployment to Heroku (PaaS).

This code is a building block, a program that tells the difference between an image of a hand and an image of a foot isn't especially useful. But all the basics are present here, so that once I have an ML model that is actually useful, it will be easy to deploy.
