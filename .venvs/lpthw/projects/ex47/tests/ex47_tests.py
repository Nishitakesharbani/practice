from nose.tools import*
from ex47.game import room

def test_room():
    gold =room("GoldRoom",
                """This room has gold in it you can grab.There,s a door to the north""")
    assert_equal(gold.name,"Goldroom")
    assert_equal(gold.paths,{})

def test_room_paths():
    center=room("center","Test room is in the center")
    north=room("center","Test room is in the north")
    south=room("center","Test room is in the south")

    center.add_paths({'north': north,'south':south})
    assert_equal(center.go('north'),north)
    assert_equal(center.go('south'),south)

def test_map():
    start=room("Start", "you can go to west and down a hole")
    west=room("Tress","There is a tree here ,you can go to east")
    down=room("Dungeon","It is a dark down here, you can go up")

    start.add_paths({'west':west,'down':down})
    west.add_paths({'east':start})
    down.add_paths({'up':start})