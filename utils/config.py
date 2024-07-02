from configparser import ConfigParser

host = "localhost",
database = "postgres",
user = "postgres",
password = "10203040"


def config(filename="C:/Users/User/Documents/Python/SkyPro/TermPaper_5_SQL+API/database.ini",
           section="postgresql"):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            'Section {0} is not found in the {1} file'.format(section, filename))
    return db
