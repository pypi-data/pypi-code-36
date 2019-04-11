from rb.core.word import Word
from rb.comprehension.utils.graph.cm_node_type import CmNodeType


class CmNodeDO:

    def __init__(self, word: Word, node_type: CmNodeType) -> None:
        self.word = word
        self.node_type = node_type
        self.is_active = False
        self.activation_score = 0.0

    def get_word(self) -> Word:
        return self.word
    

    def get_node_type(self) -> CmNodeType:
        return self.node_type


    def set_node_type(self, node_type: CmNodeType) -> None:
        self.node_type = node_type

    
    def is_active(self) -> bool:
        return self.is_active


    def activate(self) -> None:
        self.is_active = True


    def deactivate(self) -> None:
        self.is_active = False


    def get_activation_score(self) -> float:
        return self.activation_score 


    def set_activation_score(self, activation_score: float) -> None:
        self.activation_score = activation_score

    
    def increment_activation_score(self) -> None:
        self.activation_score += 1


    def __repr__(self):
        return self.word.lemma + " (" + str(self.node_type) + " - " + \
                str(self.activation_score) + " - " + str(self.is_active) + ")"


    def __str__(self):
        return self.word.lemma + " (" + str(self.node_type) + " - " + \
                str(self.activation_score) + " - " + str(self.is_active) + ")"

    
    def __eq__(self, other):
        if isinstance(other, CmNodeDO):
            return self.word.lemma == other.word.lemma
        return NotImplemented


    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

