
import psycopg2

def articles():
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select articles.title, count(newpath) as views from articles\
    join new_log on articles.slug=new_log.newpath group by articles.title order\
    by views desc limit 3;")
    article=c.fetchall()
    print article
    pg.close()

def authors():
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select authors.name, count(art_log.newpath) as views from\
    authors join art_log on authors.id=art_log.author group by authors.name order by\
    views desc;")
    author=c.fetchall()
    print author
    pg.close()

def errors():
    pg = psycopg2.connect("dbname=news")
    c = pg.cursor()
    c.execute("select day, error_ratio from error_rate limit 1;")
    error=c.fetchall()
    print error
    pg.close()

articles()
authors()
errors()
