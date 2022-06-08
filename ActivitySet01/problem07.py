def enter_text() :
    text = input("Enter the text: ")
    return text

# text = "X-DSPAM-Confidence: 0.8475 "
def find_numb(text) :

    index = text.find(':')
    number = float(text[index+1:])
    print(number)

def main() :
    te_xt = enter_text()
    find_numb(te_xt)

if __name__ =="__main__":
    try:
        main()
    except ValueError :
        print("Invalid string.Enter a string having numeric value after a ':' ")