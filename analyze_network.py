#!/usr/bin/env python3
"""
Network analysis script for DM1 pharmacology project.

This script loads a protein-protein interaction network and calculates
centrality metrics to identify key genes.
"""

import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def load_network(edge_file):
    """
    Load network from a TSV file with columns: gene1, gene2, weight.
    """
    df = pd.read_csv(edge_file, sep='\t')
    G = nx.Graph()
    for _, row in df.iterrows():
        G.add_edge(row['gene1'], row['gene2'], weight=row['weight'])
    return G

def compute_centrality(G):
    """
    Compute degree centrality for all nodes in the graph.
    Returns a dictionary mapping gene to centrality score.
    """
    centrality = nx.degree_centrality(G)
    return centrality

def main():
    # Path to the edge list (example data)
    edge_file = 'data/ppi_network.tsv'
    
    # Load network
    print("Loading network...")
    G = load_network(edge_file)
    print(f"Network contains {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    
    # Compute centrality
    print("Computing degree centrality...")
    centrality = compute_centrality(G)
    
    # Sort by centrality
    sorted_centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    
    # Output top 10 genes
    print("\nTop 10 genes by degree centrality:")
    for gene, score in sorted_centrality[:10]:
        print(f"  {gene}: {score:.4f}")
    
    # Save results to file
    df = pd.DataFrame(list(centrality.items()), columns=['gene', 'degree_centrality'])
    df.to_csv('results/centrality_scores.csv', index=False)
    print("\nResults saved to results/centrality_scores.csv")
    
    # Optional: plot degree distribution
    degrees = [d for n, d in G.degree()]
    plt.hist(degrees, bins=20, edgecolor='black')
    plt.xlabel('Degree')
    plt.ylabel('Frequency')
    plt.title('Degree Distribution of DM1 PPI Network')
    plt.savefig('results/degree_distribution.png', dpi=300)
    plt.close()
    print("Plot saved to results/degree_distribution.png")

if __name__ == '__main__':
    main()