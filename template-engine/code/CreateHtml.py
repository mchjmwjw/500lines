import time
from templite import Templite, TempliteSyntaxError

f = open('muban.wjw', 'r')
dat = f.read()
f.close()
templite = Templite(dat, {'upper': str.upper})
text = templite.render({
    'name': "Ned",
    'topics': ['Python', 'Geometry', 'Juggling'],
})
print(text)

t = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

f = open(t + '.html', 'w')
f.write(text)
f.close()