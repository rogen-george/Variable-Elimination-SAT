
# Celebrity data set

CELEB_DATASET = 'list_attr_celeba.csv'

file = CELEB_DATASET
edges = [('Young', 'Eyeglasses'), ('Young', 'Bald'), ('Young', 'Mustache'), ('Male', 'Mustache'),
                  ('Male', 'Smiling'), ('Young', 'Smiling'), ('Male', 'Wearing_Lipstick')]

#edges = [('Young', 'Eyeglasses'), ('Young', 'Bald'), ('Young', 'Mustache'), ('Male', 'Mustache'),
#                   ('Male', 'Smiling'), ('Male', 'Wearing_Lipstick'), ('Young', 'Mouth_Slightly_Open'),
#                   ('Young', 'Narrow_Eyes'), ('Male', 'Narrow_Eyes'), ('Smiling', 'Narrow_Eyes'),
#                   ('Smiling', 'Mouth_Slightly_Open'), ('Young', 'Smiling')]

KEEP_ATTS = ['Young', 'Male', 'Eyeglasses', 'Bald', 'Mustache',
             'Smiling', 'Wearing_Lipstick']
