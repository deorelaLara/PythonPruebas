#ejemplo de diccionarios
alien_0 = {
                'color':'green',
        'points': '5'

}

#print(alien_0['color'])

new_points = alien_0['points']
print('You just earned: ' + str(new_points) + ' points!')
print('##################################')
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print('###################################')
print('The alien is ' + alien_0['color'] )
#CAMBIAMOS EL COLOR
alien_0['color'] = 'Yellow'
print('Now the alien is: ' + alien_0['color'])

print('####################################')
alien_0['speed'] = 'medium'
print(alien_0)
print('Original Position: ' + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fast alien
    x_increment =3

alien_0['x_position'] = alien_0['x_position'] + x_increment
#The new position is the old position plus the x_increment
print('New x-Position:' + str(alien_0['x_position']))

print('#####################################')
del alien_0['points']
print(alien_0)
