from .tasks import longtime_add
import time

if __name__ == '__main__':
    # delay 메서드는 작업을 비동기적으로 처리하는 경우 필요합니다. 또한 작업 결과를 유지하고 정보를 출력합니다.
    result = longtime_add.delay(1,2)
    # ready는 작업이 완료되면 true, 그렇지 않으면 false를 반환합니다.
    # result 속성은 작업의 결과입니다(예제에서는 ‘3’을 반환). 작업이 완료되지 않으면 None을 반환합니다.
    # 이 지점에서 작업이 완료되지 않으므로 False를 반환합니다.
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)
    # 10초 후 작업이 완료됩니다.
    time.sleep(10)
    # 이 지점에서 작업이 완료되고 ready()가 True를 반환합니다.
    print ('Task finished? ', result.ready())
    print ('Task result: ', result.result)