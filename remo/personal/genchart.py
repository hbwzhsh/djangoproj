'''
Generate 'chart' variable to
plot using pandas_highcharts 

Install
pip install pandas-highcharts


Ex.1

Import it in your views

import pandas_highcharts
df = ... # create your dataframe here
chart = pandas_highcharts.serialize(df, render_to='my-chart', output_type='json')

In your templates

<div id="my-chart"></div>
<script type="text/javascript">
  new Highcharts.Chart({{chart|safe}});
</script>

Ex.2

import pandas as pd
import datetime
import os
import numpy as np
from pandas.compat import StringIO
from pandas.io.common import urlopen
from IPython.display import display, display_pretty, Javascript, HTML
from pandas_highcharts.core import serialize
from pandas_highcharts.display import display_charts
import matplotlib.pyplot as plt

# Data retrieved from http://www.quandl.com/api/v1/datasets/ODA/DEU_PCPIPCH.csv?column=1
data = """Date,Value\n2019-12-31,1.7\n2018-12-31,1.7\n2017-12-31,1.7\n2016-12-31,1.5\n2015-12-31,1.247\n2014-12-31,0.896\n2013-12-31,1.601\n2012-12-31,2.13\n2011-12-31,2.498\n2010-12-31,1.158\n2009-12-31,0.226\n2008-12-31,2.738\n2007-12-31,2.285\n2006-12-31,1.784\n2005-12-31,1.92\n2004-12-31,1.799\n2003-12-31,1.022\n2002-12-31,1.346\n2001-12-31,1.904\n2000-12-31,1.418\n1999-12-31,0.626\n1998-12-31,0.593\n1997-12-31,1.542\n1996-12-31,1.19\n1995-12-31,1.733\n1994-12-31,2.717\n1993-12-31,4.476\n1992-12-31,5.046\n1991-12-31,3.474\n1990-12-31,2.687\n1989-12-31,2.778\n1988-12-31,1.274\n1987-12-31,0.242\n1986-12-31,-0.125\n1985-12-31,2.084\n1984-12-31,2.396\n1983-12-31,3.284\n1982-12-31,5.256\n1981-12-31,6.324\n1980-12-31,5.447\n"""
df = pd.read_csv(StringIO(data), index_col=0, parse_dates=True)
df = df.sort_index()

'''

#BMOBR-06
#%load_ext autoreload
#%autoreload 2

import pandas as pd
import datetime
import os
import numpy as np
from pandas.compat import StringIO
from pandas.io.common import urlopen
from IPython.display import display, display_pretty, Javascript, HTML
from pandas_highcharts.core import serialize
from pandas_highcharts.display import display_charts
import matplotlib.pyplot as plt

# Data retrieved from http://www.quandl.com/api/v1/datasets/ODA/DEU_PCPIPCH.csv?column=1
# data = """Date,Value\n2019-12-31,1.7\n2018-12-31,1.7\n2017-12-31,1.7\n2016-12-31,1.5\n2015-12-31,1.247\n2014-12-31,0.896\n2013-12-31,1.601\n2012-12-31,2.13\n2011-12-31,2.498\n2010-12-31,1.158\n2009-12-31,0.226\n2008-12-31,2.738\n2007-12-31,2.285\n2006-12-31,1.784\n2005-12-31,1.92\n2004-12-31,1.799\n2003-12-31,1.022\n2002-12-31,1.346\n2001-12-31,1.904\n2000-12-31,1.418\n1999-12-31,0.626\n1998-12-31,0.593\n1997-12-31,1.542\n1996-12-31,1.19\n1995-12-31,1.733\n1994-12-31,2.717\n1993-12-31,4.476\n1992-12-31,5.046\n1991-12-31,3.474\n1990-12-31,2.687\n1989-12-31,2.778\n1988-12-31,1.274\n1987-12-31,0.242\n1986-12-31,-0.125\n1985-12-31,2.084\n1984-12-31,2.396\n1983-12-31,3.284\n1982-12-31,5.256\n1981-12-31,6.324\n1980-12-31,5.447\n"""
# df = pd.read_csv(StringIO(data), index_col=0, parse_dates=True)
# df = df.sort_index()


def bmobr06(param):
	'''
	param = 'hs', 'tp', ..
	int = interval. Ex: 
	'''

	pathname = os.environ['HOME'] + '/Dropbox/projects/BMOP/Sistemas-BMOP/Processamento/dados/BMOBR06_CF2/op/'

	dd = pd.read_csv(pathname + 'Dados_BMOBR06.csv', index_col='date', parse_dates=True)

	#pega dados quando a boia foi para agua
	dd = dd['2016-06-24':]

	#generate json
	chart = pandas_highcharts.serialize(dd[[param]], render_to='my-chart', output_type='json')

	return chart