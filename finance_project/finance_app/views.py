from django.shortcuts import render, redirect
from .models import Income, Expense
from .forms import IncomeForm, ExpenseForm

def home(request):
    return render(request, 'finance_app/home.html')

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'finance_app/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'finance_app/add_expense.html', {'form': form})

def view_history(request):
    incomes = Income.objects.all().order_by('-date')
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'finance_app/view_history.html', {
        'incomes': incomes,
        'expenses': expenses,
    })
