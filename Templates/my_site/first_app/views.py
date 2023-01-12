from django.shortcuts import render

# Create your views here.
def default_views(request):
    return render(request,'first_app/example.html')

def variable_views(request):
    my_var = {'first_name':'rosalind','second_name':'franklin','some_list':[1,2,3],'some_dict':{'inside_key':'inside_value'}}
    return render(request,'first_app/variable.html',context=my_var)