using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LightsController : MonoBehaviour
{
    public List<GameObject> lights;
    public float lightIntensity = 1;
    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        updateLightIntensity();
    }

    public void updateLightIntensity()
    {
        foreach(var lamp in lights)
        {
            lamp.GetComponent<Light>().intensity = lightIntensity;
        }
    }

}

