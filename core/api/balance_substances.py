import datetime

from core.models.balance import model_balance_general



def add(**kwargs):
    """

    :param kwargs:
        description: str
    :return:
    """
    return model_balance_general.Substances.add(**kwargs)


def substance_residues(**kwargs):
    return model_balance_general.Substances.objects.substance_residues(**kwargs)


def get_balances_by_substances(**kwargs):
    return model_balance_general.Substances.objects.get_balances_by_substances()


def get_all(**kwargs):
    return model_balance_general.Substances.objects.get_all()




