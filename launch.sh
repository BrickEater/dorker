tmux popup \
	-xC \
	-yC \
	-w80% \
	-h75% \
	-E \
	-d '#{pane_current_path}' "source /home/goblin/Repos/learning/python/dorker/venv/bin/activate && python 001.py"
