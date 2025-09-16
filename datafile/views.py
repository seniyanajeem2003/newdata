from django.shortcuts import render
def page1(request):
    return render(request,'page1.html')

def page2(request):
    array=[
        {'name': 'John', 'age': 25, 'city': 'New York'},
        {'name': 'Jane', 'age': 30, 'city': 'San Francisco'},
        {'name': 'Bob', 'age': 20, 'city': 'Chicago'}
    ]
    return render(request,'page2.html',{'array': array})


from .forms import LoginForm
def page3(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'form-data.html',{
            'name': form['name'].value,
            'email': form['email'].value,
            'password': form['password'].value
        })
    else:
        form= LoginForm
    return render(request,'page3.html',{'form':form})