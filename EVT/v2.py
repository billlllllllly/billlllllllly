import random
import json
import time
import os
import msvcrt

def load_data(filepath):
    files = os.listdir(filepath)
    vocablist, weight = [], []

    for file in files:
        with open(os.path.join(filepath, file), "r", encoding="utf-8") as vocabfile:
            for line in vocabfile.readlines():
                vocab_entry = json.loads(line)
                vocablist.append(vocab_entry)
                weight.append(vocab_entry["weight"])

    return vocablist, weight

def print_status(correctnum, wrongnum, totalnum, vocablist_len, wa):
    print("\033[2J\033[H\n", end="")
    print("\033[0m---------------")
    print("\033[92mcorrect:  %d" % correctnum)
    print("\033[91mwrong:    %d" % wrongnum)
    print("\033[96manswered: %d" % totalnum)
    print("\033[0mtotal:    %d + %d" % (vocablist_len, wrongnum * 2))
    print("\033[0m---------------\n")
    print(f"\033[93m{wa}\033[0m")
    return

def print_result(correctnum, totalnum, start_time):
    end_time = time.time()
    accuracy = (correctnum / totalnum) if totalnum else -1
    mtcpq = (end_time - start_time) / totalnum if totalnum else 0
    print("\033[2J\033[H\n", end="")
    print("\033[93m=================================")
    print("accuracy  : %d/%d" % (correctnum, totalnum))
    print("            %03.2f" % accuracy)
    print("per q.    : %0.2f sec" % mtcpq)
    print("=================================\033[0m")
    input("Press enter to exit")
    return

def print_file(filepath):
    files = os.listdir(filepath)
    print("\033[2J\033[H\n", end="")
    print(f"Path: \n\033[93m{filepath}\033[0m\n")
    print("File(s):\n\033[93m", end = '')
    print(*files, sep = '\n', end = '')
    print("\033[0m\n")
    return

def h_multiple_choice(vocablist, weight):
    l = len(vocablist)
    correctanswer = random.choices(range(l), weights=weight, k=1)[0]
    candidates = set()

    while len(candidates) < 3:
        candidate = random.choice(range(l))
        if candidate != correctanswer:
            candidates.add(candidate)

    answer_options = list(candidates)
    correct_idx = random.randint(0, 3)
    answer_options.insert(correct_idx, correctanswer)

    return correctanswer, correct_idx, answer_options


def multiple_choice(vocablist, weight, correctnum, wrongnum, totalnum, wa):
    correctanswer, correct_idx, answer_options = h_multiple_choice(vocablist, weight)
    target_language_idx = random.randint(0, 1)  # Randomly select between 0 and 1
    lanchoice = ["English", "Chinese"]

    keyreserve = -1
    key = ""
    while(1):
        temp = '';
        try:
            temp = key.decode()
        except:
            pass
        match temp:
            case '':
                pass
            case '1'|'2'|'3'|'4':
                keyreserve = int(temp) - 1
            case '9':
                return False, correctnum, wrongnum, totalnum, ""
            case '0':
                return True, correctnum, wrongnum, totalnum, ""
            case '\r':
                if keyreserve != -1:
                    break
                else:
                    key = msvcrt.getch()
                    continue
            case _:
                key = msvcrt.getch()
                continue

        print_status(correctnum, wrongnum, totalnum, len(vocablist), wa)
        print(vocablist[correctanswer][lanchoice[target_language_idx]])
        for i, ans in enumerate(answer_options):
            if i == keyreserve:
                print("\033[92m", end='')
            else:
                print("\033[0m", end='')
            print(f"({i+1}) {vocablist[ans][lanchoice[1 - target_language_idx]]}")
        key = msvcrt.getch()

    wa = ''
    if (keyreserve == correct_idx):
        weight[correctanswer] -= 2
        correctnum += 1
    else:
        weight[correctanswer] += 2
        wrongnum += 1
        wa = vocablist[correctanswer]["English"]+' '+vocablist[correctanswer]["Chinese"]+'\n'
        if keyreserve != -1:
            wa += vocablist[answer_options[keyreserve]]["English"]+' '+vocablist[answer_options[keyreserve]]["Chinese"]
    
    totalnum += 1
    #print_status(correctnum, wrongnum, totalnum, len(vocablist), error)
    return True, correctnum, wrongnum, totalnum, wa


def handwrite(vocablist, weight, correctnum, wrongnum, totalnum):
    wordidx = random.choices(range(len(vocablist)), weights=weight, k=1)[0]
    word = vocablist[wordidx]["English"]
    print(vocablist[wordidx]["Chinese"])

    if word.startswith("#"):
        weight[wordidx] -= 2
        return correctnum, wrongnum, totalnum

    expected = [w for w in word.split() if not w.startswith("[")]
    userinput = input("Input your answer: ").strip()

    if userinput.split() == expected:
        correctnum += 1
        weight[wordidx] -= 2
    else:
        wrongnum += 1
        print(f"Correct answer: {' '.join(expected)}")

    totalnum += 1
    return correctnum, wrongnum, totalnum


def main():
    #filepath = input("Enter filepath: ").strip()
    filepath = "C:/Users/sunfar/Desktop/billy/EVT/v/6.4"
    vocablist, weight = load_data(filepath)

    print_file(filepath)

    correctnum = wrongnum = totalnum = 0
    wa = ""
    start_time = time.time()

    mode = input("Enter mode [mc/hw]: \033[92m").strip()
    print("\033[0m")

    if mode == "hw":
        while True:
            correctnum, wrongnum, totalnum = handwrite(vocablist, weight, correctnum, wrongnum, totalnum)
            if all(w == 0 for w in weight):
                break
    else:
        keep_going = True
        while keep_going:
            keep_going, correctnum, wrongnum, totalnum, wa = multiple_choice(vocablist, weight, correctnum, wrongnum, totalnum, wa)

    print_result(correctnum, totalnum, start_time)


if __name__ == "__main__":
    main()
