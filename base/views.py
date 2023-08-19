from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from schools.models import *
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.


# @login_required(login_url='login')
def home(req):
    user = req.user
    levels = EducationLevel.objects.all()
    subjects = Subject.objects.all().order_by('name')
    tutors = Tutor.objects.all().order_by('user')
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    schools = School.objects.filter(
        Q(name__icontains=query)
        | Q(address__icontains=query)
        | Q(moto__icontains=query)
        | Q(tel__icontains=query)
        | Q(levels__name__icontains=query),
        is_featured=True,
        is_verified=True,
    ).distinct()

    # levels counter
    creche_count = School.objects.filter(levels=1, is_verified=True).count()
    kinder_count = School.objects.filter(levels=2, is_verified=True).count()
    prime_count = School.objects.filter(levels=3, is_verified=True).count()
    sec_count = School.objects.filter(levels=4, is_verified=True).count()
    uni_count = School.objects.filter(levels=5, is_verified=True).count()
    edu_count = School.objects.filter(levels=6, is_verified=True).count()
    pro_count = School.objects.filter(levels=7, is_verified=True).count()

    rec_posts = Blogpost.objects.all()[:4]
    rec_ads = Advert.objects.all()[:4]

    context = {
        "home_page": "active",
        'title': 'home',
        'schools': schools,
        'levels': levels,
        'subjects': subjects,
        'rec_posts': rec_posts,
        'rec_ads': rec_ads,
        'tutors': tutors,
        # --------------------------
        'creche_count': creche_count,
        'kinder_count': kinder_count,
        'prime_count': prime_count,
        'sec_count': sec_count,
        'uni_count': uni_count,
        'edu_count': edu_count,
        'pro_count': pro_count,

    }
    return render(req, 'base/index.html', context)

# --------------------------------------------------------------------blog CRUD--------------------------------------------------------


def blog(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    blogposts = Blogpost.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
    )

    context = {
        "blog_page": "active",
        'title': 'blog',
        'blogposts': blogposts,

    }
    return render(req, 'base/blog.html', context)


def blogpost(req, pk):
    curr_post = Blogpost.objects.get(id=pk)
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    blogposts = Blogpost.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
    ).exclude(id=curr_post.id)

    context = {
        "blogpost_page": "active",
        'title': 'blogpost',
        'curr_post': curr_post,
        'blogposts': blogposts,

    }
    return render(req, 'base/blogpost.html', context)


@login_required(login_url='login')
def create_blogpost(req):
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = BlogForm()
    if req.method == 'POST':
        form = BlogForm(req.POST)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {
        "create_blogpost_page": "active", "title": 'create_blogpost', "user": user, "form": form}
    return render(req, 'base/blogpost.html', context)


