import os
import webbrowser

from invoke import task

try:
    RQ_DASHBOARD_URL = os.environ["RQ_DASHBOARD_URL"]
except:
    print("Environment variables should contain RQ_DASHBOARD_URL")


@task(aliases=["db"])
def dashboard(c):
    """Open RQ dashboard
    """
    webbrowser.open(RQ_DASHBOARD_URL)
