# -*- coding: utf-8 -*-

__author__ = "Brett Feltmate"

import klibs
from klibs import P
from klibs.KLConstants import STROKE_CENTER, CIRCLE_BOUNDARY
from klibs.KLUtilities import deg_to_px
from klibs.KLGraphics import KLDraw as kld
from klibs.KLCommunication import message
from klibs.KLBoundary import BoundaryInspector

import ExpAssets.Resources.code.KLAudio as kla


BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
GRAY = (45, 45, 45, 255)

class ProAnti_IOR_Removal(klibs.Experiment):

	def setup(self):

		# Useful coordinates
		offset = deg_to_px(6.2)
		self.locs = {
			'fix': P.screen_c,
			'left': (P.screen_c[0] - offset, P.screen_c[1]),
			'right': (P.screen_c[0] + offset, P.screen_c[1]),
		}

		# Stimulus sizing properties
		self.stim_sizes = {
			'box': deg_to_px(1.5),
			'fix': deg_to_px(0.5),
			'circle': deg_to_px(0.9),
			'target': deg_to_px(1.3),
			'thickness': deg_to_px(0.1)
		}

		# Visual assets
		stroke = [STROKE_CENTER, self.stim_sizes['thickness'], BLACK]
		self.stimuli = {
			'fixation': kld.FixationCross(size=self.stim_sizes['fix'], thickness=self.stim_sizes['thickness'], fill=BLACK),
			'fix_circ': kld.Ellipse(width=self.stim_sizes['circle'], stroke=stroke),
			'target': kld.FixationCross(size=self.stim_sizes['target'], thickness=self.stim_sizes['thickness'], fill=BLACK),
			'targ_circ': kld.Ellipse(width=self.stim_sizes['target'], stroke=stroke)
		}



		# Eyelink boundaries for gaze/saccade monitoring
		radius = self.stim_sizes['box'] / 2.0 # radius of boundary, 1/2 width of placeholder
		self.bi = BoundaryInspector()  # Inspector class
		for loc in ['left', 'fix', 'right']:
			self.bi.add_boundary(label=loc, bounds=(self.locs[loc], radius), shape=CIRCLE_BOUNDARY)

		# Spawn tone object to play when drift correct fails
		self.drift_fail_alert = kla.Tone(duration=60, frequency=2000, fade_in=10, fade_out=10)


		# Error messages
		self.messages = {
			'saccade_error': message("saccade error", location=self.locs['fix'], registration=5),
			'saccade_early': message("saccade early", location=self.locs['fix'], registration=5)
		}














		"""
		locs
			screen centre
			peripherals

		Placeholders:
			gaze boundary boxes
				1.5 dva
				white fill, cued by graying
				1 at fix, 2 flanking by 6.2
			fix stimuli
				cross
					0.5 dva
					black
					centered in fix box
				black circle
					0.9 dva
					black
					centered on fixation
			targets
				1.3 dva
				black
				composed of encircled cross or x

		tone
			2000hz sine
			210ms

		response collector
			keyboard
			/ or z
			mapped to identity
			counter balanced



		:return:
		"""

		pass

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
