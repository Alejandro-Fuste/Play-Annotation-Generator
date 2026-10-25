# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_92`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 163: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - Row 164: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [67–83], lower_priority='Action_RunBlock' annotated_start=75, effective_Action_RunBlock_start=84.
> - Action 'Action_None' range [67-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-142] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-110] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-159] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [119-153] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-232] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-202] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-138] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-230] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [147-151] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [85-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [84-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-103] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-160] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-204] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-218] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-225] for track '32' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.