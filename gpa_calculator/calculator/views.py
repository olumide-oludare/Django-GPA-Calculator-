from django.shortcuts import render, redirect
from .forms import GradeForm
from .models import Grade

def index(request):
    grades = Grade.objects.all()
    total_credits = sum(grade.credits for grade in grades)
    total_points = sum(grade.credits * grade.grade for grade in grades)
    if total_credits == 0:
        gpa = 0
    else:
        gpa = round(total_points / total_credits, 2)
    context = {'grades': grades, 'total_credits': total_credits,'total_points': total_points, 'gpa': gpa}
    return render(request, 'calculator/index.html', context)


def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GradeForm()
    context = {'form': form}
    return render(request, 'calculator/add_grade.html', context)