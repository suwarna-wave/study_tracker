from django.shortcuts import render, get_object_or_404
from .models import Subject, Unit, Progress

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'tracker/subject_list.html', {'subjects': subjects})

def unit_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    units = Unit.objects.filter(subject=subject)
    progress_data = []

    for unit in units:
        progress, created = Progress.objects.get_or_create(unit=unit)
        progress_data.append({
            'unit': unit,
            'completed': progress.completed,
        })

    return render(request, 'tracker/unit_list.html', {
        'subject': subject,
        'progress_data': progress_data,
    })

def mark_completed(request, unit_id):
    unit = get_object_or_404(Unit, id=unit_id)
    progress, created = Progress.objects.get_or_create(unit=unit)
    progress.completed = True
    progress.save()
    return render(request, 'tracker/mark_completed.html', {'unit': unit})