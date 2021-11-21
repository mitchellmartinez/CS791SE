using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;

public class SoundController : MonoBehaviour
{
    public List<GameObject> soundObjects;
    public Slider soundSlider;
    public float soundLevel = 1;

    // Start is called before the first frame update
    void Start()
    {
        soundSlider.value = 0.5f;
        soundSlider.maxValue = 1.0f;
    }

    // Update is called once per frame
    void Update()
    {
        soundLevel = soundSlider.value;
        updateVolume();
    }

    public void updateVolume()
    {
        foreach (var speaker in soundObjects)
        {
            speaker.GetComponent<VideoPlayer>().SetDirectAudioVolume(0, soundLevel);
        }
    }
}
