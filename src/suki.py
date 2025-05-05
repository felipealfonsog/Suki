import tweepy

# Llaves de tu aplicación (no las compartas públicamente)
api_key = 'YazRrBxVU3TUmzmIaMFtOrDcj'
api_secret = 'MELVfpeMomPvZ8wJhsDbM9iURDDdSNWUZbEcxEIC8UnNHj9C9T'
access_token = '4765357693-yBLi3cB9kNXUXVPpoCG5jKjy1YuNTI7ejlEQJAe'
access_token_secret = 'hC2JI9k3AKeMNNEfoZSPNyOTFbqZEwAfq35vCA7M1spM8'

# Autenticación (compatible con versiones anteriores de Tweepy)
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Mensaje de ayuda
mensaje = "Ayudemos a Firulais 🐶💔 Tiene cáncer y necesita tratamiento urgente. Puedes colaborar aquí: https://www.rifaporsuki.com/ #Ayudaanimal #chile #AyudaSuki"

# Publicar tuit
try:
    api.update_status(mensaje)
    print("Tuit publicado.")
except tweepy.TweepError as e:
    print("Error al publicar el tuit:", e)
