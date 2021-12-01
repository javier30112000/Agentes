using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MovimientoPeatonal : MonoBehaviour
{
    public float speed = 10f;

    private Transform target;
    private int wavepointIndex = 0;

    void Start(){
        target = Waypoints.points[0];
    }

    void Update(){
        Vector3 direct = target.position - transform.position;
        transform.Translate(direct.normalized * speed * Time.deltaTime);

        if (Vector3.Distance(transform.position, target.position) <= 0.4f){
            GetNextWaypoint();
        }


    }

    void GetNextWaypoint(){
        /*
        if (wavepointIndex >= Waypoints.points.Length - 1){
            Destroy(gameObject);
            return;
        }
*/
        wavepointIndex = Random.Range(0, Waypoints.points.Length);
        target = Waypoints.points[wavepointIndex];
    }

}
