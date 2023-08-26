from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


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
    ).distinct()

    # # ------------------ dropdown filter
    # all_schools = School.objects.all()
    # school_filter = SchoolFilter(req.GET, queryset=all_schools)

    levels = EducationLevel.objects.all()
    ordering = ['is_featured == True']
    context = {
        "schools_page": "active",
        'title': 'schools',
        'schools': schools,
        'levels': levels,
        "has_school": has_school,
        # "school_filter": school_filter,
        'ordering': ordering,
    }
    # print(levels)
    return render(req, 'schools/index.html', context)


def school(req, pk):
    is_manager = False
    user = req.user
    school = get_object_or_404(School, id=pk)

    if user == school.manager:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    performances = school.performance_set.all()
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
        'performances': performances,
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
    school = get_object_or_404(School, manager=user)
    if not school:
        return redirect('schools')
    else:
        is_manager = True

    # people
    teachers = school.teacher_set.all()
    # structures
    Teachers = school.teacher_set.all()
    structures = school.structure_set.all()
    # information
    articles = school.schoolarticle_set.all()
    advantages = school.advantage_set.all()
    levels = EducationLevel.objects.all()

    context = {
        "my_school_page": "active",
        'title': 'my school',
        'school': school,
        'teachers': teachers,
        'Teachers': Teachers,
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
        "sch_create_page": "active", "title": 'add school', "user": user, "form": form}
    return render(req, 'schools/sch_form.html', context)


@login_required(login_url='login')
def edit_school(req, pk):
    user = req.user
    school = get_object_or_404(School, manager=user, id=pk)
    if not school:
        return redirect('schools')

    form = EditSchoolForm(instance=school)
    if req.method == 'POST':
        form = EditSchoolForm(req.POST, req.FILES, instance=school)
        if form.is_valid():
            form.save()
            return redirect('my_school')

    context = {
        "sch_edit_page": "active",
        "title": 'edit school',
        "school": school,
        "user": user,
        "form": form,
    }
    return render(req, 'schools/sch_form.html', context)


@login_required(login_url='login')
def verify_school(req, pk):
    user = req.user
    obj = get_object_or_404(School, id=pk)
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            if obj.is_verified == False:
                School.objects.filter(id=pk).update(is_verified=True)
            else:
                School.objects.filter(id=pk).update(is_verified=False)
        except School.DoesNotExist:
            return HttpResponse('School not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


@login_required(login_url='login')
def feature_school(req, pk):
    user = req.user
    obj = get_object_or_404(School, id=pk)
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if req.method == 'POST':
        try:
            if obj.is_featured == False:
                School.objects.filter(id=pk).update(is_featured=True)
            else:
                School.objects.filter(id=pk).update(is_featured=False)
        except School.DoesNotExist:
            return HttpResponse('School not found', status=404)
        except Exception:
            return HttpResponse('Internal Error', status=500)
    return redirect(req.META.get('HTTP_REFERER', '/'))


# ------------------------------------------------------classrooms CRUD--------------------------------------------------------


def classroom(req, pk):
    curr_obj = get_object_or_404(Classroom, id=pk)
    rel_classrooms = Classroom.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "rel_classrooms_page": "active",
        'title': 'classroom',
        'curr_obj': curr_obj,
        'rel_classrooms': rel_classrooms,
    }
    return render(req, 'schools/classroom.html', context)


