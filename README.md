# Udacity Log_Analysis
Udacity log analysis project is to build an internal reporting tool that will analyze information from the newspaper database to discover
what kind of articles the site's readers like. Source code can be found [here](https://github.com/vjvijayg/Log_Analysis)

## Installation and Setup:
1. Install [Vagrant](https://www.vagrantup.com/) and [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
2. Download [fullstack_nanodegree_repo zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/May/59125904_fsnd-virtual-machine/fsnd-virtual-machine.zip) or [clone here](https://github.com/udacity/fullstack-nanodegree-vm)
3. Download [News Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) or [clone here](https://github.com/vjvijayg/Log_Analysis.git) and move these files to Vagrant directory, which can be found in fullstack_nanodegree_repo.

## Implementation:
1. Navigate to full-stack-nanodegree-vm/vagrant directory through the command prompt or terminal.
2. Execute `vagrant up` command
3. Execute `vagrant ssh` command to login the Virtual Machine [you may need login details](https://www.vagrantup.com/docs/boxes/base.html)
4. Change the directory after successful `vagrant ssh` execute cd /vagrant 
5. To load and run the News Database use `psql -d news -f newsdata.sql`.
6. Create views listed below
7. After successful creation of Views Run `python log.py` to check out the output.

### Views created to solve tasks:
1. What are the most popular three articles of all time?
    ```
    create view new_log as
    select substring(path, 10) as newpath, status, id
    from log;
     ```
2. Who are the most popular article authors of all time?
    ```
    create view art_log as 
    select new_log.newpath, articles.author,articles.slug, articles.id 
    from new_log join articles 
    on articles.slug=new_log.newpath;
    ```
3. On which days did more than 1% of requests lead to errors?
    ```
    create view error_log as
    select time::timestamp::date as date, count(*) as errors
    from log where status similar to '404%' 
    group by date order by errors desc;
    ```
    ```
    create view request_log as
    select time::timestamp::date as date, count(*) as requests
    from log group by date order by requests desc;
    ```
    ```
    create view error_rate as
    select error_log.date as day, error_log.errors::float/request_log.requests*100 as error_ratio
    from error_log join request_log on error_log.date=request_log.date
    order by error_ratio desc limit 10;
    ```

#### Software and tools used:
1. [Vagrant](https://www.vagrantup.com/)
2. [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
3. [Git bash](https://git-scm.com/downloads)

#### Skills gained:
1. Sql (Postgresql)
2. Python programming

Please refer to the wiki to find more about project.

## Welcome to the Log_Analysis project, which is the part of the [Full Stack Web Developer Nanodegree course](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
***
### About Project

Creating a internal tool which generates meaningful reports for the Newspaper Database, which has Articles, Authors and log table using postgresql and python script.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page.


### Tasks
Analyzing data from the logs of a web service to answer questions such as 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? using advanced SQL queries.

### Output of the report
Building an informative summary from logs is a real task that comes up very often in software engineering.

![Sample output of the tool](https://github.com/vjvijayg/Log_Analysis/blob/master/Output.png?raw=true)

#### Software and tools used:
1. Vagrant
2. Virtual Box
3. Git bash

#### Skills gained:
1. Sql
2. Python Script
