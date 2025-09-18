import random

# สุ่มเลขระหว่าง 0 - 9
test_random = random.randint(1, 20)

print("-- เกมทายตัวเลข มาเดาใจคอมพิวเตอร์  --")
print("-- ทายเลขจำนวนเต็มตั้งแต่ 1 - 100 --")
print("-- คุณมีโอกาส 6 ครั้ง --")

i = 0

while True:

    # รับค่าทายเลขจากผู้ใช้
    print(f"ความพยายามครั้งที่ {i+1}")
    guess_number = int(input("What is your guess number (1-20)?: "))

    # condition ==> if-elif-else
    if test_random == guess_number:
        print("เก่งมาก มั่วถูกตั้งแต่ครั้งแรก เทพจริงๆ")
        break

    elif guess_number < test_random:
        print("ผิดจร้า น้อยไปเนอะ")

    else:
        print("ผิดจร้า มากไปหน่อย")

    if i == 3:
        print(get_parity_hint(test_random))
    elif i == 5:
        print(get_range_hint(test_random))
    elif i == 7:
        print(get_range_hint(test_random, test_random-12, test_random+12))
    elif i == 10:
        print(get_thefirst_digit_hint(test_random))
             
    i = i + 1
