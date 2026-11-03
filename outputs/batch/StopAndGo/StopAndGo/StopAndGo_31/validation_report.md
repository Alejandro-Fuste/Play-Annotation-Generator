# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_31`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_31/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [3–19], lower_priority='Action_PassBlock' annotated_start=6, effective_Action_PassBlock_start=20.
> - Action 'Action_None' range [3-217] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-44] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-163] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-196] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [91-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [117-118] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-223] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-199] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-202] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-192] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-173] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [181-185] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [3-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-214] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [3-261] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [6-124] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-113] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-116] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-182] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-269] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [155-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '29' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.