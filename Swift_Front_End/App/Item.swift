import RealmSwift
import SwiftUI

class Item: Object, ObjectKeyIdentifiable {
    @Persisted(primaryKey: true) var _id: ObjectId
    @Persisted var isComplete = false
    @Persisted var summary: String
    @Persisted var owner_id: String
    @Persisted var image: Photo?
    @Persisted var severity: String?
    @Persisted var claim_estimate: Double?
}
