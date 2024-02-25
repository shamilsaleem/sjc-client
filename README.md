
# SJC-CLIENT

An unofficial open-source attendance client for the students of St. Joseph's College, Devagiri which can be used only for checking attendance.

- This program uses [beautifulsoup](https://pypi.org/project/beautifulsoup4/) Python module to fetch data from official [website](https://devagiricollege.net/sjc/Home/student).
- Login credentials are stored within the browser as cookies.
- Back-end is written in Python using [Flask](https://flask.palletsprojects.com/) framework.

Usage:-
```bash
git clone https://github.com/shamilsaleem/sjc-client.git
cd sjc-client
pip install -r requirements.txt
gunicorn app:app
```
Made with ❤️ by [shamilsaleem](https://www.instagram.com/shamil.saleem)
