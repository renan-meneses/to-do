import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import 'rxjs/add/operator/toPromise';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import { Observable } from 'rxjs/Observable';

import { Headers, RequestOptions } from '@angular/http';

@Injectable()
export class ToDosService {

  private apiURL = 'http://localhost:8000/todos/'
  constructor(private http: Http) { }
  getToDos() {
    /*return Promise.resolve([
    {
      "example": "1",
    },
    {
      "example": "2",
    },
  ]);*/
    return this.http.get(this.apiURL)
                .toPromise()
                .then(response => response.json().results)
                .catch(this.handleError);
  }

  addToDo(text){
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let params:string = JSON.stringify({ "text": text,
                                        "finished": false,
                                        "time_finished": null });
    let options = new RequestOptions({ headers: headers });
    return this.http.post(this.apiURL, params, options)
                     .map(this.extractData)
                     .catch(this.handleError);
  }

  updateToDo(todo){
    let headers = new Headers({ 'Content-Type': 'application/json' });
    let params:string = JSON.stringify(todo);
    let options = new RequestOptions({ headers: headers });
    return this.http.put(this.apiURL+todo.id+"/", params, options)
                     .map(this.extractData)
                     .catch(this.handleError);
  }

  deleteToDo(id){
    return this.http.delete(this.apiURL+id+"/", {})
                     .map(this.extractData)
                     .catch(this.handleError);
  }

  extractData(data){
      return data.json();
  }

  private handleError(error: any) {
    console.error('An error occurred', error);
    return Promise.reject(error.message || error);
  }
}
