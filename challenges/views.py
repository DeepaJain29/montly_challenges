from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

challenges = {
        'january': 'Learn Django basics: models, views, templates.',
        'february': 'Deep dive into Django ORM and database relationships.',
        'march': 'Master Django forms and validation.',
        'april': 'Learn about class-based views (CBVs) in Django.',
        'may': 'Explore Django authentication system and user management.',
        'june': 'Work with Django REST framework to build APIs.',
        'july': 'Learn about Django signals and middleware.',
        'august': 'Deploy Django projects on cloud platforms like Heroku or AWS.',
        'september': 'Implement real-time features using Django channels.',
        'october': 'Optimize Django applications for performance and security.',
        'november': 'Learn Django testing with pytest and Django’s test framework.',
        'december': 'Build a full-fledged project using everything learned in Django.',
        'hola' : None,
    }

def index(request):
    # challenges_cap = {month: challenge for month, challenge in challenges.items()}
    # return render(request,'challenges/index.html', {'challenges': challenges_cap})
    # return render(request,'challenges/index.html', {'challenges': challenges})
    months = list(challenges.keys())
    return render(request,'challenges/index.html', {'months': months})


def month_by_int(request, month=1):
    month = int(month)-1
    challenges_keys = list(challenges.keys())
    print(len(challenges_keys))
    if month >= 0 and month < len(challenges_keys):
        month_name = challenges_keys[month]
        print(month_name)
        return HttpResponseRedirect(reverse('month', args=[month_name]))
    else:
        return HttpResponse(f"Invalid month. Please enter a valid month.", status=404)
    
def month(request, month=None):
    month = month.lower()
    challenge_text = challenges.get(month, "not_found")
    print(challenge_text)
    if challenge_text == "not_found":
        return HttpResponse(f"Invalid month: {month.capitalize()}. Please enter a valid month.", status=404)
    return render(request, 'challenges/month.html', {'challenge': challenge_text, 'month': month})
    # if challenge_text:
    # try:
    #     return render(request, 'challenges/month.html', {'challenge': challenge_text, 'month': month})
    # # else:
    # except:
    #     return HttpResponse(f"Invalid month: {month.capitalize()}. Please enter a valid month.", status=404)