# TwinDB Monitoring ![alt text](https://travis-ci.org/twindb/monitoring.svg?branch=master "Travis Build Status")

TwinDB monitoring provides a set of Datadog dashboards and monitors that would allow you to monitor your MySQL 
infrastructure. Scripts are provided to automatically keep the dashboards and monitors defined in Datadog in sync.
 
## Running

    make virtualenv
    source env/bin/activate
    make bootstrap
    dd_generate_dashboards
    dd_generate_monitors
    
## dd_generate_dashboards
Creates the dashboards in Datadog using the dashboard definitions present in the dd/dashboards directory.

## dd_generate_monitors
Creates the monitors in Datadog using the monitor definitions present in the dd/monitors directory.

**You have to update the monitors templates and replace _@jira-alert-recipient_ with the actual monitor alert recipient.**