from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from . import services

# Course List View
def course_list_view(request):
    """
    Renders a list of all published courses.
    """
    queryset = services.get_published_courses()
    context = {
        'obj_list': queryset,
    }
    return render(request, 'courses/course_list.html', context)


# Course Detail View
def course_detail_view(request, course_id=None, *args, **kwargs):
    """
    Renders the details of a specific course and its associated lessons.
    Raises Http404 if the course does not exist or is not published.
    """
    course_obj = services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404("Course not found or not published.")
    
    lesson_queryset = services.get_courses_lessons(course_obj)
    context = {
        'object': course_obj,  # Use 'object' instead of 'objects' for consistency
        'lesson_queryset': lesson_queryset,
    }
    return render(request, 'courses/detail.html', context)


# Lesson Detail View
def lesson_detail_view(request, course_id=None, lesson_id=None, *args, **kwargs):
    """
    Returns JSON data for a specific lesson if it exists and is published or coming soon.
    Raises Http404 if the lesson does not exist or is not accessible.
    """
    lesson_obj = services.get_lesson_detail(course_id=course_id, lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404("Lesson not found or not accessible.")
    
    # Return JSON response with lesson details
    return JsonResponse({
        "data": {
            "lesson_id": lesson_obj.id,
            "course_id": course_id,
            "title": lesson_obj.title,
            "status": lesson_obj.status,
        }
    })