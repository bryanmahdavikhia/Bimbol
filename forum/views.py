from django.shortcuts import render

from forum.serializers import ForumSerializer, ReplySerializer
from userauth.models import CustomUser
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
@api_view(['GET'])
def json(request):
    data_forum = serializers.serialize('json', Forum.objects.all())
    data_reply = serializers.serialize('json', Reply.objects.all()).replace('null', 'None')
    data_forum = eval(data_forum)
    for forum in data_forum:
        forum['fields']['author'] = CustomUser.objects.filter(pk=forum['fields']['author'])[0].username
        print(forum)

    data_reply = eval(data_reply)
    for reply in data_reply:
        reply['fields']['user'] = CustomUser.objects.filter(pk=reply['fields']['user'])[0].username
        
    data = {'data_forum' : data_forum, 'data_reply' : data_reply}
    return Response(data)

@api_view(['GET'])
def forumJson(request, id):
    data_reply = serializers.serialize('json', Reply.objects.filter(forum=id)).replace('null', 'None')
    data_reply = eval(data_reply)
    for reply in data_reply:
        reply['fields']['user'] = CustomUser.objects.filter(pk=reply['fields']['user'])[0].username
     
    return Response(data_reply)

@api_view(['GET'])
def replyJson(request, id):
    data_reply = serializers.serialize('json', Reply.objects.filter(parent=id)).replace('null', 'None')
    data_reply = eval(data_reply)
    for reply in data_reply:
        reply['fields']['user'] = CustomUser.objects.filter(pk=reply['fields']['user'])[0].username

    return Response(data_reply)

@api_view(['POST'])
def createForum(request):
    data = request.data
    print(request.user)
    forum = Forum.objects.create(
        title = data['title'],
        desc = data['desc'],
        author = request.user
    )
    serializer = ForumSerializer(forum, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createReply(request, id):
    par = Reply.objects.get(id=id)
    print("="*30)
    post = Forum.objects.get(id=par.forum.id)
    data = request.data
    reply = Reply.objects.create(
        desc = data['desc'],
        user = request.user,
        forum = post,
        parent = par
    )
    serializer = ReplySerializer(reply, many=False)
    return Response(serializer.data)

# nggak pake
@login_required(login_url='/admin/login/')
def ForumJson(request, id):
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
        form.save()
        # form = ForumForm()
        return HttpResponseRedirect('/forum')

        
    context = {
        'loged' : request.user.is_authenticated,
        'forum' : forum,
        'form' : form
    }
    return render(request, 'index.html', context)
