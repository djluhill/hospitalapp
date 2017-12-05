let hospitalsArray = [];

$(function() {
    $.getJSON('/hospitals/api/hospitals', function(response) {
        hospitalsArray = response;
        filteredHospitalsArray = hospitalsArray;
        appendHospitalsToTable(hospitalsArray);
    });
    $('#search-hospitals').on('keyup', updateSearch);
    $("#sort-by").on('change', sortHospitals);
});

function appendHospitalsToTable(hospitals) {
    console.log('appending hospitals');
    $('#hospitals-list tr').remove();
    hospitalsTemplate = '';
    hospitals.forEach(function(hospital) {
        hospitalsTemplate += `
            <tr data-hospital-id="${hospital.facility_number}">
                <td>${hospital.facility_number}</td>
                <td>${hospital.name}</td>
                <td>${hospital.zip_code}</td>
                <td>${hospital.bed_lic}</td>
                <td>${hospital.bed_avl}</td>
            </tr>
        `;
    });
    $(hospitalsTemplate).appendTo('#hospitals-list');   
}

function sortHospitals() {
    $('#search-hospitals').val('');
    const sortAttribute = $('#sort-by').val();
    let sortDirection = 1;
    if (sortAttribute !== 'name') {
        sortDirection = -1;
    }
    hospitalsArray.sort(function(hospital1, hospital2) {
        if (hospital1[sortAttribute] < hospital2[sortAttribute]) {
            return -1 * sortDirection;
        }
        else if (hospital1[sortAttribute] > hospital2[sortAttribute]) {
            return 1 * sortDirection;
        }
        else {
            return 0;
        }
    });

    appendHospitalsToTable(hospitalsArray);
}


function updateSearch(event) {
    const search = $(event.target).val().toLowerCase();
    console.log(search);

    if (search !== '' && search !== undefined) {
        const filteredHospitalsArray = hospitalsArray.filter(function(hospital) {
            return hospital.name.toLowerCase().indexOf(search) > -1 ||
                   hospital.zip_code.indexOf(search) > -1;
        });
        appendHospitalsToTable(filteredHospitalsArray)
    }
    else {
        appendHospitalsToTable(hospitalsArray);
    }
}

// Could not get Angular to re-render the template when searching, so switched to jQuery instead.
/*
angular.module('HospitalsApp', [])
    .controller('HospitalsController', ['$scope', '$http', function($scope, $http) {
        $scope.list = [];
        
        $http.get('/hospitals/api/hospitals')
        .then(function(response) {
            console.log($scope.list.concat(response.data));
            return $scope.list.concat(response.data);
        });

        $scope.hospitalSearch = '';

        // $scope.updateSearch = function(newValue) {
        //     $scope.hospitalSearch = newValue;
        // }

        $scope.getAllHospitals = () => $scope.list

        $scope.filteredList = $scope.list.filter(function(hospital) {

            return hospital.zip_code.indexOf($scope.hospitalSearch) >= 0 ||
                hospital.name.indexOf($scope.hospitalSearch) >= 0;
        });
    }]);
*/