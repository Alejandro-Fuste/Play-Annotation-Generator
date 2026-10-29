# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_179`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_179/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-100] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-46] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-91] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-100] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-97] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-95] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [34-72] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-96] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-83] for track '13' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [34-72] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-96] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-100] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [34-35] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [38-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [43-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-95] for track '19' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-63] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-83] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-96] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-95] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-90] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-95] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-91] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.