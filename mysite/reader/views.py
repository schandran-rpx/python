# reader/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import KTRFileForm
from .models import KTRFile
import xml.etree.ElementTree as ET

def upload_file(request):
    if request.method == 'POST':
        form = KTRFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ktr_reader:diagram', pk=form.instance.pk)
    else:
        form = KTRFileForm()
    return render(request, 'reader/upload.html', {'form': form})

def show_file(request, pk):
    ktr_file = KTRFile.objects.get(pk=pk)
    tree = ET.parse(ktr_file.file)
    root = tree.getroot()

    steps = []
    for step in root.findall(".//step"):
        step_info = {
            'name': step.find('name').text,
            'type': step.find('type').text,
            'description': step.find('description').text if step.find('description') is not None else ''
        }
        steps.append(step_info)

    hops = []
    for hop in root.findall(".//hop"):
        hop_info = {
            'from': hop.find('from').text,
            'to': hop.find('to').text,
            'enabled': hop.find('enabled').text if hop.find('enabled') is not None else ''
        }
        hops.append(hop_info)

    data = {
        'steps': steps,
        'hops': hops
    }

    return JsonResponse(data)

def diagram(request, pk):
    return render(request, 'reader/diagram.html', {'pk': pk})
