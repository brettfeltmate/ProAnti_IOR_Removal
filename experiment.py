# -*- coding: utf-8 -*-

__author__ = "Brett Feltmate"

import klibs
import sdl2
from klibs import P
from klibs.KLConstants import STROKE_CENTER, CIRCLE_BOUNDARY
from klibs.KLUtilities import deg_to_px
from klibs.KLGraphics import KLDraw as kld
from klibs.KLGraphics import fill, blit, flip
from klibs.KLCommunication import message
from klibs.KLBoundary import BoundaryInspector
from klibs.KLResponseCollectors import KeyMap, KeyPressResponse
from random import shuffle

import ExpAssets.Resources.code.KLAudio as kla


BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GRAY = (45, 45, 45, 255)

THICKNESS = 'thickness'
BOX = 'box'
FIX = 'fix'
CUE = 'cue'
FIX_BORDER = 'fix_border'
FIXATION = 'fixation'
TARGET = 'target'
TARG_X = 'x'
TARG_CROSS = 'cross'
TARG_BORDER = 'targ_border'
LEFT = 'left'
RIGHT = 'right'


class ProAnti_IOR_Removal(klibs.Experiment):

	def setup(self):

		# Useful coordinates
		offset = deg_to_px(6.2)
		self.locs = {
			FIX: P.screen_c,
			LEFT: (P.screen_c[0] - offset, P.screen_c[1]),
			RIGHT: (P.screen_c[0] + offset, P.screen_c[1]),
		}

		# Stimulus sizing properties
		self.stim_sizes = {
			BOX: deg_to_px(1.5),
			FIX: deg_to_px(0.5),
			CUE: deg_to_px(0.5),
			FIX_BORDER: deg_to_px(0.9),
			TARGET: deg_to_px(1.3),
			THICKNESS: deg_to_px(0.1)
		}

		# Visual assets
		stroke = [STROKE_CENTER, self.stim_sizes[THICKNESS], BLACK]


		self.placeholders = {
			LEFT: kld.Rectangle(width=self.stim_sizes[BOX], stroke=stroke, fill=WHITE),
			FIX: kld.Rectangle(width=self.stim_sizes[BOX], stroke=stroke, fill=WHITE),
			RIGHT: kld.Rectangle(width=self.stim_sizes[BOX], stroke=stroke, fill=WHITE),
		}

		self.stimuli = {
			FIXATION: kld.FixationCross(size=self.stim_sizes[FIX], thickness=self.stim_sizes[THICKNESS], fill=BLACK),
			FIX_BORDER: kld.Ellipse(width=self.stim_sizes[FIX_BORDER], stroke=stroke),
			CUE: kld.Asterisk(size=self.stim_sizes[CUE], thickness=self.stim_sizes[THICKNESS], fill=BLACK),
			TARG_CROSS: kld.FixationCross(size=self.stim_sizes[TARGET], thickness=self.stim_sizes[THICKNESS], fill=BLACK),
			TARG_X: kld.FixationCross(size=self.stim_sizes[TARGET], thickness=self.stim_sizes[THICKNESS], fill=BLACK, rotation=45),
			TARG_BORDER: kld.Ellipse(width=self.stim_sizes[TARGET], stroke=stroke)
		}



		# Eyelink boundaries for gaze/saccade monitoring
		radius = self.stim_sizes[BOX] / 2.0 # radius of boundary, 1/2 width of placeholder
		self.bi = BoundaryInspector()  # Inspector class
		for loc in [LEFT, FIX, RIGHT]:
			self.bi.add_boundary(label=loc, bounds=(self.locs[loc], radius), shape=CIRCLE_BOUNDARY)

		# Spawn tone object to play when drift correct fails
		self.drift_fail_alert = kla.Tone(duration=60, frequency=2000, fade_in=10, fade_out=10)


		'''
		Error messages
		
		- pre-cue saccade
		- wrong saccade to/from cue*
		- failure to saccade to/from cue before CB
		- failure to saccade to fix before targ
		
		* procedurally construct string, respecting pro/anti condition
		'''

		self.error_messages = {
			'saccade_error': message("saccade error", location=self.locs[FIX], registration=5),
			'saccade_early': message("saccade early", location=self.locs[FIX], registration=5)
		}




		self.keymap = KeyMap(
			'key_response',
			['z', '/'],
			['z', '/'],
			[sdl2.SDLK_z, sdl2.SDLK_BACKSLASH]
		)


	def block(self):
		"""
		instructions

		block notice
			practice
			testing

		:return:
		"""
		pass

	def setup_response_collector(self):
		"""
		keyboard
		/ or z, mapped to target identity, cross balanced

		:return:
		"""

		pass

	def trial_prep(self):



		"""
		set up events
			get cue loc
			get target loc
			get target identity
			determine if removal trial

		event manager
			cue on 250ms after drift
			cue off 90ms after on
			target on 1000ms post cue onset

		drift correct
			function
			trial() called on return



		:return:
		"""


		pass

	def trial(self):
		"""
		blit 'base' array, with encircled fix
		cue on:
			present cue
		cue off:
			remove cue


		:return:
		"""

		return {
			"block_num": P.block_number,
			"trial_num": P.trial_number
		}

	def trial_clean_up(self):
		pass

	def clean_up(self):
		pass

	def present_display(self, trial_state=None, show_placeholders=True):
		fill()

		blit(self.placeholders[FIX], location=self.locs[FIX], registration=5)
		blit(self.stimuli[FIXATION], location=self.locs[FIX], registration=5)

		if trial_state != 'drift_correct':
			blit(self.stimuli[FIX_BORDER], location=self.locs[FIX], registration=5)

		if show_placeholders:
			for loc in [LEFT, RIGHT]:
				blit(self.placeholders[loc], location=self.locs[loc], registration=5)

		if trial_state == 'cue_on':
			blit(self.stimuli[CUE], location=self.locs[self.cue_loc], registration=5)

		if trial_state == 'target_on':
			blit(self.stimuli[self.target_type], location=self.locs[self.target_loc], registration=5)
			blit(self.stimuli[TARG_BORDER], location=self.locs[self.target_loc], registration=5)

		flip()


	def drift_correct(self):
		"""
		blits 'base' array
		listens for spacebar
		on press, checks if gaze centered
		if true
			continue
		else
			beep
			repeat process

		:return: none
		"""

		pass
