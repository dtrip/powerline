#!/usr/bin/env python

from powerline.theme import requires_segment_info

@requires_segment_info
def new_last_status(pl, segment_info):
	'''Return last exit code.

	Highlight groups used: ``exit_fail``
	'''
	# if not segment_info['args'].last_exit_code:
		# return None
        if not segment_info['args'].last_exit_code:
            return str(" ")
	return [{'contents': str(segment_info['args'].last_exit_code), 'highlight_groups': ['exit_fail']}]


