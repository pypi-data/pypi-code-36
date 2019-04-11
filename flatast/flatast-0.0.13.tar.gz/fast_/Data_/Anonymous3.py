# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Data_

import flatbuffers

class Anonymous3(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsAnonymous3(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Anonymous3()
        x.Init(buf, n + offset)
        return x

    # Anonymous3
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Anonymous3
    def Element(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Element import Element
            obj = Element()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Log(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Log import Log
            obj = Log()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Delta(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Delta import Delta
            obj = Delta()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Pairs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Pairs import Pairs
            obj = Pairs()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Slices(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Slices import Slices
            obj = Slices()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Bugs(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Bugs import Bugs
            obj = Bugs()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Anonymous3
    def Graph(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from fast_.Graph import Graph
            obj = Graph()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Anonymous3Start(builder): builder.StartObject(7)
def Anonymous3AddElement(builder, element): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(element), 0)
def Anonymous3AddLog(builder, log): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(log), 0)
def Anonymous3AddDelta(builder, delta): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(delta), 0)
def Anonymous3AddPairs(builder, pairs): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(pairs), 0)
def Anonymous3AddSlices(builder, slices): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(slices), 0)
def Anonymous3AddBugs(builder, bugs): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(bugs), 0)
def Anonymous3AddGraph(builder, graph): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(graph), 0)
def Anonymous3End(builder): return builder.EndObject()
