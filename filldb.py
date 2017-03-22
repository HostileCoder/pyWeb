from app import db, models

models.Role.query.delete()
models.Project.query.delete()
models.User.query.delete()
models.users_roles.delete()
db.session.commit()

admin=models.Role('admin')
user=models.Role('user')


u = models.User(email='admin', password='123')
u.add_role(admin)
db.session.add(u)
db.session.commit()

u = models.User(email='bob', password='111')
u.add_role(user)
db.session.add(u)
db.session.commit()

u = models.User(email='amy', password='222')
u.add_role(user)
db.session.add(u)
db.session.commit()

u = models.User(email='alice', password='333')
u.add_role(user)
db.session.add(u)
db.session.commit()



u = models.User.query.get(2)
p = models.Project(name='kiki', description='good stuff', author=u)
db.session.add(p)
db.session.commit()

u = models.User.query.get(3)
p = models.Project(name='dodo', description='nice stuff', author=u)
db.session.add(p)
db.session.commit()

u = models.User.query.get(4)
p = models.Project(name='haha', description='fabulous stuff', author=u)
db.session.add(p)
db.session.commit()

u = models.User.query.get(2)
p = models.Project.query.get(3)
p.users.append(u)
db.session.add(p)
db.session.commit()


