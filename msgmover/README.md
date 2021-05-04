<p align="center">
  <img src="https://raw.githubusercontent.com/coffeebank/coffee-cogs/master/msgmover/preview.jpg" />
</p>

<h1 align="center">
  msgmover
</h1>

<h3 align="center">
  The Discord Bot for Moving Messages Between Channels and Servers
</h3>

<p align="center">
  <a href="https://github.com/coffeebank/coffee-cogs/tree/master/msgmover#Install">Add to your Discord ></a>
</p>

<p align="center">
  <a href="https://coffeebank.github.io/discord">Join the Support Discord ></a>
</p>

## What is msgmover?

**msgmover** is a Discord bot made for redirecting chats, merging Discord channels, and linking up two Discord servers. The two main features rely on the same technology:

- **msgcopy**: Copy existing messages from one Discord channel into another Discord channel  

- **msgrelay**: Forward all new messages from one Discord channel into another Discord channel


## How does it work?

Each user's profile picture, nickname/username, and message is copied and pasted into the new channel/server.

**Currently supported:**
- Embeds
- Attachments (Images, videos, text, etc.)
- Replies

**Not supported yet:**
- Syncing message edits
- Syncing message deletes


## Install

This bot isn't public for you to add, but you can run it off a computer for your Discord.

It's very easy, takes about 10-20 minutes:

### Step 1: Download Red DiscordBot

- [Installing Red on Windows](https://docs.discord.red/en/stable/install_windows.html)
- [Installing Red on Linux or Mac](https://docs.discord.red/en/stable/install_linux_mac.html)

### Step 2: Add your bot to your Discord server

- [Getting Started](https://docs.discord.red/en/stable/getting_started.html)


### Step 3: Add coffee-cogs

The bot supports adding plugins to make the bot do more stuff, and the **msgmover** cog is a plugin you can add.

Type these commands in a DM with your bot: ([p] is your prefix)

```
[p]repo add coffee-cogs https://github.com/coffeebank/coffee-cogs
[p]cog install coffee-cogs msgmover
```

You're done!

## Bot Commands

Type `[p]help Msgmover` to see everything **msgmover** can do.

- `[p]msgcopy`  
Copy existing messages to a new server  

- `[p]msgrelay`  
Forward new messages to a new channel/server