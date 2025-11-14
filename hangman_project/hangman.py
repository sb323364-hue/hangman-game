#!/usr/bin/env python3

import random

words = ["программирование", "компьютер", "алгоритм", "переменная", "функция",
         "библиотека", "синтаксис", "отладка", "интерфейс", "базаданных",
         "питон", "программа", "разработка", "объект", "класс", 
         "метод", "сервер", "клиент", "сеть", "данные"]

def draw_hangman(errors):
    stages = [
        """
  ┌─────┐
  │
  │
  │
  │
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │
  │
  │
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │     │
  │     │
  │
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │    ╱│
  │     │
  │
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │    ╱│╲
  │     │
  │
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │    ╱│╲
  │     │
  │    ╱
  │
━━┷━━
        """,
        """
  ┌─────┐
  │     ●
  │    ╱│╲
  │     │
  │    ╱ ╲
  │
━━┷━━
        """
    ]
    return stages[errors]

def hangman():
    word = random.choice(words)
    guessed = ["_"] * len(word)
    errors = 0
    
    print("🎮 Виселица для Linux")
    print("Угадай слово из IT-тематики!")
    
    while errors < 6 and "_" in guessed:
        print(f"\nСлово: {' '.join(guessed)}")
        print(f"Ошибки: {errors}/6")
        print(draw_hangman(errors))
        
        letter = input("Буква: ").lower().strip()
        
        if len(letter) != 1:
            continue
            
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
            print("✅ Верно!")
        else:
            errors += 1
            print("❌ Неверно!")
    
    print(f"\nЗагаданное слово: {word}")
    print(draw_hangman(errors))
    print("🎉 Победа!" if "_" not in guessed else "💀 Проигрыш!")

if __name__ == "__main__":
    hangman()