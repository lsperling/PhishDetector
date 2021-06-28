# Phish Detector

This application implements black-list algorithm for detecting phishing URLs.

The application provides an API to the PhishTank database for an updated phishing sites detection.


## How to use the blacklist phish detector?

* Run from command line:

```
cd path/to/repo
pip install -r requirements.txt
python test_phish_detector.py --url="<URL to check>"
```

* In case no '--url' argument is given, will show few examples.