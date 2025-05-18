'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('meetings', [
      {
        id: '33333333-3333-3333-3333-333333333333',
        title: 'AI Project Kickoff',
        duration: 60,
        start_time: new Date(),
        created_at: new Date(),
        updated_at: new Date()
      }
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('meetings', null, {});
  }
};

