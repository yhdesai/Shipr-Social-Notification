import pyrebase
from pyfcm import FCMNotification
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

config = {
    'apiKey': "AIzaSyBzQOeUPqyM8DENLY-hAVAOtVWcH3AVnCc",
    'authDomain': "mtnotification-4f3f1.firebaseapp.com",
    'databaseURL': "https://mtnotification-4f3f1.firebaseio.com",
    'projectId': "mtnotification-4f3f1",
    'storageBucket': "mtnotification-4f3f1.appspot.com",
    'messagingSenderId': "1069791168310",
    'serviceAccount': './Static/mtnotification-4f3f1-firebase-adminsdk-4say5-61aaebd488.json',
}

firebase = pyrebase.initialize_app(config)
username = 'parthav46@gmail.com'
password = 'djangoserver'

auth = firebase.auth()
database = firebase.database()

server = FCMNotification('AAAA-RSFxzY:APA91bEPD2vOMqBX_PHAOiPHLF-Ns3zssEBskLmUy3f5aZZkheqP-QbZBksQ_27ze5q_oM0SxYB6rylaCFrCuNot-1ftv0xTy1Ypr-WpwdO8hjzKjlQU8SLGbdEU5p2qiYebYn44DIAd')

@csrf_exempt
def notify(request):
    auth.sign_in_with_email_and_password(username, password)
    topic = request.POST.get('channel', '')
    key = request.POST.get('key', '')
    if key == '' or topic == '':
        return render(request, 'blank.html')
    name = database.child('chat').child(topic).child(key).child('name').get().pyres
    text = database.child('chat').child(topic).child(key).child('text').get().pyres
    message = name + ": " + text
    status = server.notify_topic_subscribers(topic_name=topic, message_body=message, message_title=topic)
    return render(request, 'blank.html')
