# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Graph_

import flatbuffers

class ContextEdges(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsContextEdges(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ContextEdges()
        x.Init(buf, n + offset)
        return x

    # ContextEdges
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ContextEdges
    def NextToken(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def NextTokenLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def Child(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def ChildLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def LastLexicalUse(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def LastLexicalUseLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def LastUse(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def LastUseLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def LastWrite(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def LastWriteLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def ReturnsTo(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def ReturnsToLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ContextEdges
    def ComputesFrom(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .Edge import Edge
            obj = Edge()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ContextEdges
    def ComputesFromLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ContextEdgesStart(builder): builder.StartObject(7)
def ContextEdgesAddNextToken(builder, nextToken): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nextToken), 0)
def ContextEdgesStartNextTokenVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddChild(builder, child): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(child), 0)
def ContextEdgesStartChildVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddLastLexicalUse(builder, lastLexicalUse): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(lastLexicalUse), 0)
def ContextEdgesStartLastLexicalUseVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddLastUse(builder, lastUse): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(lastUse), 0)
def ContextEdgesStartLastUseVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddLastWrite(builder, lastWrite): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(lastWrite), 0)
def ContextEdgesStartLastWriteVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddReturnsTo(builder, returnsTo): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(returnsTo), 0)
def ContextEdgesStartReturnsToVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesAddComputesFrom(builder, computesFrom): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(computesFrom), 0)
def ContextEdgesStartComputesFromVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ContextEdgesEnd(builder): return builder.EndObject()
