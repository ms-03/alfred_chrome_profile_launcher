on alfred_script(q)
	set profile to q

	if application "Google Chrome" is not running then
		tell application "Google Chrome"
			activate
			close windows
		end tell
	end if

	tell application "System Events" to tell process "Google Chrome"
		if profile = "SECRET" then
			click menu bar 1's menu bar item 3's menu 3
		else
			click menu bar 1's menu bar item 8's menu 1's menu item profile
		end if
	end tell

end alfred_script