@login_required(login_url='login')
def edit_blogpost(req, pk):
    user = req.user
    if not user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    curr_post = Blogpost.objects.get(id=pk)
    form = BlogForm(instance=curr_post)

    if req.method == 'POST':
        form = BlogForm(req.POST, instance=curr_post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {
        "edit_blogpost_page": "active", "title": 'edit_blogpost', "user": user, "form": form, "curr_post": curr_post}
    return render(req, 'base/blogpost.html', context)


# --------------------------------------------------------------------adverts CRUD--------------------------------------------------------


def adverts(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    adverts = Advert.objects.filter(Q(title__icontains=query))
    offers = Advert.objects.filter(Q(title__icontains=query), type='offer')
    demands = Advert.objects.filter(Q(title__icontains=query), type='demand')

    context = {
        "adverts_page": "active",
        'title': 'home',
        'adverts': adverts,
        'offers': offers,
        'demands': demands,

    }
    return render(req, 'base/adverts.html', context)


def advert(req, pk):
    curr_ad = Advert.objects.get(id=pk)
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    adverts = Advert.objects.filter(
        Q(title__icontains=query)).exclude(id=curr_ad.id)

    context = {
        "advert_page": "active",
        'title': 'advert',
        'curr_ad': curr_ad,
        'adverts': adverts,

    }
    return render(req, 'base/advert.html', context)


@login_required(login_url='login')
def create_advert(req):
    user = req.user

    form = AdvertForm()
    if req.method == 'POST':
        form = AdvertForm(req.POST)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('adverts')
    context = {
        "create_advert_page": "active",
        "title": 'create_advert',
        "user": user,
        "form": form,
    }
    return render(req, 'base/advert.html', context)


@login_required(login_url='login')
def edit_advert(req, pk):
    user = req.user
    curr_ad = Advert.objects.get(id=pk)
    if curr_ad.author != user and user.is_staff:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = AdvertForm(instance=curr_ad)
    if req.method == 'POST':
        form = AdvertForm(req.POST, instance=curr_ad)
        if form.is_valid():
            form.save()
            return redirect('advert')
    context = {
        "edit_advert_page": "active", "title": 'edit_advert', "user": user, "form": form, "curr_ad": curr_ad}
    return render(req, 'base/advert.html', context)


# --------------------------------------------------------------------tutors CRUD--------------------------------------------------------


# @login_required(login_url='login')
def tutors(req):
    user = req.user
    is_tutor = False
    if user.is_authenticated:
        tut_check = Tutor.objects.filter(user=user)
        if tut_check:
            is_tutor = True
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    tutors = Tutor.objects.filter(
        Q(subjects__icontains=query)
        | Q(grades__icontains=query)
        # | Q(years_of_experience__icontains=query)
        | Q(user__first_name__icontains=query)
        | Q(user__last_name__icontains=query)
    )
    subjects = Subject.objects.all().order_by('name')
    # ordering = ['date_added']

    context = {
        "tutors_page": "active",
        'title': 'tutors',
        'tutors': tutors,
        'is_tutor': is_tutor,
        # 'ordering': ordering,
        'subjects': subjects,
    }
    return render(req, 'base/tutors.html', context)


def tutor(req, pk):
    curr_tut = Tutor.objects.get(id=pk)
    curr_user = curr_tut.user
    rel_articles = ForumArticle.objects.filter(author=curr_user)
    context = {
        "tutor_page": "active",
        'title': 'tutor',
        'curr_tut': curr_tut,
        'rel_articles': rel_articles,

    }
    return render(req, 'base/tutor.html', context)


@login_required(login_url='login')
def create_tutor(req):
    user = req.user
    # if user.role.sec_level != 2:
    #     return redirect(req.META.get('HTTP_REFERER', '/'))

    form = TutortForm()
    if req.method == 'POST':
        form = TutortForm(req.POST)
        form.instance.user = user
        if form.is_valid():
            form.save()
            return redirect('tutors')
    context = {
        "create_tutor_page": "active", "title": 'create_tutor', "user": user, "form": form}
    return render(req, 'base/tutor.html', context)


@login_required(login_url='login')
def edit_tutor(req, pk):
    user = req.user
    curr_tut = Tutor.objects.get(id=pk)
    if curr_tut.user != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = ForumArticleForm(instance=curr_tut)
    if req.method == 'POST':
        form = ForumArticleForm(req.POST, instance=curr_tut)
        if form.is_valid():
            form.save()
            return redirect('tutors')
    context = {
        "edit_tutor_page": "active", "title": 'edit_tutor', "user": user, "form": form, "curr_tut": curr_tut}
    return render(req, 'base/tutor.html', context)

# --------------------------------------------------------------------forum CRUD--------------------------------------------------------


def forum(req):
    query = req.GET.get('query') if req.GET.get('query') != None else ''
    articles = ForumArticle.objects.filter(
        Q(title__icontains=query)
        | Q(subtitle__icontains=query)
    ).order_by('date')

    subjects = Subject.objects.all().order_by('name')
    context = {
        "forum_page": "active",
        'title': 'Forum',
        'articles': articles,
        "subjects": subjects,
    }
    return render(req, 'base/forum.html', context)


def forum_article(req, pk):
    curr_article = ForumArticle.objects.get(id=pk)
    rel_articles = ForumArticle.objects.filter(
        author=curr_article.author).exclude(id=curr_article.id)
    context = {
        "forum_article_page": "active",
        'title': 'Forum article',
        'curr_article': curr_article,
        'rel_articles': rel_articles,
    }
    return render(req, 'base/forum_article.html', context)


@login_required(login_url='login')
def create_forum_article(req):
    user = req.user
    if user.role.sec_level < 2:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = ForumArticleForm()
    if req.method == 'POST':
        form = ForumArticleForm(req.POST)
        form.instance.author = user
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {
        "create_tutor_page": "active",
        "title": 'create_tutor',
        "user": user,
        "form": form
    }
    return render(req, 'base/forum_article.html', context)


@login_required(login_url='login')
def edit_forum_article(req, pk):
    user = req.user
    curr_tut = ForumArticle.objects.get(id=pk)
    if curr_tut.user != user:
        return redirect(req.META.get('HTTP_REFERER', '/'))

    form = ForumArticleForm(instance=curr_tut)
    if req.method == 'POST':
        form = ForumArticleForm(req.POST, instance=curr_tut)
        if form.is_valid():
            form.save()
            return redirect('forum')
    context = {
        "edit_tutor_page": "active",
        "title": 'edit_tutor',
        "user": user,
        "form": form,
        "curr_tut": curr_tut,
    }
    return render(req, 'base/forum_article.html', context)


def pricing(req):

    context = {
        "pricing_page": "active",
        "title": 'Pricing',
    }
    return render(req, 'base/pricing.html', context)


# -------------------------------------------------------- client links ------------------------------------------------

def about(req):
    context = {
        "about_page": "active",
        "title": 'about', }
    return render(req, 'client/about.html', context)


def accessibility(req):
    context = {
        "accessibility_page": "active",
        "title": 'accessibility', }
    return render(req, 'client/accessibility.html', context)


def contact(req):
    context = {
        "contact_page": "active",
        "title": 'contact', }
    return render(req, 'client/contact.html', context)


def faq(req):
    context = {
        "faq_page": "active",
        "title": 'faq'}
    return render(req, 'client/faq.html', context)


def customer_service(req):
    context = {
        "customer_service_page": "active",
        "title": 'customer_service'}
    return render(req, 'client/customer_service.html', context)


def help(req):
    context = {
        "notfoud_page": "active",
        "title": 'help', }
    return render(req, 'client/help.html', context)


def how_it_works(req):
    context = {
        "notfoud_page": "active",
        "title": 'how_it_works', }
    return render(req, 'client/how_it_works.html', context)


def info(req):
    context = {
        "notfoud_page": "active",
        "title": 'info', }
    return render(req, 'client/info.html', context)


def payments(req):
    context = {
        "copy_page": "active",
        "title": 'payments', }
    return render(req, 'client/payments.html', context)


def parameters_cookies(req):
    context = {
        "copy_page": "active",
        "title": 'parameters_cookies', }
    return render(req, 'client/parameters_cookies.html', context)


def policy_commercial(req):
    context = {
        "policy_commercial_page": "active",
        "title": 'policy_commercial', }
    return render(req, 'client/policy_commercial.html', context)


def policy_confidential(req):
    context = {
        "policy_confidential_page": "active",
        "title": 'policy_confidential', }
    return render(req, 'client/policy_confidential.html', context)


def policy_security(req):
    context = {
        "policy_security_page": "active",
        "title": 'policy_security', }
    return render(req, 'client/policy_security.html', context)


def terms_conditions(req):
    context = {
        "terms_conditions_page": "active",
        "title": 'terms_conditions', }
    return render(req, 'client/terms_conditions.html', context)


def sales_conditions(req):
    context = {
        "sales_conditions_page": "active",
        "title": 'sales_conditions', }
    return render(req, 'client/sales_conditions.html', context)
