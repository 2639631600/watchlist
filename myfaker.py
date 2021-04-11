from faker import Faker
from faker.providers import internet, company
fake = Faker('zh_CN')
fake.add_provider(internet)
fake.add_provider(company)
for _ in range(10):
    print(fake.name(), fake.ascii_free_email(), fake.company())
