from django.contrib import admin

from .models import Teacher, Course, Student


class TeacherInline(admin.TabularInline):
    can_delete = False
    model = Teacher
    readonly_fields = ('name', 'surname')


class CourseInline(admin.TabularInline):
    can_delete = False
    model = Course
    readonly_fields = ('title', 'duration_months')


class StudentInline(admin.TabularInline):
    can_delete = False
    model = Student
    readonly_fields = ('name', 'surname')


class TeacherAdmin(admin.ModelAdmin):
    fields = ("__all__",)


class CourseAdmin(admin.ModelAdmin):
    fields = ("__all__",)
    # inlines = (StudentInline, )

class StudentAdmin(admin.ModelAdmin):
    fields = ("__all__",)
    # inlines = (CourseInline, )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
