from datetime import datetime
import json
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView
from djangotoolbox.http import JSONResponse
from scribble.forms import CommentForm
from scribble.models import Piece, Writeup, Comment
from django.template import loader
from django.template.context import RequestContext


class ScribbleView(ListView):
    model = Writeup
    template_name = 'scribble_view.html'

    def get_queryset(self):
        posted_on = datetime.strptime(('%s/%s/%s' % (self.kwargs['year'], self.kwargs['month'], self.kwargs['date'])),
                                      '%Y/%m/%d')
        return get_object_or_404(Writeup, posted_on=posted_on, title=self.kwargs['title'])

    def get_context_data(self, **kwargs):
        context = super(ScribbleView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        # context['comments'] = Comment.objects.filter(post_id)
        return context


class ScribbleListView(ListView):
    model = Piece
    template_name = 'home.html'
    queryset = Piece.objects.all().order_by('-posted_on')


class JSONResponseMixin(object):
    response_class = HttpResponse
    json_fields = None
    use_natural_key = None

    def render_to_response(self, context, **response_kwargs):
        return self.response_class(json.dumps(context), content_type='application/json', **response_kwargs)


class CommentView(JSONResponseMixin, FormView):
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.request.POST.get('post_id')
        obj = Comment(comment=form.cleaned_data['comment'], commentator=form.cleaned_data['commentator'], post_id=post_id)
        obj.save()
        t = loader.get_template('comment_list_item.html')
        c = RequestContext(self.request, {'comment_obj': obj})
        return self.render_to_response({'html': t.render(c), 'status': True})

    def form_invalid(self, form):
        return self.render_to_response({'status': False})

    def get(self, request, *args, **kwargs):
        writeup_pk = request.GET.get('pk')
        comments = Comment.objects.filter(post_id=writeup_pk).order_by('-posted_on')
        t = loader.get_template('comment_list.html')
        c = RequestContext(self.request, {'comments': comments})
        return self.render_to_response({'html': t.render(c), 'status': True})


