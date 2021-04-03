from functions.utils import (
    compose_expression_attr_vals,
    compose_update_expression,
    copy_dict_partial,
)

input_dict = {"name": "Kanye", "age": 99, "job": "rapper", "sex": "male"}


def test_copy_dict_partial_no_include_or_exclude():
    assert copy_dict_partial(input_dict) == input_dict


def test_copy_dict_partial_include_and_exclude():
    assert copy_dict_partial(
        input_dict, include_keys=["name", "age"], exclude_keys=["sex", "job"]
    ) == {"name": "Kanye", "age": 99}


def test_copy_dict_partial_include_and_exclude_empty():
    assert (
        copy_dict_partial(
            input_dict,
            include_keys=[""],
            exclude_keys=["name", "age", "sex", "job"],
        )
        == {}
    )


def test_copy_dict_partial_include_only():
    assert copy_dict_partial(input_dict, include_keys=["name", "age"]) == {
        "name": "Kanye",
        "age": 99,
    }


def test_copy_dict_partial_include_non_keys():
    assert copy_dict_partial(input_dict, include_keys=["bad"]) == {}


def test_copy_dict_partial_exclude_only():
    assert copy_dict_partial(input_dict, exclude_keys=["name", "age"]) == {
        "job": "rapper",
        "sex": "male",
    }


def test_copy_dict_partial_exclude_non_keys():
    assert copy_dict_partial(input_dict, exclude_keys=["bad"]) == input_dict


def test_compose_update_expression():
    result = "SET name = :val0, age = :val1, job = :val2, sex = :val3"
    assert compose_update_expression(input_dict) == result


def test_compose_expression_attr_vals():
    assert compose_expression_attr_vals(input_dict) == {
        ":val0": "Kanye",
        ":val1": 99,
        ":val2": "rapper",
        ":val3": "male",
    }
