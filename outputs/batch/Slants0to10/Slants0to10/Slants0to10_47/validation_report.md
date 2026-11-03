# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_47`
- **Input XML**: `outputs/batch/Slants0to10/Slants0to10/Slants0to10_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [1–15], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=16.
> - Action 'Action_None' range [1-35] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-126] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-127] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-104] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-279] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [282-329] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-83] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-81] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [16-28] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-286] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-316] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-190] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-43] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-63] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-12] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [7-17] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [21-23] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-133] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-63] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-320] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [91-138] for track '27' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [95-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-188] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-204] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-254] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [273-275] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-308] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-288] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '35' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.