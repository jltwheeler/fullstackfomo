def copy_dict_partial(
    input_dict: dict, include_keys=None, exclude_keys=None
) -> dict:
    new_dict = {}
    old_keys = list(input_dict.keys())

    if include_keys is None and exclude_keys is None:
        for key in old_keys:
            new_dict[key] = input_dict[key]
        return new_dict

    if include_keys is not None:
        keys = [key for key in include_keys if key in old_keys]
    else:
        keys = old_keys

    if exclude_keys is not None:
        for key in exclude_keys:
            if key in old_keys and key in keys:
                keys.remove(key)

    for key in keys:
        new_dict[key] = input_dict[key]
    return new_dict


def compose_update_expression(input_dict: dict) -> str:
    base_expression = "SET "
    expressions = ", ".join(
        f"{key} = :val{i}" for i, key in enumerate(input_dict.keys())
    )
    return base_expression + expressions


def compose_expression_attr_vals(input_dict: dict):
    return {f":val{i}": val for i, val in enumerate(input_dict.values())}
