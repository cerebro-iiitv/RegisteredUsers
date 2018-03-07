from django.shortcuts import render


def events(request):
    '''
    users_events = fetch_json(id=None)
    '''

    context = {
        # 'users_events': users_events,
    }
    return render(request=request, template_name='../templates/home.html', context=context)


def event_details(request, event_id):
    '''
    users_events = fetch_json(id=event_id)
    '''
    context = {
        # 'users_events': users_events,
    }
    return render(request=request, template_name='../templates/single_event.html', context=context)