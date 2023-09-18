from lib.add_five import *
from lib.greet import *
from lib.check_codeword import *
from lib.report_length import *
from lib.reminder import *
from lib.counter import *

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
#Counter tests 
def test_counter_add_report():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 12 so far."