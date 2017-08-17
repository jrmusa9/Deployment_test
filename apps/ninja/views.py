from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime

def index(request):

    if 'gold' not in request.session:
        request.session['gold']=0
    
    if 'gold_count' not in request.session:
        request.session['gold_count']=0
        request.session['score']=0

    score='nothing'

    return render(request,'ninja/index.html')





def process_money(request ):


    loc=request.POST['building'] #location
    request.session['loc']=loc
    print loc
    win_lose= random.randint(0,1)
    print win_lose

    if loc == 'farm' and win_lose==1:
        rand=random.randint(10,20)
        request.session['gold']+=rand
        request.session['score']='win'
    elif loc == 'farm' and win_lose==0:
        rand=random.randint(10,20)
        request.session['gold']-=rand
        request.session['score']='lose'

    if loc == 'cave' and win_lose==1:
        rand=random.randint(5,10)
        request.session['gold']+=rand
        request.session['score']='win'
    elif loc == 'cave' and win_lose==0:
        rand=random.randint(5,10)
        request.session['gold']-=rand
        request.session['score']='lose'

    if loc == 'house' and win_lose==1:
        rand=random.randint(2,5)
        request.session['gold']+=rand
        request.session['score']='win'
    elif loc == 'house' and win_lose==0:
        rand=random.randint(2,5)
        request.session['gold']-=rand
        request.session['score']='lose'

    if loc == 'casino' and win_lose==1:
        rand=random.randint(0,50)
        request.session['gold']+=rand
        request.session['score']='win'
    elif loc == 'casino' and win_lose==0:
        rand=random.randint(0,50)
        request.session['gold']-=rand
        request.session['score']='lose'

    print type(request.session['score'])
    # time= datetime.datetime.now().time()
    request.session['gold_count']+=request.session['gold']


    return redirect('/') 


def reset(request):
    request.session.clear()
    return redirect('/')