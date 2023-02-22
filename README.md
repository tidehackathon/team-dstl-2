# team-dstl-2
# TIDE HACKATHON 2023, Warsaw, Poland
# Analytics Dashboard for Interoperability Challenge
# Starting the Dashboard
To start the program go to the following directory and run:

    cd <repo root dir>

    $ docker compose up --build

# Running the Program
When you have completed the start-up instructions above you will need to open a web browser.
To access the Query Generator for the Dashboard go to:

    localhost:5000/

When operating the query creator follow the links on the main page to for the information you require.
From here you will be able to modify the query allowing you to see only the data you want.

To access the dashboard on grafana go to:

    localhost:3000/

You will need to log in to grafana using the details below:

Username:

    qwerty

Password

    qwerty

# Closing the Program

To close the program cleanly please:

<li> Close all relevant windows on the browser </li>
<li> In the terminal a new terminal window in the repo space type and execute the below command </li>

    cd <repo root dir>
    $ docker compose down

<li> Close all relevant instances of the terminal</li>