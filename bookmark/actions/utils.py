from django.contrib.contenttypes.models import ContentType

from .models import Action


def create_action(user, verb, target=None):
    """
    A shourcut function that will allow you to create ew Action objects in a simple way
    This function allows you to create actions that optionally include a target object.
    You can use this function anywhere in your code as a shortcut to add new actions to
        the activity stream.
    """
    action = Action(user=user, verb=verb, target=target)
    action.save()
