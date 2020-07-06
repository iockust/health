var goalNames = function(){
        var displayListHolder = [];
        var goalNameList = [];
        displayListHolder = $scope.displayListOfGoals;
        forEach(displayListHolder.goals, function (value, key) {
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
