try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if name == "" or feedback == "":
        raise ValueError("Name and feedback cannot be empty")

    print("Thank you", name, "for your feedback!")
    print("Your feedback:", feedback)

except ValueError as error:
    print("Error:", error)

finally:
    print("Feedback process completed.")