import pyshorteners
import streamlit as sl

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except pyshorteners.exceptions.BadURLException:
        return "La URL ingresada no es válida."
    
# APP WEB
sl.set_page_config(page_title="URL Shortener", page_icon="⛏", layout="centered")
sl.image("images/a.jpg", use_column_width=True)
sl.title("URL Shortener")

url = sl.text_input("Enter the URL")


if sl.button("Generate new URL"):
    sl.write("URL shortered: ", shorten_url(url))
