	photo =FileField(
		validators=[
			FileAllowed(photos, 'Only images are allowed'),
			FileRequired('File field should not be empty')
		]
	)