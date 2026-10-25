# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_15`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [40–56], lower_priority='Action_RunBlock' annotated_start=48, effective_Action_RunBlock_start=57.
> - Action 'Action_None' range [40-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-81] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-187] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-204] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-119] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-210] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [40-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [57-67] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [71-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-112] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [116-144] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [146-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [193-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [48-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [56-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-128] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [131-140] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-164] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-16] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-204] for track '22' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-128] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-167] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '28' has 2 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.