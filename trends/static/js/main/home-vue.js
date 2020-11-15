const vm = new Vue({
    delimiters: ['{*', '*}'],
    el: '#statApp',
    data: {
        frequences: [],
        profs: [],
        top_profs: [],
        under_profs: [],
        selected_prof: {},
        selected_profs_freqs: [],
        prof_chart: undefined,
        search_text: '',
        visible_profs: [],
    },
    mounted () {
        fetch('/api/v1/get_freqs')
        .then(response => response.json())
        .then(data => {
            this.frequences = data
        })

        fetch('/api/v1/get_profs')
        .then(response => response.json())
        .then(data => {
            this.profs = data
            this.visible_profs = data
            data.reverse()
            this.under_profs = data.slice(0,5)
            this.top_profs = data.reverse().slice(0,5)
        }).then(() => {

            let counts = this.profs.map(el => {
                return el.frequencies_count
            })
            let names = this.profs.map(el => {
                return el.name
            })

            let coefs = this.profs.map(el => {
                return el.coeff
            })

            let ctx = document.getElementById('relationsChart').getContext('2d');
            new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: names,
                    datasets: [{
                        label: 'Соотношение профессий',
                        data: counts,
                        backgroundColor: [
                            "#9ef3a2",
                            "#8bd88d",
                            "#74c778",
                            "#54bb5a",
                            "#38ac40",
                            "#329539",
                            "#2a8230",
                            "#0b7a13",
                            "#014f07",
                            "#013b05",
                        ]
                    }]
                }
            });

            let ctx2 = document.getElementById('coeffsChart').getContext('2d');
            new Chart(ctx2, {
                type: 'bar',
                data: {
                    labels: names,
                    datasets: [{
                        label: 'Коэффициент роста',
                        data: coefs,
                        backgroundColor: [
                            "#9ef3a2",
                            "#8bd88d",
                            "#74c778",
                            "#54bb5a",
                            "#38ac40",
                            "#329539",
                            "#2a8230",
                            "#0b7a13",
                            "#014f07",
                            "#013b05",
                        ]
                    }]
                }
            });
        })
    },
    methods: {
        searchProfsClicked: function() {
            let search_box = document.getElementById('search_text')
            this.search_text = search_box.value;
            
            this.visible_profs = this.profs.filter(el => {
                return el.name.toLowerCase().includes(this.search_text.toLowerCase())
            })

            let tab = document.getElementById('general-tab')
            tab.click()
        },
        selectProfession: function(name) {
            this.selected_prof = this.profs.find(el => {
                return el.name == name
            })

            this.drawChart(name);
        },
        exportCSV: function() {
            let data = this.profs;

            var csv = this.convertArrayOfObjectsToCSV({
                data: data
            });

            if (csv == null) return;

            filename = 'export.csv';

            if (!csv.match(/^data:text\/csv/i)) {
                csv = 'data:text/csv;charset=utf-8,' + csv;
            }
            data = encodeURI(csv);

            link = document.createElement('a');
            link.setAttribute('href', data);
            link.setAttribute('download', filename);
            link.click();
        },
        convertArrayOfObjectsToCSV: function(args) {
            var result, ctr, keys, columnDelimiter, lineDelimiter, data;
            
            data = args.data || null;
            if (data == null || !data.length) {
            return null;
            }
            
            columnDelimiter = args.columnDelimiter || ',';
            lineDelimiter = args.lineDelimiter || '\n';
            
            keys = Object.keys(data[0]);
            
            result = '';
            result += keys.join(columnDelimiter);
            result += lineDelimiter;
            
            data.forEach(function(item) {
            ctr = 0;
            keys.forEach(function(key) {
            if (ctr > 0) result += columnDelimiter;
            
            result += item[key];
            ctr++;
            });
            result += lineDelimiter;
            });
            
            return result;
        },
        drawChart: function(name) {
            this.selected_profs_freqs = this.frequences.filter(el => {
                return el.name == name;
            }).map(el => {
                let n_date = Date.parse(el.date);
                n_date = new Date(n_date);
                n_date = n_date.getMonth()+1 + '.' + n_date.getFullYear();

                return {
                    'date': n_date,
                    'count': el.count,
                }
            });
            

            let counts = this.selected_profs_freqs.map(el => {
                return el.count
            })
            let dates = this.selected_profs_freqs.map(el => {
                return el.date
            })

            if(this.prof_chart) {
                this.prof_chart.data.datasets = [{
                    label: 'Частота упоминаний',
                    data: counts,
                    borderColor: '#69C54D',
                    backgroundColor: 'rgba(105,197,77,0.5)',
                }];
                this.prof_chart.update()
            } else {
                let ctx = document.getElementById('professionChart').getContext('2d');
                this.prof_chart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: dates,
                        datasets: [{
                            label: 'Частота упоминаний',
                            data: counts,
                            borderColor: '#69C54D',
                            backgroundColor: 'rgba(105,197,77,0.5)',
                        }]
                    }
                });
            }
        }
    }
})