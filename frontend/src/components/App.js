import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/task")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <ul className="list-group">
        {this.state.data.map((task) => {
          return (
            <button
              type="button"
              className="list-group-item list-group-item-action"
              key={task.id}
            >
              {task.name} - {task.deadline_date}
            </button>
          );
        })}
      </ul>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
