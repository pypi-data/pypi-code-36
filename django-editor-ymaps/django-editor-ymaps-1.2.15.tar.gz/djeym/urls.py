# -*- coding: utf-8 -*-
from django.urls import path
from django.views.i18n import JavaScriptCatalog

from . import views

app_name = 'djeym'
urlpatterns = [
    path('jsi18n/',
         JavaScriptCatalog.as_view(packages=['djeym']),
         name='javascript-catalog'),
    path('ajax-get-geo-objects-placemark/',
         views.AjaxGetGeoObjectsPlacemark.as_view(),
         name='ajax_get_geo_objects_placemark'),
    path('ajax-get-heat-points/',
         views.AjaxGetHeatPoints.as_view(),
         name='ajax_get_heat_points'),
    path('ajax-get-geo-objects-polyline/',
         views.AjaxGetGeoObjectsPolyline.as_view(),
         name='ajax_get_geo_objects_polyline'),
    path('ajax-get-geo-objects-polygon/',
         views.AjaxGetGeoObjectsPolygon.as_view(),
         name='ajax_get_geo_objects_polygon'),
    path('ajax-save-geo-object/',
         views.AjaxSaveGeoObjects.as_view(),
         name='ajax_save_geo_object'),
    path('ymeditor/<slug:slug>/',
         views.EditorYMap.as_view(),
         name='editor_ymap'),
    path('ajax-cluster-icon/',
         views.AjaxCustomClusterIcon.as_view(),
         name='ajax_cluster_icon'),
    path('ajax-collection-example-icon/',
         views.AjaxCollectionExampleIcon.as_view(),
         name='ajax_collection_example_icon'),
    path('ajax-balloon-content/',
         views.AjaxBalloonContent.as_view(),
         name='ajax_balloon_content'),
    path('ajax-import-icon-collection/',
         views.AjaxImportIconCollection.as_view(),
         name='ajax_import_icon_collection'),
    path('export-icon-collection/<slug:slug>/',
         views.ExportIconCollection.as_view(),
         name='export_icon_collection'),
    path('ajax-import-tile-source/',
         views.AjaxImportTileSource.as_view(),
         name='ajax_import_tile_source'),
    path('export-tile-source/',
         views.ExportTileSource.as_view(),
         name='export_tile_source'),
    path('ajax-tile-screenshot/',
         views.AjaxTileScreenshot.as_view(),
         name='ajax_tile_screenshot'),
    path('ajax-tile-source-change/',
         views.AjaxTileSourceChange.as_view(),
         name='ajax_tile_source_change'),
    path('ajax-map-controls/',
         views.AjaxMapControls.as_view(),
         name='ajax_map_controls'),
    path('ajax-heatmap-settings/',
         views.AjaxHeatmapSettings.as_view(),
         name='ajax_heatmap_settings'),
    path('ajax-activate-heatmap/',
         views.AjaxActivateHeatmap.as_view(),
         name='ajax_activate_heatmap'),
    path('ajax-heatmap-undo-settings/',
         views.AjaxHeatmapUndoSettings.as_view(),
         name='ajax_heatmap_undo_settings'),
    path('ajax-update-likes/',
         views.AjaxUpdateLikes.as_view(),
         name='ajax_update_likes'),
    path('ajax-update-preset-settings/',
         views.AjaxUpdatePresetSettings.as_view(),
         name='ajax_update_preset_settings'),
    path('ajax-general-settings/',
         views.AjaxGeneralSettings.as_view(),
         name='ajax_general_settings'),
    path('ajax-load-indicator-icon/',
         views.AjaxLoadIndicatorIcon.as_view(),
         name='ajax_load_indicator_icon'),
    path('ajax-load-indicator-change/',
         views.AjaxLoadIndicatorChange.as_view(),
         name='ajax_load_indicator_change')
]
