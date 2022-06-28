class Config(object):
    DEBUG = True
    SECRET_HERE = '2353quq46rtrt'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}

# Это файл конфигурации приложения,в котором может храниться путь к БД, ключи шифрования или что-то еще.
# Чтобы добавить новую конфигурацию приложения, необходимо дописать ее в классе Config ниже.