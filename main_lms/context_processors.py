from main_lms.models import *
from django.contrib.admin.models import LogEntry
from django.db import connection

def hcolor(request):
    hcolor=HeaderColor.objects.all()[:1].get()
    return {'hcolor':hcolor}

def numbercount(request):
    logCount = LogEntry.objects.exclude(change_message="No fields changed.").order_by('-action_time')[:20].count()
    bcount = BooksInsert.objects.count()
    scount = StuInsert.objects.count()
    #b=BooksInsert.objects.only('btype')
    #row=StuInsert.objects.raw('SELECT id FROM BooksInsert')
    cursor = connection.cursor()    
    cursor.execute("select * from StuInsert s inner join BooksInsert b on s.sdept=b.btype ")
    results = cursor.fetchall()

    x = cursor.description
    resultsList = []   
    for r in results:
        i = 0
        d = {}
        while i < len(x):
            d[x[i][0]] = r[i]
            i = i+1
        resultsList.append(d)
    args = {'logCount':logCount, 'bcount': bcount, 'scount': scount, "results":resultsList}
    return args



#amazing, the cursor is worked





'''This worked. Converts the tuple of tuples into a list of dictionaries and gets the field description from cursor.description. Could be made as a little function. And there's probably some smart lamdba thing that could make it shorter.
       
from django.db import connection

       
        my_select="select * from StuInsert s inner join BooksInsert b on s.sdept=b.btype "
        cursor = connection.cursor()
        cursor.execute(my_select)
        results = cursor.fetchall()

        x = cursor.description
        resultsList = []   
        for r in results:
            i = 0
            d = {}
            while i < len(x):
                d[x[i][0]] = r[i]
                i = i+1
            resultsList.append(d)

        return render_to_response(my_template, {"results":resultsList})
        
in django templates

{% for r in results %}
<p style="color: darkblue;">{{r.btype}}</p>
{% endfor %} 

'''