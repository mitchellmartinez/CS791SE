using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading;
using UnityEngine;
using Assets.Classes;
using System;

public class MetricsController : MonoBehaviour
{
    // Create a new instance of Metrics 
    public Metrics UserMetrics = new Metrics();

    // Instance utilities for metric tracking
    Stopwatch stopWatch = new Stopwatch();
    int status = 0;

    // Start is called before the first frame update
    void Start()
    {
        stopWatch.Start();
    }

    // Update is called once per frame
    void Update()
    {
        // Update Metrics every frame 
        UserMetrics.timeElapsed = stopWatch.ElapsedMilliseconds.ToString("mm\\:ss\\.ff");
    }

    public void SendMetrics()
    {
        // Database connection will go here
        System.Console.Write("User Metrics Sent");
    }
}
