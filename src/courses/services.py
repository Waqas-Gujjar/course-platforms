from .models import Course, Lesson, PublishStatus
from django.core.exceptions import ObjectDoesNotExist


def get_published_courses():
    # Returns all published courses
    return Course.objects.filter(status=PublishStatus.PUBLISHED)


def get_course_detail(course_id=None):
    if course_id is None:
        return None
    obj = None
    
    try:
        return Course.objects.get(
            status=PublishStatus.PUBLISHED,
            public_id=course_id
        )
    except:
        pass
    return obj


def get_lesson_detail(lesson_id=None, course_id=None):
    if lesson_id is None or course_id is None:
        return None
    
    try:
        return Lesson.objects.get(
            course__public_id=course_id,
            course__status=PublishStatus.PUBLISHED,
            status=PublishStatus.PUBLISHED,
            public_id=lesson_id
        )
    except Lesson.DoesNotExist:
        print(f"Lesson with ID '{lesson_id}' in Course '{course_id}' does not exist.")
        return None
    except Exception as e:
        print(f"Unexpected error in get_lesson_detail: {e}")
        return None
