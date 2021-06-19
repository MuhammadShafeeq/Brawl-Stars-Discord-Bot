# Brawl-Stars-Discord-Bot
This is the complete source code of my discord bot, Brawl Stars. It takes information from a game called Brawl Stars and takes the info using http requests. Since this is not a using an library python and using a requests it will cause lag.

# How to use the bot
if you have discord you can use the bot
https://discord.com/api/oauth2/authorize?client_id=854034596537434172&permissions=8&scope=bot

# Features
It will send your account details
like this

![image](https://user-images.githubusercontent.com/83785340/122415207-c579bb00-cf98-11eb-893c-ab600ede4e3c.png) 

If you didnt register you will have to register ur account.
This is how it saves it

![image](https://user-images.githubusercontent.com/83785340/122415939-5f416800-cf99-11eb-8728-6731462e8dd0.png)


If you want to delete your account you will have to type $remove
![image](https://user-images.githubusercontent.com/83785340/122415725-35884100-cf99-11eb-90a9-2b4d59f4da45.png)

# Error Handling

![image](https://user-images.githubusercontent.com/83785340/122416310-adef0200-cf99-11eb-8591-6387b74c4b97.png)

This bot is trained to handle errors. It will detect the error and send it back to you. When you Try to save an account when it is already registered.

![image](https://user-images.githubusercontent.com/83785340/122416526-dd9e0a00-cf99-11eb-8493-6adb67e388b5.png)

When you use a command when it is not registered.

![image](https://user-images.githubusercontent.com/83785340/122416864-205fe200-cf9a-11eb-8d2f-a17c6a8f56cd.png)

When you type an incorrect account to register.

# What actually happens behind the scenes

%%%%%%%%%%% SAVING AN ACCOUNT %%%%%%%%%%%%%%%%'

When you register an account it is saved to a json file. This file saves in the dictionary form {userid:account}.
Im running the files in my own pc and here is a screenshot taken of the data saved.


![image](https://user-images.githubusercontent.com/83785340/122417655-b431ae00-cf9a-11eb-94f0-a65a021ca97a.png)

Now when this discord account saves something it will be using the saved data. Also if a save command is used we will check
if the account is there in the saved file.


![image](https://user-images.githubusercontent.com/83785340/122418208-19859f00-cf9b-11eb-8e8e-97584a98deae.png)

Then it checks if the account gotten is real by sending a request to a website that will check for a tag. (Note: This is legal because the game itself made the website)

![image](https://user-images.githubusercontent.com/83785340/122420057-6f0e7b80-cf9c-11eb-93d2-2e772ee81189.png)

Then using requests to send http for 'GET' methods to get more info.

Note: **None of this was copied and was all original.** 
Note: **You cannot run this code since discord safety automatically protects unknown ip's**
