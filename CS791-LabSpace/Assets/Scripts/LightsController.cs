using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class LightsController : MonoBehaviour
{
    public List<GameObject> lights;
    public Slider lightSlider;
    public float lightIntensity = 1;

    // Start is called before the first frame update
    void Start()
    {
        lightSlider.value = 0.5f;
        lightSlider.maxValue = 1.5f;
    }

    // Update is called once per frame
    void Update()
    {
        lightIntensity = lightSlider.value;
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

