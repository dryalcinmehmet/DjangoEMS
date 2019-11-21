from rest_framework import serializers, fields
from EventApp.models import Event, Session, User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username','password', 'email', 'is_staff')

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('name','start_date', 'end_date','speaker','event','session_id')


class EventSerializer(serializers.HyperlinkedModelSerializer):
    sessions = SessionSerializer(many=True,read_only=True)
    class Meta:
        model = Event
        fields = ('event_id','user', 'name','start_date', 'end_date','sessions')





