{"filter":false,"title":"simple_topic_publisher.py","tooltip":"/simple_topic_publisher/src/simple_topic_publisher.py","undoManager":{"mark":35,"position":35,"stack":[[{"start":{"row":0,"column":0},"end":{"row":14,"column":14},"action":"insert","lines":["#! /usr/bin/env python","","import rospy","from std_msgs.msg import Int32 ","","rospy.init_node('topic_publisher')","pub = rospy.Publisher('/counter', Int32, queue_size=1)","rate = rospy.Rate(2)","count = Int32()","count.data = 0","","while not rospy.is_shutdown(): ","  pub.publish(count)","  count.data += 1","  rate.sleep()"],"id":1}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":31},"action":"remove","lines":["counter"],"id":2},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["c"]}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["m"],"id":3}],[{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["d"],"id":4}],[{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["_"],"id":5}],[{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["v"],"id":6}],[{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["e"],"id":7}],[{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["l"],"id":8}],[{"start":{"row":6,"column":34},"end":{"row":6,"column":39},"action":"remove","lines":["Int32"],"id":9},{"start":{"row":6,"column":34},"end":{"row":6,"column":39},"action":"insert","lines":["Twist"]}],[{"start":{"row":8,"column":0},"end":{"row":9,"column":14},"action":"remove","lines":["count = Int32()","count.data = 0"],"id":10},{"start":{"row":8,"column":0},"end":{"row":8,"column":13},"action":"insert","lines":["var = Twist()"]}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":17},"action":"remove","lines":["count.data += 1"],"id":11},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["v"]}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":["a"],"id":12}],[{"start":{"row":8,"column":13},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":["v"],"id":14}],[{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["a"],"id":15}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"insert","lines":["r"],"id":16}],[{"start":{"row":9,"column":3},"end":{"row":9,"column":4},"action":"insert","lines":["."],"id":17}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":5},"action":"insert","lines":["x"],"id":18}],[{"start":{"row":9,"column":5},"end":{"row":9,"column":6},"action":"insert","lines":[" "],"id":19}],[{"start":{"row":9,"column":6},"end":{"row":9,"column":7},"action":"insert","lines":["="],"id":20}],[{"start":{"row":9,"column":7},"end":{"row":9,"column":8},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["0"],"id":22}],[{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["."],"id":23}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["5"],"id":24}],[{"start":{"row":13,"column":3},"end":{"row":13,"column":4},"action":"remove","lines":["a"],"id":25}],[{"start":{"row":13,"column":2},"end":{"row":13,"column":3},"action":"remove","lines":["v"],"id":26}],[{"start":{"row":13,"column":2},"end":{"row":14,"column":2},"action":"remove","lines":["","  "],"id":27}],[{"start":{"row":12,"column":14},"end":{"row":12,"column":19},"action":"remove","lines":["count"],"id":28},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"insert","lines":["v"]}],[{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"insert","lines":["a"],"id":29}],[{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"insert","lines":["r"],"id":30}],[{"start":{"row":8,"column":0},"end":{"row":10,"column":0},"action":"remove","lines":["var = Twist()","var.x = 0.5",""],"id":31},{"start":{"row":8,"column":0},"end":{"row":10,"column":69},"action":"insert","lines":["move = Twist()","move.linear.x = 0.5 #Move the robot with a linear velocity in the x axis","move.angular.z = 0.5 #Move the with an angular velocity in the z axis"]}],[{"start":{"row":10,"column":69},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":32}],[{"start":{"row":13,"column":14},"end":{"row":13,"column":17},"action":"remove","lines":["var"],"id":33},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"insert","lines":["m"]}],[{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"insert","lines":["o"],"id":34}],[{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"insert","lines":["v"],"id":35}],[{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"insert","lines":["e"],"id":36}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":13,"column":18},"end":{"row":13,"column":18},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1538453122000,"hash":"211b676258ded08eceac18fccdd45e53da3ec635"}