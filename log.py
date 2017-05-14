import psycopg2

""" Importing the psycopg2 library for Postgresql Database """

def articles():
    """ articles method is used to print popular articles"""
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select articles.title, count(newpath) as views from articles\
    join new_log on articles.slug=new_log.newpath group by articles.title order\
    by views desc limit 3;")
    article=c.fetchall()
    print ("Popular articles of all time are: \n", article)
    pg.close()

def authors():
    """ authors method is used to print popular Authors"""
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select authors.name, count(art_log.newpath) as views from\
    authors join art_log on authors.id=art_log.author group by authors.name order by\
    views desc;")
    author=c.fetchall()
    print ("Popular authors of all time are: \n", author)
    pg.close()

def errors():
    """ errors method is used to print errors during the day"""
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select day, error_ratio from error_rate limit 1;")
    error=c.fetchall()
    print ("Highest error rate on: \n", error)
    pg.close()

articles()
authors()
errors()
