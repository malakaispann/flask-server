# Flask Server

Made to showcase simple Flask application and also help run tests for Strata's HTTP get and Post Runners.

## Requirements

    - Docker
    - Docker Compose
    - Git

## Quickstart

1. Clone the repo: `git clone git@github.com:malakaispann/flask-server.git`
2. Change to the repo's directory: `cd flask-server`
3. Start server and run tests : `docker compose up --detach`
    - Server accessible via "http://localhost:5001"
    - Uses default network 'flask-server_default'
4. Check test logs: `docker logs flask-server-test-1`

-   Should look like this

```bash
============================= test session starts ==============================
  platform linux -- Python 3.12.11, pytest-8.4.0, pluggy-1.6.0
  rootdir: /apps/server
  collected 2 items

  test_app.py ..                                                           [100%]

  ============================== 2 passed in 0.08s ===============================
```

## Endpoints:

    - "/get_json" (or default "/") : GET only.
        - Returns: {"data": "Hello World"}
    - "/post_json" : POST only.
        - Returns: {"data": "Hello World", "input": <whatever was passed in your post request>}

See [test cases](./server/test_app.py) for some examples.

## Shutdown

Run `docker compose down --volumes --remove-orphans`
