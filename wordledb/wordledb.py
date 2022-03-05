from redbot.core import Config, commands, checks
from redbot.cogs.admin import admin
import discord
import pymongo
import re

class Wordledb(commands.Cog):
    """Wordle saver bot"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier=806715409318936616)
        default_guild = {

        }
        self.config.register_guild(**default_guild)

    # This cog does not store any End User Data
    async def red_get_data_for_user(self, *, user_id: int):
        return {}
    async def red_delete_data_for_user(self, *, requester, user_id: int) -> None:
        pass

    @commands.command()
    async def wordlepost(self, ctx, mongoUrl, dbName, collectionName, date, answer: str, *, wordle: str):
        """Save to mongodb"""
        # assert the data exists
        try:
          assert mongoUrl != "Wordle"
          assert date != "Wordle"
        except AssertionError:
          return await ctx.send("Uh oh, you forgor the date and answer! 🥴")

        # assert the answer is spoiled
        try:
          assert answer[:2] == "||"
        except AssertionError:
          return await ctx.send("Hey 😡 spoil your answer !!")

        # patch in linebreaks
        w1 = re.sub(r"(?<=\d)\s(?=[⬛🟩🟨])", "\\n\\n", wordle)
        wFinal = re.sub(r"(?<=[⬛🟩🟨])\s(?=[⬛🟩🟨])", "\\n", w1)

        # connect to mongodb
        client = pymongo.MongoClient(mongoUrl, serverSelectionTimeoutMS=5000)
        db = client[dbName]
        coll = db[collectionName]
        post = coll.insert_one({"date": date, "wordle": wFinal, "answer": answer[2:-2] })
        try:
          await ctx.send("✅\n"+str(post.inserted_id)[:1984])
        except Exception as e:
          await ctx.send("❎\n"+str(e))
