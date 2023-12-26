#Program check if the user enter correct format of phone 
string=input("Enter phone in the format (XXX)XXX-XXXX:")
valid = len(string) == 13
position = 0
while valid and position < len(string) :
    if position == 0:
        valid = string[position] == "("
    elif position == 4 :
        valid = string[position] == ")"
    elif position == 8 :
        valid = string[position] == "-"
    else:
        valid = string[position].isdigit()
    position = position + 1
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")

#Program check if the user enter correct format of phone 

string_=input("Enter phone in the format (XXX)XXX-XXXX:")
valid_ = len(string_) == 13
position_ = 0
while valid_ and position_ < len(string_) :
    valid_ = ((position_ == 0 and string_[position_] == "(") or
    (position_ == 4 and string_[position_] == ")") or
    (position_ == 8 and string_[position_] == "-") or
    (position_ != 0 and position_ != 4 and position != 8 and
    string_[position_].isdigit()))
    position_ = position_ + 1
if valid :
    print("The string contains a valid phone number.")
else:
    print("The string does not contain a valid phone number.")