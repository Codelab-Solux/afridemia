from http.client import HTTPResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def schools(req):
    has_school = False
    user = req.user
    if user.is_authenticated:
        school = School.objects.filter(manager=user)
        if school:
            has_school = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query)
        | Q(address__icontains=query)
        | Q(moto__icontains=query)
        | Q(tel__icontains=query)
        | Q(levels__name__icontains=query),
        is_verified=True,
    ).distinct()

    # # ------------------ dropdown filter
    # all_schools = School.objects.all()
    # school_filter = SchoolFilter(req.GET, queryset=all_schools)

    edu_levels = EducationLevel.objects.all()
    ordering = ['is_featured == True']
    context = {
        "schools_page": "active",
        'title': 'schools',
        'schools': schools,
        'edu_levels': edu_levels,
        "has_school": has_school,
        # "school_filter": school_filter,
        'ordering': ordering,
    }
    # print(edu_levels)
    return render(req, 'schools/index.html', context)


def school(req, pk):
    is_manager = False
    user = req.user
    school = School.objects.get(id=pk)

    if user == school.manager:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    exam_stats = school.examstat_set.all()
    classrooms = school.classroom_set.all()
    structures = school.structure_set.all()
    # information
    articles = school.schoolarticle_set.all()
    advantages = school.advantage_set.all()
    preregs = school.preregistration_set.all()

    # pre registration
    prereg_form = PreRegForm()
    if req.method == 'POST':
        prereg_form = PreRegForm(req.POST, req.FILES)
        prereg_form.instance.user = user
        prereg_form.instance.school = school
        if prereg_form.is_valid():
            prereg_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    context = {
        "schools_page": "active",
        'title': 'school',
        'school': school,
        'teachers': teachers,
        'classrooms': classrooms,
        'exam_stats': exam_stats,
        'structures': structures,
        'is_manager': is_manager,
        'articles': articles,
        'advantages': advantages,
        'preregs': preregs,
        'prereg_form': prereg_form,
    }
    return render(req, 'schools/details.html', context)


@login_required(login_url='login')
def mySchool(req):
    is_manager = False
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('schools')
    else:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    classrooms = school.classroom_set.all()
    structures = school.structure_set.all()
    # information
    articles = school.schoolarticle_set.all()
    advantages = school.advantage_set.all()
    levels = EducationLevel.objects.all()

    context = {
        "my_school_page": "active",
        'title': 'my_school',
        'school': school,
        'teachers': teachers,
        'classrooms': classrooms,
        'structures': structures,
        'is_manager': is_manager,
        'articles': articles,
        'levels': levels,
        'advantages': advantages
    }
    return render(req, 'schools/details.html', context)


@login_required(login_url='login')
def create_school(req):
    user = req.user
    school = School.objects.filter(manager=user)
    if school:
        return redirect('schools')

    form = EditSchoolForm()
    if req.method == 'POST':
        form = EditSchoolForm(req.POST, req.FILES)
        form.instance.manager = user
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_create_page": "active", "title": 'add_school', "user": user, "form": form}
    return render(req, 'schools/edit_sch.html', context)


@login_required(login_url='login')
def edit_school(req, pk):
    user = req.user
    school = School.objects.get(manager=user, id=pk)
    if not school:
        return redirect('schools')

    form = EditSchoolForm(instance=school)
    if req.method == 'POST':
        form = EditSchoolForm(req.POST, req.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('my_school')

    teacher_form = TeacherForm()
    if req.method == 'POST':
        teacher_form = TeacherForm(req.POST, req.FILES)
        teacher_form.instance.school = school
        if teacher_form.is_valid():
            teacher_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    classroom_form = ClassroomForm()
    if req.method == 'POST':
        classroom_form = ClassroomForm(req.POST, req.FILES)
        classroom_form.instance.school = school
        if classroom_form.is_valid():
            classroom_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    structure_form = StructureForm()
    if req.method == 'POST':
        structure_form = StructureForm(req.POST, req.FILES)
        structure_form.instance.school = school
        if structure_form.is_valid():
            structure_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    article_form = ArticleForm()
    if req.method == 'POST':
        article_form = ArticleForm(req.POST, req.FILES)
        article_form.instance.school = school
        if article_form.is_valid():
            article_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    photo_form = PhotoForm()
    if req.method == 'POST':
        photo_form = PhotoForm(req.POST, req.FILES)
        photo_form.instance.school = school
        if photo_form.is_valid():
            photo_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    stats_form = ExamStatForm()
    if req.method == 'POST':
        stats_form = ExamStatForm(req.POST, req.FILES)
        stats_form.instance.school = school
        if stats_form.is_valid():
            stats_form.save()
            return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        form = EditSchoolForm(req.POST, req.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('my_school')
    context = {
        "sch_edit_page": "active",
        "title": 'edit_school',
        "school": school,
        "user": user,
        "form": form,
        "teacher_form": teacher_form,
        "classroom_form": classroom_form,
        "structure_form": structure_form,
        "article_form": article_form,
        "photo_form": photo_form,
        "stats_form": stats_form,
    }
    return render(req, 'schools/edit_sch.html', context)


def sch_list(req):
    schools = School.objects.all()
    context = {'schools': schools}
    return render(req, 'components/featured_list.html', context)


# def articles(req, pk):
#     is_manager = False
#     school = School.objects.get(id=pk)
#     # people
#     articles = school.article_set.all()

#     context = {
#         "schools_page": "active",
#         'title': 'school',
#         'school': school,
#         'is_manager': is_manager,
#         'articles': articles,
#     }
#     return render(req, 'schools/articles.html', context)


# @login_required(login_url='login')
# def levelsMod(req, pk):
#     is_manager = False
#     user = req.user
#     if user.is_authenticated:
#         school = School.objects.get(manager=user, id=pk)
#         if school:
#             is_manager = True

#     all_levels = EduLevel.objects.all()
#     context = {
#         "schools_page": "active",
#         'title': 'levels_mod',
#         'school': school,
#         'all_levels': all_levels,
#     }
#     # user = req.user
#     # if user.is_authenticated:
#     #     school = School.objects.filter(manager=user, id=pk)
#     #     if school:
#     #         is_manager = True

#     if not is_manager:
#         return redirect('home')

#     if req.method == 'POST':
#         if req.POST, req.FILES.get('levels'):
#             school.levels.set(req.POST, req.FILES.get('levels').id)
#             school.save()
#             return redirect('my_school')
#     else:
#         return render(req, 'schools/levels_mod.html', context)


# # modal views

# @login_required(login_url='login')
# def add_teacher(req):
#     user = req.user
#     school = School.objects.get(manager=user)
#     if not school and user.role != 'manager':
#         return redirect('home')

#     if req.method == 'POST':
#         form = TeacherForm(req.POST, req.FILES)
#         print(form.instance.fullname)
#         # if form.is_valid():
#         #     form.instance.school = school
#         #     form.save()
#         #     return redirect('/')
#         #     # return HTTPResponse(status_code=200)
#     else:
#         form = TeacherForm()
#     context = {"form": form}
#     return render(req, 'schools/teacher_form.html', context)
