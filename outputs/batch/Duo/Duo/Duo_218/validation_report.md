# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_218`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_218/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-90] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-52] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-123] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-52] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [57-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-118] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-69] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-125] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-7] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-52] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-79] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [57-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-56] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '20' starts at frame 57, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [57-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-40] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-114] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-67] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-76] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-125] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-125] for track '28' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.