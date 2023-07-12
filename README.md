# Game project

To run the game you have to follow the next instructions in the terminal

``` sh
cd game
python3 -m venv venv
source venv/Scripts/activate
pip3 install -r requirements.txt
python3 main.py
```

# App project

```sh
git clone
cd app
python3 -m venv venv
source venv/Scripts/activate
pip3 install -r requirements.txt
python3 main.py
```

# Docker

Once created the files "Dockerfile" and "docker-compose.yml", You will new to execute the following commands

```sh
docker-compose build 
# Wait until it is builded
# Then execute to check
# that everything is uploaded
docker-compose ps
# Finally use this command to 
# execute the container
docker-compose exec app-csv bash
```

To turn it down use
```sh
docker-compose down
```
To turn it up use
```sh
docker-compose up -d
```

[Docs here](https://shorturl.at/rY269)