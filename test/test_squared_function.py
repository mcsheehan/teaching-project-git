from teaching_project.squared_function import squared


# Triple A testing
def test_squared_where_input_is_2():
    # Arrange
    number_to_be_squared = 2
    expected_output = 5

    # Act
    actual_output = squared(number_to_be_squared)

    # Assert
    assert actual_output == expected_output


def test_squared_where_input_is_9():
    number_to_be_squared = 9
    expected_output = 81

    # Act
    actual_output = squared(number_to_be_squared)

    # Assert
    assert actual_output == expected_output


def test_squared_where_input_is_4():
    number_to_be_squared = 4
    expected_output = 16

    # Act
    actual_output = squared(number_to_be_squared)

    # Assert
    assert actual_output == expected_output


def test_squared_where_input_is_0():
    number_to_be_squared = 0
    expected_output = 0

    # Act
    actual_output = squared(number_to_be_squared)

    # Assert
    assert actual_output == expected_output


def test_squared_where_input_is_negative_3():
    number_to_be_squared = -3
    expected_output = 9

    # Act
    actual_output = squared(number_to_be_squared)

    # Assert
    assert actual_output == expected_output
