package main

import (
	"fmt"
	"limelightmaster/searchtree"

	"github.com/gookit/color"
)

func BleedingEdgeCall() {
	fmt.Println("\tWelcome to the Bloody Edge")
	fmt.Println("\t(Be careful)")
	fmt.Println("\t(Experiment!!)")
	fmt.Println("\tHAVE FUN!!!\n\n\n")

	words := []*searchtree.Commit{
		searchtree.NewCommit("ABC", 4, false),
		searchtree.NewCommit("ADA", 8, false),
		searchtree.NewCommit("ABBY", 3, false),
		searchtree.NewCommit("ALEX", 4, false),
		searchtree.NewCommit("ALEXANDER", 6, false),

		searchtree.NewCommit("ALEXA", 5, false),
		searchtree.NewCommit("ALEXIS", 3, false),
		// searchtree.NewCommit("CRISTINA", 3, false),
		// searchtree.NewCommit("CRISSIE", 4, false),
		// searchtree.NewCommit("CRISSIED", 94, false),
		// searchtree.NewCommit("CRISSIEXX", 64, false),
	}

	tree := searchtree.NewSearchTree(words)

	tree.PrintTree()

	fmt.Println()

	fmt.Println("WORD | VALUE")
	for _, word := range words {
		fmt.Println(word.Member[0:len(word.Member)-1] + " : " + color.Yellow.Sprint(word.Value))
	}
}