@login_required(login_url='login')
def create_classroom(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = ClassroomForm()
    if req.method == 'POST':
        form = ClassroomForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/classroom/{id}'.format(id=instance.id))
    context = {
        "classroom_create_page": "active", "title": 'add classroom', "user": user, "form": form}
    return render(req, 'schools/classroom.html', context)


@login_required(login_url='login')
def edit_classroom(req, pk):
    user = req.user
    curr_obj = get_object_or_404(Classroom, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = ClassroomForm(instance=curr_obj)
    if req.method == 'POST':
        form = ClassroomForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/classroom/{id}'.format(id=pk))
    context = {
        "classroom_edit_page": "active", "title": 'add classroom', "user": user, "form": form}
    return render(req, 'schools/classroom.html', context)


@login_required(login_url='login')
def delete_classroom(req, pk):
    obj = get_object_or_404(Classroom, id=pk)
    if req.user.is_superadmin:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# ------------------------------------------------------teachers CRUD--------------------------------------------------------


def teacher(req, pk):
    curr_obj = get_object_or_404(Teacher, id=pk)
    rel_teachers = Teacher.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "teacher_page": "active",
        'title': 'teacher',
        'curr_obj': curr_obj,
        'rel_teachers': rel_teachers,
    }
    return render(req, 'schools/teacher.html', context)


@login_required(login_url='login')
def create_teacher(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = TeacherForm()
    if req.method == 'POST':
        form = TeacherForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/teacher/{id}'.format(id=instance.id))
    context = {
        "teacher_create_page": "active", "title": 'add teacher', "user": user, "form": form}
    return render(req, 'schools/teacher.html', context)


@login_required(login_url='login')
def edit_teacher(req, pk):
    user = req.user
    curr_obj = get_object_or_404(Teacher, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = TeacherForm(instance=curr_obj)
    if req.method == 'POST':
        form = TeacherForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/teacher/{id}'.format(id=pk))
    context = {
        "teacher_edit_page": "active", "title": 'edit teacher', "user": user, "form": form}
    return render(req, 'schools/teacher.html', context)


@login_required(login_url='login')
def delete_teacher(req, pk):
    obj = get_object_or_404(Teacher, id=pk)
    if req.user.is_superadmin:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# ------------------------------------------------------structures CRUD--------------------------------------------------------

def structure(req, pk):
    curr_obj = get_object_or_404(Structure, id=pk)
    rel_structures = Structure.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "rel_structures_page": "active",
        'title': 'Structure',
        'curr_obj': curr_obj,
        'rel_structures': rel_structures,
    }
    return render(req, 'schools/structure.html', context)


@login_required(login_url='login')
def create_structure(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = StructureForm()
    if req.method == 'POST':
        form = StructureForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/structure/{id}'.format(id=instance.id))
    context = {
        "structure_create_page": "active", "title": 'add structure', "user": user, "form": form}
    return render(req, 'schools/structure.html', context)


@login_required(login_url='login')
def edit_structure(req, pk):
    user = req.user
    curr_obj = get_object_or_404(Structure, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = StructureForm(instance=curr_obj)
    if req.method == 'POST':
        form = StructureForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/structure/{id}'.format(id=pk))
    context = {
        "structure_edit_page": "active", "title": 'edit structure', "user": user, "form": form}
    return render(req, 'schools/structure.html', context)


@login_required(login_url='login')
def delete_structure(req, pk):
    obj = get_object_or_404(Structure, id=pk)
    if req.user.is_superadmin:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# ------------------------------------------------------articles CRUD--------------------------------------------------------

def article(req, pk):
    curr_obj = get_object_or_404(SchoolArticle, id=pk)
    rel_articles = SchoolArticle.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "rel_articles_page": "active",
        'title': 'article',
        'curr_obj': curr_obj,
        'rel_articles': rel_articles,
    }
    return render(req, 'schools/article.html', context)


@login_required(login_url='login')
def create_article(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = ArticleForm()
    if req.method == 'POST':
        form = ArticleForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/article/{id}'.format(id=instance.id))
    context = {
        "article_create_page": "active", "title": 'add article', "user": user, "form": form}
    return render(req, 'schools/article.html', context)


@login_required(login_url='login')
def edit_article(req, pk):
    user = req.user
    curr_obj = get_object_or_404(SchoolArticle, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = ArticleForm(instance=curr_obj)
    if req.method == 'POST':
        form = ArticleForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/article/{id}'.format(id=pk))
    context = {
        "article_edit_page": "active", "title": 'edit article', "user": user, "form": form}
    return render(req, 'schools/article.html', context)


@login_required(login_url='login')
def delete_article(req, pk):
    obj = get_object_or_404(SchoolArticle, id=pk)
    if req.user.is_superadmin:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# ------------------------------------------------------galleries CRUD--------------------------------------------------------


def gallery(req, pk):
    curr_obj = get_object_or_404(Gallery, id=pk)
    rel_galleries = Gallery.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "rel_galleries_page": "active",
        'title': 'Gallery',
        'curr_obj': curr_obj,
        'rel_galleries': rel_galleries,
    }
    return render(req, 'schools/gallery.html', context)


@login_required(login_url='login')
def create_gallery(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = GalleryForm()
    if req.method == 'POST':
        form = GalleryForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/gallery/{id}'.format(id=instance.id))
    context = {
        "Gallery_create_page": "active", "title": 'add gallery', "user": user, "form": form}
    return render(req, 'schools/gallery.html', context)


@login_required(login_url='login')
def edit_gallery(req, pk):
    user = req.user
    curr_obj = get_object_or_404(Gallery, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = GalleryForm(instance=curr_obj)
    if req.method == 'POST':
        form = GalleryForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/gallery/{id}'.format(id=pk))
    context = {
        "Gallery_edit_page": "active", "title": 'edit gallery', "user": user, "form": form}
    return render(req, 'schools/gallery.html', context)


@login_required(login_url='login')
def delete_gallery(req, pk):
    user = req.user
    obj = get_object_or_404(Gallery, id=pk)
    if obj.school.manager != user and user.is_staff == False:
        return redirect(req.META.get('HTTP_REFERER', '/'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))


# ------------------------------------------------------performances CRUD--------------------------------------------------------


def performance(req, pk):
    curr_obj = get_object_or_404(Performance, id=pk)
    rel_performances = Performance.objects.filter(
        school=curr_obj.school).exclude(id=pk)
    context = {
        "rel_performances_page": "active",
        'title': 'Performance',
        'curr_obj': curr_obj,
        'rel_performances': rel_performances,
    }
    return render(req, 'schools/performance.html', context)


@login_required(login_url='login')
def create_performance(req):
    user = req.user
    school = School.objects.get(manager=user)
    if not school:
        return redirect('create_school')

    form = PerformanceForm()
    if req.method == 'POST':
        form = PerformanceForm(req.POST, req.FILES)
        form.instance.school = school
        if form.is_valid():
            instance = form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/performance/{id}'.format(id=instance.id))
    context = {
        "Performance_create_page": "active", "title": 'add performance', "user": user, "form": form}
    return render(req, 'schools/performance.html', context)


@login_required(login_url='login')
def edit_performance(req, pk):
    user = req.user
    curr_obj = get_object_or_404(Performance, id=pk)
    if curr_obj.school.manager != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = PerformanceForm(instance=curr_obj)
    if req.method == 'POST':
        form = PerformanceForm(req.POST, req.FILES, instance=curr_obj)
        if form.is_valid():

            form = form.save(commit=True)
            form.save()
            messages.success(req, "Success")
            return HttpResponseRedirect('/schools/performance/{id}'.format(id=pk))
    context = {
        "Performance_edit_page": "active", "title": 'edit performance', "user": user, "form": form}
    return render(req, 'schools/performance.html', context)


@login_required(login_url='login')
def delete_performance(req, pk):
    obj = get_object_or_404(Performance, id=pk)
    if req.user.is_superadmin:
        return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
    obj.delete()
    return HttpResponseRedirect(req.META.get('HTTP_REFERER'))
