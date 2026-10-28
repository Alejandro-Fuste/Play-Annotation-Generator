# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_10`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 22: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [40-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-94] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-97] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [40-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [58-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [67-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [71-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-146] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-163] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-71] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-96] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-118] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-154] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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