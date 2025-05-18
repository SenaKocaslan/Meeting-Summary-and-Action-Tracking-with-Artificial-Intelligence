'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('tasks', [
      {
        id: '77777777-7777-7777-7777-777777777777',
        description: 'Create GitHub repository for AI project',
        status: 'todo',
        participant_id: '44444444-4444-4444-4444-444444444444',
        meeting_id: '33333333-3333-3333-3333-333333333333',
        created_at: new Date(),
        updated_at: new Date()
      }
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('tasks', null, {});
  }
};

