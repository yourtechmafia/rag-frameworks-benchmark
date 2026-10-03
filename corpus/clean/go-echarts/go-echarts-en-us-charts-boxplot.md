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

 Charts Code

```
package examples

import (
	"io"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
	"github.com/montanaflynn/stats"
)

var (
	bpX = [...]string{"expr1", "expr2", "expr3", "expr4", "expr5"}
	bpY = [][]float64{
		{850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960},
		{960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800},
		{880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910, 850, 870, 840, 840, 850, 840, 840, 840},
		{890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920, 890, 860, 880, 720, 840, 850, 850, 780},
		{890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870},
	}
)

func createBoxPlotData(data []float64) []float64 {
	min, _ := stats.Min(data)
	max, _ := stats.Max(data)
	q, _ := stats.Quartile(data)

	return []float64{
		min,
		q.Q1,
		q.Q2,
		q.Q3,
		max,
	}
}

func generateBoxPlotItems(boxPlotData [][]float64) []opts.BoxPlotData {
	items := make([]opts.BoxPlotData, 0)
	for i := 0; i < len(boxPlotData); i++ {
		items = append(items, opts.BoxPlotData{Value: createBoxPlotData(boxPlotData[i])})
	}
	return items

}

func boxPlotBase() *charts.BoxPlot {
	bp := charts.NewBoxPlot()
	bp.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic boxplot example"}),
	)

	bp.SetXAxis(bpX).AddSeries("boxplot", generateBoxPlotItems(bpY))
	return bp
}

func boxPlotMulti() *charts.BoxPlot {
	bp := charts.NewBoxPlot()
	bp.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "boxplot with multi-series"}),
	)

	bp.SetXAxis(bpX[:2]).
		AddSeries("series1", generateBoxPlotItems(bpY[:2])).
		AddSeries("series2", generateBoxPlotItems(bpY[2:]))
	return bp
}

type BoxplotExamples struct{}

func (BoxplotExamples) Examples() {
	page := components.NewPage()
	page.AddCharts(
		boxPlotBase(),
		boxPlotMulti(),
	)
	f, err := os.Create("examples/html/boxplot.html")
	if err != nil {
		panic(err)
	}
	page.Render(io.MultiWriter(f))
}

Copy to clipboardErrorCopied
```

---
