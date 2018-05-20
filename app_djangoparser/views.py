from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import re
import string
import operator

def index_page(request):
    if request.method == 'POST':
        f = request.FILES['sentFile']

        with open(f.name, 'w'):
            file_content = f.read().decode('latin-1')

        file_content = "<pre class='content-file'>" + file_content + "</pre><br><br>"

        # Character count
        alphabet_count = { i: file_content.count(i) for i in list(string.ascii_lowercase) }
        sorted_alphabet_count = sorted(alphabet_count.items(), key=operator.itemgetter(1))
        character_count = "<b>CHARACTERS</b><br>"
        for i in sorted_alphabet_count[::-1]:
            character_count += f"{i[0]}: {i[1]}<br>"

        new = re.sub('[\w]+' ,'', file_content)
        character_count += f"<br><b>Special Characters</b>: {len(new)}"

        return render(request, "index.html", { 
            'file_name': f.name, 
            'file_content': file_content,
            'character_count': character_count
        })
    else:
        return render(request, "index.html")