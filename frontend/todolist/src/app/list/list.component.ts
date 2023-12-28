import { Component, OnInit } from '@angular/core';
import {ToDosService} from '../todos.service';

@Component({
  selector: 'todo-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'],
  providers: [ToDosService],
})
export class ListComponent implements OnInit {

  constructor(private todosservice: ToDosService) { }
  getToDos(){
    this.todosservice.getToDos()
    .then(todos => this.todos = todos)
    .catch(error => this.error = error);
  }

  todos: any[];
  selectedToDo: any;
  error: string;
  status: string;

  ngOnInit() {
    this.getToDos();
    this.status = "Saved";
  }

  clickedToDo(todo){
    if(this.selectedToDo){

    }
    this.selectedToDo = todo;
  }

  addToDo(event){
    this.todos.unshift(event.value);
  }

  private typedTimeout;
  keyTyped(todo){
    clearTimeout(this.typedTimeout);
    this.typedTimeout = setTimeout(() => {
      this.updateToDo(todo);
    }, 1500);
  }

  updateToDo(todo){
    this.status = "Updating...";
    setTimeout(() => {
      this.todosservice.updateToDo(todo).subscribe(
        result => {
          this.status = "Updated.";
        },
        error => {
          this.status = "Error when updating.";
        }
      );
    }, 100);
  }

  deleteToDo(todo){
    this.status = "Deleting...";
    this.todosservice.deleteToDo(todo.id).subscribe(
      result => {
        this.status = "Deleted.";
        this.todos = this.todos.filter(todocheck => {
          return todocheck.id !== todo.id;
        });
      },
      error => {
        this.status = "Error when deleting.";
      }
    );
  }

}
