# -*- coding: utf-8 -*-

from model.group import Group



def test_testAddGroup1(ap):
    old_groups = ap.group.get_group_list()
    group = Group(name="test1", header="test2", footer="test4")
    ap.group.create(group)
    new_groups = ap.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



