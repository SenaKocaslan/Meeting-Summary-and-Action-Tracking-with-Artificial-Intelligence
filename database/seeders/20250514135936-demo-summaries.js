'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert('summaries', [
      {
        id: '66666666-6666-6666-6666-666666666666',
        content: 'Summary: Goals of the AI project discussed.',
        meeting_id: '33333333-3333-3333-3333-333333333333',
        created_at: new Date(),
        updated_at: new Date()
      }
    ]);
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete('summaries', null, {});
  }
};

