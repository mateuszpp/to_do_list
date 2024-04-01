import time
from plyer import notification

# Funkcja do wyświetlania listy to-do
def wyswietl_liste_todo(lista_todo):
    print("Twoja lista to-do:")
    for idx, task in enumerate(lista_todo, start=1):
        print(f"{idx}. {task}")

# Funkcja do wysyłania powiadomienia
def wyslij_powiadomienie(naglowek, wiadomosc):
    notification.notify(
        title=naglowek,
        message=wiadomosc,
        timeout=10  # Czas wyświetlania powiadomienia (w sekundach)
    )

# Główna funkcja programu
def main():
    # Przykładowa lista to-do
    lista_todo = [
        "Zrobić zakupy spożywcze",
        "Przygotować prezentację",
        "Odebrać paczkę z poczty"
    ]

    # Wyświetlenie listy to-do
    wyswietl_liste_todo(lista_todo)

    # Pętla do wysyłania powiadomień dla każdego zadania
    for task in lista_todo:
        wyslij_powiadomienie("Zadanie do wykonania", task)
        time.sleep(5)  # Oczekiwanie 5 sekund między kolejnymi powiadomieniami

if __name__ == "__main__":
    main()
