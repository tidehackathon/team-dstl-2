# team-dstl-2
# TIDE HACKATHON 2023, Warsaw, Poland
# Analytics Dashboard for Interoperability Challenge

# Tidepedia Page
The architecture document can be found on the team tidepedia page.

https://tide.act.nato.int/mediawiki/tidepedia/index.php/Team_1118

# Introduction
The architecture consists of two main components:

1. Simple Editable Query EXecutor (SEQX): A Flask app which allows a stakeholder to
create pertinent queries relating to interoperability.  Send HTTP API requests to
the Grafana API to create new dashboard panels.
2. Grafana Dashboard: 

![Alt text](./dstl_2_archi_diagram.png?raw=true "Title")

# Spinning up with docker compose

To start the program go to the root directory of the repo and run:

    $ cd <repo root dir>
    $ docker compose up --build

# Accessing the Flask Webapp and Grafana
Open a web browser.  To access the Simple Editable Query EXecutor (SEQX) go to:

    localhost:5000/

When operating the query creator follow the links on the main page to for the information you require.

To access the dashboard on Grafana go to:

    localhost:3000/

You will need to log in to grafana using the default login below:

Username:

    admin

Password

    admin

You will then be asked to update the password, you must set it to:

    qwerty


# Spin Down with docker compose

To stop the program cleanly please:

<li> In the terminal execute the below commands </li>

    $ cd <repo root dir>
    $ docker compose down

<li> Close all relevant instances of the terminal</li>