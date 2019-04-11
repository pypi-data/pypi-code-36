############################################################################
# Copyright ESIEE Paris (2018)                                             #
#                                                                          #
# Contributor(s) : Benjamin Perret                                         #
#                                                                          #
# Distributed under the terms of the CECILL-B License.                     #
#                                                                          #
# The full license is in the file LICENSE, distributed with this software. #
############################################################################

import higra as hg


@hg.argument_helper(hg.CptHierarchy, ("leaf_graph", hg.CptRegionAdjacencyGraph))
def make_assesser_fragmentation_optimal_cut(tree,
                                            ground_truth,
                                            measure,
                                            max_regions=200,
                                            vertex_map=None):
    """
    Create an assesser for hierarchy optimal cuts w.r.t. a given ground-truth partition of the base graph vertices
    and the given optimal cut measure (see :class:`~higra.OptimalCutMeasure`).
    The algorithms will explore optimal cuts containing at most max_regions regions.

    The base graph of the hierarchy is:

        * the leaf graph of the hierarchy if it is not a region adjacency graph
        * the original graph of the leaf graph of the hierarchy if it is a region adjacency graph

    :param tree: input hierarchy (Concept :class:`~higra.CptHierarchy`)
    :param ground_truth: labelisation of base graph vertices
    :param measure: evaluation measure to use (see enumeration :class:`~higra.OptimalCutMeasure`)
    :param max_regions: maximum number of regions in the cuts
    :param vertex_map: optional, vertex mapping if the hierarchy is build on a region adjacency graph (deduced from :class:`~higra.CptRegionAdjacencyGraph` on the leaf graph of `tree`)
    :return: an object of type :class:`~higra.AssesserFragmentationOptimalCut`
    """
    if vertex_map is None:
        return hg.AssesserFragmentationOptimalCut(tree, ground_truth, measure, max_regions=max_regions)
    else:
        return hg.AssesserFragmentationOptimalCut(tree, ground_truth, measure, max_regions=max_regions,
                                                  vertex_map=vertex_map)


@hg.argument_helper(hg.CptHierarchy, ("leaf_graph", hg.CptRegionAdjacencyGraph))
def assess_fragmentation_optimal_cut(tree,
                                     ground_truth,
                                     measure,
                                     max_regions=200,
                                     vertex_map=None):
    """
    Compute the fragmentation curve of the optimal cuts in a hierarchy w.r.t. a given measure.

    The base graph of the hierarchy is:

        * the leaf graph of the hierarchy if it is not a region adjacency graph
        * the original graph of the leaf graph of the hierarchy if it is a region adjacency graph

    :param tree: input hierarchy (Concept :class:`~higra.CptHierarchy`)
    :param ground_truth: labelisation of base graph vertices
    :param measure: evaluation measure to use (see enumeration :class:`~higra.OptimalCutMeasure`)
    :param max_regions: maximum number of regions in the cuts
    :param vertex_map: optional, vertex mapping if the hierarchy is build on a region adjacency graph (deduced from :class:`~higra.CptRegionAdjacencyGraph` on the leaf graph of `tree`)
    :return: an object of type :class:`~higra.FragmentationCurve`
    """
    assesser = make_assesser_fragmentation_optimal_cut(tree, ground_truth, measure, max_regions, vertex_map)
    return assesser.fragmentation_curve()


@hg.argument_helper(hg.CptValuedHierarchy, ("leaf_graph", hg.CptRegionAdjacencyGraph))
def assess_fragmentation_horizontal_cut(altitudes,
                                        ground_truth,
                                        measure,
                                        tree,
                                        max_regions=200,
                                        vertex_map=None):
    """
    Compute the fragmentation curve of the horizontal cuts in a hierarchy w.r.t. a given measure.

    The base graph of the hierarchy is:

        * the leaf graph of the hierarchy if it is not a region adjacency graph
        * the original graph of the leaf graph of the hierarchy if it is a region adjacency graph

    :param altitudes: altitudes of the nodes of the input hierarchy (Concept :class:`~higra.CptValuedHierarchy`)
    :param tree: input hierarchy (deduced from:class:`~higra.CptValuedHierarchy`)
    :param ground_truth: labelisation of base graph vertices
    :param measure: evaluation measure to use (see enumeration :class:`~higra.PartitionMeasure`)
    :param max_regions: maximum number of regions in the cuts
    :param vertex_map: optional, vertex mapping if the hierarchy is build on a region adjacency graph (deduced from :class:`~higra.CptRegionAdjacencyGraph` on the leaf graph of `tree`)
    :return: an object of type :class:`~higra.FragmentationCurve`
    """
    if vertex_map is None:
        return hg.cpp._assess_fragmentation_horizontal_cut(tree, altitudes, ground_truth, measure,
                                                           max_regions=max_regions)
    else:
        return hg.cpp._assess_fragmentation_horizontal_cut(tree, altitudes, ground_truth, measure,
                                                           max_regions=max_regions,
                                                           vertex_map=vertex_map)
