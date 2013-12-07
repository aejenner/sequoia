from question.models import *

for i in range(1, 6):
	c1 = Category1(name = 'Toplevel' + str(i))
	c1.save()
	for j in range(1, 6):
		c2 = Category2(category=c1 , name = 'Midlevel' + str(j))
		c2.save()
		for k in range(1, 6):
			c3 = Category3(category=c2, name = 'Lowlevel' + str(k))
			c3.save()
			for q in range(1, 8):
				qq = Question(category=c3, text='Question ' + str(q))
				qq.save()
				for c in range(1, 5):
					choice = Choice(question=qq, text='Choice ' + str(c))
					if c % 3 == 0:
						choice.is_correct = True
					choice.save()

