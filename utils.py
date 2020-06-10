# these are unique graph specifications of differing sizes
EXPERIMENTAL_ATTS = [['Young', 'Smiling'],
					 ['Young', 'Mustache', 'Smiling'],
					 ['Young', 'Mustache', 'Smiling', 'Bald'],
					 ['Young', 'Mustache', 'Smiling', 'Bald', 'Male'],
					 ['Young', 'Mustache', 'Smiling', 'Bald', 'Male'],
					 ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					 ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses', 'Wearing_Lipstick']
					 ]

EXPERIMENTAL_ATTS_2 = [['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					   ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					   ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					   ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					   ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses'],
					   ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses']
					 ]

EXPERIMENTAL_ATTS_3 = ['Young', 'Mustache', 'Smiling', 'Bald', 'Male', 'Eyeglasses', 'Wearing_Lipstick', 'Mouth_Slightly_Open']
					 

EXPERIMENTAL_EDGES = [[('Young', 'Smiling')],
					  [('Young', 'Smiling'),('Young','Mustache')],
					  [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald')],
					  [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald'),('Male', 'Mustache')],
					  [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald'),('Male', 'Mustache'),('Male','Smiling')],
					  [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald'),('Male', 'Mustache'),('Male','Smiling'),('Young', 'Eyeglasses')],
					  [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald'),('Male', 'Mustache'),('Male','Smiling'),('Young', 'Eyeglasses'), ('Male', 'Wearing_Lipstick')]
					  ]

EXPERIMENTAL_EDGES_2 = [[('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Young', 'Male'), ('Young', 'Eyeglasses')],
					  [('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Male', 'Eyeglasses'), ('Young', 'Eyeglasses'), ('Male', 'Bald')],
					  [('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Male', 'Eyeglasses'), ('Young', 'Eyeglasses'), ('Male', 'Bald'), ('Male', 'Smiling')],
					  [('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Male', 'Eyeglasses'), ('Young', 'Eyeglasses'), ('Male', 'Bald'), ('Male', 'Smiling'), ('Male', 'Eyeglasses')],
					  [('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Male', 'Eyeglasses'), ('Young', 'Eyeglasses'), ('Male', 'Bald'), ('Male', 'Smiling'), ('Male', 'Eyeglasses'), ('Male', 'Mustache')],
					  [('Young', 'Mustache'), ('Young', 'Smiling'), ('Young', 'Bald'), ('Male', 'Eyeglasses'), ('Young', 'Eyeglasses'), ('Male', 'Bald'), ('Male', 'Smiling'), ('Male', 'Eyeglasses'), ('Male', 'Mustache'), ('Mustache', 'Smiling')]
					  ]

EXPERIMENTAL_EDGES_3 = [('Young', 'Smiling'),('Young', 'Mustache'),('Young', 'Bald'),('Male', 'Mustache'),('Male','Smiling'),('Young', 'Eyeglasses'), ('Male', 'Wearing_Lipstick'), ('Smiling', 'Mouth_Slightly_Open')]
