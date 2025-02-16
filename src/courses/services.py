from .models import Course, Lesson, PublishStatus
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def get_published_courses():
    # Returns all published courses
    return Course.objects.filter(status=PublishStatus.PUBLISHED)

def get_course_detail(course_id=None):
    # Returns a specific course detail if it exists and is published
    if course_id is None:
        return None
    
    try:
        return Course.objects.get(
            status=PublishStatus.PUBLISHED,
            public_id=course_id
        )
    except ObjectDoesNotExist:
        # Logging the error or handling it appropriately is better than a bare except
        print(f"Course with ID '{course_id}' does not exist or is not published.")
        return None
    except Exception as e:
        # Catch specific exceptions instead of a general exception
        print(f"Unexpected error in get_course_detail: {e}")
        return None

def get_courses_lessons(course_obj=None):
    # Returns all lessons for a given course if it is published
    if not isinstance(course_obj, Course):
        return Lesson.objects.none()
    
    lessons = course_obj.lesson_set.filter(
        course__status=PublishStatus.PUBLISHED,
        status__in=[PublishStatus.PUBLISHED, PublishStatus.COMING_SOON]
    )
    return lessons

def get_lesson_detail(lesson_id=None, course_id=None):
    # Returns a specific lesson detail if it exists and is published or coming soon
    if lesson_id is None or course_id is None:
        return None
    
    try:
        return Lesson.objects.get(
            course__public_id=course_id,
            course__status=PublishStatus.PUBLISHED,
            status__in=[PublishStatus.PUBLISHED, PublishStatus.COMING_SOON],
            public_id=lesson_id
        )
    except ObjectDoesNotExist:
        print(f"Lesson with ID '{lesson_id}' in Course '{course_id}' does not exist.")
        return None
    except Exception as e:
        print(f"Unexpected error in get_lesson_detail: {e}")
        return None