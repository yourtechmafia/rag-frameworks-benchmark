Skip to main content




Clear search

`/`
`⌃K`

[go-echarts](/go-echarts/)
==========================

* Basic
  + [Setup go-echarts](#/en-us/ "Setup go-echarts")
* Concepts
  + [Dive into go-echarts](#/en-us/dive-into "Dive into go-echarts")
  + [Chart Container](#/en-us/chart-container "Chart Container")
  + [Event and Action](#/en-us/event-and-action "Event and Action")
  + [Chart Render](#/en-us/render "Chart Render")
* Advanced
  + [ConfigurationVisitor](#/en-us/visitor "ConfigurationVisitor")
  + [Render to Image](#/en-us/render-to-image "Render to Image")
* Chart Configration
  + [Global Option Summary](#/en-us/options/global "Global Option Summary")
  + [Series Option Summary](#/en-us/options/series "Series Option Summary")
  + Options
    - [title](#/en-us/options/title "title")
    - [grid](#/en-us/options/grid "grid")
    - [legend](#/en-us/options/legend "legend")
    - [xAxis](#/en-us/options/xAxis "xAxis")
    - [yAxis](#/en-us/options/yAxis "yAxis")
* [Ecosystem](#/en-us/ecosystem "Ecosystem")
* Examples with sample code
  + [Line](#/en-us/charts/line "Line")
  + [Bar](#/en-us/charts/bar "Bar")
  + [Pie](#/en-us/charts/pie "Pie")
  + [Scatter](#/en-us/charts/scatter "Scatter")
  + [Geo/Map](#/en-us/charts/map "Geo/Map")
  + [Candlestick/Kline](#/en-us/charts/kline "Candlestick/Kline")
  + [Radar](#/en-us/charts/radar "Radar")
  + [Boxplot](#/en-us/charts/boxplot "Boxplot")
  + [Heatmap](#/en-us/charts/heatmap "Heatmap")
  + [Graph](#/en-us/charts/graph "Graph")
  + [Tree](#/en-us/charts/tree "Tree")
  + [Treemap](#/en-us/charts/treemap "Treemap")
  + [Sunburst](#/en-us/charts/sunburst "Sunburst")
  + [Parallel](#/en-us/charts/parallel "Parallel")
  + [Sankey](#/en-us/charts/sankey "Sankey")
  + [Funnel](#/en-us/charts/funnel "Funnel")
  + [Gauge](#/en-us/charts/gauge "Gauge")
  + [ThemeRiver](#/en-us/charts/themeriver "ThemeRiver")
  + [Bar3D](#/en-us/charts/bar3d "Bar3D")
  + [Scatter3D](#/en-us/charts/scatter3d "Scatter3D")
  + [Surface3D](#/en-us/charts/surface3d "Surface3D")
  + [Line3D](#/en-us/charts/line3d "Line3D")
  + [Liquid](#/en-us/charts/liquid "Liquid")
  + [WordCloud](#/en-us/charts/wordcloud "WordCloud")

![art](https://github.githubassets.com/images/icons/emoji/unicode/1f3a8.png?v8.png) Charts![musical_keyboard](https://github.githubassets.com/images/icons/emoji/unicode/1f3b9.png?v8.png) Code

```
package examples

import (
	"io"
	"math/rand"
	"os"
	"strconv"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
)

func generateSunburstItems() []opts.SunBurstData {
	items := make([]opts.SunBurstData, 0)
	for i := 0; i < 7; i++ {
		items = append(items, opts.SunBurstData{
			Value: rand.Float64(),
			Name:  "parent-" + strconv.Itoa(i),
			Children: []*opts.SunBurstData{
				{
					Value: rand.Float64(),
					Name:  "child-" + strconv.Itoa(i),
				},
			},
		})
	}
	return items
}

func sunburstBase() *charts.Sunburst {
	sunburst := charts.NewSunburst()
	sunburst.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic sunburst example"}),
	)
	sunburst.AddSeries("sunburst", generateSunburstItems())
	return sunburst
}

type SunburstExample struct{}

func (SunburstExample) Examples() {
	page := components.NewPage()
	page.AddCharts(
		sunburstBase(),
	)
	f, err := os.Create("examples/html/sunburst.html")
	if err != nil {
		panic(err)
	}
	page.Render(io.MultiWriter(f))

}

Copy to clipboardErrorCopied
```

---