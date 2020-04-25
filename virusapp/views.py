from django.shortcuts import render
from django.http import HttpResponse
from keras.models import load_model
import numpy
import os
import h5py
import tensorflow as tf
from virusapp.models import Person
from keras.models import model_from_json

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    
    module_dir = os.path.dirname(__file__)  
    file_path = os.path.join(module_dir, 'model.h5')
    model_new = load_model(file_path)

    name = request.POST["name"]
    age_group = request.POST["age"]      #value for form_field
    sneezing = int(request.POST["Sneezing"])    #value for form_field
    run_nose = int(request.POST["nose"])    #value for form_field
    fatigue = int(request.POST["Fatigue"])    #value for form_field
    dry_cough = int(request.POST["dry"])    #value for form_field
    fever = int(request.POST["Fever"])    #value for form_field
    sour_throat = int(request.POST["throat"])    #value for form_field
    breathing = int(request.POST["breadth"])    #value for form_field
    cases_around = int(request.POST["case"])    #value for form_field
    sick_frequency = int(request.POST["freq"])    #value for form_field
    pneumonia = int(request.POST["Pneumonia"])    #value for form_field

    data_point = []
    if(age_group=='a'):
        data_point.extend([1,0,0])
    elif(age_group=='b'):
        data_point.extend([0,1,0])
    elif(age_group=='c'):
        data_point.extend([0,0,1])

    data_point.extend([sneezing, run_nose, fatigue, dry_cough, fever, sour_throat, breathing, cases_around, sick_frequency, pneumonia])


    Y_pred_test = model_new.predict(numpy.array(data_point).reshape(1,13))
    # Y_pred_test = pneumonia
    if(Y_pred_test>=0.5):
        detect = Person()
        detect.name = name
        detect.age = age_group
        detect.sneezing = sneezing
        detect.run_nose = run_nose
        detect.fatigue = fatigue
        detect.dry_cough = dry_cough
        detect.fever = fever
        detect.sour_throat = sour_throat
        detect.breathing = breathing
        detect.cases_around = cases_around
        detect.sick_frequency = sick_frequency
        detect.pneumonia = pneumonia
        detect.save()
        return render(request,'success.html')
    else:
        return render(request,'fail.html')


def detect(request):
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    # evaluate loaded model on test data
    loaded_model.compile(optimizer = "adam", loss='mean_squared_error', metrics=['accuracy'])