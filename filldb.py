from app import db, models
models.User.query.delete()

u = models.User(email='bob', password='111')
db.session.add(u)
db.session.commit()
u = models.User(email='alice', password='222')
db.session.add(u)
db.session.commit()
u = models.User(email='amy', password='333')
db.session.add(u)
db.session.commit()


u = models.User.query.get(1)
p = models.Project(name='kiki', description='good stuff', author=u)
db.session.add(p)
db.session.commit()