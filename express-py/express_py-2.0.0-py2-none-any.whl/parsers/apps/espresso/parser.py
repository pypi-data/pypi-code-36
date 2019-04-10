import os
import numpy as np

from express.parsers import BaseParser
from express.parsers.utils import find_file
from express.parsers.apps.espresso import settings
from express.parsers.mixins.ionic import IonicDataMixin
from express.parsers.apps.espresso.settings import NEB_DAT_FILE
from express.parsers.mixins.reciprocal import ReciprocalDataMixin
from express.parsers.mixins.electronic import ElectronicDataMixin
from express.parsers.apps.espresso.formats.txt import EspressoTXTParser
from express.parsers.apps.espresso.formats.xml import EspressoXMLParser


class EspressoParser(BaseParser, IonicDataMixin, ElectronicDataMixin, ReciprocalDataMixin):
    """
    Espresso parser class.
    """

    def __init__(self, *args, **kwargs):
        super(EspressoParser, self).__init__(*args, **kwargs)
        self.work_dir = self.kwargs["work_dir"]
        self.stdout_file = self.kwargs["stdout_file"]
        self.txt_parser = EspressoTXTParser(self.work_dir)
        self.xml_parser = EspressoXMLParser(find_file(settings.XML_DATA_FILE, self.work_dir))

    def total_energy(self):
        """
        Returns total energy.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.total_energy
        """
        return self.txt_parser.total_energy(self._get_file_content(self.stdout_file))

    def fermi_energy(self):
        """
        Returns fermi energy.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.fermi_energy
        """
        return self.xml_parser.fermi_energy()

    def nspins(self):
        """
        Returns the number of spins.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.nspins
        """
        return self.xml_parser.nspins()

    def eigenvalues_at_kpoints(self):
        """
        Returns eigenvalues for all kpoints.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.eigenvalues_at_kpoints
        """
        return self.xml_parser.eigenvalues_at_kpoints()

    def ibz_k_points(self):
        """
        Returns ibz_k_points.

        Note:
            The function assumes that kpoints extracted from parsed source are inside the irreducible wedge of the
            Brillouin zone. Without checking whether it is the case or not.

        Reference:
            func: express.parsers.mixins.reciprocal.ReciprocalDataMixin.ibz_k_points
        """
        return np.array([eigenvalueData["kpoint"] for eigenvalueData in self.eigenvalues_at_kpoints()])

    def dos(self):
        """
        Returns density of states.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.dos
        """
        return self.txt_parser.dos()

    def initial_basis(self):
        """
        Returns initial basis.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.initial_basis
        """
        return self.txt_parser.initial_basis(self._get_file_content(self.stdout_file))

    def initial_lattice_vectors(self):
        """
        Returns initial lattice vectors.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.initial_lattice_vectors
        """
        return self.txt_parser.initial_lattice_vectors(self._get_file_content(self.stdout_file))

    def final_basis(self):
        """
        Returns final basis.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.basis
        """
        return self.xml_parser.final_basis()

    def final_lattice_vectors(self):
        """
        Returns final lattice.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.lattice_vectors
        """
        return self.xml_parser.final_lattice_vectors(reciprocal=False)

    def convergence_electronic(self):
        """
        Extracts convergence electronic.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.convergence_electronic
        """
        return self.txt_parser.convergence_electronic(self._get_file_content(self.stdout_file))

    def convergence_ionic(self):
        """
        Returns convergence ionic.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.convergence_ionic
        """
        return self.txt_parser.convergence_ionic(self._get_file_content(self.stdout_file))

    def stress_tensor(self):
        """
        Returns stress tensor.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.stress_tensor
        """
        return self.txt_parser.stress_tensor(self._get_file_content(self.stdout_file))

    def pressure(self):
        """
        Returns pressure.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.pressure
        """
        return self.txt_parser.pressure(self._get_file_content(self.stdout_file))

    def total_force(self):
        """
        Returns total force.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.total_force
        """
        return self.txt_parser.total_force(self._get_file_content(self.stdout_file))

    def atomic_forces(self):
        """
        Returns forces that is exerted on each atom by its surroundings.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.atomic_forces
        """
        return self.txt_parser.atomic_forces(self._get_file_content(self.stdout_file))

    def total_energy_contributions(self):
        """
        Extracts total energy contributions.

        Reference:
            func: express.parsers.mixins.electronic.ElectronicDataMixin.total_energy_contributions
        """
        return self.txt_parser.total_energy_contributions(self._get_file_content(self.stdout_file))

    def zero_point_energy(self):
        """
        Returns zero point energy.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.zero_point_energy
        """
        return self.txt_parser.zero_point_energy(self._get_file_content(self.stdout_file))

    def phonon_dos(self):
        """
        Returns phonon dos.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.phonon_dos
        """
        return self.txt_parser.phonon_dos()

    def phonon_dispersions(self):
        """
        Returns phonon dispersions.

        Reference:
            func: express.parsers.mixins.ionic.IonicDataMixin.phonon_dispersions
        """
        return self.txt_parser.phonon_dispersions()

    def reaction_coordinates(self):
        """
        Returns reaction coordinates.

        Returns:
             list
        """
        neb_dat_file = os.path.join(self.work_dir, NEB_DAT_FILE)
        return self.txt_parser.reaction_coordinates(self._get_file_content(neb_dat_file))

    def reaction_energies(self):
        """
        Returns reaction energies.

        Returns:
             list
        """
        neb_dat_file = os.path.join(self.work_dir, NEB_DAT_FILE)
        return self.txt_parser.reaction_energies(self._get_file_content(neb_dat_file))
