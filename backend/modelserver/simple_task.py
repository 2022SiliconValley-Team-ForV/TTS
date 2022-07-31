from celery_app import app


lst = []
for i in range(3):
    lst.append(i)


@app.task(name="add")
def add(x,y):
    result = int(x)+int(y)+lst[1]
    print(result)
    return result