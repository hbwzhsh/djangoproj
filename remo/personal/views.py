# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
import pandas as pd
import os
from pandas_highcharts.core import serialize

# Create your views here.

def index(request):
	return render(request, 'personal/home.html')

def bmobr06(request):
	return render(request, 'personal/bmobr06.html')

def data(request):
	return render(request, 'personal/data.html')

def waves(request):
	# '/Dropbox/projects/BMOP/Sistemas-BMOP/Processamento/dados/BMOBR06_CF2/op/'
	pathname = os.environ['HOME'] + \
	'/Downloads/'
	
	dd = pd.read_csv(pathname + 'Dados_BMOBR06.csv', index_col='date', parse_dates=True)

	# dd = dd.ix[-14*24:,:] # dd = dd['2016-06-24':]

	dd['Hs'] = dd.hs
	dd['Tp'] = dd.tp
	dd['Dp'] = dd.dp
	
	
	args = {
			'kind': 'line',
			'zoom': 'xy',
			'grid': 'on',
			'output_type': 'json'
			}

	param = {'Hs': ['my-chart1', 'Altura Significativa - Hs'],
			 'Tp': ['my-chart2', 'Período de Pico - Tp'],
			 'Dp': ['my-chart3', 'Direção de Pico - Dp']
			 }

	chart = {}

	for p in param:

		chart[p] = serialize(dd[[p]], render_to=param[p][0],
								      title=param[p][1],
								      kind=args['kind'],
								      zoom=args['zoom'],
								      grid=args['grid'],
								      output_type=args['output_type'],
								      yAxis_title=p
								      )
		print p

	# return render(request, 'personal/waves.html')
	# return render_to_response('personal/waves.html', {'chart': chart})
	return render_to_response('personal/waves.html', chart)

def contact(request):
	return render(request, 'personal/contact.html')
