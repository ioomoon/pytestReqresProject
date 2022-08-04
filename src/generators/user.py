from faker import Faker


class User:
    def __init__(self):
        self.fake = Faker()
        self.result = {}
        self.build()

    def set_name(self):
        self.result['name'] = self.fake.name()

    def set_job(self):
        self.result['job'] = self.fake.job()

    def build(self):
        self.set_name()
        self.set_job()
        return self.result


