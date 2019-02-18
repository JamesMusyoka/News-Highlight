
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):

   title = StringField('Review title',validators=[Required()])
   blog = TextAreaField('headings')
   submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = StringField('Comment title', validators = [Required()])
    comment = TextAreaField('blog a Comment',validators = [Required()])
    submit = SubmitField('Add Comment')