import pytest

from lib.add_five import *
from lib.greet import *
from lib.check_codeword import *
from lib.report_length import *
from lib.reminder import *
from lib.counter import *
from lib.string_builder import *

# test 1
def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8

# test 2
def test_greet_name():
    result = greet('Filip')
    assert result == 'Hello, Filip!'

# test 3
def test_check_codeword_close():
    result = check_codeword('hope')
    assert result == "Close, but nope."

# test 4
def test_check_codeword_wrong():
    result = check_codeword('hola')
    assert result == "WRONG!"

# test 5
def test_check_codeword_correct():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

# test 6
def test_report_lenght():
    result = report_lenght('Homo sapiens')
    assert result == "This string was 12 characters long."

# test 7
def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# test 8
#Counter tests add multiple numbers to 12
def test_counter_add_multiple_numbers_report():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    counter.add(2) 
    assert counter.report() == "Counted to 12 so far."

# test 9
def test_counter_initially_report_zero():
    counter = Counter()
    assert counter.report() == "Counted to 0 so far."

# test 10
def test_counter_add_single_number_report():
    counter = Counter()
    counter.add(5)
    assert counter.report() == "Counted to 5 so far."

#Exercise 2 - string builder

# test 11
def test_string_builder_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

#test 12
def test_string_builder_add_one_string_output():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.output() == "hello"

#test 13
def test_string_builder_add_string_set_size_to_that_string_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    assert string_builder.size() == 5

#test 14
def test_string_builder_adding_multiple_strings_outputs_concatenated_strings():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ") #space
    string_builder.add("everyone")
    assert string_builder.output() == "hello everyone"

#test 15
def test_string_builder_adding_multiple_strings_outputs_correct_total_size():
    string_builder = StringBuilder()
    string_builder.add("hello")
    string_builder.add(" ") #space
    string_builder.add("everyone")
    assert string_builder.size() == 14

#TESTING ERRORS
#Test 16
def test_reminder():
    reminder = Reminder("Kay")
    with pytest.raises(Exception) as e: # <-- New code
        reminder.remind()
    error_message = str(e.value) # <-- New code
    assert error_message == "No reminder set!"