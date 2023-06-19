import pytest
import  datetime

@pytest.fixture(scope='session', autouse=True)
def test_session_start_end(request):
    start_time = datetime.datetime.now()
    print(f'\nTest session start {start_time}')

    def session_end():
        end_time = datetime.datetime.now()
        print(f'\n Test session end {end_time}')
        duration = end_time - start_time
        print(f'Test session duration: {duration}')

        request.addfinalizer(session_end)

@pytest.fixture(scope='function')
def time_test(request):
    start_time = datetime.datetime.now()
    print(f'Test start {start_time}')

    def test_end():
        end_time = datetime.datetime.now()
        print(f'\nTest end {end_time}')
        duration = end_time - start_time
        print(f'Test duration: {duration}')

    request.addfinalizer(test_end)