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
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"os"

	"github.com/go-echarts/go-echarts/v2/charts"
	"github.com/go-echarts/go-echarts/v2/components"
	"github.com/go-echarts/go-echarts/v2/opts"
)

var graphNodes = []opts.GraphNode{
	{Name: "Node1"},
	{Name: "Node2"},
	{Name: "Node3"},
	{Name: "Node4"},
	{Name: "Node5"},
	{Name: "Node6"},
	{Name: "Node7"},
	{Name: "Node8"},
}

func genLinks() []opts.GraphLink {
	links := make([]opts.GraphLink, 0)
	for i := 0; i < len(graphNodes); i++ {
		for j := 0; j < len(graphNodes); j++ {
			links = append(links, opts.GraphLink{Source: graphNodes[i].Name, Target: graphNodes[j].Name})
		}
	}
	return links
}

func graphBase() *charts.Graph {
	graph := charts.NewGraph()
	graph.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "basic graph example"}),
	)
	graph.AddSeries("graph", graphNodes, genLinks(),
		charts.WithGraphChartOpts(
			opts.GraphChart{Force: &opts.GraphForce{Repulsion: 8000}},
		),
	)
	return graph
}

func graphCircle() *charts.Graph {
	graph := charts.NewGraph()
	graph.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{Title: "Circular layout"}),
	)

	graph.AddSeries("graph", graphNodes, genLinks()).
		SetSeriesOptions(
			charts.WithGraphChartOpts(
				opts.GraphChart{
					Force:  &opts.GraphForce{Repulsion: 8000},
					Layout: "circular",
				}),
			charts.WithLabelOpts(opts.Label{Show: opts.Bool(true), Position: "right"}),
		)
	return graph
}

func graphNpmDep() *charts.Graph {
	graph := charts.NewGraph()
	graph.SetGlobalOptions(
		charts.WithTitleOpts(opts.Title{
			Title: "npm dependencies demo",
		}))

	f, err := ioutil.ReadFile("fixtures/npmdepgraph.json")
	if err != nil {
		panic(err)
	}

	type Data struct {
		Nodes []opts.GraphNode
		Links []opts.GraphLink
	}

	var data Data
	if err := json.Unmarshal(f, &data); err != nil {
		fmt.Println(err)
	}

	graph.AddSeries("graph", data.Nodes, data.Links).
		SetSeriesOptions(
			charts.WithGraphChartOpts(opts.GraphChart{
				Layout:             "none",
				Roam:               opts.Bool(true),
				FocusNodeAdjacency: opts.Bool(true),
			}),
			charts.WithEmphasisOpts(opts.Emphasis{
				Label: &opts.Label{
					Show:     opts.Bool(true),
					Color:    "black",
					Position: "left",
				},
			}),
			charts.WithLineStyleOpts(opts.LineStyle{
				Curveness: 0.3,
			}),
		)
	return graph
}

type GraphExamples struct{}

func (GraphExamples) Examples() {
	page := components.NewPage()
	page.AddCharts(
		graphBase(),
		graphCircle(),
		graphNpmDep(),
	)

	f, err := os.Create("examples/html/graph.html")
	if err != nil {
		panic(err)

	}
	page.Render(io.MultiWriter(f))
}

Copy to clipboardErrorCopied
```

---