#https://help.alibre.com/articles/#!alibre-help-v23/useful-dialogs
Win = Windows()
Win.InfoDialog('I am about to create a part', 'My Script')
Win.ErrorDialog("Oops. That didn't go as planned", 'My Script')
# returns True for 'yes' and False for 'no'
print Win.QuestionDialog('Shall I stop?', 'My Script')