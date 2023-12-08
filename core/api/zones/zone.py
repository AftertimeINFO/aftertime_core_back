from core.models.zones import ZoneIndex
from core.models.zones import ZoneIndexZones
from core.models.zones import ZonePoints

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def get_belong_zone_by_coordinates(lat, lon):
    check_point = Point(lat, lon)
    zone_index = ZoneIndex.objects.filter(lat_l__lte=lat, lat_g__gt=lat, lon_l__lte=lon, lon_g__gt=lon)

    for cur_zone_index in zone_index:
        zones = ZoneIndexZones.objects.filter(zone_index=cur_zone_index.id)

        for cor_zone in zones:
            points = ZonePoints.objects.filter(zone=cor_zone.zone_id)
            poligon_points = []
            for cur_point in points:
                poligon_points.append([cur_point.lat, cur_point.lon])

            # lons_lats_vect = np.column_stack((lons_vect, lats_vect))  # Reshape coordinates
            polygon_a = Polygon(poligon_points)  # create polygon
             # create point
            print(polygon_a.contains(check_point))  # check if polygon contains point
            pass
            # print(check_point.within(polygon))  # check if a point is in the polygon
            #
            # pass