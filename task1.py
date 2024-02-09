person = {"Darth Vader": "father",
          "Leia": "sister",
          "Han": "brother in law"
}
for key, value in person.items():
    if key == "Darth Vader":
        print(f"{key},Luke I'm ur {value}")
    elif key == "Leia":
        print(f"{key},Luke I'm ur{value}")
    elif key == "Han":
        print(f"{key},Luke I'm ur{value}")