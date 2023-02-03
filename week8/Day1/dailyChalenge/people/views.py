from django.shortcuts import render
from django.http import HttpResponse


def people(request):
	people = [
	  {
	    'id': 1,
	    'name': 'Bob Smith',
	    'age': 35,
	    'country': 'USA'
	  },
	  {
	    'id': 2,
	    'name': 'Martha Smith',
	    'age': 60,
	    'country': 'USA'
	  },
	  {
	    'id': 3,
	    'name': 'Fabio Alberto',
	    'age': 18,
	    'country': 'Italy'
	  },
	  {
	    'id': 4,
	    'name': 'Dietrich Stein',
	    'age': 85,
	    'country': 'Germany'
	  }
	]
	infos = sorted(people, key=lambda d: d['age'])
	return render(request, "people/index.html", {'people' : infos, 'id' : -1})

def info(request, id):
	people = [
	  {
	    'id': 1,
	    'name': 'Bob Smith',
	    'age': 35,
	    'country': 'USA'
	  },
	  {
	    'id': 2,
	    'name': 'Martha Smith',
	    'age': 60,
	    'country': 'USA'
	  },
	  {
	    'id': 3,
	    'name': 'Fabio Alberto',
	    'age': 18,
	    'country': 'Italy'
	  },
	  {
	    'id': 4,
	    'name': 'Dietrich Stein',
	    'age': 85,
	    'country': 'Germany'
	  }
	]
	X = id
	return render(request, "people/index.html", {'people' : people, 'id' : X})