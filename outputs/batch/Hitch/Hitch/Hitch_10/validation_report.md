# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_10`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 17: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 18: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 18: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_PassBlock' for track '7' has invalid range: start=11, end=7. Clamping end to start.
> - Action 'Action_None' range [8-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-232] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-32] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-145] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '6' starts at frame 23, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [23-85] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-228] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-145] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-105] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [116-214] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [212-216] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '26' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.