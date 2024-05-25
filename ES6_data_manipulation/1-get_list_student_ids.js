/* eslint-disable */
export default function getListStudentIds(objects) {
    if (!Array.isArray(objects)) {
      return [];
    }
    return objects.map(item => item.id);
  }