"""
accept dictionary of authors and ids, insert default user, pass dict to Django filter method to query and return response

@author... 


"""

# unused std lib imports, but could see reason for handling return type as json or implementing logging
# import json
# import logging


def filter_authors_ids(authors_ids_dict: dict) -> None:
    """
    inserts a default user
    passes authors_dict to Django's ORM filter method
    returns response of filter method, no handling or parsing
    
    :param authors_ids_dict: 
    :return: TODO: determine return type and structure, think its a Django QuerySet
    https://docs.djangoproject.com/en/3.1/ref/models/querysets/#methods-that-return-new-querysets
    """
    try:
        # TODO what is purpose of this hardcoding. is this setting the default user?
        #  how are 'other users' handled/inserted?
        authors_ids_dict['author'] = 'user2'
        authors_ids_dict['id'] = '3'

        # was doing lots of printing, could be a reason to implement logging. consider application levels and entry formats
        # logger.info(authors_dict)

        # TODO understand why empty dict handling in original
        #  would never be empty because of default insertion above
        # if authors_dict:   

        # TODO - SomeObject not imported or instantiated, will fail. need to understand source of SomeObject
        return SomeObject.objects.filter(**authors_ids_dict)  # unpacking the authors_dict

    # narrow down possible exceptions caught from 'catch-all'
    # could implement own exception hierarchy
    except AttributeError:
        # do something here, dont just 'pass' which suppresses the exception
        pass


