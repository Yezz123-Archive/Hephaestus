<p align="center">
    <img src=".github/school-of-athens.jpg" alt="School of Athena">
</p>

# Hephaestus :rocket:

- In Greek mythology, Hephaestus was either the son of Zeus and Hera or he was Hera's parthenogenous child. ... As a smithing god, Hephaestus made all the weapons of the gods in Olympus. He served as the blacksmith of the gods, and was worshipped in the manufacturing and industrial centres of Greece, particularly Athens.

## Get Started :rocket:

- An Restful Api project developed with Flask.

- I used [Prometheus](https://prometheus.io/) and [Grafana](https://grafana.com/) for monitoring and containerization with Docker.

### Monitoring

- Using [Prometheus Flask exporter](https://pypi.org/project/prometheus-flask-exporter/) This library provides HTTP request metrics to export into Prometheus. It can also track method invocations using convenient functions.

- Grafana is a multi-platform open source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources.

### containerization

- Docker hosts and containers monitoring with Prometheus, Grafana, Flask, MySQL.

- To run the project you need docker-compose and run this command:

```bash
docker-compose up -d
```

- To stop:

```bash
docker-compose down
```

## Requirements :rocket:

- To start using Hephaestus try first to understand how Grafana & Prometheus work by reading some official docs here :

- [Prometheus: Introduction](https://prometheus.io/docs/introduction/overview/)

- [Get started or start exploring Grafana](https://grafana.com/docs/)

- [Visualize almost anything with Grafana and Python](http://oz123.github.io/writings/2019-06-16-Visualize-almost-anything-with-Grafana-and-Python/index.html)

### Installation

- Get started by cloning the repository :

```bash
git clone https://github.com/yezz123/Hephaestus
```

- Create & activate a python3 [virtual environment](https://docs.python.org/3/tutorial/venv.html) (optional, but very recommended).

- Install [requirements](requirements.txt):

```bash
pip install -r requirements.txt
```

- Then in your [app/**init**.py](app/__init__.py) change the MYSQL connection :

```py
db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@db/Database_db"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### Routes

- **"/"** : show information's about what routes are available.

- **"/fibonacci/<int>"** : the n-th fibonacci number.

- **"/power/<float>/<float>"** : show power of first number to second number

- **"/factorial/<int>"** : show the factorial of a number

- **"/get_requests"** : show all requests saved in DB

- **"/metric"** : show metrics
