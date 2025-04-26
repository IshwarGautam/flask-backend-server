def expect(ns, model, exclude_fields=[], name_suffix="Input"):
    """
    Returns a decorator like @ns.expect(), but removes specified fields from the model.
    """

    def decorator(func):
        # Clone and remove specified fields
        input_model = ns.clone(model.name + name_suffix, model)
        for field in exclude_fields:
            input_model.pop(field, None)

        # Apply the modified model with ns.expect
        return ns.expect(input_model)(func)

    return decorator
