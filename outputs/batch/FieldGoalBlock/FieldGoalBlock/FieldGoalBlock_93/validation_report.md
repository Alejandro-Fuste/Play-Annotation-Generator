# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_93`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [30-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-120] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-60] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-57] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [35-37] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-52] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 30, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [30-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '26' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.