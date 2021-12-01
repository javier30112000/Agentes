using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LectorDeCordenadas : MonoBehaviour
{
public TextAsset cordenadasAuto;
private string theWholeText;
private List<string> lines;

private string DelitionOfTrashLeft = "[";
private string delitionOfTrashRight = "]";

private string tempStr;

private float x;
private float y;

private int contador = 0;
private float timer = 0f;
public float wait = 0f;

    // Start is called before the first frame update
    void Start()
    {
        
        theWholeText = cordenadasAuto.text;

        lines = new List<string>();
        lines.AddRange(theWholeText.Split("\n"[0]));

        Debug.Log(lines[1]);
        /*
        tempStr = lines[1];
        tempStr = tempStr.Replace(DelitionOfTrashLeft, "");
        tempStr = tempStr.Replace(delitionOfTrashRight, "");
        Debug.Log(tempStr);
        Debug.Log("Tamaño de str: " + tempStr.Length);

        if (tempStr.Length == 8){
            Debug.Log("Fue al 8");
            x = float.Parse(tempStr.Substring(0,3));
            y = float.Parse(tempStr.Substring(4,3));
        }
        else if (tempStr.Length == 9){
            Debug.Log("Fue al 9");
            x = float.Parse(tempStr.Substring(0,4));
            y = float.Parse(tempStr.Substring(5,3));
        }
        else if (tempStr.Length == 10){
            x = float.Parse(tempStr.Substring(0,4));
            y = float.Parse(tempStr.Substring(5,4));
        }

        Debug.Log(x);
        Debug.Log(y);
        Vector3 target = new Vector3 (x, 0f, y);

        //------------------------------------------

        transform.position = target;
        */
        Debug.Log("length of list: " + lines.Count);
    }

    // Update is called once per frame
    void Update()
    {
        timer += 1 * Time.deltaTime;
        if(timer >= wait){
            if(contador < lines.Count){
                tempStr = lines[contador];
                tempStr = tempStr.Replace(DelitionOfTrashLeft, "");
                tempStr = tempStr.Replace(delitionOfTrashRight, "");
                Debug.Log(tempStr);
                Debug.Log("Tamaño de str: " + tempStr.Length);

                if (tempStr.Length == 8){
                    Debug.Log("Fue al 8");
                    x = float.Parse(tempStr.Substring(0,3));
                    y = float.Parse(tempStr.Substring(4,3));
                }
                else if (tempStr.Length == 9){
                    Debug.Log("Fue al 9");
                    x = float.Parse(tempStr.Substring(0,4));
                    y = float.Parse(tempStr.Substring(5,3));
                }
                else if (tempStr.Length == 10){
                    Debug.Log("Fue al 10");
                    x = float.Parse(tempStr.Substring(0,4));
                    y = float.Parse(tempStr.Substring(5,4));
                }

                Debug.Log(x);
                Debug.Log(y);
                Vector3 target = new Vector3 (x, 0f, y);

                //------------------------------------------

                transform.position = target;
                contador++;
                Debug.Log("The counter is: " + contador);
            }
            timer = 0;
            Debug.Log("Loading...");
        }
    }

    IEnumerator YieldCoroutine(){
        Debug.Log("Loading...");
        yield return new WaitForSeconds(5);
    }

}
