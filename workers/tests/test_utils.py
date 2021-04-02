from functions.utils import copy_dict_partial

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