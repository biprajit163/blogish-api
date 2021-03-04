# blogish-api
A Backend developed with Django Rest Framework that allows the user to make HTTP calls allowing them to Make, Create, Get, Delete Blogs!
This Api is structured so the user can make calls to get all the users, blogs created, and a features to get comments on each blog. These are all elational models with the user to blog relation being a one-to-many and the blog to comment being a one-to-many but it is an embedded model. 

### future goals
utalize djangos built in token auth to hash user password and allow for a feature that allows users to change/update their password via email confirmation.


