import os

input_path = """


"""

try:
    input_path = input_path.strip()

    if not input_path:
        input_path = os.path.dirname(__file__).replace('\\','/')

    os.system("start " + input_path)


except Exception as e:
    print(e)
    import time
    time.sleep(10)

