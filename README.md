# sample-website-django

#using Mosh https://www.youtube.com/watch?v=_uQrJ0TkZlc&feature=youtu.be
Creatinmg Admin User (05:37)


Tables needed

courses
    name
    course_code
    price
    days
    start_time
    end_time
    instructor_id (fk)
    


instructors
    instructor_id
    fname
    lname

Course(id, name, level, day, start time, end time)

students

users


#From Demola

If a User Registers successfully, 
    we need to redirect user to a login page
else
    raise Form is not valid and  remain on page with error (Use Django messages)