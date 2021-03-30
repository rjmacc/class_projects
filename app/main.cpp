// main.cpp
//
// ICS 46 Spring 2020
// Project #5: Rock and Roll Stops the Traffic
//
// This is the program's main() function, which is the entry point for your
// console user interface.


#include "TripReader.hpp"
#include "RoadMapReader.hpp"
#include <iostream>
#include <string>

struct miles {
    double operator()(RoadSegment seg) {return seg.miles;};
};

struct mph {
    double operator()(RoadSegment seg) {return seg.miles * seg.milesPerHour;};
};

int main()
{
    RoadMapReader r;
    InputReader in = InputReader(std::cin);
    RoadMap roadMap = r.readRoadMap(in);
   
    TripReader t;
    std::vector<Trip> trips = t.readTrips(in);

    for (int i = 0; i < trips.size(); ++i)
    {
        std::string line = in.readLine();
        std::cout << "Shortest distance from " + roadMap.vertexInfo(trips[i].startVertex);
        std::cout << " to " + roadMap.vertexInfo(trips[i].endVertex) << std::endl;
        std::cout << "Begin at " + roadMap.vertexInfo(trips[i].startVertex);

        if (trips[i].metric == TripMetric::Distance)
        {
            std::map<int, int> shortestPaths = roadMap.findShortestPaths(trips[i].startVertex, miles());
        } else {
            std::map<int, int> shortestPaths = roadMap.findShortestPaths(trips[i].startVertex, mph());
        }
    
        
    }
    return 0;
}


