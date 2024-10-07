from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'challenges/index.html')
    # return HttpResponse("hola!")

def month(request, month=None):
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
        'december': 'Build a full-fledged project using everything learned in Django.'
    }
    month = month.lower()
    challenge_text = challenges.get(month, None)
    if challenge_text:
        return render(request, 'challenges/month.html', {'challenge': challenge_text})
    else:
        return HttpResponse(f"Invalid month: {month.capitalize()}. Please enter a valid month.", status=404)