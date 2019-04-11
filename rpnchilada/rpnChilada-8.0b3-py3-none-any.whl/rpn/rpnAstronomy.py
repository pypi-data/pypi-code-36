#!/usr/bin/env python

# //******************************************************************************
# //
# //  rpnAstronomy.py
# //
# //  RPN command-line calculator astronomical operators
# //  copyright (c) 2019, Rick Gutleber (rickg@his.com)
# //
# //  License: GNU GPL 3.0 (see <http://www.gnu.org/licenses/gpl.html> for more
# //  information).
# //
# //******************************************************************************

import ephem

from mpmath import acos, fabs, fadd, fdiv, fmul, fsub, mpmathify, pi, power, sqrt
from pytz import timezone

from rpn.rpnDateTime import RPNDateTime
from rpn.rpnLocation import getLocation, RPNLocation, getTimeZone
from rpn.rpnMeasurement import RPNMeasurement
from rpn.rpnMath import subtract
from rpn.rpnUtils import oneArgFunctionEvaluator, twoArgFunctionEvaluator, \
                         loadAstronomyData, real_int

import rpn.rpnGlobals as g


# //******************************************************************************
# //
# //  class RPNAstronomicalObject
# //
# //******************************************************************************

class RPNAstronomicalObject( object ):
    '''This class is for identifying astronomical objects.'''
    def __init__( self, object ):
        self.object = object

    def getDistanceFromEarth( self, date=None ):
        if date:
            self.object.compute( date.to( 'utc' ).format( ) )

        return RPNMeasurement( fmul( self.object.earth_distance, ephem.meters_per_au ), 'meters' )

    def getAngularSize( self, location=None, date=None ):
        if location and date:
            if isinstance( location, str ):
                location = getLocation( location )

            location.observer.date = date.to( 'utc' ).format( )
            self.object.compute( location.observer )

        # I have no idea why size seems to return the value in arcseconds... that
        # goes against the pyephem documentation that it always uses radians for angles.
        return RPNMeasurement( mpmathify( fdiv( fmul( fdiv( self.object.size, 3600 ), pi ), 180 ) ), 'radian' )

    def getAngularSeparation( self, other, location, date ):
        if isinstance( location, str ):
            location = getLocation( location )

        location.observer.date = date.to( 'utc' ).format( )

        self.object.compute( location.observer )
        other.object.compute( location.observer )

        return RPNMeasurement( mpmathify( ephem.separation( ( self.object.az, self.object.alt ),
                                                            ( other.object.az, other.object.alt ) ) ), 'radian' )

    def getAzimuthAndAltitude( self, location=None, date=None ):
        if location and date:
            if isinstance( location, str ):
                location = getLocation( location )

            location.observer.date = date.to( 'utc' ).format( )
            self.object.compute( location.observer )

        return RPNMeasurement( mpmathify( self.object.az ), 'radians' ), \
               RPNMeasurement( mpmathify( self.object.alt ), 'radians' )

        return self.getAzimuthAndAltitude( )

    def getAstronomicalEvent( self, location, date, func, horizon=None, useCenter=False, matchUSNO=False ):
        if isinstance( location, str ):
            location = getLocation( location )

        if horizon is None:
            horizon = float( location.observer.horizon )

        if matchUSNO:
            location.pressure = 0
            horizon -= 34/60        # 34 arcminutes

        old_horizon = location.observer.horizon

        location.observer.date = date.to( 'utc' ).format( )
        location.observer.horizon = str( horizon )

        if useCenter:
            result = RPNDateTime.convertFromEphemDate( func( location.observer, self.object, use_center=useCenter ) )
        else:
            result = RPNDateTime.convertFromEphemDate( func( location.observer, self.object ) )

        location.observer.horizon = old_horizon

        return result

    def getNextRising( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.next_rising, horizon, useCenter, matchUSNO )

    def getNextSetting( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.next_setting, horizon, useCenter, matchUSNO )

    def getNextTransit( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.next_transit, horizon, useCenter, matchUSNO )

    def getNextAntitransit( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.next_antitransit, horizon, useCenter, matchUSNO )

    def getPreviousRising( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.previous_rising, horizon, useCenter, matchUSNO )

    def getPreviousSetting( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.previous_setting, horizon, useCenter, matchUSNO )

    def getPreviousTransit( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.previous_transit, horizon, useCenter, matchUSNO )

    def getPreviousAntitransit( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        return self.getAstronomicalEvent( location, date, ephem.Observer.previous_antitransit, horizon, useCenter, matchUSNO )

    def getTransitTime( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        result1 = self.getAstronomicalEvent( location, date, ephem.Observer.next_rising, horizon, useCenter, matchUSNO )
        result2 = self.getAstronomicalEvent( location, result1, ephem.Observer.next_setting, horizon, useCenter, matchUSNO )

        return subtract( result2, result1 )

    def getAntitransitTime( self, location, date, horizon=None, useCenter=False, matchUSNO=False ):
        result1 = self.getAstronomicalEvent( location, date, ephem.Observer.next_setting, horizon, useCenter, matchUSNO )
        result2 = self.getAstronomicalEvent( location, result1, ephem.Observer.next_rising, horizon, useCenter, matchUSNO )

        return subtract( result2, result1 )


# //******************************************************************************
# //
# //  getSeason
# //
# //  0 = spring, 1 = summer, 2 = autumn, 3 = winter
# //
# //******************************************************************************

def getSeason( n, season ):
    '''Returns the date of the season for year n.'''
    from skyfield import almanac
    loadAstronomyData( )

    if not g.astroDataAvailable:
        raise ValueError( "Astronomy functions are unavailable." )

    t, y = almanac.find_discrete( g.timescale.utc( real_int( n ), 1, 1 ),
                                  g.timescale.utc( n, 12, 31 ), almanac.seasons( g.ephemeris ) )
    result = RPNDateTime.parseDateTime( t[ season ].utc_datetime( ) )
    return result.getLocalTime( )


# //******************************************************************************
# //
# //  getVernalEquinox
# //
# //******************************************************************************

@oneArgFunctionEvaluator( )
def getVernalEquinox( n ):
    '''Returns the date of the vernal equinox for year n.'''
    return getSeason( n, 0 )



# //*****************************************************************************
# //
# //  getSummerSolstice
# //
# //******************************************************************************

@oneArgFunctionEvaluator( )
def getSummerSolstice( n ):
    '''Returns the date of the summer solstice for year n.'''
    return getSeason( n, 1 )


# //******************************************************************************
# //
# //  getAutumnalEquinox
# //
# //******************************************************************************

@oneArgFunctionEvaluator( )
def getAutumnalEquinox( n ):
    '''Returns the date of the autumnal equinox for year n.'''
    return getSeason( n, 2 )


# //*****************************************************************************
# //
# //  getWinterSolstice
# //
# //******************************************************************************

@oneArgFunctionEvaluator( )
def getWinterSolstice( n ):
    '''Returns the date of the winter solstice for year n.'''
    return getSeason( n, 3 )


# //******************************************************************************
# //
# //  getEphemTime
# //
# //******************************************************************************

def getEphemTime( n, func ):
    '''Returns a pyephem date-time value from an RPNDateTime value.'''
    if not isinstance( n, RPNDateTime ):
        raise ValueError( 'expected a date-time argument' )

    result = RPNDateTime.convertFromEphemDate( func( n.format( ) ) )
    return result.getLocalTime( )

@oneArgFunctionEvaluator( )
def getNextFirstQuarterMoon( n ):
    return getEphemTime( n, ephem.next_first_quarter_moon )

@oneArgFunctionEvaluator( )
def getNextFullMoon( n ):
    return getEphemTime( n, ephem.next_full_moon )

@oneArgFunctionEvaluator( )
def getNextLastQuarterMoon( n ):
    return getEphemTime( n, ephem.next_last_quarter_moon )

@oneArgFunctionEvaluator( )
def getNextNewMoon( n ):
    return getEphemTime( n, ephem.next_new_moon )

@oneArgFunctionEvaluator( )
def getPreviousFirstQuarterMoon( n ):
    return getEphemTime( n, ephem.previous_first_quarter_moon )

@oneArgFunctionEvaluator( )
def getPreviousFullMoon( n ):
    return getEphemTime( n, ephem.previous_full_moon )

@oneArgFunctionEvaluator( )
def getPreviousLastQuarterMoon( n ):
    return getEphemTime( n, ephem.previous_last_quarter_moon )

@oneArgFunctionEvaluator( )
def getPreviousNewMoon( n ):
    return getEphemTime( n, ephem.previous_new_moon )


# //******************************************************************************
# //
# //  getMoonPhase
# //
# //******************************************************************************

@oneArgFunctionEvaluator( )
def getMoonPhase( n ):
    '''Returns the current moon phase as a percentage, starting from the new moon.'''
    if not isinstance( n, RPNDateTime ):
        raise ValueError( '\'moon_phase\' expects a date-time argument' )

    datetime = n.format( )

    previous = RPNDateTime.convertFromEphemDate( ephem.previous_new_moon( datetime ) )
    next = RPNDateTime.convertFromEphemDate( ephem.next_new_moon( datetime ) )

    cycle = next - previous
    current = n - previous

    return current.total_seconds( ) / cycle.total_seconds( )


# //******************************************************************************
# //
# //  getSkyLocation
# //
# //******************************************************************************

def getSkyLocation( body, location, date ):
    '''Returns the location of an astronomical object in the sky in terms of azimuth and altitude.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    az, alt = body.getAzimuthAndAltitude( location, date )

    return [ az.convert( 'degree' ), alt.convert( 'degree' ) ]


# //******************************************************************************
# //
# //  getAngularSize
# //
# //******************************************************************************

def getAngularSize( body, location, date ):
    '''Returns the angular size of an astronomical object in radians.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    return body.getAngularSize( location, date )


# //******************************************************************************
# //
# //  getAngularSeparation
# //
# //******************************************************************************

def getAngularSeparation( body1, body2, location, date ):
    '''Returns the angular size of an astronomical object in radians.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body1, RPNAstronomicalObject ) or not isinstance( body2, RPNAstronomicalObject ) and \
       not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected two astronomical objects, a location and a date-time' )

    return body1.getAngularSeparation( body2, location, date )


# //******************************************************************************
# //
# //  getNextRising
# //
# //******************************************************************************

def getNextRising( body, location, date ):
    '''Returns the next rising time for an astronomical object.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getNextRising( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getNextSunrise( n, k ):
    return getNextRising( RPNAstronomicalObject( ephem.Sun( ) ), n, k )

@twoArgFunctionEvaluator( )
def getNextMoonRise( n, k ):
    return getNextRising( RPNAstronomicalObject( ephem.Moon( ) ), n, k )


# //******************************************************************************
# //
# //  getNextSetting
# //
# //******************************************************************************

def getNextSetting( body, location, date ):
    '''Returns the next setting time for an astronomical object.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getNextSetting( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getNextSunset( n, k ):
    return getNextSetting( RPNAstronomicalObject( ephem.Sun( ) ), n, k )

@twoArgFunctionEvaluator( )
def getNextMoonSet( n, k ):
    return getNextSetting( RPNAstronomicalObject( ephem.Moon( ) ), n, k )


# //******************************************************************************
# //
# //  getNextTransit
# //
# //******************************************************************************

def getNextTransit( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getNextTransit( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getSolarNoon( n, k ):
    return getNextTransit( RPNAstronomicalObject( ephem.Sun( ) ), n, k )

@twoArgFunctionEvaluator( )
def getNextMoonTransit( n, k ):
    return getNextTransit( RPNAstronomicalObject( ephem.Moon( ) ), n, k )


# //******************************************************************************
# //
# //  getNextAntitransit
# //
# //******************************************************************************

def getNextAntitransit( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getNextAntitransit( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getNextSunAntitransit( n, k ):
    return getNextAntitransit( RPNAstronomicalObject( ephem.Sun( ) ), n, k )

@twoArgFunctionEvaluator( )
def getNextMoonAntitransit( n, k ):
    return getNextAntitransit( RPNAstronomicalObject( ephem.Moon( ) ), n, k )


# //******************************************************************************
# //
# //  getTransitTime
# //
# //******************************************************************************

def getTransitTime( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    return body.getTransitTime( location, date )

@twoArgFunctionEvaluator( )
def getDayTime( n, k ):
    return getTransitTime( RPNAstronomicalObject( ephem.Sun( ) ), n, k )


# //******************************************************************************
# //
# //  getAntitransitTime
# //
# //******************************************************************************

def getAntitransitTime( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    return body.getAntitransitTime( location, date )

@twoArgFunctionEvaluator( )
def getNightTime( n, k ):
    return getAntitransitTime( RPNAstronomicalObject( ephem.Sun( ) ), n, k )


# //******************************************************************************
# //
# //  getPreviousRising
# //
# //******************************************************************************

def getPreviousRising( body, location, date ):
    '''Returns the previous rising time for an astronomical object.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getPreviousRising( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )


# //******************************************************************************
# //
# //  getPreviousSetting
# //
# //******************************************************************************

def getPreviousSetting( body, location, date ):
    '''Returns the previous setting time for an astronomical object.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getPreviousSetting( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )


# //******************************************************************************
# //
# //  getPreviousTransit
# //
# //******************************************************************************

def getPreviousTransit( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getPreviousTransit( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )


# //******************************************************************************
# //
# //  getPreviousAntitransit
# //
# //******************************************************************************

def getPreviousAntitransit( body, location, date ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body, RPNAstronomicalObject ) or not isinstance( location, RPNLocation ) or \
       not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected an astronomical object, a location and a date-time' )

    result = body.getPreviousAntitransit( location, date )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )


# //******************************************************************************
# //
# //  getNextDawn
# //
# //  -6 is "civil" twilight
# //  -12 is nautical twilight
# //  -18 is astronomical twilight
# //
# //******************************************************************************

def getNextDawn( location, date, horizon = -6 ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected location and date-time arguments' )

    result = RPNAstronomicalObject( ephem.Sun( ) ).getNextRising( location, date, horizon=horizon )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getNextCivilDawn( n, k ):
    return getNextDawn( n, k, -6 )

@twoArgFunctionEvaluator( )
def getNextNauticalDawn( n, k ):
    return getNextDawn( n, k, -12 )

@twoArgFunctionEvaluator( )
def getNextAstronomicalDawn( n, k ):
    return getNextDawn( n, k, -18 )


# //******************************************************************************
# //
# //  getNextDusk
# //
# //  -6 is "civil" twilight
# //  -12 is nautical twilight
# //  -18 is astronomical twilight
# //
# //******************************************************************************

def getNextDusk( location, date, horizon = -6 ):
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected location and date-time arguments' )

    result = RPNAstronomicalObject( ephem.Sun( ) ).getNextSetting( location, date, horizon=horizon )
    return result.getLocalTime( timezone( getTimeZone( location ) ) )

@twoArgFunctionEvaluator( )
def getNextCivilDusk( n, k ):
    return getNextDusk( n, k, -6 )

@twoArgFunctionEvaluator( )
def getNextNauticalDusk( n, k ):
    return getNextDusk( n, k, -12 )

@twoArgFunctionEvaluator( )
def getNextAstronomicalDusk( n, k ):
    return getNextDusk( n, k, -18 )


# //******************************************************************************
# //
# //  getDistanceFromEarth
# //
# //******************************************************************************

@twoArgFunctionEvaluator( )
def getDistanceFromEarth( n, k ):
    if not isinstance( n, RPNAstronomicalObject ) or not isinstance( k, RPNDateTime ):
        raise ValueError( '\'sky_location\' expects an astronomical object and a date-time' )

    return RPNMeasurement( n.getDistanceFromEarth( k ), 'meters' )


# //******************************************************************************
# //
# //  getCircleIntersectionTerm
# //
# //  http://mathworld.wolfram.com/Circle-CircleIntersection.html
# //
# //******************************************************************************

def getCircleIntersectionTerm( radius1, radius2, separation ):
    distance = fdiv( fadd( fsub( power( separation, 2 ), power( radius1, 2 ) ),
                           power( radius2, 2 ) ),
                     fmul( 2, separation ) )

    #print( 'radius1', radius1 )
    #print( 'radius2', radius2 )
    #print( 'distance', distance )
    #print( 'radius1 - distance', fsub( radius1, distance ) )
    #print( 'radius1^2 - distance^2', fsub( power( radius1, 2 ), power( distance, 2 ) ) )
    #print( )

    if power( distance, 2 ) > power( radius1, 2 ):
        return fmul( power( radius1, 2 ), fdiv( pi, 2 ) )

    return fsub( fmul( power( radius1, 2 ), acos( fdiv( distance, radius1 ) ) ),
                 fmul( distance, sqrt( fsub( power( radius1, 2 ), power( distance, 2 ) ) ) ) )


# //******************************************************************************
# //
# //  getEclipseTotality
# //
# //******************************************************************************

def getEclipseTotality( body1, body2, location, date ):
    '''Returns the angular size of an astronomical object in radians.'''
    if isinstance( location, str ):
        location = getLocation( location )

    if not isinstance( body1, RPNAstronomicalObject ) or not isinstance( body2, RPNAstronomicalObject ) and \
       not isinstance( location, RPNLocation ) or not isinstance( date, RPNDateTime ):
        raise ValueError( 'expected two astronomical objects, a location and a date-time' )

    separation = body1.getAngularSeparation( body2, location, date ).value

    radius1 = body1.getAngularSize( ).value
    radius2 = body2.getAngularSize( ).value

    if separation > fadd( radius1, radius2 ):
        return 0

    distance1 = body1.getDistanceFromEarth( date )
    distance2 = body2.getDistanceFromEarth( date )

    area1 = fmul( pi, power( radius1, 2 ) )
    area2 = fmul( pi, power( radius2, 2 ) )

    area_of_intersection = fadd( getCircleIntersectionTerm( radius1, radius2, separation ),
                                 getCircleIntersectionTerm( radius2, radius1, separation ) )

    if distance1 > distance2:
        result = fdiv( area_of_intersection, area1 )
    else:
        result = fdiv( area_of_intersection, area2 )

    if result > 1:
        return 1
    else:
        return result



#function [Az El] = RaDec2AzEl(Ra,Dec,lat,lon,time)
#% Programed by Darin C. Koblick 01/23/2010
#%--------------------------------------------------------------------------
#% External Function Call Sequence:
#% [Az El] = RaDec2AzEl(0,0,0,-104,'1992/08/20 12:14:00')
#%
#% Worked Example: pg. 262 Vallado
#%[Az El] = RaDec2AzEl(294.9891115,-20.8235624,39.007,-104.883,'1994/05/14 13:11:20.59856')
#%[210.7514  23.9036] = RaDec2AzEl(294.9891115,-20.8235624,39.007,-104.883,'1994/05/14 13:11:20.59856')
#%
#% Worked Example: http://www.stargazing.net/kepler/altaz.html
#% [Az El] = RaDec2AzEl(344.95,42.71667,52.5,-1.91667,'1997/03/14 19:00:00')
#% [311.92258 22.40100] = RaDec2AzEl(344.95,42.71667,52.5,-1.91667,'1997/03/14 19:00:00')
#%
#% [Beta,el] = RaDec2AzEl(alpha_t,delta_t,phi,lamda,'yyyy/mm/dd hh:mm:ss')
#%
#% Function Description:
#%--------------------------------------------------------------------------
#% RaDec2AzEl will take the Right Ascension and Declination in the topocentric
#% reference frame, site latitude and longitude as well as a time in GMT
#% and output the Azimuth and Elevation in the local horizon
#% reference frame.
#%
#% Inputs:                                                       Format:
#%--------------------------------------------------------------------------
#% Topocentric Right Ascension (Degrees)                         [N x 1]
#% Topocentric Declination Angle (Degrees)                       [N x 1]
#% Lat (Site Latitude in degrees -90:90 -> S(-) N(+))            [N x 1]
#% Lon (Site Longitude in degrees -180:180 W(-) E(+))            [N x 1]
#% UTC (Coordinated Universal Time YYYY/MM/DD hh:mm:ss)          [N x 1]
#%
#% Outputs:                                                      Format:
#%--------------------------------------------------------------------------
#% Local Azimuth Angle   (degrees)                               [N x 1]
#% Local Elevation Angle (degrees)                               [N x 1]
#%
#%
#% External Source References:
#% Fundamentals of Astrodynamics and Applications
#% D. Vallado, Second Edition
#% Example 3-5. Finding Local Siderial Time (pg. 192)
#% Algorithm 28: AzElToRaDec (pg. 259)
#% -------------------------------------------------------------------------

#%Example 3-5
#[yyyy mm dd HH MM SS] = datevec(datenum(time,'yyyy/mm/dd HH:MM:SS'));
#JD = juliandate(yyyy,mm,dd,HH,MM,SS);
#T_UT1 = (JD-2451545)./36525;
#ThetaGMST = 67310.54841 + (876600*3600 + 8640184.812866).*T_UT1 ...
#+ .093104.*(T_UT1.^2) - (6.2*10^-6).*(T_UT1.^3);
#ThetaGMST = mod((mod(ThetaGMST,86400*(ThetaGMST./abs(ThetaGMST)))/240),360);
#ThetaLST = ThetaGMST + lon;

#%Equation 4-11 (Define Siderial Time LHA)
#LHA = mod(ThetaLST - Ra,360);

#%Equation 4-12 (Elevation Deg)
#El = asind(sind(lat).*sind(Dec)+cosd(lat).*cosd(Dec).*cosd(LHA));

#%Equation 4-13 / 4-14 (Adaptation) (Azimuth Deg)
#%Az = mod(atand(-(sind(LHA).*cosd(Dec)./(cosd(lat).*sind(Dec) - sind(lat).*cosd(Dec).*cosd(LHA)))),360);
#Az = mod(atan2(-sind(LHA).*cosd(Dec)./cosd(El),...
#    (sind(Dec)-sind(El).*sind(lat))./(cosd(El).*cosd(lat))).*(180/pi),360);


#function jd = juliandate(year, month, day, hour, min, sec)
#YearDur = 365.25;
#for i = length(month):-1:1
#    if (month(i)<=2)
#        year(i)=year(i)-1;
#        month(i)=month(i)+12;
#    end
#end
#A = floor(YearDur*(year+4716));
#B = floor(30.6001*(month+1));
#C = 2;
#D = floor(year/100);
#E = floor(floor(year/100)*.25);
#F = day-1524.5;
#G = (hour+(min/60)+sec/3600)/24;
#jd =A+B+C-D+E+F+G;
