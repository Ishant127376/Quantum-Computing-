
import cmath

# Convert to polar form
z = 2 + 3j  # Complex number in rectangular form
polar_form = cmath.polar(z)
print(polar_form)  
# Output is (magnitude, phase in radians)


# Convert back to rectangular form
magnitude, phase = polar_form
rectangular_form = cmath.rect(magnitude, phase)
print(rectangular_form)  