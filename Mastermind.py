import random
def get_guess():
    while True:
        try:
            user_input = input("Enter a number: ")
            user_list = []
            for item in user_input:
                user_list.append(int(item))

            illegal_num1 = False
            illegal_num2 = False
            illegal_length = False

            for number in user_list:
            # First condition: To be in the range 1-7
                if number > 7 or number < 1:
                    illegal_num1 = True
            # Second condition: To be a unique value
                if user_list.count(number) > 1:
                    illegal_num2 = True
            # Third condition
            if len(user_list) != 4:
                illegal_length = True

            if illegal_num1:
                print "The number is not in range 1-7"
            if illegal_num2:
                print "The number should be unique"
            if illegal_length:
                print "The guess should have a length of 4"
            if not illegal_num1 and not illegal_num2 and not illegal_length:
                return user_input
        except ValueError:
            print "Please enter only numbers. Error 404!"

def check_values(num_array, guesses):
    response = []
    for number in num_array:
        if number in guesses:
            if num_array.index(number) == guesses.index(number):
                response.append("RED")
            else:
                response.append("WHITE")
        else:
            response.append("BLACK")
    random.shuffle(response)
    print response
    return (check_win(response))

def check_win(response_list):
    win = 0
    for guess in response_list:
        if guess == "RED":
            win = win + 1
    if win == 4:
        print "You win!"
    return win

def create_comp_list():
    list = []
    while len(list) < 4:
        random_num = random.randint(1,7)
        if random_num not in list:
            list.append(random_num)
    return list

def play_game():
    game_list = create_comp_list()
    total_guesses = 0

    while total_guesses < 5:
        print "Guesses remaining: " + str(5 - total_guesses)
        user_input = get_guess()

        if check_values(game_list,user_input) == 4:
            break

        total_guesses = total_guesses + 1
    if total_guesses == 5:
        print "Sorry! That's all the guesses you get!"
        print "This is the correct answer: "
        print game_list
    print "Thanks for playing!"

print create_comp_list()
print play_game()
