#import ROS

print "Move arm to starting position"
print "Use CVread to scan bottles"
print

node=["green","red","yellow","blue"]

recipe=1

if recipe==0:
    print "Recipe 1:"
    print
    for i in range(4):
        if node[i]=="green":
            bottle1=i
        elif node[i]=="red":
            bottle2=i
    print "Move arm to pregrip position for node",bottle1
    print "Grip bottle",bottle1
    print "Move arm to safe position",bottle1
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle1
    print "Place bottle back at node",bottle1
    print "Move arm to pregrip position for node",bottle1

    print "Move arm to pregrip position for node",bottle2
    print "Grip bottle",bottle2
    print "Move arm to safe position",bottle2
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle2
    print "Place bottle back at node",bottle2
    print "Move arm to pregrip position for node",bottle2

    print "Move arm back to starting position"
elif recipe==1:
    print "Recipe 2:"
    print
    for i in range(4):
        if node[i]=="yellow":
            bottle1=i
        elif node[i]=="blue":
            bottle2=i
    print "Move arm to pregrip position for node",bottle1
    print "Grip bottle",bottle1
    print "Move arm to safe position",bottle1
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle1
    print "Place bottle back at node",bottle1
    print "Move arm to pregrip position for node",bottle1

    print "Move arm to pregrip position for node",bottle2
    print "Grip bottle",bottle2
    print "Move arm to safe position",bottle2
    print "Move arm above glass"
    print "Pour"
    print "Move arm to safe position",bottle2
    print "Place bottle back at node",bottle2
    print "Move arm to pregrip position for node",bottle2

    print "Move arm back to starting position"