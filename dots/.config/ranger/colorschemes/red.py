# Ranger theme
# Mod of Spacecolors

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Default(ColorScheme):
	def use(self, context):
		fg, bg, attr = default_colors

		if context.reset:
			return default_colors

		elif context.in_browser:
			if context.selected:
				attr = reverse
			else:
				attr = normal
			if context.empty or context.error:
				bg = black
			if context.border:
				attr |= bold
				fg = black
			if context.media:
				if context.image:
					fg = yellow
				else:
					fg = green
			if context.container:
				attr |= bold
				fg = magenta
            # !!!
			if context.directory:
				attr |= bold
				fg = red
			elif context.executable and not \
					any((context.media, context.container,
						context.fifo, context.socket)):
				attr |= bold
				fg = green
			if context.socket:
				fg = magenta
			if context.fifo or context.device:
				fg = red
				if context.device:
					attr |= bold
			if context.link:
				fg = context.good and cyan or magenta
			if context.tag_marker and not context.selected:
				attr |= bold
				if fg in (red, magenta):
					fg = white
				else:
					fg = magenta
			if not context.selected and (context.cut or context.copied):
				fg = black
				attr |= bold
			if context.main_column:
				if context.selected:
					attr |= normal
				if context.marked:
					attr |= bold
					fg = magenta
			if context.badinfo:
				if attr & reverse:
					bg = magenta
				else:
					fg = magenta

		elif context.in_titlebar:
			attr |= bold
			if context.hostname:
				attr |= bold
				fg = context.bad and black or black
			elif context.directory:
				fg = magenta
			elif context.tab:
				if context.good:
					bg = green
			elif context.link:
				fg = cyan

		elif context.in_statusbar:
			if context.permissions:
				if context.good:
					fg = magenta
				elif context.bad:
					fg = cyan
			if context.marked:
				attr |= bold | reverse
				fg = yellow
			if context.message:
				if context.bad:
					attr |= bold
					fg = yellow

		if context.text:
			if context.highlight:
				attr |= reverse

		if context.in_taskview:
			if context.title:
				fg = blue

			if context.selected:
				attr |= reverse

		return fg, bg, attr
