def drawComparison( X, actualY, predY, n_rows = 1, row = 1 ):
    
    skip = (row - 1) * 2
    isoX = Isomap().fit_transform( X )
    plt.subplot( n_rows, 2, skip + 1 )
    plt.scatter( isoX[:,0], isoX[:,1], c = actualY )
    plt.title( "Actual" )
    plt.subplot( n_rows, 2, skip + 2 )
    plt.scatter( isoX[:,0], isoX[:,1], c = predY )
    plt.title( "Prediction" )
    plt.show()
    plt.tight_layout( pad = .1 )