from django.contrib import messages
from django.http import HttpResponseRedirect
from base.models import *
from schools.models import *
from schools.models import *
from schools.forms import *
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(req):
    has_school = False
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    if user.is_authenticated:
        school = School.objects.filter(manager=user)
        if school:
            has_school = True

    schools = School.objects.all()
    sch_count = School.objects.all().count()
    verified_sch_count = School.objects.filter(is_verified=True).count()
    unverified_sch_count = School.objects.filter(is_verified=False).count()
    # ----------------------------------------------------
    tutors = Tutor.objects.all()
    tut_count = Tutor.objects.all().count()
    verified_tut_count = Tutor.objects.filter(is_verified=True).count()
    unverified_tut_count = Tutor.objects.filter(is_verified=False).count()
    # ----------------------------------------------------
    # ----
    free_sch_subs = Subscription.objects.filter(
        plan__in=Plan.objects.filter(type='school'), plan=0).count()
    pro_sch_subs = Subscription.objects.filter(plan=2).count()
    vip_sch_subs = Subscription.objects.filter(plan=3).count()
    # ----
    free_tut_subs = Subscription.objects.filter(
        plan__in=Plan.objects.filter(type='tutor'), plan=0).count()
    pro_tut_subs = Subscription.objects.filter(plan=4).count()
    vip_tut_subs = Subscription.objects.filter(plan=5).count()
    # people
    levels = EducationLevel.objects.all()

    context = {
        "dashboard_page": "active",
        'title': 'dashboard',
        #
        'schools': schools,
        'sch_count': sch_count,
        'verified_sch_count': verified_sch_count,
        'unverified_sch_count': unverified_sch_count,
        'free_sch_subs': free_sch_subs,
        'pro_sch_subs': pro_sch_subs,
        'vip_sch_subs': vip_sch_subs,
        #
        'tutors': tutors,
        'tut_count': tut_count,
        'verified_tut_count': verified_tut_count,
        'unverified_tut_count': unverified_tut_count,
        'free_tut_subs': free_tut_subs,
        'pro_tut_subs': pro_tut_subs,
        'vip_tut_subs': vip_tut_subs,
        #
        'has_school': has_school,
        'levels': levels,
    }
    return render(req, 'dashboard/index.html', context)


def dash_schools(req):
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query)
        | Q(address__icontains=query)
        | Q(moto__icontains=query)
        | Q(tel__icontains=query)
        | Q(levels__name__icontains=query),
    ).distinct()

    levels = EducationLevel.objects.all()
    ordering = ['is_featured == True']
    context = {
        "dash_sch_page": "active",
        'title': 'schools',
        'schools': schools,
        'levels': levels,
        'ordering': ordering,
    }
    return render(req, 'dashboard/schools.html', context)


def dash_tutors(req):
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    tutors = Tutor.objects.filter(
        Q(subjects__name__icontains=query)
        | Q(levels__name__icontains=query)
        | Q(user__first_name__icontains=query)
        | Q(user__last_name__icontains=query)
    ).distinct()
    subjects = Subject.objects.all().order_by('name')

    context = {
        "dash_tutors_page": "active",
        'title': 'tutors',
        'tutors': tutors,
        'subjects': subjects,
    }
    return render(req, 'dashboard/tutors.html', context)


def dash_forum(req):
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    query = req.GET.get('query') if req.GET.get('query') != None else ''
    articles = ForumArticle.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
    ).order_by('date')

    subjects = Subject.objects.all().order_by('name')
    context = {
        "dash_forum_page": "active",
        'title': 'Dashboard Forum',
        'articles': articles,
        "subjects": subjects,
    }
    return render(req, 'dashboard/forum.html', context)
