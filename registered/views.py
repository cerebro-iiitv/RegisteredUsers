from django.shortcuts import render
from registered.parser import parse_json
from registered.write_to_sheet import write_sheet
from django.http import HttpResponse


def events(request):
    users_events = parse_json()
    context = {
                    'users_events': users_events,
    }
    return render(request=request, template_name='../templates/events.html', context=context)


def event_details(request, event_id):
    users_events = parse_json(event_id=event_id)
    print(users_events[0][1])
    context = {
            'name': users_events[0][0],
            'participants': users_events[0][1],
    }
    return render(request=request,
                  template_name='../templates/single_event.html',
                  context=context)

def create_sheet(request):
    users_events = parse_json()
    write_sheet(users_events)
    return HttpResponse('<h1>Sheet created</h1>')