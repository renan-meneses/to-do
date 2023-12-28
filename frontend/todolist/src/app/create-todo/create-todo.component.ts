import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import {ToDosService} from '../todos.service';
import { ListComponent } from '../list/list.component';

@Component({
  selector: 'create-todo',
  templateUrl: './create-todo.component.html',
  styleUrls: ['./create-todo.component.css'],
  providers: [ToDosService],
})
export class CreateTodoComponent implements OnInit {

  constructor(private todosservice: ToDosService) { }

  inputText: string;
  tipText: string;
  @Output() status: string;
  defaultTipText = "Press enter to add todo";
  emptyTipText = "Todo can not be empty";
  placeholder = 'Add todo...';
  @Output() addedtodo = new EventEmitter();

  ngOnInit() {
      this.inputText = '';
      this.tipText = this.defaultTipText;
      this.status = '';
  }

  addToDo(){
    this.status = "Adding...";
    this.todosservice.addToDo(this.inputText).subscribe(
      result => {
        this.status = "Added.";
        this.addedtodo.emit({value: result});
      },
      error => {
        this.status = "Error when adding.";
      },
    );
    this.inputText = "";
  }

  computeTip(){
    if(this.inputText == ''){
      this.tipText = this.emptyTipText;
      setTimeout(() => {
        this.tipText = this.defaultTipText;
      }, 2000)
    }
    else{
      this.tipText = this.defaultTipText;
    }
  }

}
