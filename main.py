import os
from openai import OpenAI
from dotenv import load_dotenv


def load_api_key():
    "ładowanie klucza do API OpenAI z pliku env"
    load_dotenv()
    return os.getenv("OPENAI_API_KEY")


def read_file(file_path):
    "wczytywanie zawartosci pliku tekstowego do przerobienia"
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def generate_html_from_text(client, text):
    "wysyłanie prompta do ChatGPT aby przerobil tekst"
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": f"Przekształć poniższy tekst w kod HTML z odpowiednimi tagami do strukturyzacji treści. Kod nie powinien zawierac znacznikow <html>, <head> ani <body>. Ma byc to jedynie zwartosc do wstawienia pomiedzy tagami body. Wstaw tagi <img> w miejscach na grafiki, z atrybutem src='image_placeholder.jpg' i w atrybucie alt napisz dokladny prompt jaki powinienem uzyc do wyegenrowania przez AI takiej grafiki. Pod grafikami umiesc podpisy uzywajac odpowiedniego tagu HTML.\n\nTekst: {text}",
        }],
        model="gpt-4o",
    )
    return response.choices[0].message.content


def save_html(content, file_path):
    "zapisywanie odpowiedzi do pliku"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    file_path = 'tresc_artykulu.txt'
    html_path = 'artykul.html'

    api_key = load_api_key()
    client = OpenAI(api_key=api_key)

    file_content = read_file(file_path)
    html_content = generate_html_from_text(client, file_content)

    save_html(html_content, html_path)
    print(f"HTML został zapisany w pliku: {html_path}")


if __name__ == "__main__":
    main()
