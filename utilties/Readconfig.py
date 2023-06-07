import configparser
config = configparser.RawConfigParser()
config.read("C:\\Users\\suraj\\Desktop\\automation project\\QAsuits\\Configuration\\config.ini")

class Redconfig:

    @staticmethod
    def First_name():
        first_name = config.get('common info', 'first_name')
        return first_name

    @staticmethod
    def lastname():
        last_name = config.get('common info', 'last_name')
        return last_name

    @staticmethod
    def email():
        email = config.get('common info', 'email')
        return email

    @staticmethod
    def mobno():
        mobno = config.get('common info', 'mobno')
        return mobno

    @staticmethod
    def org():
        org = config.get('common info', 'organisationname')
        return org

    @staticmethod
    def password():
        password = config.get('common info', 'password')
        return password