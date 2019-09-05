@bot.command(pass_context=True)
async def animu(ctx, *, title):
	title = title.replace(' ', '%20')
	init = await kitsu(title, 1)
	if type(init) is str:
		await bot.say(init)
		return 'No result'
	else:
		pass

	maxPage = int(init['dataLength'])
	firstRun = True
	while True:
		if firstRun:
			firstRun = False
			num = 1
			find = await kitsu(title, num)
			embed=discord.Embed(title="Anime Info", color=0x81e28d)
			embed.set_image(url=find['posterImg'])
			embed.add_field(name='Title', value=find['title'], inline=False)
			embed.add_field(name='Episode', value=find['episode'], inline=True)
			embed.add_field(name='Status', value=find['episode'], inline=True)
			embed.add_field(name='Score', value=find['score'], inline=True)
			embed.add_field(name='Start Date', value=find['startDate'], inline=True)
			embed.add_field(name='End Date', value=find['endDate'], inline=True)
			msg = await bot.say(embed=embed)
			msg2 = await bot.say('```{}```'.format(str(find['synopsis'])))	

		if maxPage == 1 and num == 1:
			print('{}/{}'.format(str(num),str(maxPage)))
			toReact = ['✅']
		elif num == 1:
			print('{}/{}'.format(str(num),str(maxPage)))
			toReact = ['⏩', '✅']
		elif num == maxPage:
			print('{}/{}'.format(str(num),str(maxPage)))
			toReact = ['⏪', '✅']
		elif num > 1 and num < maxPage:
			print('{}/{}'.format(str(num),str(maxPage)))
			toReact = ['⏪', '⏩', '✅']
		for reaction in toReact:
			await bot.add_reaction(msg2, reaction)
		#feel free to change ✅ to 🆗 or the opposite
		def checkReaction(reaction, user):
			e = str(reaction.emoji)
			return e.startswith(('⏪', '⏩', '✅'))

		res = await bot.wait_for_reaction(message=msg2, user=ctx.message.author, timeout=10, check=checkReaction)
		if res is None:
			await bot.delete_message(ctx.message)
			await bot.delete_message(msg)
			await bot.delete_message(msg2)
			break
		elif '⏪' in str(res.reaction.emoji):
			num = num - 1
			find = await kitsu(title, num)
			embed=discord.Embed(title="Anime Info", color=0x81e28d)
			embed.set_image(url=find['posterImg'])
			embed.add_field(name='Title', value=find['title'], inline=False)
			embed.add_field(name='Episode', value=find['episode'], inline=True)
			embed.add_field(name='Status', value=find['episode'], inline=True)
			embed.add_field(name='Score', value=find['score'], inline=True)
			embed.add_field(name='Start Date', value=find['startDate'], inline=True)
			embed.add_field(name='End Date', value=find['endDate'], inline=True)
			fmtSyn = '```{}```'.format(str(find['synopsis']))
			await bot.delete_message(msg)
			await bot.delete_message(msg2)
			msg = await bot.say(embed=embed)
			msg2 = await bot.say(fmtSyn)
		elif '⏩' in str(res.reaction.emoji):
			num = num + 1
			find = await kitsu(title, num)
			embed=discord.Embed(title="Anime Info", color=0x81e28d)
			embed.set_image(url=find['posterImg'])
			embed.add_field(name='Title', value=find['title'], inline=False)
			embed.add_field(name='Episode', value=find['episode'], inline=True)
			embed.add_field(name='Status', value=find['episode'], inline=True)
			embed.add_field(name='Score', value=find['score'], inline=True)
			embed.add_field(name='Start Date', value=find['startDate'], inline=True)
			embed.add_field(name='End Date', value=find['endDate'], inline=True)
			fmtSyn = '```{}```'.format(str(find['synopsis']))
			await bot.delete_message(msg)
			await bot.delete_message(msg2)
			msg = await bot.say(embed=embed)
			msg2 = await bot.say(fmtSyn)
		elif '✅' in str(res.reaction.emoji):
			await bot.delete_message(ctx.message)
			await bot.delete_message(msg)
			await bot.delete_message(msg2)
			break
