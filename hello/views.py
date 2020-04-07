from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import HelloForm



def index(request):
	data = Friend.objects.all().values('id', 'name', 'age')
	params = {
		'title': 'Hello',
		'data': data,
		}
	return render(request, 'hello/index.html', params)

	def __new_str__(self):
	result = ''
	for item in self:
		result += '<tr>'
		for k in item:
			result += '<td>' + str(k) + '=' + str(item[k]) +'</td>'
		result += '</tr>'
	return result

QuerySet.__str__ = __new_str__