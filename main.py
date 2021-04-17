import os
import random
from dotenv import load_dotenv
from pyrogram import Client, filters

load_dotenv()

app = Client(":memory:",
    api_id=os.getenv("APP_API_ID"),
    api_hash=os.getenv("APP_API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

recetas = [
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
]

extra = [
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

help_message = "Usa el comando /menu para obtener un menu semanal aleatorio"

def create_menu():
    entre_semana = ""
    fin_de_semana = ""

    for dia in ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]:
        entre_semana += f"{dia} - {random.choice(recetas)}\n"
    for dia in ["Sabado", "Domingo"]:
        fin_de_semana += f"{dia} - {random.choice(extra)}\n"

    return entre_semana, fin_de_semana


@app.on_message(filters.command("menu"))
def menu(client, message):
    semana, fin_semana = create_menu()
    client.send_message(chat_id=message.chat.id, text=semana)
    client.send_message(chat_id=message.chat.id, text=fin_semana)

@app.on_message(filters.command(["start", "help"]))
def menu(client, message):
    client.send_message(chat_id=message.chat.id, text=help_message)


app.run()
