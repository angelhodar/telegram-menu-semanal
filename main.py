import os
from random import sample
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(":memory:",
    api_id=os.getenv("APP_API_ID"),
    api_hash=os.getenv("APP_API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

recipes = {
    "weekdays": [
        "Lentejas",
        "Fabada",
        "Paella",
        "Migas",
        "Puchero de calabaza",
        "Bacalao con tomate",
        "Cazuela de fideos",
        "Ensaladilla rusa",
        "Croquetas con ensalada",
        "Empanada",
        "Lasaña",
        "Ñoquis",
        "Carne en salsa",
        "Albondigas en salsa con patatas fritas",
        "Pollo con patatas",
        "Potaje de semana santa",
        "Calamares en su tinta",
        "Cachopo"
    ],
    "weekend": [
        "Costillas agridulce",
        "Arroz a la cubana",
        "Spaguettis con chorizo",
        "Huevos a la reina",
        "Judias verdes con huevo y puré de patata",
        "Trucha a la plancha",
        "Salmorejo",
        "Berenjenas fritas",
        "Huevos al plato",
        "Ensalada mar y montaña",
        "Champiñones con huevo y queso",
        "Musaka",
        "Pollo al curry con arroz",
        "Patatas a la importancia",
        "Salmon a la plancha con champiñones, bacon y salsa",
        "Ternena con patatas",
        "Cebolla pochada con patatas, guiantes y jamón",
        "Wantu",
        "Gyozas"
    ]
}

help_message = "Usa el comando /menu para obtener un menu semanal aleatorio"


def create_menu():
    weekdays = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    weekend = ["Sabado", "Domingo"]

    wd_recipes = sample(recipes["weekdays"], 5)
    we_recipes = sample(recipes["weekend"], 2)

    weekdays_menu = [f"{d} - {r}" for d, r in zip(weekdays, wd_recipes)]
    weekend_menu = [f"{d} - {r}" for d, r in zip(weekend, we_recipes)]

    return "\n".join(weekdays_menu), "\n".join(weekend_menu)

def send_menu(client, chat_id):
    weekday_menu, weekend_menu = create_menu()
    client.send_message(chat_id=chat_id, text=weekday_menu)
    client.send_message(chat_id=chat_id, text=weekend_menu)


@app.on_message(filters.command("menu"))
def menu(client, message):
    send_menu(client, message.chat.id)

@app.on_message(filters.command(["start", "help"]))
def help(client, message):
    client.send_message(chat_id=message.chat.id, text=help_message)


app.run()
