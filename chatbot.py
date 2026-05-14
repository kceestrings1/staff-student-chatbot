print("=" * 50)
print("WELCOME TO STAFF/STUDENT CHATBOT")
print("=" * 50)

name = input("Enter your name: ")
print(f"\nHello {name}! 👋")

while True:
    print("\nChoose an option:")
    print("1. School Fees")
    print("2. Course Registration")
    print("3. Result Checking")
    print("4. Hostel Information")
    print("5. Contact Lecturer")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n💰 School fees can be paid through the school portal.")
        print("Visit the bursary unit for more information.")

    elif choice == "2":
        print("\n📚 Course registration is done online.")
        print("Ensure all courses are registered before deadline.")

    elif choice == "3":
        print("\n📄 Results can be checked on the student portal.")
        print("Use your matric number and password to login.")

    elif choice == "4":
        print("\n🏠 Hostel allocation is based on availability.")
        print("Visit the student affairs office for support.")

    elif choice == "5":
        lecturer = input("Enter lecturer name: ")
        print(f"\n📧 Contact request for {lecturer} has been noted.")
        print("Please check the department notice board for office hours.")

    elif choice == "6":
        print(f"\nGoodbye {name}! Thanks for using the chatbot. 👋")
        break

    else:
        print("\n❌ Invalid option. Please enter a number from 1 to 6.")