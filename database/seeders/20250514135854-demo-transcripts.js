'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('transcripts', [
      {
        id: '55555555-5555-5555-5555-555555555555',
        filename: 'kickoff.mp3',
        content: 'Welcome to the AI project kickoff meeting...',
        meeting_id: '33333333-3333-3333-3333-333333333333',
        created_at: new Date(),
        updated_at: new Date()
      }
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('transcripts', null, {});
  }
};

