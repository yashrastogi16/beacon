from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from models import *
from django.conf import settings
from forms import *
from beacon_info.models import *
from offers.models import *
import datetime

def user_login_required(f):
		def wrap(request, *args, **kwargs):
				print "decorater is calling"
				#this check the session if userid key exist, if not it will redirect to login page
				if 'user' not in request.session.keys():
						return HttpResponseRedirect("/")
				return f(request, *args, **kwargs)
		wrap.__doc__=f.__doc__
		wrap.__name__=f.__name__
		return wrap
def login(request):
	form = Store_userForm(request.POST)
	content = {}
	content['form'] = form
	content.update(csrf(request))
	if 'user' in request.session.keys():
		return HttpResponseRedirect("/index")

	if request.method == "POST":
		print "post method"
		username = request.POST['userid']
		# password = request.POST['password']
		password = request.POST['password']
		# password = hashpass(in_password)
		user_list = store_user.objects.filter(user_id=username, password=password)
		if(user_list):
			userobj = user_list[0]
			s=store_userlogin(username = userobj.firstname, userid = userobj.user_id, store = userobj.store_admin, logintime = datetime.datetime.now())
			s.save()   
			request.session['user'] = userobj
			# return HttpResponse("This is Admin Home Page")
			return HttpResponseRedirect("/dashboard")
		else:
			content['err_msg'] = 'Invalid username or password'
			# return HttpResponse("Login Failed")
		return render_to_response('login.html', content, context_instance=RequestContext(request))

	return render_to_response('login.html', content, context_instance=RequestContext(request))
# def login(request):
# 	return render_to_response('login.html',context_instance=RequestContext(request))
@user_login_required
def dashboard(request):
	user1 = request.session['user']
	content = {}
	content['name'] = user1.firstname
	content['lastname'] = user1.lastname
	content['id'] =user1.id
	return render_to_response('dashboard.html', content, context_instance=RequestContext(request))
@user_login_required
def logout(request):
	print "logout"
	print type(request)
	user = request.session['user']
	s=store_userlogout(username = user.firstname, userid = user.user_id, store = user.store_admin, logouttime = datetime.datetime.now())            
	s.save()
	session_keys = request.session.keys()
	form = Store_userForm(request.POST)
	for key in session_keys:
		print "del"
		del request.session[key]
	# content.update(csrf(request))
	return HttpResponseRedirect('/')
@user_login_required
def adduser(request):
	form = MemberForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/viewuser/')
	return render_to_response('adduser.html',locals(),context_instance=RequestContext(request))
@user_login_required
def userlist(request):
	user = members.objects.all()
	content = {'lists' : user}
	return render_to_response('viewusers.html',content,context_instance=RequestContext(request))
@user_login_required
def adddepartment(request):
	form = DepartmentForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/viewdepartment/')
	return render_to_response('adddepartment.html',locals(),context_instance=RequestContext(request))
@user_login_required
def departmentlist(request):
	user1 = request.session['user']
	user = department.objects.filter(store = user1.store_admin)
	content = {'lists' : user}
	return render_to_response('viewdepartment.html',content,context_instance=RequestContext(request))

@user_login_required
def addbeacon(request):
	form = Beacon_macForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/viewbeacon/')
	return render_to_response('addbeacon.html',locals(),context_instance=RequestContext(request))
@user_login_required
def beaconlist(request):
	user = becon_mac.objects.all()
	content = {'lists' : user}
	return render_to_response('viewbeacon.html',content,context_instance=RequestContext(request))
@user_login_required
def addoffer(request):
	form = OfferForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('/viewoffer/')
	return render_to_response('addoffers.html',locals(),context_instance=RequestContext(request))
@user_login_required
def offerlist(request):
	user = offer.objects.all()
	content = {'lists' : user}
	return render_to_response('viewoffer.html',content,context_instance=RequestContext(request))

