from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, CourseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Course, Subscription
from django.contrib import messages


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


def students_courses(request):
    courses = Course.objects.filter(category='students')
    return render(request, 'main/students_courses.html', {'courses': courses})


def ege_courses(request):
    courses = Course.objects.filter(category='ege')
    return render(request, 'main/ege_courses.html', {'courses': courses})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.can_edit_courses:
                    return redirect('course_edit')
                else:
                    return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def index(request):
    return render(request, 'main/main.html')


def about(request):
    return render(request, 'main/about.html')



def course_edit(request, course_id=None):
    # Проверяем, является ли пользователь аутентифицированным и имеет права на редактирование курсов
    if request.user.is_authenticated and request.user.can_edit_courses:
        courses = Course.objects.all()  # Получаем все курсы
        if course_id is not None:
            # Редактирование существующего курса
            course = get_object_or_404(Course, id=course_id)
        else:
            # Добавление нового курса
            course = None

        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('home')  # Или другую страницу после успешного сохранения
        else:
            form = CourseForm(instance=course)

        return render(request, 'main/course_edit.html', {'form': form, 'course_id': course_id, 'courses': courses})
    else:
        return redirect('home')  # Или обработайте ошибку соответствующим образом


def course_delete(request, course_id):
    if request.user.is_authenticated and request.user.can_edit_courses:
        course = get_object_or_404(Course, id=course_id)
        course.delete()
        return redirect('home')  # Или другую страницу после успешного удаления
    else:
        return redirect('home')  # Или обработайте ошибку соответствующим образом


def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_edit')
    else:
        form = CourseForm()

    return render(request, 'main/course_add.html', {'form': form})


def course_subscription(request, course_id):
    if request.method == 'POST':
        course = Course.objects.get(id=course_id)
        # Проверяем, что пользователь аутентифицирован
        if request.user.is_authenticated:
            # Создаем объект Subscription и связываем его с текущим пользователем и курсом
            subscription, created = Subscription.objects.get_or_create(user=request.user, course=course)
            if created:
                # Курс успешно добавлен
                messages.success(request, 'Course successfully added to your courses.')
                return render(request, 'main/student_courses', {'course': course})
            else:
                # Пользователь уже имеет этот курс в своих курсах
                messages.info(request, 'You already have this course in your courses.')
                return render(request, 'main/student_courses', {'course': course})


@login_required
def my_courses(request):
    user = request.user
    courses = user.subscriptions.all()
    return render(request, 'main/my_courses.html', {'courses': courses})