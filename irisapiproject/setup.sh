#uvicorn fast:app –reload
gunicorn -w 4 -k uvicorn.workers.UvicornWorker fast:app
