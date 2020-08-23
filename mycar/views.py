from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import MyCarForm, CommentForm
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView,
                                  CreateView)

from .models import MyCar, Category, Comment 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


#@login_required
#def auto_create(request):
#    if request.method == 'POST':
#        form = MojAutoForm(request.POST,request.FILES)
#        if form.is_valid():
#            auto = form.save(commit=False)
#            auto.author = request.user 
#            auto.save()
#            return redirect('index')
#    else:
#         form = MojAutoForm()
#    return render(request,'mojauto/mojauto_form.html',{'form':form})        
     

class MyCarCreateView(LoginRequiredMixin, CreateView):
    form = MyCarForm
    model = MyCar
    fields = ('category','brand','model','image','owner','year')
    success_url = reverse_lazy('mycar:car_list')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.author = self.request.user 
        car.save()
        return super().form_valid(form)   


#class MyCarListView(ListView):
   # context_object_name = 'cars'
   # model = models.MyCar
   # ordering = ['-created_at']

    #MISLIM DA NE RADI ZATO STO SU SVI OBJEKTI DODATI PRE NEGO STO JE DODAT OVAJ FIELD!! PRVO PROBATI SA ordering pa onda sa QUERYSET!!! 

    #def get_queryset(self):
        #return YourModel.objects.order_by('model_field_here')


def is_valid_queryparam(param):
        return param != '' and param is not None


# Had to be this approach(not class-based-view), because of the search option 
@login_required
def car_list(request):
    qs = MyCar.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    category = request.GET.get('category')


    if is_valid_queryparam(category) and category != 'All':
        qs = qs.filter(category__name=category)    

    context = {
        'cars': qs, 
        'categories':categories,
    }

    return render(request,'mycar/mycar_list.html',context)



class MyCarDetailView(DetailView):
    context_object_name = 'car_detail'
    model = MyCar
    template_name = 'mycar/car_detail.html'


class MyCarUpdateView(UpdateView):
    form_class = MyCarForm
    model = MyCar
    success_url = reverse_lazy('mycar:car_list')


class MyCarDeleteView(DeleteView):
    model = MyCar
    success_url = reverse_lazy('mycar:car_list')
 

def add_comment(request, pk):
    car = get_object_or_404(MyCar,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.car = car
            comment.save()
            return redirect('mycar:car_detail',pk=car.pk)
    else:
        form = CommentForm()

    return render (request,'mycar/comment_form.html',{'form':form})            


def comment_remove(request,pk):
        comment = get_object_or_404(Comment,pk=pk)
        car_pk = comment.car.pk

        if comment.author == request.user:
    #if models.Comment.author == request.user:
            comment.delete()
    #else:   
        return redirect('mycar:car_detail',pk=car_pk)
   