# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_72`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 30 |
| Ball Tracks | 2 |
| CSV events parsed | 16 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 144: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_FakePassDroptoHandoff' for track '7' has invalid range: start=88, end=83. Clamping end to start.
> - Segment 'Action_BallCarry' for track '7' has invalid range: start=107, end=83. Clamping end to start.
> - Action 'Action_PassBlock' range [73-144] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '0' starts at frame 149, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [149-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-96] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [70-83] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-141] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-227] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [111-112] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [119-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-14] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-236] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.