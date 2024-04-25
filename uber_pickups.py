import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st
import random

# List of some League of Legends champions for demonstration.
champions = [
    "Aatrox", "Ahri", "Akali", "Alistar", "Amumu",
    "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol",
    "Azir", "Bard", "Blitzcrank", "Brand", "Braum",
    "Caitlyn", "Camille", "Cassiopeia", "Cho'Gath", "Corki",
    "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko",
    "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora",
    "Fizz", "Galio", "Gangplank", "Garen", "Gnar",
    "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger",
    "Illaoi", "Irelia", "Ivern", "Janna", "Jarvan IV",
    "Jax", "Jayce", "Jhin", "Jinx", "Kai'Sa",
    "Kalista", "Karma", "Karthus", "Kassadin", "Katarina",
    "Kayle", "Kayn", "Kennen", "Kha'Zix", "Kindred",
    "Kled", "Kog'Maw", "LeBlanc", "Lee Sin", "Leona",
    "Lillia", "Lissandra", "Lucian", "Lulu", "Lux",
    "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune",
    "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus",
    "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf",
    "Orianna", "Ornn", "Pantheon", "Poppy", "Pyke",
    "Qiyana", "Quinn", "Rakan", "Rammus", "Rek'Sai",
    "Rell", "Renata Glasc", "Renekton", "Rengar", "Riven",
    "Rumble", "Ryze", "Samira", "Sejuani", "Senna",
    "Seraphine", "Sett", "Shaco", "Shen", "Shyvana",
    "Singed", "Sion", "Sivir", "Skarner", "Sona",
    "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench",
    "Taliyah", "Talon", "Taric", "Teemo", "Thresh",
    "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch",
    "Udyr", "Urgot", "Varus", "Vayne", "Veigar",
    "Vel'Koz", "Vi", "Viego", "Viktor", "Vladimir",
    "Volibear", "Warwick", "Wukong", "Xayah", "Xerath",
    "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi",
    "Zac", "Zed", "Zeri", "Ziggs", "Zilean",
    "Zoe", "Zyra",
]


st.title('Random League of Legends Champion')

if st.button('Get Random Champion'):
    chosen_champion = random.choice(champions)
    st.markdown(f"<h3 style='color: linear-gradient(45deg, #FF0000, #FF7F00, #FFFF00, #00FF00, #0000FF, #4B0082, #9400D3); font-size: 40px;'>{chosen_champion}</h3>", unsafe_allow_html=True)

