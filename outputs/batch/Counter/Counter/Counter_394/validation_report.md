# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_394`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_394/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '6' (LT) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Validation warning: Action 'Action_DownBlock' for track '9' (LG) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Validation warning: Action 'Action_DownBlock' for track '11' (C) duration 94 frames exceeds threshold 90 frames [start=94, end=187].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [91–106], lower_priority='Action_DownBlock' annotated_start=94, effective_Action_DownBlock_start=107.
> - Action 'Action_PreSnap' range [0-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-218] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [223-242] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-211] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [94-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-164] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-192] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-134] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-146] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [94-133] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [139-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-122] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [94-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-284] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-138] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-187] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-242] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-264] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-279] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-282] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-221] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-233] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-266] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-287] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '25' has 1 frames without a visible bounding box.
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