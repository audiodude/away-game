agApp = angular.module('AwayGameApp', ['ngMaterial']);

agApp.service('ApiService', function($http) {
  this.getTeams = function() {
    return $http.get('/api/local/teams');
  };

  this.getAirports = function() {
    return $http.get('/api/local/airports');
  };

  this.qpx = function(date) {
    return $http.get('/api/qpx/trips/search?date=' + date);
  };
});

main = function($scope, ApiService) {
  $scope.teams = [];
  ApiService.getTeams().then(function(httpResp) {
    $scope.teams = httpResp.data.teams;
  });

  $scope.airports = [];
  ApiService.getAirports().then(function(httpResp) {
    $scope.airports = httpResp.data;
  });

  $scope.selected = null;
  $scope.selectTeam = function(abbr) {
    $scope.selected = abbr;
    angular.forEach($scope.teams, function(val) {
      if (val.team == abbr) {
        $scope.airport = val.airport_code
      }
    });
    $scope.expandedIndex = 1;
  };

  $scope.isSelected = function(abbr) {
    return abbr == $scope.selected;
  };

  $scope.expandedIndex = 0;
  $scope.isExpanded = function(index) {
    return $scope.expandedIndex == index;
  };

  $scope.submitAirport = function() {
    $scope.expandedIndex = 2;
  };

  $scope.gameDate = null;

  $scope.gameDetails = '--'
  $scope.onDateChange = function() {
    $scope.gameDetails = '@ Chicago White Sox, 7:15 PM CST';
  };

  $scope.flights = []
  $scope.findFlights = function() {
    // TODO: Turn the date selected into an YYYY-MM-DD, or whatever format
    // QPX requires.

    var data = null;
    ApiService.qpx('2016-05-02').then(function(httpResp) {
      data_day_before = httpResp.data;
    });
    ApiService.qpx('2016-05-03').then(function(httpResp) {
      data = httpResp.data;
      angular.forEach(data.trips.tripOption, function(option) {
        var flight = {};
        if (option.slice[0].segment.length > 1) {
          return true;
        }
        flight.price = option.saleTotal.replace('USD', '$');
        leg = option.slice[0].segment[0].leg[0]
        flight.carrier = option.slice[0].segment[0].carrier
        flight.origin = leg.origin;
        flight.destination = leg.destination;
        flight.arrivalTime = leg.arrivalTime;
        flight.departureTime = leg.departureTime;
        $scope.flights.push(flight)
      });
    });
  };

  $scope.eventSources = [];
};

agApp.controller('MainController', ['$scope', 'ApiService', main]);
