from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum, Count
from .models import User, Record, Curriculum, Invoice, Report
from .forms import UserForm, RecordForm


def home(request):
    return render(request, 'management/home.html')

def users_index(request):
    users = User.objects.all()
    return render(request, 'management/user_index.html', {'users': users})

def user_edit(request, user_id=None):
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = User()
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('management:user_index')
    else:
        form = UserForm(instance=user)
    return render(request, 'management/user_edit.html', dict(form=form, user_id=user_id))


def record_index(request):
    records = Record.objects.all()
    return render(request, 'management/record_index.html', {'records': records})

def record_edit(request, record_id=None):
    if record_id:
        record = get_object_or_404(Record, pk=record_id)
    else:
        record = Record()
    
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            record = form.save(commit=False)
            if record.curriculum.name == 'プログラミング' and record.time > 5 :
                record.charge = record.curriculum.metered_charge * record.time + record.curriculum.basic_charge - 5 * record.curriculum.metered_charge
                record.save()
                return redirect('management:record_index')
            elif record.curriculum.name == 'プログラミング' and record.time <= 5 :
                record.charge = record.curriculum.basic_charge
                record.save()
                return redirect('management:record_index')
            else:
                record.charge = record.curriculum.metered_charge * record.time + record.curriculum.basic_charge
                record.save()
                return redirect('management:record_index')
    else:
        form = RecordForm(instance=record)
    return render(request, 'management/record_edit.html', dict(form=form, record_id=record_id))



def invoices_index(request):
    invoices = [ Invoice(user) for user in User.objects.all() ]
    return render(request, 'management/invoice_index.html', {'invoices': invoices })

def reports_index(request):
    report_by_gender = []
    for curriculum in Curriculum.objects.all():
        for i in [1,2]:
            report_object = Report(
                curriculum__id     = curriculum.id,
                user__gender          = i,
            )
            report_by_gender.append({
                'curriculum_name' : curriculum.name,
                'user_gender'        : i,
                'records_count'   : report_object.records_count,
                'users_count'     : report_object.users_count,
                'sum_charge'      : report_object.sum_charge
            })

    report_by_generation = []
    for curriculum in Curriculum.objects.all():
        for i in [1,2]:
            for generation in range(10,90,10):
                report_object = Report(
                    curriculum__id     = curriculum.id,
                    user__gender          = i,
                    user__age__range   = (generation, generation + 9),
                )
                report_by_generation.append({
                    'curriculum_name' : curriculum.name,
                    'user_gender'        : i,
                    'user_generation' : generation,
                    'records_count'   : report_object.records_count,
                    'users_count'     : report_object.users_count,
                    'sum_charge'      : report_object.sum_charge
                })
    return render(request, 'management/report_index.html',
                  { 'report_by_gender'       : report_by_gender,
                    'report_by_generation': report_by_generation })

