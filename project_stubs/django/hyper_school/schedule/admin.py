from django.contrib import admin

from .models import Teacher, Course, Student


class TeacherCourseInline(admin.StackedInline):
    can_delete = False
    model = Course.teacher.through


class StudentCourseInline(admin.TabularInline):
    can_delete = False
    model = Student.course.through


class TeacherAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'age', 'about')
    inlines = (TeacherCourseInline,)


class CourseAdmin(admin.ModelAdmin):
    inlines = (StudentCourseInline, TeacherCourseInline)
    exclude = ('teacher',)


class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentCourseInline,)
    exclude = ('course',)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
