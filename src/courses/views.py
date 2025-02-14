from django.shortcuts import render
from . import services
from django.http import Http404,JsonResponse

# Create your views here.
def course_list_view(request):
    queryset = services.get_published_courses()
    print(queryset)
    context ={
        'object': queryset,
    }
    # return JsonResponse({"data": [x.path for x in queryset]})
    return render(request, 'courses/course_list.html',context)



def course_detail_view(request,course_id=None,*args, **kwargs):
    course_obj = services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lesson_queryset = course_obj.lesson_set.all()
    context ={
        'object_list': course_obj,
        'lesson_queryset': lesson_queryset,  # passing queryset to template for rendering
    }
    # return JsonResponse({"data": course_obj.id , "lessons": [x.path for x in lesson_queryset]  })
    return render(request, 'courses/detail.html',context)



def lesson_detail_view(request,course_id=None,lesson_id = None,*args, **kwargs):
    lesson_obj = services.get_lesson_detail(
        course_id=course_id,
        lesson_id = lesson_id)
    print(course_id,lesson_id)
    if lesson_obj is None:
        raise Http404
    return JsonResponse({"data": lesson_obj.id})
    
    # return render(request, 'cource/lession_detail.html')