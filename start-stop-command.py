started=False
while True:
    command = input(">")

    if command.lower() == "help":
        print(''' 
start - to start
stop - to stop
quit - to quit
        ''')

    elif command.lower() == "start":
        if started:
            print("car has already started")
        else:
            started=True
            print("car started...")
    elif command.lower() == "stop":
        if not started:
            print("the car has already stopped")
        else:
            started=False
            print("the car stopped")


    elif command.lower() == "quit":
        break
    else:
        print("sorry, i don't understand")
