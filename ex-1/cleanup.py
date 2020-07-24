def filter_model(model, filter_kwargs=None):
    """
    Given a model and a dict of filter params as kwargs, return a filtered
    queryset.
    """
    if filter_kwargs is None:
        filter_kwargs = {
            'author': 'user2',
            'id': '3',
        }
    queryset = model.objects.filter(**filter_kwargs)
    return queryset
