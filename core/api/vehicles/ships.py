from core.models.general import model_locations


def add(**kwargs):
    """

    :param kwargs:
        description: str
    :return:
    """
    return model_locations.Locations.add(**kwargs)

class tt:
    pass

def get_by_uuid(**kwargs):
    return model_locations.Locations.objects.get_by_uuid(**kwargs)


def get_all():
    return model_locations.Locations.objects.get_all()
