# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_256`
- **Input XML**: `outputs/batch/Power/Power/Power_256/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 57 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 512: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 512: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 512: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - Row 512: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '6' (RT) duration 105 frames exceeds threshold 90 frames [start=58, end=162].
> - Validation warning: Action 'Action_DownBlock' for track '7' (Unknown) duration 105 frames exceeds threshold 90 frames [start=58, end=162].
> - Validation warning: Action 'Action_PullBlock' for track '14' (LG) duration 105 frames exceeds threshold 90 frames [start=58, end=162].
> - Action 'Action_PreSnap' range [16-209] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-122] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [58-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [58-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [92-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-110] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-193] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-200] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-102] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [58-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-169] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-127] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-153] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-204] for track '26' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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