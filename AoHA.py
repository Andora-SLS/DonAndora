import discord
from discord.ui import Select, View
from discord.ext import commands

TOKEN = ""

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = "Wirtschaftsingenieurwesen B.Sc.", value = 1094989409050431519),
            discord.SelectOption(label = "Wirtschaftsinformatik B.Sc.",     value = 1097247416132051015),
            discord.SelectOption(label = "Maschinenbau B.Sc.",              value = 1097249030649688175),
            discord.SelectOption(label = "Nachhaltiges Management B.Sc.",   value = 1097736715910778920),
        ]
        super().__init__(placeholder = "Wählen Sie einen Studiengang aus", options = options)
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guilde = interaction.guild

        if int(self.values[0]) == 1094989409050431519:
            if guilde.get_role(1094989409050431519) in user.roles:
                await user.remove_roles(guilde.get_role(1094989409050431519))
                await interaction.response.send_message("Studiengang: Wirtschaftsingenieurwesen B.Sc. wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094989409050431519))
                await interaction.response.send_message("Studiengang: Wirtschaftsingenieurwesen B.Sc. wurde hinzugefügt!", ephemeral = True)
        elif int(self.values[0]) == 1097247416132051015:
            if guilde.get_role(1097247416132051015) in user.roles:
                await user.remove_roles(guilde.get_role(1097247416132051015))
                await interaction.response.send_message("Studiengang: Wirtschaftsinformatik B.Sc. wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1097247416132051015))
                await interaction.response.send_message("Studiengang: Wirtschaftsinformatik B.Sc. wurde hinzugefügt!", ephemeral = True)
        elif int(self.values[0]) == 1097249030649688175:
            if guilde.get_role(1097249030649688175) in user.roles:
                await user.remove_roles(guilde.get_role(1097249030649688175))
                await interaction.response.send_message("Studiengang: Maschinenbau B.Sc. wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1097249030649688175))
                await interaction.response.send_message("Studiengang: Maschinenbau B.Sc. wurde hinzugefügt!", ephemeral = True)
        elif int(self.values[0]) == 1097736715910778920:
            if guilde.get_role(1097736715910778920) in user.roles:
                await user.remove_roles(guilde.get_role(1097736715910778920))
                await interaction.response.send_message("Studiengang: Nachhaltiges Management B.Sc. wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1097736715910778920))
                await interaction.response.send_message("Studiengang: Nachhaltiges Management B.Sc. wurde hinzugefügt!", ephemeral = True)
        else:
            await interaction.response.send_message("Ein Fehler ist aufgetreten!", ephemeral = True)


class SelectModul(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label = "GLET (Service)", value = 1094992920102326293),
            discord.SelectOption(label = "Grundlagen der Fahrzeugantriebe",     value = 1094993689736122388),
            discord.SelectOption(label = "Konstruktion I",              value = 1094993761530028062),
            discord.SelectOption(label = "Marketing und Produktionsmanagement",   value = 1094994011414089728),
            discord.SelectOption(label = "Statistik I für Wiwi",   value = 1094994101092491408),
            discord.SelectOption(label = "Wirtschaftspolitik",   value = 1094994211528523888),
            discord.SelectOption(label = "Einführung in die Informatik I",   value = 1098988767030808740),
        ]
        super().__init__(placeholder = "Wählen Sie ihre Module aus", options = options)
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guilde = interaction.guild

        if int(self.values[0]) == 1094992920102326293:
            if guilde.get_role(1094992920102326293) in user.roles:
                await user.remove_roles(guilde.get_role(1094992920102326293))
                await interaction.response.send_message("Modul: GLET (Service) wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094992920102326293))
                await interaction.response.send_message("Modul: GLET (Service) wurde hinzugefügt!", ephemeral = True)

        elif int(self.values[0]) == 1094993689736122388:
            if guilde.get_role(1094993689736122388) in user.roles:
                await user.remove_roles(guilde.get_role(1094993689736122388))
                await interaction.response.send_message("Modul: Grundlagen der Fahrzeugantriebe wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094993689736122388))
                await interaction.response.send_message("Modul: Grundlagen der Fahrzeugantriebe wurde hinzugefügt!", ephemeral = True)

        elif int(self.values[0]) == 1094993761530028062:
            if guilde.get_role(1094993761530028062) in user.roles:
                await user.remove_roles(guilde.get_role(1094993761530028062))
                await interaction.response.send_message("Modul: Konstruktion I wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094993761530028062))
                await interaction.response.send_message("Modul: Konstruktion I wurde hinzugefügt!", ephemeral = True)

        elif int(self.values[0]) == 1094994011414089728:
            if guilde.get_role(1094994011414089728) in user.roles:
                await user.remove_roles(guilde.get_role(1094994011414089728))
                await interaction.response.send_message("Modul: Marketing und Produktionsmanagement wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094994011414089728))
                await interaction.response.send_message("Modul: Marketing und Produktionsmanagement wurde hinzugefügt!", ephemeral = True)
        
        elif int(self.values[0]) == 1094994101092491408:
            if guilde.get_role(1094994101092491408) in user.roles:
                await user.remove_roles(guilde.get_role(1094994101092491408))
                await interaction.response.send_message("Modul: Statistik I für Wiwi wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094994101092491408))
                await interaction.response.send_message("Modul: Statistik I für Wiwi wurde hinzugefügt!", ephemeral = True)

        elif int(self.values[0]) == 1094994211528523888:
            if guilde.get_role(1094994211528523888) in user.roles:
                await user.remove_roles(guilde.get_role(1094994211528523888))
                await interaction.response.send_message("Modul: Wirtschaftspolitik wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1094994211528523888))
                await interaction.response.send_message("Modul: Wirtschaftspolitik wurde hinzugefügt!", ephemeral = True)

        elif int(self.values[0]) == 1098988767030808740:
            if guilde.get_role(1098988767030808740) in user.roles:
                await user.remove_roles(guilde.get_role(1098988767030808740))
                await interaction.response.send_message("Modul: Einführung in die Informatik I wurde entfernt!", ephemeral = True)
                return
            else:
                await user.add_roles(guilde.get_role(1098988767030808740))
                await interaction.response.send_message("Modul: Einführung in die Informatik I wurde hinzugefügt!", ephemeral = True)

        else:
            await interaction.response.send_message("Ein Fehler ist aufgetreten!", ephemeral = True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout: float = None):
        super().__init__(timeout = timeout)
        self.add_item(Select())

class SelectViewModul(discord.ui.View):
    def __init__(self, *, timeout: float = None):
        super().__init__(timeout = timeout)
        self.add_item(SelectModul())


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is ready!")

    selectMenuChannel = bot.get_channel(1099099760754966609)
    log_channel = bot.get_channel(1099078044825686116)
    msg = 'Bot booted up and is now running!'
    embed = discord.Embed(
        color = discord.Color.blue(),
        description = msg,
        timestamp = discord.utils.utcnow(),
    )

    async for msg in selectMenuChannel.history(limit=2):
        await msg.delete()


    await log_channel.send(embed = embed)
    await selectMenuChannel.send("Wählen Sie Studiengänge aus, die Sie hinzufügen oder entfernen möchten:", view = SelectView())
    await selectMenuChannel.send("Wählen Sie Module aus, die Sie hinzufügen oder entfernen möchten:", view = SelectViewModul())



#@bot.command()
async def role(ctx):
    await ctx.send("Wählen Sie Studiengänge aus, die Sie hinzufügen oder entfernen möchten:", view = SelectView(), view2 = SelectViewModul())

bot.run(TOKEN)

