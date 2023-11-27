from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from flask import Flask, render_template, request, Response, redirect,url_for
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template.loader import render_to_string
from django.urls import reverse
from datetime import datetime

from events.eventresource import eventresource
from events.database_initializer import initialize_database
from events.serializers_event import eventserializer

app = Flask(__name__)

db = initialize_database()

#flask
@app.route("/",methods=["GET"])
def list(request):
    events = eventresource.getlist_all(db)
    # user = 'user should be deliver from api.'
    return render(request,'list.html', {'events': events})

#django api
@api_view(['GET','POST'])
def create(request):
    if request.method == "POST":
        data=request.data
        print(data)
        date = datetime.strptime(data['e_date'], '%Y-%m-%d').date()
        """
        cat_mapping = {
            1: "Career",
            2: "Social",
            3: "Sport",
            4: "Panel",
        }
        cat = cat_mapping.get(data['cat_category'], "Career")
        """


        event_id = eventresource.create(event_title=data[ 'event_title'],
                                        date=date,
                                        capacity=data['capacity'],
                                        holder_id=data['holder_id'],
                                        e_detail=data['e_detail'],
                                        cat=data['cat_category'],
                                        db =db)
        print(event_id)

        return HttpResponseRedirect(reverse("home"))
    rendered = render_to_string('form_create.html', {'action': 'Create'})

    return HttpResponse(rendered)


@app.route("/",methods=["GET"])
def view(request, event_id):
    event = eventresource.get_event(event_id= event_id,db= db)
    #rendered = render_to_string('view.html', {'Event': event})
    # user = 'user should be deliver from api.'
    if event.e_complete == True:
        Complete = 'YES'
    else:
        Complete = 'No...'
    return render(request,'view.html', {'event': event,'Complete':Complete })
#put is not working
@api_view(['GET','POST','PUT'])
def edit_event(request,event_id):
    if request.method == 'GET':
        event = eventresource.get_event(event_id= event_id,db= db)
        e_date = event.e_date.strftime('%Y-%m-%d')
        return render(request, 'form.html', {'action': 'Edit','event': event,'e_date':e_date})
    elif request.method == 'POST':
        data = request.data
        print(data)
        date = datetime.strptime(data['e_date'], '%Y-%m-%d').date()
        """
        cat_mapping = {
            1: "Career",
            2: "Social",
            3: "Sport",
            4: "Panel",
        }
        cat = cat_mapping.get(data['cat_category'], "Career")
        """
        if 'state' in data:
            complete = True
        else:
            complete =False
        event = eventresource.edit_event(event_id = event_id,
                                        event_title=data[ 'event_title'],
                                        date=date,
                                        capacity=data['capacity'],
                                        holder_id=data['holder_id'],
                                        e_detail=data['e_detail'],
                                        cat=data['cat_category'],
                                        e_complete=complete,
                                        db =db)
        return HttpResponseRedirect(reverse("home"))
    elif request.method == 'PUT':
        data = request.data
        print(data)
        date = datetime.strptime(data['e_date'], '%Y-%m-%d').date()
        """
        cat_mapping = {
            1: "Career",
            2: "Social",
            3: "Sport",
            4: "Panel",
        }
        cat = cat_mapping.get(data['cat_category'], "Career")
        """
        if 'e_complete' in data:
            complete = True
        else:
            complete = False
        event = eventresource.edit_event(event_id = event_id,
                                        event_title=data[ 'event_title'],
                                        date=date,
                                        capacity=data['capacity'],
                                        holder_id=data['holder_id'],
                                        e_detail=data['e_detail'],
                                        cat=data['cat_category'],
                                        e_complete=complete,
                                        db =db)
        return HttpResponseRedirect(reverse("home"))



@api_view(['DELETE'])
def delete(request,event_id):
    eventresource.delete_event(event_id=event_id, db=db)

    return Response({"message": f"Event with ID {event_id} deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



