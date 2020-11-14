from django.shortcuts import render, redirect
from .models import Frequencies, Proffessions
import json
import os, sys
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView


def add_freqs(request):
    Frequencies.objects.all().delete()
    with open(os.path.join(settings.BASE_DIR, "apps", "freqs_predict", "data", "predicted_freqs.json"), "r", encoding='utf-8') as read_file:
         data = json.load(read_file)

    for item in data:
        date = item['date']
        date_arr = date.split('-')
        date_arr.reverse()
        date = '-'.join(date_arr)
        item = Frequencies(name = item['name'], count = item['count'], date = date, coeff = '-')
        item.save()

    return redirect('home')

def change_model(request):
    if request.method == "POST":
        months = request.POST.get('months')
        r_type = request.POST.get('r_type')
        epsilon = request.POST.get('epsilon')
        C_param = request.POST.get('C_param')

        m_settings = {
            "months_count": int(months),
            "kernel": r_type,
            "C": int(C_param),
            "epsilon": float(epsilon.replace(',','.'))
        }

        with open(os.path.join(settings.BASE_DIR, "apps", "freqs_predict", "settings.json"), "w", encoding='utf-8') as write_file:
            json.dump(m_settings, write_file, indent=4, ensure_ascii=False)


        exec(open(os.path.join(settings.BASE_DIR, "apps", "freqs_predict", "main.py")).read(), globals(), globals())

        return redirect('add_freqs')

    else:
        with open(os.path.join(settings.BASE_DIR, "apps", "freqs_predict", "settings.json"), "r", encoding='utf-8') as read_file:
            m_settings = json.load(read_file)

        return render(
            request,
            'main/change_model.html',
            context = {'settings': m_settings}
        )

class GetFreqsView(APIView):
    def get(self, request):
        freqs = [{'name': x.name, 'count': x.count, 'date': x.date, 'coeff': x.coeff} for x in Frequencies.objects.all()]
        return Response(freqs)


class GetProfessionsView(APIView):
    def get(self, request):
        profs = [{'id': x.id, 'rating': x.rating_position ,'name': x.name, 'frequencies_count': x.frequencies_count, 'change': x.change, 'coeff': x.coeff} for x in Proffessions.objects.extra(
            select={'rating_position_int': 'CAST(rating_position AS INTEGER)'}
        ).order_by('rating_position_int')]
        return Response(profs)