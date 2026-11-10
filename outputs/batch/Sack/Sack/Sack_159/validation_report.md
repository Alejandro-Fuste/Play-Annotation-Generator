# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_159`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 21 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 320: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-46] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-78] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-85] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-89] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-53] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [38-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-54] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-10] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-16] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-90] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-90] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [86-90] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-90] for track '20' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.