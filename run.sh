gunicorn --reload --access-logformat "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(M)s" --access-logfile '-' app:app

