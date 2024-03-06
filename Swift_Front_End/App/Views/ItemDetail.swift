import SwiftUI
import RealmSwift
import PhotosUI

/// Show a detail view of a task Item. User can edit the summary or mark the Item complete.
struct ItemDetail: View {
    // This property wrapper observes the Item object and
    // invalidates the view when the Item object changes.
    @ObservedRealmObject var item: Item
    
    var body: some View {
        Form {
            Section(header: Text("Edit Item Summary")) {
                // Accessing the observed item object lets us update the live object
                // No need to explicitly update the object in a write transaction
                TextField("Summary", text: $item.summary)
            }
            Section {
                Toggle(isOn: $item.isComplete) {
                    Text("Complete")
                }
            }
            Section {
                VStack {
                    if (item.image != nil && item.image!.picture != nil) {
                        Image(uiImage: UIImage(data: item.image!.picture!)!)
                            .resizable()
                            .scaledToFit()
                    } else {
                        Image(uiImage: UIImage(named: "nopicture")!)
                            .resizable()
                            .scaledToFit()
                    }
                    Spacer()
                }
            }
        }
        .navigationBarTitle("Update Item", displayMode: .inline)
    }
}
