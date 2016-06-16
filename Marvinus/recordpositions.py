import positions
from effector import Effector
import time

PORT = 9559
IP = "10.0.1.7" 



effector = Effector(IP, PORT)
effector.get_ready()
effector.hit_key('F')



effector.hit_key('C')
time.sleep(0.2)
effector.hit_key('D')
time.sleep(0.2)
effector.hit_key('E')
time.sleep(0.2)
effector.hit_key('F')
time.sleep(0.2)
effector.hit_key('G')
time.sleep(0.2)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('A')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('F')
time.sleep(0.3)
effector.hit_key('F')
time.sleep(0.3)
effector.hit_key('F')
time.sleep(0.3)
effector.hit_key('F')
time.sleep(0.3)
effector.hit_key('E')
time.sleep(0.3)
effector.hit_key('E')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('G')
time.sleep(0.3)
effector.hit_key('C')
time.sleep(0.3)

while True:
    effector.hit_key('C')
    time.sleep(0.3)
    effector.hit_key('G')
    time.sleep(0.3)
    effector.hit_key('D')
    time.sleep(0.3)
    effector.hit_key('A')
    time.sleep(0.3)
    effector.hit_key('B')
    time.sleep(0.3)
    effector.hit_key('E')
    time.sleep(0.3)
    effector.hit_key('F')
    time.sleep(0.3)
    effector.hit_key('Ch')
    time.sleep(0.3)


effector.proxy.stiffnessInterpolation('RHand', 1, 0.01)


while True:
    arm,position,default = positions.get_position('D' )
    leftArmEffector.move_to_absolute_position(position,default,arm)
    time.sleep(0.3)
    arm,position,default = positions.get_position('C' )
    leftArmEffector.move_to_absolute_position(position,default,arm)
    time.sleep(0.3)
    arm,position,default = positions.get_position('E' )
    leftArmEffector.move_to_absolute_position(position,default,arm)
    time.sleep(0.3)
    arm,position,default = positions.get_position('F' )
    leftArmEffector.move_to_absolute_position(position,default,arm)
    time.sleep(0.3)

#leftArmEffector.proxy.setStiffnesses("Body", 1)

#leftArmEffector.proxy.stiffnessInterpolation('LArm', 1, 0.01)

#arm, pos, hand, rot = positions.get_default_position('LArm')
#leftArmEffector.move_to_absolute_position(pos, rot)

#names = ["LArm"]
#keys2 = [0.8160459995269775, 0.5844120979309082, -1.5846638679504395, -0.570605993270874, 1.1657980680465698, 0.9139999747276306]


effector.proxy.stiffnessInterpolation('LWrist', 0, 0.01)
effector.proxy.stiffnessInterpolation('LWristYaw', 0, 0.01)
effector.proxy.stiffnessInterpolation('LArm', 0, 0.01)
effector.proxy.closeHand('LHand')

effector.proxy.stiffnessInterpolation('LHand', 1, 0.01)
effector.get_absolute_position('LArm')


RARM
[0.6121079921722412, -0.7563040256500244, -0.05066394805908203, 0.2853660583496094, 0.5077121257781982, 0.9455999732017517]

[0.7838320732116699]
[-0.08901405334472656]


B
[0.5430779457092285, -0.638185977935791, -0.06753802299499512, 0.08287787437438965, 0.7838320732116699, 0.9455999732017517]



[0.7838320732116699]

[0.48938798904418945, -0.6688659191131592, -0.3068418502807617, 0.10895586013793945, 0.7838320732116699, 0.9455999732017517]

G
[0.4817180633544922, -0.42342591285705566, -0.08594608306884766, 0.08594608306884766, 0.7838320732116699, 0.9459999799728394]   





C:
[0.2990880012512207, 0.9188239574432373, 0.41567206382751465, -0.30368995666503906, -0.127363920211792, 0.9139999747276306]


D
[0.39879798889160156, 0.8145120143890381, 0.49697399139404297, -0.30675792694091797, -0.2728039264678955, 0.9139999747276306]

E:
-0.2028039264678955
[0.4110701084136963, 0.7424139976501465, 0.43868207931518555, -0.3159620761871338, -0.9112381935119629, 0.9139999747276306]

BODY DEFAULT
[-0.02611994743347168, 0.14568805694580078, 0.39879798889160156, 0.8145120143890381, 0.49697399139404297, -0.30675792694091797, -0.3728039264678955, 0.9139999747276306, -0.8298521041870117, 0.3467259407043457, -1.535889744758606, 1.2915860414505005, 0.9225810170173645, -8.26716423034668e-05, -0.8298521041870117, -0.3803901672363281, -1.535889744758606, 1.3883118629455566, 0.8621501922607422, 0.04206877946853638, 1.0262880325317383, -0.24701595306396484, 0.6457719802856445, 1.3745059967041016, 1.0354080200195312, 0.7963999509811401]




effector.proxy.setAngles('LWristYaw',[-0.3728039264678955],0.1)


























c
[0.9801840782165527, 0.7454819679260254, -1.5371098518371582, -0.5782761573791504, 1.3529460430145264, 0.9139999747276306]
c not
[0.9817180633544922, 0.7500841617584229, -1.5355758666992188, -0.5782761573791504, 0.9663779735565186, 0.9139999747276306]
d
[0.951038122177124, 0.6887240409851074, -1.4404678344726562, -0.5936160087585449, 1.2885180711746216, 0.9139999747276306]
d not
[0.9541060924530029, 0.6963939666748047, -1.4404678344726562, -0.590548038482666, 0.9341640472412109, 0.9139999747276306]
e[0.8804740905761719, 0.610490083694458, -1.3837099075317383, -0.5966839790344238, 1.345276117324829, 0.9139999747276306]
e not
[0.877406120300293, 0.6181600093841553, -1.3852438926696777, -0.5936160087585449, 0.98785400390625, 0.9143999814987183]
f
[0.7838320732116699, 0.5153820514678955, -1.3269519805908203, -0.5982179641723633, 1.4557241201400757, 0.9143999814987183]
f not
[0.7838320732116699, 0.5322561264038086, -1.3300199508666992, -0.5890140533447266, 1.0737581253051758, 0.9139999747276306]



default overall
[0.9356980323791504, 0.6825881004333496, -1.392913818359375, -0.5629360675811768, 0.98785400390625, 0.9143999814987183]


[0.9464361667633057, 0.6933259963989258, -1.569324016571045, -0.5721399784088135, 1.4373160600662231, 0.9139999747276306]

[0.9556400775909424, 0.6273641586303711, -1.569324016571045, -0.5721399784088135, 1.4373160600662231, 0.9139999747276306]

[0.9617760181427002, 0.5399260520935059, -1.569324016571045, -0.5721399784088135, 1.4373160600662231, 0.9139999747276306]

[0.9387660026550293, 0.4632260799407959, -1.569324016571045, -0.5721399784088135, 1.4373160600662231, 0.9139999747276306]

[0.8988821506500244, 0.5798101425170898, -1.5539841651916504, -0.5767421722412109, 1.254770040512085, 0.9139999747276306]