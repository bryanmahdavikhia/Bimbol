from django.shortcuts import render
from .forms import ForumForm, ReplyForm, ReplyofReplyForm
from .models import Forum, Reply
from datetime import datetime
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @login_required(login_url='/admin/login/')
@api_view(['GET', 'POST'])
def json(request):
    data_forum = serializers.serialize('json', Forum.objects.all())
    data_reply = serializers.serialize('json', Reply.objects.all()).replace('null', 'None')
    print(data_forum)
    data = {'data_forum' : eval(data_forum), 'data_reply' : eval(data_reply)}
    print(data)
    return Response(data)

@login_required(login_url='/admin/login/')
def postPageJson(request, id):
    temp =  Forum.objects.filter(pk=id)
    print(temp)
    # temp[0]['fields']['username'] = temp[0].author.username
    # print("----------" + temp[0].author.username)
    data_post = serializers.serialize('json', temp)
    data_post = eval(data_post)
    data_post[0]['fields']['username'] = temp[0].author.username
    return JsonResponse(data_post, safe=False)
    # data_post = serializers.serialize('json', data_post)
    # return HttpResponse(data_post, content_type="application/json")

@login_required(login_url='/pendaftaransiswa/')
def postPage(request, id):
    post = Forum.objects.get(id=id)

    reply = ReplyForm(request.POST or None)
    replyofreply = ReplyofReplyForm(request.POST or None)

    if reply.is_valid():
        obj = reply.save(commit=False)
        obj.user = request.user
        obj.forum = post
        obj.parent = None
        obj.created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        reply.save()
        # form = ForumForm()
        return HttpResponseRedirect('/forum/post/' + str(id) + '#' + str(obj.id))

    context = {
        'reply_form' : reply,
        'reply_of_reply_form' : replyofreply,
        'post' : post
    }
    return render(request, 'post.html', context)

@login_required(login_url='pendaftaransiswa/')
def replyPage(request):
    form = ReplyofReplyForm(request.POST or None)

    if form.is_valid():
        post_id = request.POST.get('post')
        parent_id = request.POST.get('parent')
        obj = form.save(commit=False)
        obj.user = request.user
        obj.forum = Forum(id=post_id)
        obj.parent = Reply(id=parent_id)
        obj.save();
        return HttpResponseRedirect('/forum/post/' + str(post_id) + '#' + str(obj.id))

def index(request):
    forum = Forum.objects.all().order_by('-created')

    form = ForumForm(request.POST or None)

    if form.is_valid() and request.user.is_authenticated:
        obj = form.save(commit=False)
        obj.author = request.user
        obj.created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        form.save()
        # form = ForumForm()
        return HttpResponseRedirect('/forum')

        
    context = {
        'loged' : request.user.is_authenticated,
        'forum' : forum,
        'form' : form
    }
    return render(request, 'index.html', context)
