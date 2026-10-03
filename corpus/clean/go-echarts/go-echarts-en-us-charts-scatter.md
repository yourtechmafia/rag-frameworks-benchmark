Charts Code

```
package examples

import (
	"io"
	"math/rand"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
)

var (
	itemCntScatter = 6
	sports         = []string{"Swimming", "Surfing", "Shooting ", "Skating", "Wrestling", "Diving"}
)

func generateScatterItems() []opts.ScatterData {
	items := make([]opts.ScatterData, 0)
	for i := 0; i < itemCntScatter; i++ {
		items = append(items, opts.ScatterData{
			Value:        rand.Intn(100),
			Symbol:       "roundRect",
			SymbolSize:   20,
			SymbolRotate: 10,
		})
	}
	return items
}
func scatterBase() *charts.Scatter {
	scatter := charts.NewScatter()
	scatter.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic scatter example"}),
	)

	scatter.SetXAxis(sports).
		AddSeries("Category A", generateScatterItems()).
		AddSeries("Category B", generateScatterItems())

	return scatter
}

func scatterShowLabel() *charts.Scatter {
	scatter := charts.NewScatter()
	scatter.SetGlobalOptions(charts.WithTitleOpts(
		opts.Title{
			Title: "label options",
		}),
	)

	scatter.SetXAxis(sports).
		AddSeries("Category A", generateScatterItems()).
		AddSeries("Category B", generateScatterItems()).
		SetSeriesOptions(charts.WithLabelOpts(
			opts.Label{
				Show:     opts.Bool(true),
				Position: "right",
			}),
		)
	return scatter
}

func scatterSplitLine() *charts.Scatter {
	scatter := charts.NewScatter()
	scatter.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{
			Title: "splitline options",
		}),
		charts.WithXAxisOpts(opts.XAxis{
			Name: "Sports",
			SplitLine: &opts.SplitLine{
				Show: opts.Bool(true),
			},
		}),
		charts.WithYAxisOpts(opts.YAxis{
			Name: "Score",
			SplitLine: &opts.SplitLine{
				Show: opts.Bool(true),
			}}),
	)

	scatter.SetXAxis(sports).
		AddSeries("Player A", generateScatterItems()).
		AddSeries("Player B", generateScatterItems())
	return scatter
}

type ScatterExamples struct{}

func (ScatterExamples) Examples() {
	page := components.NewPage()
	page.AddCharts(
		scatterBase(),
		scatterShowLabel(),
		scatterSplitLine(),
	)
	f, err := os.Create("examples/html/scatter.html")
	if err != nil {
		panic(err)
	}
	page.Render(io.MultiWriter(f))
}
```

---

 Charts Code

```
package examples

import (
	"io"
	"math/rand"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
)

var player = []string{"Kobe", "Jordan", "Iverson", "LeBron", "Wade", "McGrady"}

func generateEffectScatterItems() []opts.EffectScatterData {
	items := make([]opts.EffectScatterData, 0)
	for i := 0; i < len(player); i++ {
		items = append(items, opts.EffectScatterData{Value: rand.Intn(100)})
	}
	return items
}

func esBase() *charts.EffectScatter {
	es := charts.NewEffectScatter()
	es.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic EffectScatter example"}),
	)

	es.SetXAxis(player).
		AddSeries("Dunk", generateEffectScatterItems())
	return es
}

func esEffectStyle() *charts.EffectScatter {
	es := charts.NewEffectScatter()
	es.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{
			Title: "wave style",
		}),
	)

	es.SetXAxis(player).
		AddSeries("Dunk", generateEffectScatterItems(),
			charts.WithRippleEffectOpts(opts.RippleEffect{
				Period:    4,
				Scale:     10,
				BrushType: "stroke",
			})).
		AddSeries("Shoot", generateEffectScatterItems(),
			charts.WithRippleEffectOpts(opts.RippleEffect{
				Period:    3,
				Scale:     6,
				BrushType: "fill",
			}),
		)
	return es
}

type EffectscatterExamples struct{}

func (EffectscatterExamples) Examples() {
	page := components.NewPage()
	page.AddCharts(
		esBase(),
		esEffectStyle(),
	)

	f, err := os.Create("examples/html/effectscatter.html")
	if err != nil {
		panic(err)
	}
	page.Render(io.MultiWriter(f))
}
```

---
