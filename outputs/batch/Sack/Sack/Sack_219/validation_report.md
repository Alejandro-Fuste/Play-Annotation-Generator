# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_219`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-46] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [73-81] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [85-89] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-90] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-18] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-73] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-23] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-90] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-90] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-90] for track '21' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.