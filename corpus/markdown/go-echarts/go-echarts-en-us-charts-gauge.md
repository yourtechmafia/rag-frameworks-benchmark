Skip to main content




Clear search

`/`
`⌃K`

[go-echarts](/go-echarts/)
==========================

![art](https://github.githubassets.com/images/icons/emoji/unicode/1f3a8.png?v8.png) Charts![musical_keyboard](https://github.githubassets.com/images/icons/emoji/unicode/1f3b9.png?v8.png) Code

```
package examples

import (
	"fmt"
	"io"
	"math/rand"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
)

func gaugeBase() *charts.Gauge {
	gauge := charts.NewGauge()
	gauge.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic Gauge example"}),
	)

	gauge.AddSeries("ProjectA", []opts.GaugeData{{Name: "Work progress", Value: rand.Intn(50)}})
	return gauge
}

func gaugeTimer() *charts.Gauge {
	gauge := charts.NewGauge()
	gauge.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "javascript timer"}),
	)

	gauge.AddSeries("ProjectB", []opts.GaugeData{{Name: "Work progress", Value: rand.Intn(50)}})

	fn := fmt.Sprintf(`setInterval(function () {
			option_%s.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
			goecharts_%s.setOption(option_%s, true);
		}, 2000);`, gauge.ChartID, gauge.ChartID, gauge.ChartID)
	gauge.AddJSFuncs(fn)
	return gauge
}

type GaugeExamples struct{}

func (GaugeExamples) Examples() {
	page := components.NewPage()
	page.AddCharts(
		gaugeBase(),
		gaugeTimer(),
	)

	f, err := os.Create("examples/html/gauge.html")
	if err != nil {
		panic(err)
	}
	page.Render(io.MultiWriter(f))
}
```

---