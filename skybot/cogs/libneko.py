from discord.ext import commands
from libneko import pag

# Read the dummy text in.
with open('dummy-text.txt') as fp:
    dummy_text = fp.read()



@bot.command()
async def test(ctx):
    """We will be coding in here in the next part."""


def setup(bot):
    bot.add_cog(Libneko(bot))
