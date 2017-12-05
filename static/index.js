angular.module('HospitalsApp', [])
    .controller('HospitalsController', ['$scope', '$http'], function ($scope, $http) {
        $scope.list = [];

        $http.get('localhost:8000/hospitals/api/hospitals')
        .then(function (response) {
            console.log(response.data);
            $scope.list = response.data;
        });

        /*
        $scope.list = [
            {
                facility_number: 123456787,
                name: "Hospital 1",
                year: 2016,
                bed_lic: 45,
                bed_avl: 42,
                zip_code: "90210"
            },
            {
                facility_number: 123456788,
                name: "Hospital 2",
                year: 2016,
                bed_lic: 120,
                bed_avl: 118,
                zip_code: "90068"
            },
            {
                facility_number: 123456789,
                name: "Hospital 3",
                year: 2016,
                bed_lic: 500,
                bed_avl: 485,
                zip_code: "90069"
            }
        ];
        */

        $scope.hospitalSearch = '';

        // $scope.updateSearch = function(newValue) {
        //     $scope.hospitalSearch = newValue;
        // }

        $scope.filteredList = $scope.list.filter(function (hospital) {
            return hospital.zip_code.indexOf($scope.hospitalSearch) >= 0 ||
                hospital.name.indexOf($scope.hospitalSearch) >= 0;
        });
    });
