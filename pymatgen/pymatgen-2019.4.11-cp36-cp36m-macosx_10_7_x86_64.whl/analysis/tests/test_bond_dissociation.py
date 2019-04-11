# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.


import unittest
import os

from monty.serialization import loadfn
from pymatgen.analysis.bond_dissociation import BondDissociationEnergies

try:
    import openbabel as ob
except ImportError:
    ob = None

module_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))


class BondDissociationTest(unittest.TestCase):

    def setUp(self):
        self.PC_65_principle = loadfn(os.path.join(module_dir, "PC_65_principle.json"))
        self.PC_65_principle["initial_molecule"] = self.PC_65_principle["initial_molecule"].as_dict()
        self.PC_65_principle["final_molecule"] = self.PC_65_principle["final_molecule"].as_dict()
        self.PC_65_fragments = loadfn(os.path.join(module_dir, "PC_65_fragments.json"))
        for entry in self.PC_65_fragments:
            entry["initial_molecule"] = entry["initial_molecule"].as_dict()
            entry["final_molecule"] = entry["final_molecule"].as_dict()
        self.PC_correct = [[-0.1537378967699965, [(0, 6)], 'O', 'C', '[O][C@H](CO[C]=O)C', 'no_change', 0, 3, -381.557913621934], [-0.13698599276000323, [(0, 3)], 'O', 'C', 'O=C(OC[CH]C)[O]', 'no_change', 0, 3, -381.574665525944], [-0.13862754671799848, [(1, 4)], 'O', 'C', 'O([C@H]([CH2])C)C(=O)[O]', 'no_change', 0, 3, -381.573023971986], [-0.15215890127200282, [(1, 6)], 'O', 'C', 'O([C@H](C[O])C)[C]=O', 'no_change', 0, 3, -381.559492617432], [-0.7159314516110271, [(2, 6)], 'O', 'C', 'O1[C@H](CO[C]1)C', 'no_change', -1, 2, -306.454993516193, '[O]', 'no_change', 1, 2, -74.5407265509], [-0.2463273115880611, [(2, 6)], 'O', 'C', 'O1[C@H](CO[C]1)C', 'no_change', 0, 1, -306.402705691416, '[O]', 'no_change', 0, 3, -75.0626185157], [-0.3083568154030445, [(2, 6)], 'O', 'C', 'O1[C@H](CO[C]1)C', 'no_change', 1, 2, -306.159209742101, '[O]', 'no_change', -1, 2, -75.2440849612], [-0.2757153725892181, [(3, 5)], 'C', 'C', 'O1[CH]COC1=O', 'no_change', -1, 1, -341.848790340731, '[CH3]', 'no_change', 1, 1, -39.5871458053838], [-0.23669554002367477, [(3, 5)], 'C', 'C', 'O1[CH]COC1=O', 'no_change', 1, 1, -341.536118459517, '[CH3]', 'no_change', -1, 1, -39.9388375191633], [-0.15603034591947562, [(3, 5)], 'C', 'C', 'O1[CH]COC1=O', 'no_change', 0, 2, -341.725750601598, '[CH3]', 'no_change', 0, 2, -39.8298705711865], [-0.1455391987270218, [(3, 4)], 'C', 'C', 'O([CH]C)C(=O)O[CH2]', 'no_change', 0, 3, -381.566112319977], [-0.18308384202697425, [(3, 7)], 'C', 'H', 'O1[C](COC1=O)C', 'no_change', 1, 1, -380.872362641477, '[H]', 'no_change', -1, 1, -0.6562050352], [-0.1619771586430261, [(3, 7)], 'C', 'H', 'O1[C](COC1=O)C', 'no_change', 0, 2, -381.046845508561, '[H]', 'no_change', 0, 2, -0.5028288515], [-0.201648081019016, [(4, 9)], 'C', 'H', 'O1[C@H]([CH]OC1=O)C', 'no_change', 1, 1, -380.853798402485, '[H]', 'no_change', -1, 1, -0.6562050352], [-0.1664265655520012, [(4, 9)], 'C', 'H', 'O1[C@H]([CH]OC1=O)C', 'no_change', 0, 2, -381.042396101652, '[H]', 'no_change', 0, 2, -0.5028288515], [-0.17386520505198177, [(5, 12)], 'C', 'H', 'O1[C@H](COC1=O)[CH2]', 'no_change', 0, 2, -381.034957462152, '[H]', 'no_change', 0, 2, -0.5028288515], [-0.34285821379000936, [(5, 12)], 'C', 'H', 'O1[C@H](COC1=O)[CH2]', 'no_change', 1, 3, -380.712588269714, '[H]', 'no_change', -1, 1, -0.6562050352], [-0.18298781245698592, [(5, 12)], 'C', 'H', 'O1[C](COC1=O)C', 'bond_change', 1, 1, -380.872458671047, '[H]', 'no_change', -1, 1, -0.6562050352]]
        self.neg_EC_40_principle = loadfn(os.path.join(module_dir, "neg_EC_40_principle.json"))
        self.neg_EC_40_principle["initial_molecule"] = self.neg_EC_40_principle["initial_molecule"].as_dict()
        self.neg_EC_40_principle["final_molecule"] = self.neg_EC_40_principle["final_molecule"].as_dict()
        self.neg_EC_40_fragments = loadfn(os.path.join(module_dir, "neg_EC_40_fragments.json"))
        for entry in self.neg_EC_40_fragments:
            entry["initial_molecule"] = entry["initial_molecule"].as_dict()
            entry["final_molecule"] = entry["final_molecule"].as_dict()
        self.EC_correct = [[0.02488474745905478, [(0, 5)], 'O', 'C', 'O1CCO[C]1[O]', 'more_bonds', -1, 2, -342.440795051501], [0.06645176460301627, [(0, 3)], 'O', 'C', 'O=C(OC[CH2])[O]', 'no_change', -1, 2, -342.482362068645], [-0.08663102172198478, [(2, 5)], 'O', 'C', 'O1CCO[C]1', 'no_change', 0, 1, -267.08645842702, '[O]', 'no_change', -1, 2, -75.2428208553], [-0.21497449222397336, [(2, 5)], 'O', 'C', 'O1CCO[C]1', 'no_change', -1, 2, -267.138323931018, '[O]', 'no_change', 0, 3, -75.0626118808], [-0.0652242017809499, [(3, 6)], 'C', 'H', 'O1[CH]COC1=O', 'no_change', -1, 1, -341.847857507061, '[H]', 'no_change', 0, 2, -0.5028285952], [-0.03541898787199216, [(3, 6)], 'C', 'H', 'O1[CH]COC1=O', 'no_change', 0, 2, -341.72560514147, '[H]', 'no_change', -1, 1, -0.6548861747], [-0.05485312948695764, [(3, 4)], 'C', 'C', 'O([CH2])C(=O)O[CH2]', 'no_change', -1, 2, -342.361057174555]]
        self.neg_TFSI_principle = loadfn(os.path.join(module_dir, "neg_TFSI_principle.json"))
        self.neg_TFSI_principle["initial_molecule"] = self.neg_TFSI_principle["initial_molecule"].as_dict()
        self.neg_TFSI_principle["final_molecule"] = self.neg_TFSI_principle["final_molecule"].as_dict()
        self.neg_TFSI_fragments = loadfn(os.path.join(module_dir, "neg_TFSI_fragments.json"))
        for entry in self.neg_TFSI_fragments:
            entry["initial_molecule"] = entry["initial_molecule"].as_dict()
            entry["final_molecule"] = entry["final_molecule"].as_dict()
        self.TFSI_correct = [[-0.15474507240992352, [(0, 2)], 'S', 'O', 'S(=O)(=O)(C(F)(F)F)[N][S@](=O)C(F)(F)F', 'no_change', -1, 1, -1752.01611801942, '[O]', 'no_change', 0, 3, -75.0626185157], [-0.15103778016987235, [(0, 2)], 'S', 'O', 'S(=O)(=O)(C(F)(F)F)[N][S@](=O)C(F)(F)F', 'no_change', 0, 2, -1751.83835886616, '[O]', 'no_change', -1, 2, -75.2440849612], [-0.13498512745195512, [(0, 14)], 'S', 'N', '[S]([O])([O])C(F)(F)F', 'no_change', 0, 2, -886.155841072364, 'S(=O)(=O)(C(F)(F)F)[N]', 'no_change', -1, 2, -940.942655407714], [-0.18234084293294472, [(0, 14)], 'S', 'N', '[S]([O])([O])C(F)(F)F', 'no_change', -1, 1, -886.286067516302, '[S@]1(O[N]1)([O])C(F)(F)F', 'more_bonds', 0, 1, -940.765073248295], [-0.17810498602898406, [(0, 6)], 'S', 'C', 'S(=O)(=O)(C(F)(F)F)[N][S@@](=O)[O]', 'no_change', 0, 1, -1489.42685775311, 'F[C](F)F', 'no_change', -1, 1, -337.628518868391], [-0.10131920738194822, [(0, 6)], 'S', 'C', 'S(=O)(=O)(C(F)(F)F)[N][S]([O])[O]', 'no_change', -1, 2, -1489.56757113509, 'F[C](F)F', 'no_change', 0, 2, -337.564591265058], [-0.19376265759979105, [(6, 10)], 'C', 'F', 'S(=O)(=O)(C(F)(F)F)[N]S(=O)(=O)[C](F)F', 'no_change', -1, 2, -1727.31068781023, '[F]', 'no_change', 0, 2, -99.7290311397], [-0.16665302734986653, [(6, 10)], 'C', 'F', '[S@]1([O])(OC(S(=O)(=O)[N]1)(F)F)C(F)(F)F', 'more_bonds', 0, 1, -1727.21369677138, '[F]', 'no_change', -1, 1, -99.8531318088]]

    def tearDown(self):
        pass

    @unittest.skipIf(not ob, "OpenBabel not present. Skipping...")
    def test_tfsi_neg_no_pcm(self):
        BDE = BondDissociationEnergies(self.neg_TFSI_principle, self.neg_TFSI_fragments)
        self.assertEqual(len(BDE.filtered_entries),16)
        self.assertEqual(BDE.bond_dissociation_energies,self.TFSI_correct)

    @unittest.skipIf(not ob, "OpenBabel not present. Skipping...")
    def test_pc_neutral_pcm_65(self):
        BDE = BondDissociationEnergies(self.PC_65_principle, self.PC_65_fragments)
        self.assertEqual(len(BDE.filtered_entries),36)
        self.assertEqual(BDE.bond_dissociation_energies,self.PC_correct)

    @unittest.skipIf(not ob, "OpenBabel not present. Skipping...")
    def test_ec_neg_pcm_40(self):
        BDE = BondDissociationEnergies(self.neg_EC_40_principle, self.neg_EC_40_fragments)
        self.assertEqual(len(BDE.filtered_entries),18)
        self.assertEqual(BDE.bond_dissociation_energies,self.EC_correct)

if __name__ == "__main__":
    unittest.main()