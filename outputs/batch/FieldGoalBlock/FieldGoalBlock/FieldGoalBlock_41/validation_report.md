# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_41`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 20 |
| Player Tracks | 20 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [56-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-77] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_KickBall' range [56-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-62] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-97] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-89] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-54] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-74] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-120] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-120] for track '19' has 2 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.