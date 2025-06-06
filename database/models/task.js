'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Task extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  Task.init({
    description: DataTypes.TEXT,
    status: DataTypes.STRING,
    due_date: DataTypes.DATE
  }, {
    sequelize,
    modelName: 'Task',
  });
  return Task;
};