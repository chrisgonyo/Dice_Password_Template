# Dice Password Template
This software is intended for educational purposes only. The author does NOT
recommend you use this software to generate actual passwords. Template output on the
command line can be retrieved by a sophisticated attacker which significantly lowers
password entropy.  

### Concept
Create a password by combining entropy from your operating system and dice rolls.

User inputs number of dice sides and number of dice rolled to create a template.

User rolls dice and uses the template to determine password values.

Entropy calculation and approximate brute-force cost increment as you generate
additional templates and increase password length.


### Brute Force Calculation
A common metric to evaluate password strength revolves around a "Time to Brute-Force"
calculation. This metric is logically flawed because it assumes a fixed hash rate.
Cost to Brute Force should be used to estimate password strength instead.

The Brute Force Calculation used in this app is quite basic and has not been tested
in the wild. It assumes the attacker has intercepted a password hash and attempting
to brute force using HashCat on an AWS machine (g4dn.xlarge) with an hourly run
cost of $8.10. It assumes that the password will be brute-forced after 50% of
all possible combinations have been tried.

HashCat benchmark hash rates were pulled from online articles. The author of this
program has not verified these results personally. Consider using this rough metric
to demonstrate the importance of password length. If the attacker has access to
a FPGA cluster the cost value would be reduced significantly.


### Warning
This software is intended for educational purposes only. Template output on the
command line can be retrieved by a sophisticated attacker which significantly lowers
password entropy. If you really want to use this software consider running in TailsOS
offline and reboot machine prior to reconnecting to the internet. This has not
been tested and should still be considered risky.
