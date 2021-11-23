# Lacework Jupyter Helper

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lacework/python-sdk/blob/master/jupyter/notebooks/colab_sample.ipynb)

**laceworkjupyter** is a community developed Python library for interacting with the Lacework APIs in a
Jupyter notebook environment.

The purpose of this library is to simplify using the Lacework SDK in a Jupyter notebook environment. This allows
users to more easily work with the output of all API calls to the SDK in a notebook environment.

To get a data frame with the events within a time range one can simply write this code:

```
import laceworkjupyter

with laceworkjupyter.LaceworkHelper() as lw:
    client = lw.get_client()
    df = client.events.get_for_date_range('2021-08-25T00:00:00', '2021-08-27T23:59:23')
```

And to get events from the last 5 days:

```
import laceworkjupyter

with laceworkjupyter.LaceworkHelper() as lw:
    client = lw.get_client()
    start_time, end_time = lw.parse_date_offset('LAST 5 DAYS')

    df = client.events.get_for_date_range(start_time=start_time, end_time=end_time)
```

## Requirements

- Python 3.6 or higher
- Lacework API Credentials
  - Account Name
  - API Key
  - API Secret
- Lacework Python SDK
- Pandas version 1.0.1 or higher

## Lacebook - Docker Container

One way to start using the Lacework Jupyter helper is to make use of the docker notebook container called
`lacebook`. The easiest way to run the container is to fetch the docker-compose file:

```shell
$ curl -O https://raw.githubusercontent.com/lacework/python-sdk/master/jupyter/docker/docker-compose.yml
$ docker-compose pull
$ docker-compose up -d
```

The other option is to create a file called `docker-compose.yml` with the content of:

```
version: '3'
services:
  lacebook:
    container_name: lacebook
    image: docker.io/lacework/lacebook:latest
    ports:
      - 127.0.0.1:8899:8899
    restart: on-failure
    volumes:
      - $HOME/.lacework.toml:/home/lacework/.lacework.toml
      - /$HOME/data/:/usr/local/src/lacedata/
```

(*if you use this docker compose file you will either need to create the folder $HOME/data that is
readable and writeable by a user with the UID/GID 1000:1000. or change the line to point to a folder
with that permission*)

This will start up a lacebook container which starts a Jupyter container listening on port 8899.
To access the lacebook container visit http://localhost:8899. When prompted for a password
use `lacework`.

### Customize Container

By default persistent storage for notebooks is in the user's /tmp directory. To change that,
edit the file `docker-compose.yml' and change the line:

```
      - /tmp/:/usr/local/src/lacedata/
```

To a directory that persists through reboots. This can be any folder on your host system,
the only limitations are that the folder needs to be readable and writeable by a user 
with UID/GID 1000:1000 for the container user to be able to make use of it.

### Use Lacebook with Colab

The lacebook container can also be used with Colab notebooks. Select `Connect to a local runtime`
and enter the backend URL: `http://localhost:8899/?token=lacework`

## How-To

More to come here.

One way to start exploring is to run this [Colab notebook](https://colab.research.google.com/github/lacework/python-sdk/blob/master/jupyter/notebooks/colab_sample.ipynb)