#!/usr/bin/python3 

# Module imports go here
import json 
import os 
import sys
import time

#Classes go herer

class Player:
	def __init__(self, name, title_class, description, icon, skill1, skill2, skill3, skill4, skill5, condition, health, cognition, psyche, social, discipline):
		name = self.name
		title_class = self.title_class 
		description = self.description
		icon = self.icon
		skill1 = self.skill1
		skill2 = self.skill2
		skill3 = self.skill3
		skill4 = self.skill4
		skill5 = self.skill5
		condition = self.condition
		health = self.health
		cognition = self.cognition
		psyche = self.psyche
		social = self.social
		discipline = self.discipline
		inventory = [" "]
		level = 1
		xp = 0
		missions = [" "]
		
		
	


class Skill:
	def __init__(self, name, description, attribute, category, icon):
		name = self.name
		description = self.description
		level = self.level
		attribute = self.attribute
		category = self.category
		icon = self.icon
		xp = 0
		level = 1
		missions = [" "]
		
		
		
class Item:
	def __init__(self, name, description, category, quantity, consumable, icon):
		name = self.name
		description = self.description
		category = self.category
		quantity = self.quantity
		consumable = self.consumable
		icon = self.icon
		
		
		
class Mission:
	def __init__(self):
		pass
		
