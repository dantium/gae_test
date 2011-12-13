from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.create_update import delete_object
from django.http import HttpResponseRedirect

from forms import PostForm
from models import Post

def list_posts(request):      
    posts = Post.objects.published()
    return render(request, 'blog/list.html', {'posts':posts})
    
def display_post(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post':post})

@login_required()
def delete_post(request,object_id):
    return_path = reverse('blog-listposts', kwargs={})
    template_name = 'blog/delete.html'
    return delete_object(request,Post,return_path,object_id=object_id,template_name=template_name)
    
@login_required()    
def create_edit_post(request,object_id=None):
    return_path = reverse('blog-listposts', kwargs={})
    if object_id is None:
        post = Post()
    else:
        post = get_object_or_404(Post,id=object_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid(): 
            post = post_form.save()
            return HttpResponseRedirect(return_path)
    else:
        post_form = PostForm(instance=post)
        
    return render(request, 'blog/create_edit.html', {'object_id':object_id, 'form':post_form})

