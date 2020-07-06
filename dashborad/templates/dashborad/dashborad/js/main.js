(function() {
    var t;

    function size(animate) {
        if (animate == undefined) {
            animate = false;
        }
        clearTimeout(t);
        t = setTimeout(function() {
            $("canvas").each(function(i, el) {
                $(el).attr({
                    "width": $(el).parent().width(),
                    "height": $(el).parent().outerHeight()
                });
            });
            redraw(animate);
            var m = 0;
            $(".widget").height("");
            $(".widget").each(function(i, el) { m = Math.max(m, $(el).height()); });
            $(".widget").height(m);
        }, 30);
    }

    // THIS WILL RE-RENDER ALL CHARTS WHEN WINDOW SIZE CHANGES
    // $(window).on('resize', function(){ size(false); });


    function redraw(animation) {
        var options = {};
        if (!animation) {
            options.animation = false;
        } else {
            options.animation = true;
        }

        // ------------------------------------------------------------------------------
        // BUTTONS ----------------------------------------------------------------------
        // ------------------------------------------------------------------------------
        $('#addElement').click(function() {
            contracts.data.datasets[0].data[2] = 50;
            contracts.update();
        });

        $('#removeElement').click(function() {
            contracts.data.datasets[0].data[2] = 16;
            contracts.update();
        });

        $('#addNewData').click(function() {
            var color = random_rgba();
            addDataColor(hours, makeID(), Math.floor(Math.random() * 20), makeRGBA(color, 0.2), makeRGBA(color, 1));
        });

        $('#removeNewData').click(function() {
            removeData(hours);
        });


        $('#ajax').click(function() {
            $.ajax({
                method: "GET",
                url: "https://uinames.com/api/?amount=2&region=United%20States&ext",
                dataType: "jsonp",
                crossDomain: true,
                timeout: 5000,
                success: function(data) {
                    // var data = JSON.parse(data);
                    $.each(data, function(index, el) {
                        var dataName = data[index].name;
                        var dataPoint = data[index].age;
                        var color = random_rgba();
                        addDataColor(hours, dataName, dataPoint, makeRGBA(color, 0.2), makeRGBA(color, 1));
                    });
                },
                error: function(jqXHR, textStatus, errorThrown) {
                    alert('error ' + textStatus + " " + errorThrown);
                }
            });
        });

        // ------------------------------------------------------------------------------
        // HELPER FUNCTIONS ----------------------------------------------------------------------
        // ------------------------------------------------------------------------------

        function addData(chart, label, data) {
            chart.data.labels.push(label);
            chart.data.datasets.forEach((dataset) => {
                dataset.data.push(data);
            });
            chart.update();
        }

        function addDataColor(chart, label, data, bgcolor, bordercolor) {
            chart.data.labels.push(label);
            chart.data.datasets.forEach((dataset) => {
                dataset.data.push(data);
            });
            chart.data.datasets.forEach((backgroundcolors) => {
                backgroundcolors.backgroundColor.push(bgcolor);
            });
            chart.data.datasets.forEach((bordercolors) => {
                bordercolors.borderColor.push(bordercolor);
            });
            chart.update();
        }

        function removeData(chart) {
            chart.data.labels.pop();
            chart.data.datasets.forEach((dataset) => {
                dataset.data.pop();
            });
            chart.update();
        }

        function makeID() {
            var text = "";
            var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

            for (var i = 0; i < 4; i++)
                text += possible.charAt(Math.floor(Math.random() * possible.length));
            return text.toUpperCase();
        }

        function random_rgba() {
            var o = Math.round,
                r = Math.random,
                s = 255;

            var first = o(r() * s);
            var second = o(r() * s);
            var third = o(r() * s);

            var rgbColor = [];
            rgbColor.push(first);
            rgbColor.push(second);
            rgbColor.push(third);

            return rgbColor
        }

        function makeRGBA(rgb, a) {
            var r = rgb[0];
            var g = rgb[1];
            var b = rgb[2];

            return 'rgba(' + r + ',' + g + ',' + b + ',' + a + ')';
        }


        // ------------------------------ DOUGHNUT GRAPH ------------------------------
        // ------------------------------------------------------------

        data = {

            datasets: [{
                label: 'Breakdown: Appropriation Type',
                data: [46, 17, 24],
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
            }],
            labels: ["RDTE", "OMMC", "PMC"]
        };

        var ctx = document.getElementById("hours");

        var hours = new Chart(ctx, {
            type: 'doughnut',
            data: data
        });

        // ------------------------------------------------------------
        // ------------------------------ BAR GRAPH ------------------------------
        // ------------------------------------------------------------

        var barData = {
            labels: ["C-1", "A-1", "A-2", "B-1"],
            datasets: [{
                label: "Label",
                // xAxisID: "Contract",
                // yAxisID: "Millions",
                data: [17, 16, 30, 24],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        }

        var cty = document.getElementById("contracts");
        var contracts = new Chart(cty, {
            type: 'bar',
            data: barData,
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                },
                legend: {
                    display: false
                }
            }
        });

        // ------------------------------------------------------------
        // ------------------------------ RADAR GRAPH ------------------------------
        // ------------------------------------------------------------

        data = {
            datasets: [{
                data: [20, 40, 30, 60],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }],

            labels: [
                'X',
                'Y',
                'Z',
                'B'

            ]
        };

        var ctz = document.getElementById("expenditure");
        var expenditure = new Chart(ctz, {
            data: data,
            type: 'polarArea'
        });
        // ------------------------------------------------------------

        // ------------------------------------------------------------
        // ------------------------------ RADAR GRAPH ------------------------------
        // ------------------------------------------------------------

        var radarData = {
            labels: ["Applications", "Cloud", "IT Stewardship", "Services", "Migration", "Modernization"],
            datasets: [{
                    label: "2016",
                    data: [39, 56, 60, 60, 40, 40],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255,99,132,1)'
                    ],
                    borderWidth: 1
                },
                {
                    label: "2017",
                    data: [24, 54, 40, 50, 39, 60],
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.2)'
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)'
                    ],
                    borderWidth: 1
                }
            ]

        }

        var ctr = document.getElementById("goals");
        var goals = new Chart(ctr, {
            type: 'radar',
            data: radarData,
            options: {
                legend: {
                    position: 'top'
                },
                scale: {
                    scaleLabel: {
                        padding: { top: 20 }
                    }
                }
            }
        });

        var ctrC = document.getElementById("goalsC");
        var goalsC = new Chart(ctrC, {
            type: 'radar',
            data: radarData
        });

        /* ------------------------------------------------------LINE GRAPH----------------------------------
            ------------------------------------------------------------------------------------------------ */
        var lineData = {
            labels: ["January", "February", "March", "April", "May", "June", "July", "August"],
            datasets: [{
                label: "2017",
                data: [39, 56, 65, 80, 70, 40, 30, 10],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)'
                ],
                borderWidth: 1
            }]
        }



        var ctrB = document.getElementById("cost");
        var cost = new Chart(ctrB, {
            type: 'line',
            data: lineData
        });


        /* ----------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------ */

        // var presets = window.chartColors;
        // var utils = Samples.utils;
        // var inputs = {
        //   min: 20,
        //   max: 80,
        //   count: 8,
        //   decimals: 2,
        //   continuity: 1
        // };

        // function generateData() {
        //   return utils.numbers(inputs);
        // }

        // function generateLabels(config) {
        //   return utils.months({count: inputs.count});
        // }

        // utils.srand(42);

        // var data = {
        //   labels: generateLabels(),
        //   datasets: [{
        //     backgroundColor: utils.transparentize(presets.red),
        //     borderColor: presets.red,
        //     data: generateData(),
        //     hidden: true,
        //     label: 'D0'
        //   }, {
        //     backgroundColor: utils.transparentize(presets.orange),
        //     borderColor: presets.orange,
        //     data: generateData(),
        //     label: 'D1',
        //     fill: '-1'
        //   }, {
        //     backgroundColor: utils.transparentize(presets.yellow),
        //     borderColor: presets.yellow,
        //     data: generateData(),
        //     hidden: true,
        //     label: 'D2',
        //     fill: 1
        //   }, {
        //     backgroundColor: utils.transparentize(presets.green),
        //     borderColor: presets.green,
        //     data: generateData(),
        //     label: 'D3',
        //     fill: '-1'
        //   }, {
        //     backgroundColor: utils.transparentize(presets.blue),
        //     borderColor: presets.blue,
        //     data: generateData(),
        //     label: 'D4',
        //     fill: '-1'
        //   }, {
        //     backgroundColor: utils.transparentize(presets.grey),
        //     borderColor: presets.grey,
        //     data: generateData(),
        //     label: 'D5',
        //     fill: '+2'
        //   }, {
        //     backgroundColor: utils.transparentize(presets.purple),
        //     borderColor: presets.purple,
        //     data: generateData(),
        //     label: 'D6',
        //     fill: false
        //   }, {
        //     backgroundColor: utils.transparentize(presets.red),
        //     borderColor: presets.red,
        //     data: generateData(),
        //     label: 'D7',
        //     fill: 8
        //   }, {
        //     backgroundColor: utils.transparentize(presets.orange),
        //     borderColor: presets.orange,
        //     data: generateData(),
        //     hidden: true,
        //     label: 'D8',
        //     fill: 'end'
        //   }]
        // };

        // var options = {
        //   maintainAspectRatio: false,
        //   spanGaps: false,
        //   elements: {
        //     line: {
        //       tension: 0.000001
        //     }
        //   },
        //   scales: {
        //     yAxes: [{
        //       stacked: true
        //     }]
        //   },
        //   plugins: {
        //     filler: {
        //       propagate: false
        //     },
        //     samples_filler_analyser: {
        //       target: 'chart-analyser'
        //     }
        //   }
        // };

        // var chart = new Chart('chart-0', {
        //   type: 'line',
        //   data: data,
        //   options: options
        // });

        // function togglePropagate(btn) {
        //   var value = btn.classList.toggle('btn-on');
        //   chart.options.plugins.filler.propagate = value;
        //   chart.update();
        // }

        // function toggleSmooth(btn) {
        //   var value = btn.classList.toggle('btn-on');
        //   chart.options.elements.line.tension = value? 0.4 : 0.000001;
        //   chart.update();
        // }

        // function randomize() {
        //   chart.data.datasets.forEach(function(dataset) {
        //     dataset.data = generateData();
        //   });
        //   chart.update();
        // }

        /* ----------------------------------------------------------------------------------------------
            ------------------------------------------------------------------------------------------------ */



    }
    size(true);

}());
