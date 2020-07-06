angular.module('activitiApp')
    .controller('rangeController', ['$rootScope', '$scope', '$http', function ($rootScope, $scope, $http) {

        var url = 'http://titan.blue.com:7070/GetFakeProjectData';
            console.log("getting data from " + url);
           // Fetch all the projects from an external REST service
           // that responds with JSON
           $http.get(url).
           success(function(data, status, headers, config) {
                console.log('API call to ' + url + ' succeeded!');
                console.log("Status Code: " + status);
                $scope.listOfProjects = data;
                console.log($scope.listOfProjects);
             }).
           error(function(data, status, headers, config) {
                alert('Error: '+ status);
                console.log('API call to ' + url + ' failed');
                console.log("Status Code: " + status);
           });
        //-----------------------------------------------------------------//

    $scope.startValue = 0;
    $scope.endValue = 100;
    $scope.displayValue = 0;
    $scope.totalSpend = 0;
    var todayDate = new Date();

    Date.prototype.yyyymmdd = function() {
        var mm = this.getMonth() + 1; // getMonth() is zero-based
        var dd = this.getDate();

        return [this.getFullYear(),
            (mm>9 ? '' : '0') + mm,
            (dd>9 ? '' : '0') + dd
        ].join('-');
    };

    $scope.budgetDate = todayDate.yyyymmdd();

    $scope.listOfProjects = {
        "projects"  : [
            { "rank" : 0, "priority" : 2, "contract" : "Contract A-1", "name" : "Project A", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 12, "execution" : 16 },
            { "rank" : 0, "priority" : 2, "contract" : "Contract A-2", "name" : "Project A", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 15, "execution" : 30 },
            { "rank" : 0, "priority" : 1, "contract" : "Contract C-1", "name" : "Project C", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 24, "execution" : 17 },
            { "rank" : 0, "priority" : 4, "contract" : "Contract B-1", "name" : "Project B", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 16, "execution" : 24 },
            { "rank" : 0, "priority" : 4, "contract" : "Contract B-2", "name" : "Project B", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 16, "execution" : 24 },
            { "rank" : 0, "priority" : 5, "contract" : "Contract E-1", "name" : "Project E", "startDate" : "1/1/2017", "endDate" : "1/1/2018", "funding": 14, "execution" : 90 },
            { "rank" : 0, "priority" : 5, "contract" : "Contract D-1", "name" : "Project D", "startDate" : "1/1/2018", "endDate" : "1/1/2019", "funding": 10, "execution" : 34 }
        ]
    };

    $scope.displayListOfProjects = {};
    $scope.ineligibleProjects = {};
    // $scope.displayListOfProjects = $scope.listOfProjects;

    var applyToTable = function(){
        var runningTotal = $scope.displayValue;
        var totalSpend = 0;
        var listHolder = [];
        var ineligibleHolder = [];
        var myDate=$scope.budgetDate.split("-");
        var newDate=myDate[1]+"/"+myDate[2]+"/"+myDate[0];
        var dateSelected = new Date(newDate).getTime() / 1000;

        console.log($scope.budgetDate);
        var sortedListOfProjects = [];

        //need a better way to sort projects by priority
        //this method assumes pritority will be integers and it hardcodes a max,
        //but it appears the SEI tool that will be used to set the priorities will not be integers
        for(var p = 1; p <= 100; p++) {
            angular.forEach($scope.listOfProjects.projects, function (value, key) {
                if (value.priority === p) {
                    sortedListOfProjects.push(value);
                }
            });
        };
        angular.forEach(sortedListOfProjects, function(value, key) {
            var startDateComp = new Date(value.startDate).getTime() / 1000;
            var endDateComp = new Date(value.endDate).getTime() / 1000;
            if(dateSelected > startDateComp && dateSelected < endDateComp){
                if(value.execution <= runningTotal){
                    listHolder.push(value);
                    runningTotal = runningTotal - value.execution;
                    totalSpend = totalSpend + value.execution;
                }
                else{
                    ineligibleHolder.push(value);
                }
            }
        });
        $scope.displayListOfProjects.projects = listHolder;
        $scope.ineligibleProjects.projects = ineligibleHolder;
        $scope.totalSpend = totalSpend;
        $scope.surplusAmt = $scope.displayValue - totalSpend;
        $scope.$apply();
        updateChart();
    };

    var contractNames = function(){
        var displayListHolder = [];
        var contractNameList = [];
        displayListHolder = $scope.displayListOfProjects;
        angular.forEach(displayListHolder.projects, function (value, key) {
            contractNameList.push(value.contract+" ("+value.name+")");
        });
        return contractNameList;
    };

    var contractAmounts = function(){
        var displayListHolder = [];
        var contractAmountList = [];
        displayListHolder = $scope.displayListOfProjects;
        angular.forEach(displayListHolder.projects, function (value, key) {
            contractAmountList.push(value.execution);
        });
        return contractAmountList;
    };

    $("input#budget-date").on("input change", function() {
        $scope.budgetDate = $("input#budget-date").val();
        console.log($scope.budgetDate);
        $scope.$apply();
        applyToTable();
        updateGoalChart();
    });

    $("input#budget-range").on("input change", function() {
        $scope.displayValue = $("input#budget-range").val();
        $scope.$apply();
        applyToTable();
        updateGoalChart();
    });

    var updateChart = function(){
        myChart.data.datasets[0].data = contractAmounts();
        myChart.data.labels = contractNames();
        myChart.update();
    };

/*-----------------------------------------------------------------*/
/*-------GOAL BAR CHART---------------------------------------*/
/*-------------------------------------------------------*/

    //apply to Goal Table to generate the data on screen on load

    $scope.listOfGoals = {}

    $scope.displayListOfGoals = {};

    //temporary hardcoding of list of goals
    $scope.displayListOfGoals = $scope.listOfGoals;

    var goalNames = function(){
        var displayListHolder = [];
        var goalNameList = [];
        displayListHolder = $scope.displayListOfGoals;
        angular.forEach(displayListHolder.goals, function (value, key) {
            goalNameList.push(value.strategic_goal);
        });
        console.log(goalNameList);
        return goalNameList;
    };

    var goalAmounts = function(){
        var displayListHolder = [];
        var goalAmountList = [];
        displayListHolder = $scope.displayListOfGoals;
        angular.forEach(displayListHolder.goals, function (value, key) {
            goalAmountList.push(value.fundable_total);
        });
        console.log(goalAmountList);
        return goalAmountList;
    };

    var updateGoalChart = function(){
        $scope.listOfGoals = [];
        if ($scope.displayValue == 16) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "16", "unfundable_total": "30"},
                    {"strategic_goal":"OMMC", "fundable_total": "0", "unfundable_total": "17"},
                    {"strategic_goal":"PMC", "fundable_total": "0", "unfundable_total": "24"}
                ]
            };
        }
        else if ($scope.displayValue >= 17 && $scope.displayValue < 33 ) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "0", "unfundable_total": "46"},
                    {"strategic_goal":"OMMC", "fundable_total": "17", "unfundable_total": "0"},
                    {"strategic_goal":"PMC", "fundable_total": "0", "unfundable_total": "24"}
                ]
            };
        }
        else if ($scope.displayValue >= 33 && $scope.displayValue < 57 ) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "16", "unfundable_total": "30"},
                    {"strategic_goal":"OMMC", "fundable_total": "17", "unfundable_total": "0"},
                    {"strategic_goal":"PMC", "fundable_total": "0", "unfundable_total": "24"}
                ]
            };
        }
        else if ($scope.displayValue >= 57 && $scope.displayValue < 63 ) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "16", "unfundable_total": "30"},
                    {"strategic_goal":"OMMC", "fundable_total": "17", "unfundable_total": "0"},
                    {"strategic_goal":"PMC", "fundable_total": "24", "unfundable_total": "0"}
                ]
            };
        }
        else if ($scope.displayValue >= 63 && $scope.displayValue < 87 ) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "46", "unfundable_total": "0"},
                    {"strategic_goal":"OMMC", "fundable_total": "17", "unfundable_total": "0"},
                    {"strategic_goal":"PMC", "fundable_total": "0", "unfundable_total": "24"}
                ]
            };
        }
        else if ($scope.displayValue >= 87) {
           $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "46", "unfundable_total": "0"},
                    {"strategic_goal":"OMMC", "fundable_total": "17", "unfundable_total": "0"},
                    {"strategic_goal":"PMC", "fundable_total": "24", "unfundable_total": "0"}
                ]
            };
        }
        else {
            $scope.listOfGoals = {
                "goals" :
                [
                    {"strategic_goal":"RDTE", "fundable_total": "0", "unfundable_total": "46"},
                    {"strategic_goal":"OMMC", "fundable_total": "0", "unfundable_total": "17"},
                    {"strategic_goal":"PMC", "fundable_total": "0", "unfundable_total": "24"}
                ]
            };
        }

        $scope.displayListOfGoals = $scope.listOfGoals;
        goalChart.data.datasets[0].data = goalAmounts();
        goalChart.data.labels = goalNames();
        goalChart.update();
    };

// GOAL BAR CHART
    var cty = document.getElementById("goalBarChart");
    var goalChart = new Chart(cty, {
        type: 'bar',
        data: {
            labels: goalNames(),
            datasets: [{
                label: 'cost in millions',
                data: goalAmounts(),
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
// END GOAL BAR CHART

    var ctx = document.getElementById("projectFundChart");
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: contractNames(),
            datasets: [{
                label: 'cost in millions',
                data: contractAmounts(),
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });

}])
.controller('goalController', ['$rootScope', '$scope', function ($rootScope, $scope) {

    $scope.startValue = 0;
    $scope.endValue = 100;
    $scope.displayValue = 0;
    $scope.totalSpend = 0;
    var todayDate = new Date();

    Date.prototype.yyyymmdd = function() {
        var mm = this.getMonth() + 1; // getMonth() is zero-based
        var dd = this.getDate();

        return [this.getFullYear(),
            (mm>9 ? '' : '0') + mm,
            (dd>9 ? '' : '0') + dd
        ].join('-');
    };

    $scope.budgetDate = todayDate.yyyymmdd();

}]);
