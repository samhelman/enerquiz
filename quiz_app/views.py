from django.shortcuts import render, redirect
from .models import Result
import requests

def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'quiz_app/home.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'quiz_app/about.html', context)

def quiz(request):
    questions = requests.get('https://energuytrainingdb.herokuapp.com/get-10-questions').json()
    num = 1
    for question in questions:
        question['id'] = num
        num += 1

        if question['answer_1'][-6:] =='(True)':
            question['answer_1'] = question['answer_1'][:-6]
            question['correct_answer'] = question['answer_1']
        else:
            question['answer_1'] = question['answer_1'][:-7]

        if question['answer_2'][-6:] =='(True)':
            question['answer_2'] = question['answer_2'][:-6]
            question['correct_answer'] = question['answer_2']
        else:
            question['answer_2'] = question['answer_2'][:-7]

        if question['answer_3'][-6:] =='(True)':
            question['answer_3'] = question['answer_3'][:-6]
            question['correct_answer'] = question['answer_3']
        else:
            question['answer_3'] = question['answer_3'][:-7]

        if question['answer_4'][-6:] =='(True)':
            question['answer_4'] = question['answer_4'][:-6]
            question['correct_answer'] = question['answer_4']
        else:
            question['answer_4'] = question['answer_4'][:-7]
    context = {
        'title': 'Quiz',
        'questions': questions,
    }
    return render(request, 'quiz_app/quiz.html', context)

def results(request, score):
    past_results_query = Result.objects.all()
    Result(result=score).save()
    past_results = [result.result for result in past_results_query]
    num_of_past_results = len(past_results)
    past_results_less_than_score = [result for result in past_results if result < score]
    num_of_past_results_less_than_score = len(past_results_less_than_score)
    rank = int(((num_of_past_results - num_of_past_results_less_than_score) / num_of_past_results) * 100)
    results = {
        'score': score,
        'rank': rank,
    }
    context = {
        'title': 'Results',
        'results': results,
    }
    return render(request, 'quiz_app/results.html', context)
